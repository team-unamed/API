import requests
import dotenv
import json
import os


class KeK:
    def __init__(self, key=None) -> None:
        dotenv.load_dotenv()
        if key:
            self.key = key
        else:
            self.key = os.getenv("key")
        self.endpoint = os.getenv("endpoint")

    
        self.headers = {
            "Content-Type": "application/json",
            "x-api-key": self.key
        }
        print("initalised class")


    def ask(self, question: str, model: str):

        models = {
            "solidity": "cltqjk12m001n35zqh6v2l4jg",
            "bitcoin": ""
        }
        print(self.key)
        if model not in models:
            return "This model does not exist"

        data = {
            "question": question,
            "chat_history": [],
            "knowledge_source_id": "cltqjk12m001n35zqh6v2l4jg"
        }
        print("Reached pre api stage")
        text = requests.post(self.endpoint, headers=self.headers, json=data).json()
        return text