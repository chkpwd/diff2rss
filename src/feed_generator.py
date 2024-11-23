import logging

from rfeed import Feed

from src.utils.feed import create_feed_item
from src.utils.github import get_entry_diff
from src.utils.time import convert_to_utc_time

logger = logging.getLogger(__name__)


def create_feed_items(atom_feed):
    """
    Create RSS feed items.
    """
    items = []

    feed = atom_feed["feed"]
    entries = atom_feed["entries"]

    title = feed["title"]
    link = feed["link"]
    id = feed["id"]

    for entry in entries:
        try:
            title = entry["title"]
            link = entry["link"]
            description = (
                f"<p><strong>Author:</strong> {entry['author']}</p>"
                f"<p><strong>Link:</strong> <a href=\"{entry['link']}\">{entry['link']}</a></p>"
                f"<pre><code>{get_entry_diff(entry)}</code></pre>"
            )

            author = entry["author"]
            guid = id
            pubDate = convert_to_utc_time(entry["updated"])

            item = create_feed_item(title, link, description, author, guid, pubDate)
            items.append(item)

        except Exception as e:
            logger.error(f"Error generating RSS feed item: {str(e)}")

    return items


def create_feed(atom_feed):
    """
    Create an RSS feed from GitHub Atom Entries.
    """
    items = create_feed_items(atom_feed)

    feed = atom_feed["feed"]

    feed = Feed(
        title=f"GitHub Feed for {feed['title']}",
        link=f"{feed['link']}",
        description="Latest entries from GitHub repository",
        language=feed["language"],
        lastBuildDate=convert_to_utc_time(feed["updated"]),
        items=items,
    )

    return feed.rss()
