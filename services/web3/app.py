from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
  return jsonify({"Hello": "from app 3"})

if __name__ == "__main__":
  app.run()