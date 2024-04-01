from flask import Flask, jsonify, request
from ai import KeK


app = Flask(__name__)


@app.route("/", methods=["GET"])
def check_status():
    return "Welcome to the Unamed A.I"


@app.route("/ask", methods=["POST"])
def ask(api_key=None):

    question = request.args.get("question")
    model = request.args.get("model")
    api_key = request.args.get("api_key")
    kek = KeK(api_key)


    answer = kek.ask(question, model)
    print(answer)
    if answer == "This model does not exist":
        return jsonify("This model does not exist"), 404
    else:
        return answer, 200


if __name__ == "__main__":
    app.run(debug=True)
