from .backend import OraBackend

class QueryClientFactory:
    def __init__(self, backend: str):
        self.backend=backend

    def create(self):
        if self.backend == "ora":
            return OraBackend()
        pass