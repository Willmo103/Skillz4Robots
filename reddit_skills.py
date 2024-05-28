import os
from praw import Reddit, exceptions
from typing import Annotated
from dotenv import load_dotenv

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
    results = []
    try:
        return Annotated[list, "List of matching subreddits"](
            [
                r
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
            _reddit.subreddit(subreddit).hot(limit=10)
        )
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
        return Annotated[
            list, "List of submissions in the subreddit that contain the keyword"
        ](_reddit.subreddit(subreddit).search(keyword, limit=10))
    except exceptions.PRAWException:
        return Annotated[
            list, "List of submissions in the subreddit that contain the keyword"
        ]([])


__doc__ = """
Reddit Search
=============
This module provides functions to search for subreddits, users, and submissions in a subreddit.

Functions
---------
create_reddit_instance() -> Reddit:
    Create a Reddit instance

search_for_a_subreddit(subreddit: str) -> list:
    Search for subreddits by name

search_for_a_user(user: str) -> list:
    Search for users by name

scrape_subreddit(subreddit: str) -> list:
    Search for submissions in a specific subreddit

search_subreddit_by_keyword(subreddit: str, keyword: str) -> list:
    Search for submissions in a specific subreddit that contain a keyword

Attributes
----------

__doc__ : str
    Module documentation string: Reddit Search

__package__ : str
    Package name: reddit_skills

__path__ : str
    Module path: reddit_skills.py
"""

