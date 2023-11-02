from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from io import BytesIO
import temp1

app = Flask(__name__)
CORS(app)


@app.route("/", methods=['POST'])
def index():
    param = request.get_json()

    firstDate = str(param['firstDate'])
    secondDate = str(param['secondDate'])
    item = str(param['item'])
    num = int(param['num'])
    num = num + 1
    print(item, firstDate, secondDate)
    img_base64, value1, value2 = temp1.graph(firstDate, secondDate, item)

    response_data = {
        "image": img_base64,
        "value1": value1,
        "value2": value2
    }
    return jsonify(response_data)


app.run(debug=True, host="0.0.0.0")
