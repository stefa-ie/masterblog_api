from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")


@app.route('/api/posts', methods=['POST'])
def addPost():
    return render_template("index.html")


@app.route('/api/posts/<int:id>', methods=['DELETE'])
def deletePost(id):
    return render_template("index.html")


@app.route('/api/posts/<int:id>', methods=['PUT'])
def updatePost(id):
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5002, debug=True)
