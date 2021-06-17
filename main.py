from jetforce import GeminiServer

from gemini.app import app

server = GeminiServer(
    app=app,
    host="127.0.0.1"
)

server.run()
