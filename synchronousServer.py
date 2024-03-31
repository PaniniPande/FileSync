from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import time
# Define a custom request handler class inheriting from SimpleXMLRPCRequestHandler
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)# Set the RPC path

# Method to add two numbers
def add(i, j):
    time.sleep(5)  
    return i + j
# Method to sort an array
def sort_array(arr):
    time.sleep(5)  
    return sorted(arr)
# Main block
if __name__ == "__main__":
    # Create a SimpleXMLRPCServer instance listening on localhost:8000
    with SimpleXMLRPCServer(('localhost', 8000), requestHandler=RequestHandler) as server:
        server.register_function(add, 'add')
        server.register_function(sort_array, 'sort_array')
        print("Synchronous RPC Server is running on http://localhost:8000")
        server.serve_forever()
