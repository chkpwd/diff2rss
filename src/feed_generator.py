import datetime
import logging

from rfeed import Feed

from src.utils import create_feed_item


logger = logging.getLogger()


def create_feed_items(repo_ref, commits):
    """
    Create an RSS feed from GitHub commits.
    """

    items = []

    for commit in commits:
        title = commit['message']
        link = f"https://github.com/{repo_ref}/commit/{commit['patches'][0]}"
        description = (
            f"Diff: {commit['message']}\nPatches: {commit['patches']}"
        )
        author = commit["user"]
        guid = f"https://github.com/{repo_ref}/commit/{commit['patches'][0]}"
        pubDate = datetime.datetime.now()

        item = create_feed_item(title, link, description, author, guid, pubDate)
        items.append(item)

    return items


def create_feed(repo_ref, commits):
    """
    Create an RSS feed from GitHub commits.
    """
    items = create_feed_items(repo_ref, commits)

    feed = Feed(
        title=f"GitHub Commits Feed for {repo_ref}",
        link=f"https://github.com/{repo_ref}",
        description=f"Latest commits for {repo_ref}",
        language="en-US",
        lastBuildDate=datetime.datetime.now(),
        items=items,
    )

    return feed.rss()
