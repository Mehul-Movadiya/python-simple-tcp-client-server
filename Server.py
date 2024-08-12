import socket 
def start_server(host="127.0.0.1", port=65433): 
    """ 
    Function to start a TCP server. 
    Parameters: 
    host (str): The IP address the server listens on. Default is localhost. 
    port (int): The port the server listens on. Default is 65433. 
    """ 
    # Create a TCP/IP socket 
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    # Bind the socket to the address and port 
    server_socket.bind((host, port)) 
    # Enable the server to accept connections (max backlog of connections is 1) 
    server_socket.listen(1) 
    print(f"Server listening on {host}:{port}") 

    while True: 
        print("Waiting for a connection") 
        
        # Wait for a connection 
        conn, addr = server_socket.accept() 
        
        try: 
            print(f"Connection from {addr}") 

            while True: 
                # Receive data from the client in chunks of 1024 bytes 
                data = conn.recv(1024) 
                
                if data: 
                    # Decode and print the received data 
                    print(f"Received {data.decode()} from {addr}") 
                    
                    # Send acknowledgment to the client 
                    acknowledgment = "Message received" 
                    conn.sendall(acknowledgment.encode()) 
                else: 
                    # Break the loop if no more data is received 
                    break 

        finally: 
            # Clean up the connection 
            conn.close() 
            print(f"Connection from {addr} closed") 
 
if __name__ == "__main__": 
    # Start the server with default parameters 
    start_server() 