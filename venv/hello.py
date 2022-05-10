from flask import Flask
from multiprocessing import shared_memory as sharedmem

app = Flask(__name__)

shm = sharedmem.SharedMemory(create=True, size=10)
shm.buf[0:1] = bytearray([12, ])


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/hej")
def hej():
    value = int(shm.buf[0:1].hex(), 16)
    return "<h>Testing SHM for Flask</h>" \
           "<p>Value read from SHM: %s </p>" % value


@app.route("/changeValue")
def changeVal():
    shm.buf[0:1] = bytearray([3, ])
    return "<h> Changed valued... </h>"
