#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Minimal GitHub code search to find Java Virtual Threads usage (and Platform Threads baselines),
aggregate by repository, and export CSVs to the current folder.

Outputs:
  - results_code_hits.csv  -> one row per matching file
  - results_repos.csv      -> one row per repository (aggregated)
"""

import os
import time
import csv
import math
import requests
import pandas as pd

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
if not GITHUB_TOKEN:
    print("ERROR: Please set GITHUB_TOKEN environment variable.")
    raise SystemExit(1)

SESSION = requests.Session()
SESSION.headers.update({
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "X-GitHub-Api-Version": "2022-11-28",
    "User-Agent": "vt-msr-minimal-script"
})

# ---- Adjust your queries here ----
# Keep it simple: we focus on VT signatures; PT baseline queries are optional.
# GitHub limits search results to 1000 items per query, we'll page through.

QUERIES = [
    # --- Virtual Threads (core)
    'Thread.ofVirtual() language:Java',
    'Executors.newVirtualThreadPerTaskExecutor language:Java',
    'StructuredTaskScope language:Java',
    # --- Optional baselines / context (uncomment if you want PTs too)
    # 'new Thread( language:Java',
    # 'ThreadPoolExecutor language:Java',
    # 'Executors.newFixedThreadPool language:Java',
]

# Optional: time window / filters (example)
SEARCH_PARAMS = {
    "per_page": 100,
    # Uncomment to restrict by date or org/user if quiser:
    # "q_suffix": " pushed:>=2024-01-01"
}

# Basic safety to avoid hammering the API if you run many queries
REQUEST_SLEEP = 1.0  # seconds between pages


def github_get(url, params=None, retry=3):
    for attempt in range(1, retry + 1):
        resp = SESSION.get(url, params=params)
        if resp.status_code == 200:
            return resp
        if resp.status_code == 403:
            # rate limited or forbidden; try to respect reset header
            reset = resp.headers.get("X-RateLimit-Reset")
            if reset:
                wait_for = max(0, int(reset) - int(time.time())) + 2
                print(f"[rate-limit] waiting {wait_for}s...")
                time.sleep(wait_for)
                continue
        # brief backoff for transient issues
        print(f"[warn] GET {url} -> {resp.status_code}, attempt {attempt}/{retry}")
        time.sleep(2 * attempt)
    resp.raise_for_status()
    return resp


def search_code(query):
    """Return list of code items for a query (up to 1000 results)."""
    items = []
    # Add optional suffix filters if set
    q = query
    if SEARCH_PARAMS.get("q_suffix"):
        q = f"{q} {SEARCH_PARAMS['q_suffix']}"

    # First call to get total_count
    url = "https://api.github.com/search/code"
    params = {"q": q, "per_page": SEARCH_PARAMS["per_page"], "page": 1}
    r = github_get(url, params=params)
    data = r.json()
    total = min(1000, data.get("total_count", 0))  # GitHub caps at 1000
    if total == 0:
        print(f"[info] No results for: {query}")
        return items

    pages = math.ceil(total / SEARCH_PARAMS["per_page"])
    print(f"[info] Query: '{query}' -> total_count={data.get('total_count', 0)}, fetching up to {total} in {pages} page(s)")

    # Page 1 already fetched
    items.extend(data.get("items", []))

    # Remaining pages
    for page in range(2, pages + 1):
        time.sleep(REQUEST_SLEEP)
        params["page"] = page
        r = github_get(url, params=params)
        data = r.json()
        items.extend(data.get("items", []))

    return items


def get_repo_info(full_name):
    """Return repo metadata dict."""
    url = f"https://api.github.com/repos/{full_name}"
    r = github_get(url)
    j = r.json()
    return {
        "repo_full_name": full_name,
        "repo_html_url": j.get("html_url"),
        "repo_description": (j.get("description") or "")[:300],
        "repo_language": j.get("language"),
        "stargazers_count": j.get("stargazers_count"),
        "forks_count": j.get("forks_count"),
        "open_issues_count": j.get("open_issues_count"),
        "default_branch": j.get("default_branch"),
        "created_at": j.get("created_at"),
        "updated_at": j.get("updated_at"),
        "pushed_at": j.get("pushed_at"),
        "archived": j.get("archived"),
    }


def main():
    all_hits = []  # flat list of code results across queries
    for q in QUERIES:
        hits = search_code(q)
        for it in hits:
            rep = it.get("repository", {})
            all_hits.append({
                "query": q,
                "repo_full_name": rep.get("full_name"),
                "repo_html_url": rep.get("html_url"),
                "path": it.get("path"),
                "html_url": it.get("html_url"),
                "score": it.get("score"),
            })

    if not all_hits:
        print("[done] No matches found for given queries.")
        return

    # Save raw hits
    df_hits = pd.DataFrame(all_hits).drop_duplicates()
    df_hits.sort_values(["repo_full_name", "query", "path"], inplace=True)
    df_hits.to_csv("results_code_hits.csv", index=False, quoting=csv.QUOTE_MINIMAL)
    print(f"[ok] Saved results_code_hits.csv with {len(df_hits)} rows")

    # Aggregate by repo
    agg = (
        df_hits.groupby("repo_full_name")
        .agg(
            matches_total=("path", "count"),
            distinct_queries=("query", "nunique"),
            repo_html_url=("repo_html_url", "first"),
        )
        .reset_index()
    )

    # Fetch repo metadata
    meta_rows = []
    for full_name in agg["repo_full_name"].tolist():
        try:
            meta = get_repo_info(full_name)
            meta_rows.append(meta)
            time.sleep(0.2)
        except Exception as e:
            print(f"[warn] repo meta failed for {full_name}: {e}")

    df_meta = pd.DataFrame(meta_rows)
    df_repos = agg.merge(df_meta, on="repo_full_name", how="left")

    # Optional: quick filters you may want initially
    # e.g., only repos with default language Java or pushed recently.
    # df_repos = df_repos[(df_repos["repo_language"] == "Java")]

    df_repos.sort_values(["matches_total", "stargazers_count"], ascending=[False, False], inplace=True)
    df_repos.to_csv("results_repos.csv", index=False, quoting=csv.QUOTE_MINIMAL)
    print(f"[ok] Saved results_repos.csv with {len(df_repos)} repositories")

    # Small console summary
    top = df_repos.head(10)[["repo_full_name", "matches_total", "distinct_queries", "stargazers_count", "pushed_at"]]
    print("\nTop repositories by matches_total:")
    print(top.to_string(index=False))


if __name__ == "__main__":
    main()
