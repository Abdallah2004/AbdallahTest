import os


DEBUG = False
SECRET_KEY = 'topsecret'
SQLALCHEMY_DATABASE_URI=os.environ['postgres://hrliqysnjbjdgw:67b169670dd95bac7676f136bba51832682a8403073d86f76e815a4e1c858da7@ec2-54-228-243-238.eu-west-1.compute.amazonaws.com:5432/d72qs1qv3dphch']
SQLALCHEMY_TRACK_MODIFICATIONS = False