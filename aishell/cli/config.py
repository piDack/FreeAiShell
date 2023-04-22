import yaml
import os
CONFIG_FILE = 'config.yaml'
DEFAULT_BACKEND = 'ora'
VALID_BACKENDS = ['quora', 'phind', 't3nsor', 'ora', 'writesonic', 'you', 'cocalc']

class Config:
    def __init__(self, backend):
        self.backend = backend

    def save(self):
        data = {'backend': self.backend}
        with open(CONFIG_FILE, 'w') as f:
            yaml.dump(data, f)

    @classmethod
    def load(cls):
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, 'r') as f:
                data = yaml.safe_load(f)
            return cls(data['backend'])
        else:
            return cls(DEFAULT_BACKEND)

    @property
    def backend(self):
        return self._backend

    @backend.setter
    def backend(self, value):
        if value not in VALID_BACKENDS:
            raise ValueError(f"Invalid backend: {value}, valid backends are {VALID_BACKENDS}")
        self._backend = value