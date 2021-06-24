
from flask import Flask,jsonify

app= Flask(__name__)

students = [{'name':"Himanshu",
             'student_id':"0",
             'role':"Back-end developer"},
            {'name':"Rohit",
             'student_id':"1",
             'role':"Back-end developer"},
            {'name':"Aman",
             'student_id':"2",
             'role':"Front-end developer"}
            ]

@app.route('/')
def index() :
    return "Hello, Welcome"

@app.route('/students', methods=['GET'])
def get():
    return jsonify({'Students':students})

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    return jsonify({'students': students[student_id]})

if __name__ == "__main__":
    app.run(debug=True)
