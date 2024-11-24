import logging

import fastfeedparser

logger = logging.getLogger(__name__)


def parse_feed_uri(source, author, branch):
    feed_url = ""
    base_url = f"https://github.com/{source}"

    if not source:
        logger.error("Missing 'source' parameter.")
        return (
            "Error: Please provide a valid GitHub repository reference and token as query parameters.",
            400,
        )

    if branch:
        feed_url = f"{base_url}/commits/{branch}.atom"
    else:
        feed_url = f"{base_url}/commits.atom"

    if author:
        feed_url += f"?author={author}"

    return feed_url


def parse_atom_feed(feed_url):
    """
    Helper function for parsing an Atom feed.
    """
    parsed_atom = fastfeedparser.parse(feed_url)

    return parsed_atom
