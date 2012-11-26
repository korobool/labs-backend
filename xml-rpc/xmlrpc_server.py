from SimpleXMLRPCServer import SimpleXMLRPCServer
import cls

class ServerClass():
    def __init__(self):
        self.ai_agent = cls.Classifier()
    def classify_text(self, text):
        genre = self.ai_agent.document_class(text)
        return genre
    def get_genres_list(self):
        return self.ai_agent.genres

server = SimpleXMLRPCServer(("", 8001))
server.register_instance(ServerClass())
server.register_introspection_functions()
server.serve_forever()
