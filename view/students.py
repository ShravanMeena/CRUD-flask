from flask_restful import Resource
from flask import request, jsonify

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

DATABASE_URL = "postgres://minjavhilkiuxq:67d77a9e62ff7092cdf6a082aad7214fc1fd79c98c54b94628d591ec0066d6f3@ec2-3-224-97-209.compute-1.amazonaws.com:5432/d67mvtuvg2g5b0"

# Set up database
engine = create_engine(DATABASE_URL)
db = scoped_session(sessionmaker(bind=engine))


class Register(Resource):
    # registrations api
    def post(self):
        data = request.get_json()

        name = data["name"]
        email = data["email"]
        password = data["password"]
        phone = data["phone"]
        semester = data["semester"]
        course_name = data["course_name"]
        room_number = data["room_number"]

        result = db.execute("SELECT phone FROM students WHERE phone=:phone",
                            {"phone": phone}).fetchall()
        db.commit()
        db.close()

        if not result:
            db.execute("INSERT INTO students(name,email,password,phone,semester,course_name,room_number) VALUES(:name,:email,:password,:phone,:semester,:course_name,:room_number)",
                       {"name": name, "email": email, "password": password, "phone": phone, "semester": semester, "course_name": course_name, "room_number": room_number})

            db.commit()
            db.close()

            response = {
                "status": "true",
                "message": "student register successfully",
                "token": "aakdha98a8sd9sad8saduasu9d8uas9ud9sadhas9asc8d77eq92zw9qmw9qxe9yec7ey91sv97e93783"
            }
            return jsonify(response)

        else:
            response = {
                "status": "false",
                "message": "You are already registered"
            }
            return jsonify(response)


class Login(Resource):
    # login api
    def post(self):
        data = request.get_json()

        phone = data["phone"]
        password = data["password"]

        result = db.execute("SELECT * FROM students WHERE phone=:phone AND password=:password",
                            {"phone": phone, "password": password}).fetchall()
        db.commit()
        db.close()

        if result:
            response = {
                "status": "true",
                "message": "you are logged in successully",
            }
            return jsonify(response)

        else:
            response = {
                "status": "false",
                "message": "User not found",
            }
            return jsonify(response)


class Delete(Resource):
    def delete(self):
        data = request.get_json()

        id = data["id"]

        result = db.execute("DELETE FROM students WHERE id =:id", {"id": id})
        db.commit()
        db.close()
        if result:
            response = {
                "status": "true",
                "message": "User deleted successfully"
            }
            return jsonify(response)
        else:
            response = {
                "status": "false",
                "message": "User not found"
            }
            return jsonify(response)


class Update(Resource):
    def put(self):
        data = request.get_json()

        name = data["name"]
        email = data["email"]
        password = data["password"]
        phone = data["phone"]
        semester = data["semester"]
        course_name = data["course_name"]
        room_number = data["room_number"]

        db.execute("INSERT INTO students(name,email,password,phone,semester,course_name,room_number) VALUES(:name,:email,:password,:phone,:semester,:course_name,:room_number)",
                   {"name": name, "email": email, "password": password, "phone": phone, "semester": semester, "course_name": course_name, "room_number": room_number})
        db.commit()
        db.close()

        response = {
            "status": 'true',
            "message": 'User data updated successfully'
        }
        return jsonify(response)
