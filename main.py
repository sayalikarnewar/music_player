from aiohttp import web
import jinja2
import aiohttp_jinja2

from routes import routes

app = web.Application()

#setting up the jinja template
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))

#adding the routes
routes(app)

#run the web app
web.run_app(app)