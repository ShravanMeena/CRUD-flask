from flask import Flask
from flask_restful import Api
from view.students import Register
from view.students import Login
from view.students import Delete
from view.students import Update


app = Flask(__name__)
api = Api(app)


api.add_resource(Register, '/register')
api.add_resource(Login, '/login')
api.add_resource(Delete, '/delete')
api.add_resource(Update, '/update')

if __name__ == '__main__':
    app.run(debug=True)
