from flask import Flask, request

app = Flask(__name__)
token = "abc123"
@app.route("/person")
def home():
    #creating a pass for accessing data:
    if request.args.get("token") == token:
        return {"name":"ali", "family":"alipour"}
    else:
        return {"error":"Access Denied !!!"}


app.run(host="192.168.1.102", port=80, debug=True)


# import pandas as pd
# import requests
# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# print(response)
#
#
# data = response.json()
#
# for d in data:
#     print(d["userId"], d["title"])
#
# data = pd.read_json(response.json())

from plotly import
