from reddit_search import (
    search_for_a_subreddit,
    search_for_a_user,
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
        return ".", result[0].display_name
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
        return ".", result[0].title
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
        return ".", result[0].title
    except AssertionError as e:
        return "F", str(e)
    except Exception as e:
        return "!", str(e)


def run_tests():
    results = []
    for test in [
        test_search_for_a_subreddit,
        test_search_for_a_user,
        test_scrape_subreddit,
        test_search_subreddit_by_keyword,
    ]:
        result = test()
        results.append((test.__name__, result[1]))
        print(result[0], end="", flush=True)
    print()
    for result in results:
        print(f"{result[0]}: {result[1]}")
    print("Tests completed")


if __name__ == "__main__":
    run_tests()
