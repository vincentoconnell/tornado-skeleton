import json

from modules import NotEnabledException


class ExampleDAO:
    def __init__(self, config):
        if config["exampleconfig"]["enabled"] is True:
            self.enabled = True

    async def getHelloWorld(self):
        if self.enabled:
            response = {
                "message": "Hello World"
            }
            return response
        else:
            raise NotEnabledException("dao module is not enabled.")



