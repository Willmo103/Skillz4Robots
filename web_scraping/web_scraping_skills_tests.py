from test_helpers import run_tests
from web_scraping_skills import get_page


def test_get_page_format():
    """
    The output of the function should format the html response
    into markdown formatted text
    :return:
    """
    _input = "https://notes.willmo.dev/"
    try:
        result = get_page(_input)
        assert result is not None
        assert len(result) > 0
        return ".", result[:10]
    except AssertionError as e:
        return "F", str(e)
    except Exception as e:
        return "!", str(e)


if __name__ == '__main__':
    run_tests([test_get_page_format], "web_scraping_skills")
