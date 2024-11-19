from aiohttp import web
import asyncio
import logging
from mimicry.scheduler import Mock, MockScheduler

logging.basicConfig(level=logging.DEBUG)

REQUESTS_HISTORY = []
scheduler = MockScheduler()


async def handle(request):
    path = request.path
    mock = scheduler.get_mock(path)

    if not mock:
        return web.Response(text="404: Not Found", status=404)
    
    # Apply response delay if specified
    delay = mock.get("delay", 0)
    await asyncio.sleep(delay)
    
    return web.Response(
        text=str(mock['body']),
        status=mock['status_code'],
        headers=mock['headers'])

async def create_mock_handler(request):
    """
    API endpoint to schedule a new mock.
    Expects JSON payload with:
    - path (string): The endpoint path to mock.
    - status (int): HTTP status code for the response.
    - headers (dict): Optional HTTP headers.(content-type: text/plain is default) 
    - body (string): Optional Response body.
    - delay (float): Optional delay in seconds.
    """
    try:
        data = await request.json()  # Parse JSON payload
        mock_data = Mock(**data)
        scheduler.create_mock(mock_data)
        return web.json_response({"message": f"Mock for '{mock_data.path}' created successfully"}, status=200)
    except (ValueError, TypeError) as e:
        return web.json_response({"Payload validation Error": str(e)}, status=400)
    except Exception as e:
        return web.json_response({"error": f"Failed to create mock. Error: {str(e)}"}, status=500)
    
async def update_mock_handler(request):
    # Placeholder function for updating a mock
    pass

async def get_mocks_handler(request):
    # Placeholder function for getting mocks
    pass


if __name__ == "__main__":
    app = web.Application()
    app.router.add_route('*', '/{tail:.*}', handle)
    app.router.add_post('/mocks/create', create_mock_handler)
    app.router.add_patch('/mocks/update', update_mock_handler)
    app.router.add_get('/mocks', get_mocks_handler)
    web.run_app(app)
