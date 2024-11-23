import logging

import requests

logger = logging.getLogger(__name__)


def get_entry_diff(entry):
    """
    Helper function for extracting the diff from an Atom entry.
    """

    response = requests.get(f"{entry["link"]}.diff")

    diff = response.text

    return diff
