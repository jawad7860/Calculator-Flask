from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/calculate", methods = ["POST"])
def Calculate():
    
    try:
        result = ""
        body = request.get_json()
        a, b = int(body["a"]), int(body["b"])

        if (body["operator"] == "+"):
            result = a + b
        elif (body["operator"] == "-"):
            result = a - b
        elif (body["operator"] == "*"):
            result = a * b
        elif (body["operator"] == "/"):
            result = a / b
        else:
            result = "not a valid request"

        return str(result)

    except Exception as e:
        return e
    
if __name__ == '__main__':
	app.run(host="0.0.0.0")