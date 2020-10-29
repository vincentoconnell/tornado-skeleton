import aioredis
import tornado.httpserver
import tornado.autoreload
from app import init_app
import asyncio
import sys
import json
import os


async def main():
    config = {}
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as json_file:
            config = json.load(json_file)
    else:
        raise RuntimeError("No Configuration Specified!")

    # do some global init things like creating a DB session and pass in teh config dict
    redis = await aioredis.create_redis_pool('redis://localhost', password='blah')
    config['redis'] = redis

    app = init_app(config)
    port = 8888
    host = "localhost"
    # restart is config changes
    tornado.autoreload.start()
    tornado.autoreload.watch(os.path.abspath(sys.argv[1]))
    server = tornado.httpserver.HTTPServer(app)
    server.listen(port)
    print(f"listening on {host}:{port}")
    while True:
        await asyncio.sleep(100)


if __name__ == "__main__":
    asyncio.run(main())
