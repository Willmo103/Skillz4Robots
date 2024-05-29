from test_helpers import run_tests
from reddit_skills import (
    search_for_a_subreddit,
    scrape_subreddit,
    search_subreddit_by_keyword,
)


def test_search_for_a_subreddit():
    # Format print the results for testing purposes
    try:
        result = search_for_a_subreddit("python")
        assert result is not None
        assert len(result) > 0
        assert result[0].display_name == "Python"
        assert result[0].title != ""
        assert result[0].subscribers > 0
        return ".", result
    except AssertionError as e:
        return "F", str(e)
    except Exception as e:
        return "!", str(e)


def test_scrape_subreddit():
    # Format print the results for testing purposes
    try:
        result = scrape_subreddit("python")
        assert result is not None
        assert len(result) > 0
        assert result[0].title != ""
        assert result[0].score > 0
        return ".", result
    except AssertionError as e:
        return "F", str(e)
    except Exception as e:
        return "!", str(e)


def test_search_subreddit_by_keyword():
    # Format print the results for testing purposes
    try:
        result = search_subreddit_by_keyword("python", "reddit")
        assert result is not None
        assert len(result) > 0
        assert result[0].title != ""
        assert result[0].score > 0
        return ".", result
    except AssertionError as e:
        return "F", str(e)
    except Exception as e:
        return "!", str(e)


def run_reddit_tests():
    tests = [
        test_search_for_a_subreddit,
        test_scrape_subreddit,
        test_search_subreddit_by_keyword,
    ]
    run_tests(tests, "reddit_skills")


if __name__ == "__main__":
    run_reddit_tests()
