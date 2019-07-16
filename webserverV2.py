import json
import redis
from aiohttp import web
import jinja2
import aiohttp_jinja2
from highscorelist import Highscorelist

routes = web.RouteTableDef()
r = redis.StrictRedis(host='localhost', port=6379)


@routes.view('/')
class WebView(web.View):
    async def get(self):
        scores = Highscorelist('Scores.json')
        context = {'score_list': scores.highscores}
        response = aiohttp_jinja2.render_template('index.html', self.request, context)
        return response

    async def post(self):
        data = await self.request.json()
        message = json.dumps(data)
        r.publish('game_action', message)
        return web.Response()


@routes.view('/tetris_message')
class WebView(web.View):
    async def post(self):
        data = await self.request.json()
        message = json.dumps(data)
        r.publish('game_action', message)
        return web.Response()


@routes.view('/highscores')
class WebView(web.View):
    async def get(self):
        scores = Highscorelist('Scores.json')
        context = {'score_list': scores.to_dict()}
        response = web.json_response(context)
        return response


@routes.view('/favicon.ico')
class WebView(WebView):
    async def get(self):
        return web.FileResponse('./static/favicon.ico')


app = web.Application()
app['static_root_url'] = '/static'
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))
app.router.add_static('/static', 'static', name='static')
app.add_routes(routes)

if __name__ == '__main__':
    web.run_app(app, port=80)
