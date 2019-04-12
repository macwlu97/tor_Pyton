import time
from json import dumps
from pkgutil import get_data
import numpy as np

from flask import Flask , request , Response , jsonify , make_response , abort

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello Worlds!'


@app.route('/api/v1/status', methods=['GET'])
def home():
    data = {
        "status": "true"
    }
    js = dumps(data)
    resp = Response(js , status=200 , mimetype='application/json')
    return resp
    # data = []
    # for i in range(1,9):
    #     idstat = dict()
    #     idstat['id'] = i
    #     data.append(idstat)


    # js = dumps(data)
    #
    # resp = Response(js , status=200 , mimetype='application/json')
    # resp.headers['Link'] = 'http://luisrei.com'

    # return resp


@app.route("/api/v1/deliver", methods=["POST"])
def deliver():
    if request.method == "POST":
        if not request.json:
            abort(400)
        print(request.json)
        time.sleep(10)
        return dumps(request.json)




#         name = str(request.data.get('name' , ''))
#         if name:
#             bucketlist = Bucketlist(name=name)
#             bucketlist.save()
#             response = jsonify({
#                 'id': bucketlist.id ,
#                 'name': bucketlist.name ,
#                 'date_created': bucketlist.date_created ,
#                 'date_modified': bucketlist.date_modified
#             })
#             response.status_code = 201
#             return response


if __name__ == '__main__':
    app.run()
