import grpc
import chat_pb2
import chat_pb2_grpc

class ChatService(chat_pb2_grpc.ChatServiceServicer):
    def __init__(self):
        self.chat_history = []

    def JoinChat(self, request, context):
        for message in self.chat_history:
            yield message

    def SendMessage(self, request, context):
        self.chat_history.append(request)
        return chat_pb2.Empty()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chat_pb2_grpc.add_ChatServiceServicer_to_server(ChatService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
