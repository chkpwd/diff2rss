import logging

from flask import Flask, Response

from src.feed_generator import create_feed
from src.utils.parsing import parse_atom_feed, parse_feed_uri

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

app = Flask(__name__)


@app.route("/generate_rss", methods=["GET"])
def generate_rss():
    feed_url = parse_feed_uri()

    atom_feed = parse_atom_feed(feed_url)

    try:
        rss_feed = create_feed(atom_feed)
        return Response(rss_feed, content_type="application/rss+xml")
    except Exception as e:
        logger.error(f"Error generating RSS feed: {str(e)}", exc_info=True, stack_info=True)
        return f"Error: {str(e)}", 500


def main():
    app.run(debug=True)


if __name__ == "__main__":
    logger.info("Starting diff2rss...")
    main()
