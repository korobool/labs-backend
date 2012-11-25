from SimpleXMLRPCServer import SimpleXMLRPCServer
import random
import cls

class ServerClass():
    def __init__(self):
        self.ai_agent = cls.Classifier()
    def classify_text(self, text):
        genre = self.ai_agent.document_class(text)
        return genre

server = SimpleXMLRPCServer(("", 8001))
server.register_instance(ServerClass())
server.register_introspection_functions()
server.serve_forever()
