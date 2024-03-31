from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import os

serverSide = 'serverSide'

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

with SimpleXMLRPCServer(('localhost', 8000), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    print("Server is now active and listening for connections on port 8000.")

    if not os.path.exists(serverSide):
        os.makedirs(serverSide)

    def upload_file(file_name, file_data):
        try:
            with open(os.path.join(serverSide, file_name), 'wb') as f:
                f.write(file_data.data)
            return "OK"
        except Exception as e:
            return str(e)

    def update_file(file_name, file_data):
        try:
            with open(os.path.join(serverSide, file_name), 'wb') as f:
                f.write(file_data.data)
            return "OK"
        except Exception as e:
            return str(e)

    def delete_file(file_name):
        try:
            fp = os.path.join(serverSide, file_name)
            os.unlink(fp)
            return "OK"
        except Exception as e:
            return str(e)

    server.register_function(upload_file, 'upload_file')
    server.register_function(update_file, 'update_file')
    server.register_function(delete_file, 'delete_file')

    server.serve_forever()
