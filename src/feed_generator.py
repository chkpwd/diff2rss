import logging

import fastfeedparser
from feedgen.feed import FeedGenerator

from src.utils.github import get_entry_diff

logger = logging.getLogger(__name__)


def create_feed(atom_feed: fastfeedparser.FastFeedParserDict):
    """
    Create an RSS feed from GitHub Atom Entries.
    """

    src_feed = atom_feed["feed"]

    feed = FeedGenerator()
    feed.language(src_feed["language"])
    feed.title(src_feed["title"])
    feed.link(href=src_feed["link"])
    feed.description("gitcommits")
    feed.generator("diff2rss")
    src_entries = atom_feed["entries"]
    for entry in src_entries:
        feed_item = feed.add_entry()
        try:
            feed_item.title(entry["title"])
            feed_item.link(href=entry["link"])
            feed_item.description(
                f"{entry['title']} by {entry['author']} on {entry['updated']}"
            )
            feed_item.author({"name": entry["author"]})
            feed_item.pubDate(entry["updated"])
            feed_item.content(
                f"<p><strong>Author:</strong> {entry['author']}</p>"
                f"<p><strong>Link:</strong> <a href=\"{entry['link']}\">{entry['link']}</a></p>"
                f"<pre><code>{get_entry_diff(entry)}</code></pre>",
                type="html"
            )
        except Exception as e:
            logger.error(f"Error generating RSS feed item: {str(e)}")
    return feed.rss_str(pretty=True)
