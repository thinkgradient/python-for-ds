import os
import json
from openai import AzureOpenAI

class ChatBotClient:
    def __init__(self):
     
       
        self.client = AzureOpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            api_version=os.getenv("OPENAI_API_VERSION"),
            azure_endpoint=os.getenv("OPENAI_API_BASE")
        )
        
    def get_chat_response(self, messages):
        """
        Sends messages to the OpenAI chat model and returns the response.
        
        Parameters:
        messages (list): A list of message dictionaries with "role" and "content" keys.
        
        Returns:
        str: The content of the response message from the AI model.
        """
        chat_completion = self.client.chat.completions.create(
            model="gpt-4-Turbo",  # Model = "deployment_name".
            messages=messages,
            temperature=0,
            top_p=0.95,
            presence_penalty=0,
            frequency_penalty=0
        )
        response_json = json.loads(chat_completion.model_dump_json(indent=2))
        return response_json['choices'][0]['message']['content']