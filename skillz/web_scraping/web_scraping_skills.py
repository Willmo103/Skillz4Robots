# annotation
from markdownify import markdownify as md
import requests
from requests import Response
from duckduckgo_search import DDGS
from typing import Annotated


def get_webpage(
        url: Annotated[str, "URL of the page you want to scrape"]
) -> Annotated[str, "Markdown converted content of the page"]:
    """ Get the content of a web page using the URL, and convert it to
    minified markdown format.

    :param url: str - URL of the page you want to scrape
    :return: str - Markdown converted content of the page
    """
    response: Response = requests.get(url)
    converted = md(response.text, heading_style="MD").strip().replace("\n", "").replace("\t", "")
    if response.status_code != 200:
        return Annotated[str, "Markdown converted content of the page"](
            f"# Error: Unable to fetch the page. Status code [{response.status_code}]\n\n" +
            "**URL:**\n{url}\n\n**Response:**\n{response.text}")
    return Annotated[str, "Markdown converted content of the page"](converted)


def duckduckgo_keyword_search(
        keyword: Annotated[str, "keyword to search using the duckduckgo search engine and patterns"]
) -> Annotated[list[dict], "The results from the search limit 5"]:
    """search for a keywords using the duckduckgo search engine.

    :param keyword: Annotated[str] - The topic you want to search for
    :return: List[dict] - The search results from the search limit 5
    """
    results = DDGS().text(keyword, region='us-en', safesearch='off', max_results=5)
    return Annotated[list[dict], "The results from the search limit 5"](results)
