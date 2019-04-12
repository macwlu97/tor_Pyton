from json import dumps
from pkgutil import get_data
import numpy as np

from flask import Flask , request , Response , jsonify , make_response

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello Worlds!'


@app.route('/api/v1/status', methods=['GET'])
def home():
    arr = [1,2,3,4,5]
    # arr = np.random.randint(5 , size=(2 , 4))
    # response = jsonify({
    #                 'id': bucketlist.id ,
    #             })
    # response.status_code = 201
    # return response
    return make_response(dumps(arr))


# @app.route('/hello', methods = ['GET'])
# def api_hello():
#     data = {
#         'hello'  : 'world',
#         'number' : 3
#     }
#     js = dumps(data)
#
#     resp = Response(js, status=200, mimetype='application/json')
#     resp.headers['Link'] = 'http://luisrei.com'
#
#     return resp

#
# @app.route("/api/v1/deliver", methods=["POST"])
# def bucketlists():
#     if request.method == "POST":
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
