# gRPC Chat Application

A real-time chat application built using gRPC, enabling efficient communication between clients and a server. This simple chat application allows users to join chat rooms and exchange messages in real-time.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Architecture](#architecture)
- [Contributing](#contributing)
- [License](#license)

## Features
- Join a chat room with a unique username.
- Send and receive real-time messages in the chat room.
- Multiple clients can participate in the same chat room.
- Basic message history is preserved.
- Easy-to-extend gRPC-based communication.

## Prerequisites
- Python 3
- gRPC and gRPC Tools (install via `pip install grpcio grpcio-tools`)

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/grpc-chat-application.git
   cd grpc-chat-application

2. Generate the gRPC code from the .proto file:

  ```sh
  python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. chat.proto
  ```

3. Start the server:
  ```sh
  python server.py
  ```

4. Run one or more client instances:
  ```sh
  python client.py
  ```


## Usage
1. Start the server by running `server.py`.
2. Run one or more client instances using `client.py`.
3. Enter a unique username when prompted.
4. Begin sending and receiving messages in the chat room.


## Architecture
- The chat application uses a gRPC server implemented in Python to handle client requests.
- The .proto file defines the service and message types used for communication.
- Clients connect to the server, join a chat room, and send/receive messages through gRPC streams.

