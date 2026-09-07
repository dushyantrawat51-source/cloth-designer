from flask import Flask, request, jsonify
from flask_cors import CORS

from design import get_designs

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "Cloth Designer Backend Running"


@app.route("/scan", methods=["POST"])
def scan():

    cloth_type = request.form.get(
        "cloth",
        "tshirt"
    )

    designs = get_designs(
        cloth_type
    )

    return jsonify({

        "cloth": cloth_type,
        "designs": designs

    })


if __name__ == "__main__":
    app.run()
