import logging

from flask import Flask, Response, request

from src.feed_generator import create_feed
from src.git_commits import get_all_commits

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

app = Flask(__name__)


@app.route("/generate_rss", methods=["GET"])
def generate_rss():
    repo_ref = request.args.get("feed")
    github_token = request.args.get("token")

    if not repo_ref or not github_token:
        logger.error("Missing 'feed' or 'token' parameter.")
        return (
            "Error: Please provide a valid GitHub repository reference and token as query parameters.",
            400,
        )

    try:
        commits = get_all_commits(repo_ref, github_token)
        rss_feed = create_feed(repo_ref, commits)

        return Response(rss_feed, content_type="application/rss+xml")
    except Exception as e:
        logger.error(f"Error generating RSS feed for {repo_ref}: {str(e)}")
        return f"Error: {str(e)}", 500


def main():
    app.run(debug=True)


if __name__ == "__main__":
    logger.info("Starting diff2rss...")
    main()
