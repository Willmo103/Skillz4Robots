from skillz.tests.test_helpers import run_tests
from skillz.tests.reddit_skills_tests import (
     test_search_for_a_subreddit,
     test_scrape_subreddit,
     test_search_subreddit_by_keyword,
 )
from skillz.tests.web_scraping_skills_tests import test_get_page_format
reddit_tests = [
     test_search_for_a_subreddit,
     test_scrape_subreddit,
     test_search_subreddit_by_keyword,
 ]

youtube_tests = []
web_scraping_tests = [
        test_get_page_format,
]

all_tests = reddit_tests + web_scraping_tests + youtube_tests


def run_all_tests():
    global all_tests
    results = run_tests(all_tests, "")
    print("\n\nResults:")
    for result in results:
        print(result)


if __name__ == '__main__':
    run_all_tests()
