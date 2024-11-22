import datetime
import logging

from rfeed import Feed

from src.git_commits import get_all_commits
from src.utils import create_feed_item


logger = logging.getLogger()


def create_feed_items(REPO_REF):
    """
    Create an RSS feed from GitHub commits.
    """
    commits = get_all_commits(REPO_REF)

    items = []

    for commit in commits:
        title = f"Commit by {commit['user']}"
        link = f"https://github.com/{REPO_REF}/commit/{commit['patches'][0]}"
        description = (
            f"Commit message: {commit['message']}\nPatches: {commit['patches']}"
        )
        author = commit["user"]
        guid = f"https://github.com/{REPO_REF}/commit/{commit['patches'][0]}"
        pubDate = datetime.datetime.now()  # or use commit['date'] if available

        item = create_feed_item(title, link, description, author, guid, pubDate)
        items.append(item)

    return items


def create_feed(REPO_REF):
    """
    Create an RSS feed from GitHub commits.
    """
    items = create_feed_items(REPO_REF)

    feed = Feed(
        title=f"GitHub Commits Feed for {REPO_REF}",
        link=f"https://github.com/{REPO_REF}",
        description=f"Latest commits for {REPO_REF}",
        language="en-US",
        lastBuildDate=datetime.datetime.now(),
        items=items,
    )

    return feed.rss()
