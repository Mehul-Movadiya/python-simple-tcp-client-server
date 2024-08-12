import socket 
 
def start_client(host='127.0.0.1', port=65433): 
    """ 
    Function to start a TCP client. 
 
    Parameters: 
    host (str): The IP address of the server to connect to. Default is 
    localhost. 
    port (int): The port on which the server is listening. Default is 65433. 
    """ 
     
    # Create a TCP/IP socket 
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
 
    # Connect the socket to the server's port 
    client_socket.connect((host, port)) 
    print(f"Connected to server {host}:{port}") 
 
    try: 
        while True: 
            # Prompt user for a message to send to the server 
            message = input("Enter message to send (type 'exit' to close): ") 
 
            # Exit the loop if the user types 'exit' 
            if message.lower() == 'exit': 
                break 
 
            # Send the message to the server 
            client_socket.sendall(message.encode()) 
 
            # Receive the response from the server 
            data = client_socket.recv(1024) 
            print(f"Received {data.decode()} from server") 
 
    finally: 
        # Close the connection to the server 
        client_socket.close() 
        print("Connection closed") 
 
if __name__ == "__main__": 
    # Start the client with default parameters 
    start_client() 