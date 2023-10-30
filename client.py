import grpc
import chat_pb2
import chat_pb2_grpc

def chat_client():
    channel = grpc.insecure_channel('localhost:50051')
    stub = chat_pb2_grpc.ChatServiceStub(channel)

    username = input("Enter your username: ")
    join_request = chat_pb2.JoinRequest(username=username)
    chat_stream = stub.JoinChat(join_request)

    for message in chat_stream:
        print(f'{message.username}: {message.text}')

    while True:
        message_text = input(f'{username}: ')
        chat_message = chat_pb2.ChatMessage(username=username, text=message_text)
        stub.SendMessage(chat_message)

if __name__ == '__main__':
    chat_client()
