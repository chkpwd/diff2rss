import fastfeedparser
import logging

from flask import request

logger = logging.getLogger(__name__)

def parse_feed_uri():
    feed_url = ""

    repo_ref = request.args.get("source")
    content = request.args.get("content")
    branch = request.args.get("branch")

    base_url = f"https://github.com/{repo_ref}"

    if not repo_ref:
        logger.error("Missing 'source' parameter.")
        return (
            "Error: Please provide a valid GitHub repository reference and token as query parameters.",
            400,
        )

    if not content:
        logger.error("Missing 'content' parameter.")
        content = "commits"
        return (
            "Warning: Missing 'content' parameter. Defaulting to 'commits'.",
            400,
        )

    if branch:
        feed_url = f"{base_url}/{content}/{branch}.atom"
    else:
        feed_url = f"{base_url}/{content}/main.atom"

    return feed_url


def parse_atom_feed(feed_url):
    """
    Helper function for parsing an Atom feed.
    """
    parsed_atom = fastfeedparser.parse(feed_url)

    return parsed_atom
