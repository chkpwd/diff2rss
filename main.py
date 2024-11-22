import logging
import os

from src.feed_generator import create_feed_items


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")


def main():
    repo = os.environ["REPO_REF"]

    if repo is None:
        raise Exception("Missing REPO_REF environment variable")

    rss_feed = create_feed_items(repo)
    print(rss_feed)



if __name__ == "__main__":
    logger.info("Checking for new commits...")
    main()
