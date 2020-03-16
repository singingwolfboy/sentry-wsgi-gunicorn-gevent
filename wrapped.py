import sentry_sdk
from sentry_sdk.integrations.wsgi import SentryWsgiMiddleware

from app import wsgi_app

# This will automatically pick up the DSN from the `SENTRY_DSN` environment variable
sentry_sdk.init()

wsgi_app = SentryWsgiMiddleware(wsgi_app)
