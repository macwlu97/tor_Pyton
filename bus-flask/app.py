import time
import requests

from flask import Flask , Response
from flask_cors import CORS
from event_bus import EventBus
from flask_socketio import SocketIO, emit

bus = EventBus()
app = Flask(__name__)
cors = CORS(app, origins=['http://localhost:8080'])
socketio = SocketIO(app)

@app.route('/api/v1/popular/<phrase>', methods=['GET'])
def popular(phrase):
    url = "https://api.allegro.pl/offers/listing"
    url += "?phrase="+phrase
    url+="&sort=-popularity"
    # access_token =  'eyJleHAiOjE1NTUxNjIxMTIsInVzZXJfbmFtZSI6IjQ0MTU4NDAyIiwianRpIjoiOTBkYmVlZGMtNzUyZS00ZGYwLTgxZTItZGExMjYyN2M1M2M3IiwiY2xpZW50X2lkIjoiY2U2YjI5ZDdlZjE0NDMxOThiY2UwZDkyZWJlZTQ5MzEiLCJzY29wZSI6WyJhbGxlZ3JvX2FwaSJdfQ.R2Hfu2WJvDjSOblCm0uMYcEMWcx00wMwhX3MPuhLqMAIyRV5bDSaYpL9NBdk52wwFDR4FGWcCsEUACLNqSKDsCJ1FBiTmfspv-zlyOAklChz1nQ8Arkb0VNpv-n5s1in2AdTDtN8z3xJ1g-3gcLKHGF1xrv9NUvS5lFfIWbGJzwmt4HZcglsNgqJLIQjw85ShtBfl9ig7diaga56Ix0cdeR1u3fqoqNPDV2Np6V-s_iUbpsdUDG1uu-gYYbtk_SrPrJJ8QZtPI6qhfbhU9O81wBt7eh4PJCS9QS9qf5X3u9qOKQK75mCZH9GieUYdqEAYZTLMs1yP26RdT777Gn_Gw'
    access_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzY29wZSI6WyJhbGxlZ3JvX2FwaSJdLCJleHAiOjE1NTUyMDcwNjMsImp0aSI6Ijg3Zjg2MmU4LWI0MTAtNGYwYi04YWJlLTRiYmE4ZWZmNDc3OCIsImNsaWVudF9pZCI6ImM1MjYyZWRlNDAzNDRhOTM5OTE3MjQ5ZDBiYTg5ODgyIn0.Zh0ZnSFQbSzFAYCU7B7iok2g0h-faWXwYEUGCHIn3ttZ5jBvFz4oKPQ9kqE_sSmeQPjfsr6eyM75Kp9tkwKTLAqnpzL-GKwSsMEwMCDaVAWY5zxEWWZiVpVDlcApB5KHOIg5SUJBBk9xT5qurxdOmbaqaqJ-zim9cCxJTP3AR8EviEbxWfoPlC1kc1YB5bsVGyGVtTIcBdoLhNCgRfOVnuWtNP15wO7tDY2YZj758mq3PW2arXGqFBgvwLL7aiZqZzOJJzellrWQ8rHW7f_UHaxcd4698VTyToSZB9Sw2Sx74dEhm4Ec73PAXNodMOk_W4L9SQNKW3Ax1OoAu6zPRg"
    result = requests.get(url ,
                           headers={'Content-Type': 'application/json' ,
                                    'Authorization': 'Bearer {}'.format(access_token),
                                    'Accept': 'application/vnd.allegro.public.v1+json'})

    return Response(result , status=200 , mimetype='application/json')

@bus.on('Provider')
def provider_event():
    time.sleep(10)
    emit('deliver_success', {'data':'provider_id'})

@bus.on('Status')
def status_event():
    print("test-status")
    emit('status_success', {"status": "true"})

@socketio.on('connect')
def test_connect():
    emit('after connect', {'data':'Connect Success'})

@socketio.on('deliver')
def deliver_message():
    bus.emit('Provider')

@socketio.on('status')
def status_message():
    bus.emit('Status')

if __name__ == '__main__':
    app.run()
