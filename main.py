from flask import Flask
from boto3.session import Session
from funcs import find_file
from const import *

app = Flask(__name__)


@app.route('/')
def home():
    return 'Welcome to the download file from s3 bucket web server'


@app.route('/<obj>', methods=['GET'])
def download_file(obj):
    session = Session(aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
    s3 = session.resource('s3')
    bucket = s3.Bucket(BUCKET_NAME)
    return find_file(bucket, obj)


if __name__ == '__main__':
    app.run(debug=DEBUG, host=HOST, port=PORT)
