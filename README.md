# fizzbuzz

Overview
================
Flask 와 SQLAlchemy 기반으로 REST Style로 HTTP 요청을 받아, 누적된 요청 횟수를 반환하는 API를 만든다.

Requirements
===============
  - Python 2.7
  
Install
===============
    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install Flask
    $ pip install SQLAlchemy==1.0.8
    $ pip install Flask-SQLAlchemy


How To Run
==============
SQLAlchemy 를 올리기 위해 Python Shell을 실행시킨다.
   
    $ python
    >> from app import db
    >> db.create_all()
    >> exit()

