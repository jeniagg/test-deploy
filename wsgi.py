from flask import Flask
from flask import jsonify
# from flask_restful import Resource, Api

app = Flask(__name__)
# api = Api(app)


class HelloWorld:
    @app.route('/', methods=['GET'])
    def get():
        data = {'bbb': 'aaa'}
        return jsonify(data)
    
    @app.route('/task', methods=['GET'])
    def getNew():
        data = {'hesmllo': 'new'}
        return jsonify(data)


# api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run()

# from flask import Flask
# application = Flask(__name__)

# @application.route("/")
# def hello():
#     return "Hello World!"

# if __name__ == "__main__":
#     application.run()