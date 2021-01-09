"""Async web parser"""

import asyncio
import logging
import sys

import aiohttp
import aiohttp.web_exceptions
from aiohttp import ClientSession
from bs4 import BeautifulSoup

urls = ('https://www.google.com', 'https://www.amazon.com',
        'https://www.linkedin.com')

parsed_titles = []


async def _parse_single(url: str, session: ClientSession):
    if not isinstance(url, str) or not url:
        raise ValueError('URL must be filled string')

    try:
        response = await session.request('GET', url)
        response.raise_for_status()
    except aiohttp.web_exceptions.HTTPError:
        logging.error('Invalid URL passed')
        return

    response = await response.read()

    html = BeautifulSoup(response)

    title = html.find('title').contents

    if isinstance(title, list):
        len_ = len(title)
        if len_ == 1:
            title = title[0]
        elif len_ > 1:
            title = ', '.join(title)
        else:
            return
    else:
        return

    parsed_titles.append(title)


async def parse():
    async with ClientSession() as session:
        await asyncio.gather(*[_parse_single(url, session)
                               for url in urls])


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    try:
        loop.run_until_complete(parse())
    finally:
        loop.close()

    print(parsed_titles)
    sys.exit()
