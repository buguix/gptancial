"""Flask application."""
from flask import Flask
from flask import request
from flask import make_response
from flask import Response
from flask import render_template
from .data import get_symbols
from .analytics import generate_analysis

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
def route_ping() -> Response:
    """Test method."""
    symbol = request.get_json().get("symbol")
    financial, gpt = generate_analysis(symbol=symbol)
    return make_response({"financial": financial, "gpt": gpt}, 200)


if __name__ == "__main__":
    app.run()
