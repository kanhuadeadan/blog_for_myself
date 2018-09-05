from wsgiref.simple_server import make_server
from blog import config
from magweb import MagWeb
from blog.handler.user import user_router

if __name__ == "__main__":
    application = MagWeb()
    # 注册路由
    application.register(user_router)   # /user/

    server = make_server(config.WSIP, config.WSPORT , application)

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()