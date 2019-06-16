from flask import Flask
from flask import request
from flask import jsonify
from flask import Response
from flask import make_response
import fitness


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world!"

@app.route("/other")
def other_hello():
    return "Hello other world!"

@app.route("/fitness", methods=['GET', 'POST'])
def read_json():
    content = request.get_json(force=True)
    print(content)
    answer = fitness.handle(content)
    respData =jsonify({"payload": {
        "google": {
            "expectUserResponse": False,
            "richResponse": {
                "items": [
                    {"simpleResponse": {
                        "textToSpeech": answer
                    }
                }
                ]
            }
        }
    }
    })

    resp = make_response(respData, 200)
    resp.headers['Content-Type'] = 'application/json'
    resp.mimetype = "application/json"
    return resp

app.run()