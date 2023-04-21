import sys
from abc import ABCMeta, abstractmethod
sys.path.append("../../gpt4free/")
# import quora (poe) package
import quora

class Backend:
    @abstractmethod
    def query(self,prompt: str) -> str:
        pass
        
class QuoraBackend(Backend):
    def __init__(self):
        self.token = quora.Account.create(logging = True, enable_bot_creation=True)
        self.model = quora.Model.create(
            token = self.token,
            model = 'gpt-3.5-turbo', # or claude-instant-v1.0
            system_prompt = 'you are ChatGPT a large language model ...' 
        )

    def query(self, prompt: str) -> str:
        response = quora.Completion.create(
            custom_model = self.model,
            prompt       = prompt,
            token        = self.token)
        return response.completion.choices[0].text

import ora
class QuoraBackend(Backend):
    def __init__(self):
        self.model = ora.CompletionModel.create(
        system_prompt = 'You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible',
        description   = 'ChatGPT Openai Language Model',
        name          = 'gpt-3.5')

    def query(self, prompt: str) -> str:
        response = ora.Completion.create(
            model  = self.model,
            prompt = prompt)
        return response.completion.choices[0].text