from pymongo import MongoClient
import requests           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.




@app.route('/')
def home():
   return render_template('index.html')


@app.route('/candle', methods=['GET'])
def listing():
      orders = list(db.candleOrder.find({}, {'_id': 0}))
      return jsonify({'result': 'success', 'orders': orders})


# API 역할을 하는 부분
@app.route('/candle', methods=['POST'])
def orders():
      name_receive = request.form['name_give']
      number_receive = request.form['number_give']
      address_receive = request.form['address_give']
      phone_receive = request.form['phone_give']

      order = {
         'name': name_receive,
         'number': number_receive,
         'address': address_receive,
         'phone': phone_receive,
      }

      db.candleOrder.insert_one(order)
      return jsonify({'result':'success', 'msg':'주문이 정상처리되었습니다!'})

if __name__ == '__main__':
       app.run(port=5000, debug=True)