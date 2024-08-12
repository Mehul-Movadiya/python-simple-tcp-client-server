# python-simple-tcp-client-server
TCP communication  between server and client using python.

## Overview
TCP (Transmission Control Protocol) is an important network protocol that lets two hosts 
connect and exchange data streams. TCP guarantees the delivery of data and packets in the 
same order as they were sent. 
TCP's role is to ensure the packets are reliably delivered, and error-free. TCP implements 
congestion control, which means the initial requests start small, increasing in size to the 
levels of bandwidth the computers, servers, and network can support. 

## Prerequisites 
• Python installed on both machines. 
• Both machines must be on the same network. 
• Knowledge of IP addresses and basic Python programming. 

## Getting Started
**1. Clone the Repository**
Clone this repository to your local machine:

```
git clone https://github.com/Mehul-Movadiya/python-simple-tcp-client-server.git
cd python-simple-tcp-client-server
```
**2. Running the Server**
To start the TCP server, run the following command:

```
python server.py
```
**3. Running the Client**
On the client machine, run the following command to connect to the server:
```
python client.py
```
**4. Testing the Connection**
Once both the server and client are running, you can start sending messages from the client to the server. The server will receive the messages and can respond accordingly.

## Example Usage
**Start the server on one machine:**
```
python server.py
```

**Connect the client from another machine (using the server’s IP address):**
```
python client.py
```
**Exchange messages between the server and client.**

# Troubleshooting
Ensure both machines are on the same network.
Verify the IP address and port used by the server.
Check firewall settings that might block the connection.
