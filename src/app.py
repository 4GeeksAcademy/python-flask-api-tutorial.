from flask import Flask, jsonify
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    
]
# These two lines should always be at the end of your app.py file
@app.route('/todos', methods=['GET'])
def get_todos():
     return jsonify(todos)





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
    