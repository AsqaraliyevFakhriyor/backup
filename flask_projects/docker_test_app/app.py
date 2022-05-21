import re
from flask import Flask, jsonify, request, abort
from models import db, Student, School


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db" 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.app = app
db.init_app(app)


@app.route("/")
def home():
    student = [student.format() for student in Student.query.all()]
    school = [school.format() for school in School.query.all()]
    return jsonify({
        "success": True,
        "status_code": 200,
        "students":student,
        "schools": school,
    })


@app.route("/create/school", methods=["POST", "GET"])
def create_shool():
    name = request.args.get("name", None) 
    if name is None:
        abort(400)

    new_shool = School(
        name = name
    )
    db.session.add(new_shool)
    db.session.commit()

    return jsonify({
        "success": True,
        "status_code": 200,
        "id": new_shool.id
    })


@app.route("/create/student", methods=["POST", "GET"])
def create_studnet():
    name = request.args.get("name", None)
    school_id = request.args.get("school_id", None)

    if name is None:
        abort(400)

    if school_id is None:
        new_student = Student(
            name=name
        )

    else:
        new_student = Student(
        name = name,
        school_id = school_id
        )

    db.session.add(new_student)
    db.session.commit()
    print("new student", new_student.name)

    return jsonify({
        "success": True,
        "status_code": 200,
        "id": new_student.id
    })

        