
from flask_cors import CORS, cross_origin
from flask import Flask
app = Flask(__name__)
cors = CORS(app)

import graduateBack.views
