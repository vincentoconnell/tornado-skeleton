import tornado.web
import json


class CredentialLoginHandler(tornado.web.RequestHandler):
    def initialize(self, interface):
        self.interface = interface
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    async def get(self):
        response = await self.interface.getLogin()

        if response is None:
            raise tornado.web.HTTPError(
                 400, "no response from backend")

        await self.finish(json.dumps(response))
