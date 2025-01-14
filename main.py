import logging

from fastapi import FastAPI
from fastapi.responses import Response

from src.feed_generator import create_feed
from src.utils.parsing import parse_atom_feed, parse_feed_uri

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

app = FastAPI(title="GitHub Feed Generator")


@app.get("/generate_rss")
async def generate_rss(source: str, author: str = "", branch: str = "main"):
    feed_url = parse_feed_uri(source, author, branch)

    atom_feed = parse_atom_feed(feed_url)

    try:
        rss_feed = create_feed(atom_feed)
        return Response(rss_feed, media_type="application/rss+xml")
    except Exception as e:
        logger.error(
            f"Error generating RSS feed: {str(e)}", exc_info=True, stack_info=True
        )
        return f"Error: {str(e)}", 500
