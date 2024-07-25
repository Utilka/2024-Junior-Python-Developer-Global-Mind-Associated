from aiohttp import web

async def handle_get(request):
    """
    Handle GET requests and return a welcome message.
    """
    return web.Response(text="Welcome to the aiohttp server!")

async def handle_post(request):
    """
    Handle POST requests and echo back the received data.
    """
    try:
        data = await request.json()
        response_text = f"Received data: {data}"
    except Exception as e:
        response_text = f"Failed to decode JSON: {str(e)}"
    return web.Response(text=response_text)

async def init_app():
    """
    Initialize the aiohttp application and set up routes.
    """
    app = web.Application()
    app.router.add_get('/', handle_get)
    app.router.add_post('/', handle_post)
    return app

if __name__ == '__main__':
    # Create and run the web application.
    web.run_app(init_app(), host='0.0.0.0', port=8080)
