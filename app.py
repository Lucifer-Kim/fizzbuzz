# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/fizzbuzz.db'
db = SQLAlchemy(app)


class Data(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	count = db.Column(db.Integer)
	
	def __init__(self, count):
		self.count = count

@app.route('/1/fizzbuzz', methods=['GET', 'POST'])
def get_response():
	data = Data.query.limit(1).all()
	
	if request.method == 'GET':
		if not data:
			db.session.add(Data(0))
			db.session.commit()

	if request.method == 'POST':
		if data:
			data[0].count += 1
		else:
			db.session.add(Data(1))
		db.session.commit()
	
	data = Data.query.limit(1).all()
	count = data[0].count
		
	if count % 3 == 0 and count % 5 == 0:
		return jsonify({'fizzbuzz':'FizzBuzz'})
	elif count % 3 == 0:
		return jsonify({'fizzbuzz':'Fizz'})
	elif count % 5 == 0:
		return jsonify({'fizzbuzz':'Buzz'})

	return jsonify({'fizzbuzz': count})


if __name__ == '__main__':
	app.run(debug=True)
