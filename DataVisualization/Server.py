from flask import Flask, request, jsonify, Response
from flask_cors import CORS
import Chart1, Chart2


app = Flask(__name__)
CORS(app)

Chart2.graphDefault()
# Chart2.graph("2014-04","2021-08","식품")

@app.route("/", methods=['POST'])
def index():
    param = request.get_json()
    if param is not None:
        firstDate = str(param['firstDate'])
        secondDate = str(param['secondDate'])
        item = str(param['item'])
        num = int(param['num'])
        num = num + 1

    img_base64, value1, value2 = Chart1.graph(firstDate, secondDate, item)
    valList = [value1, value2]
    response_data = {
        "image": img_base64,
        "valList": valList
    }
    return jsonify(response_data)


@app.route("/menu1", methods=['POST'])
def menu1():
    param = request.get_json()

    firstDate = str(param['firstDate'])
    secondDate = str(param['secondDate'])
    item = str(param['item'])
    img_base64, value1, value2 = Chart1.graph(firstDate, secondDate, item)

    valList = [value1, value2]
    response_data = {
        "image": img_base64,
        "valList": valList
    }
    return jsonify(response_data)


@app.route("/menu1/default", methods=['GET'])
def menu1Default():
    img_buffer = Chart1.graphDefault()

    return Response(img_buffer, content_type='image/png')


app.run(debug=True, host="0.0.0.0")



