import tornado.web

from api.v1.ExampleHandler import ExampleHandler
from modules.example.data_access import ExampleDAO
from api.v1.credential.CredentialLoginHandler import CredentialLoginHandler
from modules.credential.CredentialFacadeImpl import CredentialFacadeImpl


def init_app(config):

    orm_or_other_data_integration = ExampleDAO(config)
    credentialInterface = CredentialFacadeImpl()

    # In order to respect Single-responsibility principle,
    # and to make the api spec visible at a glance in this one location,
    # responsibility creating the routes is here and
    # the handlers are responsible for catching exceptions if their
    # interface is not enabled, via Python's  EAFP principle.
    return tornado.web.Application(
        [
            (
                r'/api/v1/credential/login',
                CredentialLoginHandler,
                dict(interface=credentialInterface)
            ),
            (
                r'/api/vi/example',
                ExampleHandler,
                dict(interface=orm_or_other_data_integration)
            )
        ],
        **config
    )
