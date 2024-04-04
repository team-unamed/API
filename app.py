from flask import Flask, jsonify, request
from ai import KeK
import os
from dotenv import load_dotenv
from flask_cors import CORS


app = Flask(__name__)
load_dotenv()


CORS(app)


master_keys = os.getenv("master_keys")
print(master_keys)
@app.route("/", methods=["GET"])
def check_status():
    return "Welcome to the Unamed A.I"


@app.route("/ask", methods=["POST"])
def ask(api_key=None):

    question = request.args.get("question")
    model = request.args.get("model")
    api_key = request.args.get("api_key")
    master_key = request.args.get("master_key")
    kek = KeK(api_key)

    if master_key not in master_keys:
        return jsonify("Invalid master key"), 401


    answer = kek.ask(question, model)
    print(answer)
    if answer == "This model does not exist":
        return jsonify("This model does not exist"), 404
    else:
        return answer, 200


