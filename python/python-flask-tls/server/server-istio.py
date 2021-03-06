from flask import Flask
from flask import request
from werkzeug import serving
import logging
import socket
from socket import AF_INET, SOCK_STREAM, SO_REUSEADDR, SOL_SOCKET, SHUT_RDWR
import ssl
import uuid

app = Flask(__name__)

logger = logging.getLogger('python_tls_app')
logger.setLevel(logging.INFO)
fh = logging.FileHandler("python_tls.log")
fh.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(fh)
logger.addHandler(ch)

@app.route("/")
def ping():
    return "Contacted server"

@app.route('/token', methods=['POST'])
def token():
    token = ""
    print(token)
    try:
        logger.info(request.get_json())
        logger.info(request.get_json()['name'])
        logger.info(hash(request.get_json()['name']))
        logger.info(str(uuid.uuid3(uuid.NAMESPACE_DNS, request.get_json()['name'])))
        token = str(uuid.uuid3(uuid.NAMESPACE_DNS, request.get_json()['name']))
    except Exception as e:
        logger.error(e)
    return token

serving.run_simple("0.0.0.0", 5002, app)