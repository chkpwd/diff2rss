import logging

from github import Auth, Github

logger = logging.getLogger(__name__)


def get_all_commits(repo_ref, github_token=None):
    result = []

    if github_token is None:
        raise Exception("Missing GITHUB_TOKEN parameter")

    g = Github(auth=Auth.Token(github_token))

    repo = g.get_repo(repo_ref)
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
