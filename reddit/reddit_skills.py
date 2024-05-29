import os
from praw import Reddit, exceptions
from typing import Annotated
from dotenv import load_dotenv
# from praw.models import Subreddit
# from praw.models import Submission
# from praw.models import Comment
# from praw.models import Redditor

load_dotenv()


def create_reddit_instance() -> Reddit:
    """
    Create a Reddit instance

    :return: Reddit - Reddit
    """
    return Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT"),
    )


def search_for_a_subreddit(
    subreddit: Annotated[str, "Name of the subreddit you want to search"]
) -> Annotated[list, "List of matching subreddits"]:
    """
    Search for subreddits by name

    :param subreddit: str - name of the subreddit you want to search
    :return: list - List of matching subreddits
    """
    _reddit = create_reddit_instance()
    try:
        return Annotated[list, "List of matching subreddits"](
            [
                r.__dict__
                for r in _reddit.subreddits.search(subreddit, limit=10)
                if r.subscribers > 0
            ]
        )
    except exceptions.PRAWException:
        return Annotated[list, "List of matching subreddits"]([])


def scrape_subreddit(
    subreddit: Annotated[str, "Name of the subreddit you want to search"]
) -> Annotated[list, "List of submissions in the subreddit"]:
    """
    Search for submissions in a specific subreddit

    :param subreddit: str - name of the subreddit you want to search
    :return: list - List of submissions in the subreddit
    """
    _reddit = create_reddit_instance()
    try:
        return Annotated[list, "List of submissions in the subreddit"](
            r.__dict__ for r in _reddit.subreddit(subreddit).hot(limit=10))
    except exceptions.PRAWException:
        return Annotated[list, "List of submissions in the subreddit"]([])


def search_subreddit_by_keyword(
    subreddit: Annotated[str, "Name of the subreddit you want to search"],
    keyword: Annotated[str, "Keyword you want to search for"],
) -> Annotated[list, "List of submissions in the subreddit that contain the keyword"]:
    """
    Search for submissions in a specific subreddit that contain a keyword

    :param subreddit: str - name of the subreddit you want to search
    :param keyword: str - keyword you want to search for
    :return: list - List of submissions in the subreddit that contain the keyword
    """
    _reddit = create_reddit_instance()
    try:
        results = _reddit.subreddit(subreddit).search(keyword, limit=10)
        results = [r.__dict__ for r in results]
        return Annotated[
            list, "List of submissions in the subreddit that contain the keyword"
        ](results)
    except exceptions.PRAWException:
        return Annotated[
            list, "List of submissions in the subreddit that contain the keyword"
        ]([])

# TODO: create extraction middleware for the reddit models
# def extract_subreddit(subreddit: Subreddit) -> dict:
# def extract_submission(submission: Submission) -> dict:
# def extract_comment(comment: Comment) -> dict:
# def extract_redditor(redditor: Redditor) -> dict:
# def extract_submission_comments(submission: Submission) -> dict:
# def extract_user_posts(redditor: Redditor) -> dict:
# def extract_user_comments(redditor: Redditor) -> dict:
# def extract_user_subreddits(redditor: Redditor) -> dict:
# TODO New Tools: top_posts_by_keyword, top_subreddits_by_keyword, total_trending_subreddits, total_trending_posts
# def top_posts_by_keyword(keyword: str) -> list:
# def top_subreddits_by_keyword(keyword: Annotation[str, "Keyword you want to search for"]) -> list:
# def total_trending_subreddits(limit: int = 10) -> Annotation[list, "List of trending subreddits"]:
# def total_trending_posts(limit: int = 10) -> Annotation[list, "List of trending posts"]:

# TODO: annotated skills for crawling reddit using user, subreddit, etc, looping stearable research by llm
# def deep_dive_session(subreddit: str, keyword: str, limit: int = 10) -> dict:
