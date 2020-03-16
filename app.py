from sentry_sdk import capture_message

def wsgi_app(environ, start_response):
    data = b"Hello, World!\n"
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    capture_message("This message was sent from WSGI, via Gunicorn/Gevent")
    return iter([data])