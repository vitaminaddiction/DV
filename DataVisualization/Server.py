from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from io import BytesIO

app = Flask(__name__)
CORS(app)


@app.route("/", methods=['POST'])
def index():
    param = request.get_json()
    
    year = 2023 # 현재 고정상태
    # 일단 date 한개만 받는다고 가정

    date = str(param['date']) # 날짜1

    # date = str(param['date2'])  # 날짜2


    msg = str(param['msg']) # 몇퍼 올랐다 내렸다 결과
    num = int(param['num']) # 품목의 인덱스
    num = num + 1 # 품목이 해당된 인덱스


    print(date)
    print(msg)
    print(num)


    return jsonify({"msg": num})


@app.route("/img1/<int:x>/<int:y>")
def img1(x, y):
    # x가 날짜, y가 품목
    print(x)
    print(y)
    plt.figure(figsize=(4, 3))
    plt.scatter(kn.bream_length, kn.bream_weight)
    plt.scatter(kn.smelt_length, kn.smelt_weight)
    plt.scatter(kn.my_length, kn.my_weight)
    plt.scatter(x, y, s=100)

    img_buffer = BytesIO()
    plt.savefig(img_buffer, format="png")
    img_buffer.seek(0)

    return Response(img_buffer, content_type='image/png')


app.run(debug=True, host="0.0.0.0")
