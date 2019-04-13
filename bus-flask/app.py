import time
from json import dumps
import json
import requests

from flask import Flask , Response , jsonify , make_response , abort , request
from flask_cors import CORS
from requests.auth import HTTPDigestAuth

app = Flask(__name__)
cors = CORS(app, origins=['http://localhost:8080'])

@app.route('/')
def hello_world():
    return 'Hello Worlds!'

@app.route('/api/v1/popular/<phrase>', methods=['GET'])
def popular(phrase):
    url = "https://api.allegro.pl.allegrosandbox.pl/offers/listing"
    url += "?phrase="+phrase
    url+="&sort=-popularity"

    access_token =  'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NTUxNjIxMTIsInVzZXJfbmFtZSI6IjQ0MTU4NDAyIiwianRpIjoiOTBkYmVlZGMtNzUyZS00ZGYwLTgxZTItZGExMjYyN2M1M2M3IiwiY2xpZW50X2lkIjoiY2U2YjI5ZDdlZjE0NDMxOThiY2UwZDkyZWJlZTQ5MzEiLCJzY29wZSI6WyJhbGxlZ3JvX2FwaSJdfQ.R2Hfu2WJvDjSOblCm0uMYcEMWcx00wMwhX3MPuhLqMAIyRV5bDSaYpL9NBdk52wwFDR4FGWcCsEUACLNqSKDsCJ1FBiTmfspv-zlyOAklChz1nQ8Arkb0VNpv-n5s1in2AdTDtN8z3xJ1g-3gcLKHGF1xrv9NUvS5lFfIWbGJzwmt4HZcglsNgqJLIQjw85ShtBfl9ig7diaga56Ix0cdeR1u3fqoqNPDV2Np6V-s_iUbpsdUDG1uu-gYYbtk_SrPrJJ8QZtPI6qhfbhU9O81wBt7eh4PJCS9QS9qf5X3u9qOKQK75mCZH9GieUYdqEAYZTLMs1yP26RdT777Gn_Gw'


    result = requests.get(url ,
                           headers={'Content-Type': 'application/json' ,
                                    'Authorization': 'Bearer {}'.format(access_token),
                                    'Accept': 'application/vnd.allegro.public.v1+json'})

    resp = Response(result , status=200 , mimetype='application/json')
    return resp


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

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
