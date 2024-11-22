import logging
import os

from github import Auth, Github

logger = logging.getLogger(__name__)


def get_all_commits(REPO_REF):
    result = []

    auth = os.getenv("GITHUB_TOKEN")
    if auth is None:
        raise Exception("Missing GITHUB_TOKEN environment variable")

    g = Github(auth=Auth.Token(auth))

    repo = g.get_repo(REPO_REF)
    commits = repo.get_commits()

    for commit in commits:
        result.append(
            {
                "user": commit.author.login,
                "message": commit.commit.message,
                "patches": [patch["patch"] for patch in commit.raw_data["files"]],
            }
        )
    logger.debug(f"Found {len(result)} commits")
    return result
