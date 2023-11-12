__author__ = 'reposyte'

import logging;logging.basicConfig(level=logging.INFO)
import asyncio
#pip install aiohttp
from aiohttp import web

async def index(request):
    return web.Response(body=b'<h1>Hello World Web by Py</h1>',content_type='text/html')

def init():
    app=web.Application()
    app.router.add_get('/',index)
    web.run_app(app,host='127.0.0.1',port=8081)

if __name__ == "__main__":
    init()
