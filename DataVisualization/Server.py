from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from io import BytesIO
import temp1

app = Flask(__name__)
CORS(app)


@app.route("/", methods=['POST'])
def index():
    param = request.get_json()
    if param is not None:
        firstDate = str(param['firstDate'])
        secondDate = str(param['secondDate'])
        item = str(param['item'])
        num = int(param['num'])
        num = num + 1

    img_base64, value1, value2 = temp1.graph(firstDate, secondDate, item)
    valList = [value1, value2]
    response_data = {
        "image": img_base64,
        "valList": valList
    }
    return jsonify(response_data)


@app.route("/menu1", methods=['POST'])
def menu1():
    param = request.get_json()
    if param and 'firstDate' in param and 'secondDate' in param and 'item' in param:
        firstDate = str(param['firstDate'])
        secondDate = str(param['secondDate'])
        item = str(param['item'])
        img_base64, value1, value2 = temp1.graph(firstDate, secondDate, item)
    else:
        img_base64, value1, value2 = temp1.graph()

    valList = [value1, value2]
    response_data = {
        "image": img_base64,
        "valList": valList
    }
    return jsonify(response_data)


@app.route("/menu1/default", methods=['GET'])
def menu1Default():
    img_buffer = temp1.graphDefault()

    return Response(img_buffer, content_type='image/png')


app.run(debug=True, host="0.0.0.0")
