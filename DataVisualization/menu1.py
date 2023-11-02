import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from io import BytesIO

app = Flask(__name__)
CORS(app)

# @app.route("/", methods=['POST'])
# def index():
#     param = request.get_json()
#     date1 = float(param['date1'])
#     date2 = float(param['date2'])
#     item = str(param['item'])
#     result = f"{date1} 날짜와 + {date2} 날짜의 + {item} 품목"
#     return jsonify({"msg": result})

@app.route("/menu1/<string:date1>/<string:date2>/<string:item>")
def menu01(date1,date2,item):

        data = pd.read_excel('../sml1.xlsx')
        data.set_index('시점',inplace=True)
        # date1 = "2023-04"
        date1 = float(date1.replace('-','.'))
        # date2 = "2023-08"
        date2 = float(date2.replace('-','.'))
        # item = "사과"
        value1 = float(data.loc[date1,item])
        value2 = float(data.loc[date2,item])

        x = [1,2]
        date = [date1,date2]
        value = [value1,value2]

        plt.figure(figsize=(15, 8))
        plt.bar(x, value, width=0.45)

        plt.annotate('', xytext=(1,value1), xy=(2,value2), xycoords='data',
                arrowprops=dict(arrowstyle='->', color='red', lw=3))

        # 백분율(절댓값)
        per = str(round((value[1]-value[0])*100/value[0],1)) + "%"
        # 백분율 텍스트 위치 지정
        plt.text( (x[0]+x[1])/2, ((value[0]+value[1])/2)*1.1, per)

        plt.xticks(x, date, rotation=45)
        # plt.show()

        img_buffer = BytesIO()
        plt.savefig(img_buffer, format="png")
        img_buffer.seek(0)

        return Response(img_buffer,content_type="image/png")

app.run(debug=True,host="0.0.0.0")





