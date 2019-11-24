from flask import Flask, jsonify

app  = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return jsonify({"result":"OK"})

@app.route("/resources", methods=['GET'])
def get_resources():
    results = []
    return jsonify([])

@app.route("/resources/<int:id>", methods=['GET'])
def get_resource(id):
    return jsonify({"result": id})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)