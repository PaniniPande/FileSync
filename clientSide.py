from threading import Thread
import xmlrpc.client
import os
import time
import hashlib

# Define directories and server address
clientSide = 'clientSide'
serverSide = 'serverSide'
ser_address = 'http://localhost:8000/RPC2'

# Colors for console output
class colors:
    HEADER = '\033[95m'    # Purple
    OKGREEN = '\033[92m'   # Green
    OKBLUE = '\033[94m'    # Blue
    FAIL = '\033[91m'      # Dark Red
    ENDC = '\033[0m'       # Reset

# Function to upload a file to the server
def file_upload(file_name, file_data):
    try:
        server = xmlrpc.client.ServerProxy(ser_address)
        return server.upload_file(file_name, file_data)
    except Exception as e:
        return str(e)

# Function to delete a file from the server
def file_delete(file_name):
    try:
        server = xmlrpc.client.ServerProxy(ser_address)
        return server.delete_file(file_name)
    except Exception as e:
        return str(e)

# Function to calculate the hash of a file
def get_file_hash(file_path):
    with open(file_path, 'rb') as f:
        file_hash = hashlib.sha256(f.read()).hexdigest()
    return file_hash

# Function to print messages with color
def print_message(message, color):
    print(color + message + colors.ENDC)

# Function to check synchronization between client and server
def check_sync():
    try:
        while True:
            start_time = time.time()
            # Get hashes of files in client and server directories
            client_files = {file: get_file_hash(os.path.join(clientSide, file)) for file in os.listdir(clientSide) if file != ".DS_Store"}
            server_files = {file: get_file_hash(os.path.join(serverSide, file)) for file in os.listdir(serverSide) if file != ".DS_Store"}
            # Upload new or modified files from client to server
            for file, hash_client in client_files.items():
                if file not in server_files or hash_client != server_files[file]:
                    with open(os.path.join(clientSide, file), 'rb') as f:
                        file_data = xmlrpc.client.Binary(f.read())
                    result = file_upload(file, file_data)
                    if result == "OK":
                        if file in server_files:
                            print_message(f"Updated '{file}' on the server.", colors.OKBLUE)
                        else:
                            print_message(f"Uploaded '{file}' to the server.", colors.OKGREEN)
                    else:
                        print_message(f"Failed to upload '{file}' to the server: {result}", colors.FAIL)
            # Delete files from server if not present in client
            for file in server_files.keys():
                if file not in client_files:
                    result = file_delete(file)
                    if result == "OK":
                        print_message(f"Deleted '{file}' from the server.", colors.FAIL)
                    else:
                        print_message(f"Failed to delete '{file}' from the server: {result}", colors.FAIL)
            # Calculate elapsed time and sleep for the remaining time if needed
            elapsed_time = time.time() - start_time
            if elapsed_time < 10:
                time.sleep(10 - elapsed_time)
    except Exception as e:
        print_message(f"Error: {str(e)}", colors.FAIL)

# Main function
if __name__ == '__main__':
    # Create client directory if it doesn't exist
    if not os.path.exists(clientSide):
        os.makedirs(clientSide)
    # Start synchronization thread
    sync_thread = Thread(target=check_sync)
    sync_thread.daemon = True
    sync_thread.start()
    print_message("Client synchronization service is running.", colors.HEADER)

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        print_message("Client synchronization service terminated.", colors.HEADER)
