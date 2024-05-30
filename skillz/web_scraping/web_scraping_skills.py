# annotation
from typing import Annotated
from markdownify import markdownify as md
import requests
from requests import Response
import duckduckgo_search


def get_webpage(
        url: Annotated[str, "URL of the page you want to scrape"]
) -> Annotated[str, "Markdown converted content of the page"]:
    """ Get the content of a web page using the URL, and convert it to
    minified markdown format.

    :param url: str - URL of the page you want to scrape
    :return: str - Markdown converted content of the page
    """

    # Get the content of the page
    response: Response = requests.get(url)
    converted = md(response.text, heading_style="MD").strip().replace("\n", "").replace("\t", "")
    if response.status_code != 200:
        return Annotated[str, "Markdown converted content of the page"](
            f"# Error: Unable to fetch the page. Status code [{response.status_code}]\n\n" +
            "**URL:**\n{url}\n\n**Response:**\n{response.text}")
    return Annotated[str, "Markdown converted content of the page"](converted)


# using the duckduckgo minified search python package to search
# for a topic then use the search results to scrape the web page
# !pip install duckduckgo_search
def search_topic():
    pass

