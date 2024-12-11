import socket
import logging
import threading
from datetime import datetime
from flask import Flask, render_template, request, send_from_directory
import os

# Configure logging for the honeypot
logging.basicConfig(filename='PoohBear.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Flask App Configuration
app = Flask(__name__)

# Base directory for the honeypot files
BASE_DIR = "honeypot_files"

# Log access attempts
def log_access(file_or_folder):
    with open("access_log.txt", "a") as log_file:
        log_file.write(f"Access attempted: {file_or_folder}\n")
    logging.info(f"Access attempted: {file_or_folder}")

# Dynamically read directory contents
def get_directory_data(base_path):
    directory_data = []
    for entry in os.listdir(base_path):
        entry_path = os.path.join(base_path, entry)
        if os.path.isdir(entry_path):
            directory_data.append({'name': entry, 'type': 'folder'})
        else:
            directory_data.append({'name': entry, 'type': 'file'})
    return directory_data

@app.route('/')
def home():
    directory_data = get_directory_data(BASE_DIR)
    return render_template('index.html', directory=directory_data)


@app.route('/access', methods=['POST'])
def access_item():
    item_name = request.form.get('item_name')
    if not item_name:
        return "No item specified", 400

    log_access(item_name)
    item_path = os.path.join(BASE_DIR, item_name)

    if os.path.exists(item_path):
        if os.path.isfile(item_path):
            # Handle file: read content
            try:
                with open(item_path, 'r', errors='ignore') as file:
                    file_content = file.read()
                return render_template('access.html', item_name=item_name, file_content=file_content, directory=None)
            except Exception as e:
                return f"Error reading file: {str(e)}", 500
        elif os.path.isdir(item_path):
            # Handle folder: list contents
            try:
                directory_contents = get_directory_data(item_path)
                return render_template('access.html', item_name=item_name, file_content=None, directory=directory_contents)
            except Exception as e:
                return f"Error reading directory: {str(e)}", 500

    return "File or folder not found", 404


# Function to start the Flask app
def start_flask():
    app.run(debug=False, use_reloader=False, port=5000)

# Function to start the socket honeypot
def start_honeypot(host='0.0.0.0', port=8080):
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the host and port
    server_socket.bind((host, port))
    
    # Listen for incoming connections
    server_socket.listen(5)
    print(f"[+] PoohBear is running on {host}:{port}")
    
    while True:
        # Accept a connection
        client_socket, client_address = server_socket.accept()
        print(f"[!] Connection from {client_address}")
        
        # Log the connection details
        logging.info(f"Connection from {client_address}")
        
        # Close the connection
        client_socket.close()

if __name__ == "__main__":
    # Run the Flask app and socket honeypot concurrently
    flask_thread = threading.Thread(target=start_flask)
    honeypot_thread = threading.Thread(target=start_honeypot)
    
    flask_thread.start()
    honeypot_thread.start()

    flask_thread.join()
    honeypot_thread.join()
