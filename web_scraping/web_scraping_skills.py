# annotation
from typing import Annotated
from markdownify import markdownify as md
import requests
from requests import Response


def get_page(
        url: Annotated[str, "URL of the page you want to scrape"]
) -> Annotated[str, "Markdown converted content of the page"]:
    """ Get the content of a web page

    :param url: str - URL of the page you want to scrape
    :return: str - Markdown converted content of the page
    """

    # Get the content of the page
    response: Response = requests.get(url)
    if response.status_code != 200:
        return Annotated[str, "Markdown converted content of the page"](
            f"# Error: Unable to fetch the page. Status code [{response.status_code}]\n\n" +
            "**URL:**\n{url}\n\n**Response:**\n{response.text}")
    return Annotated[str, "Markdown converted content of the page"](md(response.text, heading_style="MD"))
