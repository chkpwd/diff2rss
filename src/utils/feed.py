from rfeed import Item, Guid


def create_feed_item(title, link, description, author, guid, pubDate):
    """
    Helper function for structuring commit data into an RSS-friendly format.
    """
    return Item(
        title=title,
        link=link,
        description=description,
        author=author,
        guid=Guid(guid),
        pubDate=pubDate,
    )
