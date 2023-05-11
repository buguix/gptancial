"""Flask application."""
from flask import Flask
from flask import request
from flask import make_response
from flask import Response
from flask import render_template
from .data import get_symbols
from .analytics import generate_analysis
from .analytics import handle_user_question

app = Flask(__name__)

@app.route("/", methods=["GET"])
def rounte_index() -> Response:
    """Test method."""
    return render_template("index.html")


@app.route("/symbols", methods=["GET"])
def route_symbols() -> Response:
    """Test method."""
    res = {"symbols": get_symbols()}
    return make_response(res, 200)


@app.route("/generate", methods=["POST"])
def route_generate() -> Response:
    """Test method."""
    symbol = request.get_json().get("symbol")
    financial, gpt = generate_analysis(symbol=symbol)
    return make_response({"financial": financial, "gpt": gpt}, 200)


@app.route("/chat", methods=["POST"])
def route_chat() -> Response:
    """Test method."""
    req_data = request.get_json()
    symbol = req_data.get("symbol")
    user_question = req_data.get("user_question")
    financial_data = req_data.get("financial_data")
    answer = handle_user_question(symbol=symbol, user_question=user_question, prompt_data=financial_data)
    return make_response({"answer": answer}, 200)


if __name__ == "__main__":
    app.run()
