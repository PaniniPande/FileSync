import aiohttp  
from aiohttp import web  
import asyncio  

# Handler function for 'add' endpoint
async def add(request):
    data = await request.json()  # Extract JSON data from the request
    i = data['i']
    j = data['j']
    await asyncio.sleep(5)  # Simulate delay with sleep
    result = i + j  # Perform addition
    return web.json_response({'result': result})  # Return JSON response with result

# Handler function for 'sort_array' endpoint
async def sort_array(request):
    data = await request.json()  # Extract JSON data from the request
    arr = data['arr']
    await asyncio.sleep(5)  # Simulate delay with sleep
    sorted_arr = sorted(arr)  # Sort the array
    return web.json_response({'sorted_arr': sorted_arr})  # Return JSON response with sorted array

# Create a web application instance
app = web.Application()

# Add routes to the application
app.router.add_post('/add', add)  # Route for 'add' endpoint
app.router.add_post('/sort_array', sort_array)  # Route for 'sort_array' endpoint

# Entry point of the script
if __name__ == "__main__":
    web.run_app(app, host='localhost', port=8000)  # Run the web application on localhost:8000
