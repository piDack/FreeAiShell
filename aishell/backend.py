import sys
from abc import ABCMeta, abstractmethod
#sys.path.append("./gpt4free/")
# import quora (poe) package
class Backend:
    @abstractmethod
    def query(self,prompt: str) -> str:
        pass

from .ora import CompletionModel,Completion
class OraBackend(Backend):
    def __init__(self):
        self.model = CompletionModel.create(
        system_prompt = 'You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible',
        description   = 'ChatGPT Openai Language Model',
        name          = 'gpt-3.5')

    def query(self, prompt: str) -> str:
        response = Completion.create(
            model  = self.model,
            prompt = prompt)
        return response.completion.choices[0].text
