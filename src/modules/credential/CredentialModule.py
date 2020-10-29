import traceback
from datetime import datetime, timedelta

import jwt

hardware_delay = 1


class CredentialInterface:

    def __init__(self):
        self.encoded = None

    async def getLogin(self):
        try:
            encoded = jwt.encode({'some': 'payload'}, 'secret', algorithm='HS256')
            date = datetime.now()
            expire_date = (date + timedelta(minutes=15)) - date

            token = {
                'token': str(encoded),
                'tokenExpirationDate': str(date),
                'tokenExpirationMinutes': str(expire_date)
            }

            return f"{token}"
        except Exception:
            # TODO log error
            traceback.print_exc()
            return "Unknown error occured"
