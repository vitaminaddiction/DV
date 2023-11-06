from flask import Flask, request, jsonify, Response
from flask_cors import CORS
import Chart1, Chart2, Chart3, Chart4


app = Flask(__name__)
CORS(app)

# 연도 선택 : 2020, 품목 : 사과
Chart4.graph(selected_year=2019,item='빵')


@app.route("/menu1", methods=['POST'])
def menu1():
    param = request.get_json()

    firstDate = str(param['firstDate'])
    secondDate = str(param['secondDate'])
    item = str(param['item'])

    img_base64, value1, value2 = Chart1.graph(firstDate, secondDate, item)
    Chart1.plt.close()
    valList = [value1, value2]
    response_data = {
        "image": img_base64,
        "valList": valList
    }
    return jsonify(response_data)


@app.route("/menu1/default", methods=['GET'])
def menu1Default():
    img_buffer = Chart1.graphDefault()

    Chart1.plt.close()

    return Response(img_buffer, content_type='image/png')


@app.route("/menu2", methods=['POST'])
def menu2():
    param = request.get_json()

    startMonth = str(param['startDate'])
    endMonth = str(param['endDate'])
    item = str(param['item'])

    img_base64, value1, value2 = Chart2.graph(startMonth, endMonth, item)

    Chart2.plt.close()

    response_data = {
        "image": img_base64,
        "val1List": value1,
        "val2List": value2
    }
    return jsonify(response_data)


@app.route("/menu2/default", methods=['GET'])
def menu2Default():
    img_buffer = Chart2.graphDefault()
    Chart2.plt.close()
    return Response(img_buffer, content_type='image/png')

# @app.route("/menu3", methods=['POST'])
# def menu3():
#     param = request.get_json()
#
#     startMonth = str(param['startDate'])
#     endMonth = str(param['endDate'])
#     item = str(param['item'])
#
#     img_base64, value1, value2 = Chart3.graph(startMonth, endMonth, item)
#
#     Chart3.plt.close()
#
#     response_data = {
#         "image": img_base64,
#         "val1List": value1,
#         "val2List": value2
#     }
#     return jsonify(response_data)
#
#
# @app.route("/menu3/default", methods=['GET'])
# def menu3Default():
#     img_buffer = Chart3.graphDefault()
#     Chart3.plt.close()
#     return Response(img_buffer, content_type='image/png')

@app.route("/menu4", methods=['POST'])
def menu4():
    param = request.get_json()

    selected_year = str(param['selected_year'])
    item = str(param['One'])

    img_base64, value1 = Chart4.graph(selected_year, item)

    Chart4.plt.close()

    response_data = {
        "image": img_base64,
        "val1List": value1
    }
    return jsonify(response_data)


@app.route("/menu4/default", methods=['GET'])
def menu4Default():
    img_buffer = Chart4.graphDefault()
    Chart4.plt.close()
    return Response(img_buffer, content_type='image/png')


app.run(debug=True, host="0.0.0.0")



