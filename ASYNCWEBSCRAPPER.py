## web scrapper ,while building an async python application , we  are not allowed to use any  python module
# but we are only supposed to use waitbale functions that using asyncio library
# http is requests library is not compatibel with asyunc io
# requests is built on top of url lib3 which inturn is python's http and socket modules and by default socket operations are blokcing
#https://project-awesome.org/timofurrer/awesome-asyncio # gives all aio files
# instead of using requests we need to use aiohttp , which defines awaitable co-routines

import asyncio
import aiohttp
import aiofiles

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        html = await response.text()
        return html

async def write_to_file(file,text):
    async with aiofiles.open(file, 'w'):
        await f.write(text)

async def main(urls):
    tasks = []
    for url in urls:
        file= f'{url.split("//")[-1]}.txt'
        html = await fetch(url)
        tasks.append(write_to_file(file, html))

    await asynio.gather(*tasks)

urls = ('https://python.org', 'https://stackoverflow.org', 'https://google.com')
asyncio.run(main(urls))

# we cannot use ordinary file response to store http respones becasue ordinary one's are blocking
# to read from or write to files asynchronously
# aiofile help store in asycn way