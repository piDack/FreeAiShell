from backend import QuoraBackend,OraBackend

class QueryClientFactory:
    def __init__(self, backend: str):
        self.backend=backend
    def create(self):
        if self.backend == "ora":
            return OraBackend
        elif self.backend == "quora":
            return QuoraBackend
        pass