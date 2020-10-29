import asyncio
from modules.credential.CredentialFacade import CredentialFacade
from modules.credential.CredentialModule import CredentialInterface


class CredentialFacadeImpl(CredentialFacade):
    def __init__(self):
        self.credentialInterface = CredentialInterface()

    async def getLogin(self):
        login_response = await self.credentialInterface.getLogin()

        return login_response
