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

        self.models = {
            "solidity": "cltqjk12m001n35zqh6v2l4jg",
            "bitcoin": "cls3bm1yf00017drv1rv2p137",
            "ethereum": "cls4frht2000njy824nn3c7g5",
            "ton": "cluls3lx70001144zx1dfd6mu"
        }
        print(self.key)
        if model not in self.models:
            return "This model does not exist"

        data = {
            "question": question,
            "chat_history": [],
            "knowledge_source_id": self.models[model]
        }
        print("Reached pre api stage")
        text = requests.post(self.endpoint, headers=self.headers, json=data).json()
        return text