from flask import Flask,jsonify,request
from data import data
app = Flask(__name__)

@app.route('/')
def first_page():
  return jsonify({
      "data" : data,
      "message" : "Success"
  }),200

@app.route('/star')
def description():
    name = request.args.get("Stars")
    star_data = (neb for neb in data if neb["Stars"] == name)
    return jsonify({
       "data" : star_data,
       "message" : "Success"
    }),200


if __name__ == "__main__":
    app.run()