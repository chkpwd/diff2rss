import logging
import os
from urllib.parse import urlparse

import requests

logger = logging.getLogger(__name__)

GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]


def parse_commit_url(entry) -> tuple[str, str, str]:
    """
    Parses a GitHub commit URL to extract owner, repo, and commit hash.
    """

    commit_link: str = entry["link"]
    parsed = urlparse(commit_link)
    parts = parsed.path.strip("/").split("/")

    if len(parts) < 4 or parts[2] != "commit":
        raise ValueError(f"Unexpected GitHub commit URL format: {commit_link}")

    owner, repo, _, commit_hash = parts
    return owner, repo, commit_hash


def get_entry_diff(entry):
    """
    Fetches the diff patch (unified format) from a GitHub commit URL in an Atom feed entry.
    """
    owner, repo, commit_hash = parse_commit_url(entry)

    url = f"https://api.github.com/repos/{owner}/{repo}/commits/{commit_hash}"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    data = response.json()
    if not data.get("files"):
        logger.warning("No files found in commit.")
        return ""

    patches = [f.get("patch", "") for f in data["files"] if f.get("patch")]
    return "\n\n".join(patches)
