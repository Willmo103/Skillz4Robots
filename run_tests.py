from test_helpers import run_tests
from reddit.reddit_skills_tests import (
     test_search_for_a_subreddit,
     test_scrape_subreddit,
     test_search_subreddit_by_keyword,
 )

reddit_tests = [
     test_search_for_a_subreddit,
     test_scrape_subreddit,
     test_search_subreddit_by_keyword,
 ]

youtube_tests = []

all_tests = reddit_tests + youtube_tests


def run_all_tests():
    global all_tests
    results = run_tests(all_tests, "")
    print("\n\nResults:")
    for result in results:
        print(result)

