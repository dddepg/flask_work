from flask_cors import CORS, cross_origin
from flask import Flask
app = Flask(__name__)
cors = CORS(app)


import graduateBack.loginAndGetlines
import graduateBack.getUserInfo
import graduateBack.updata
import graduateBack.downloadFile
import graduateBack.addpdfInfo
import graduateBack.getallPaper
import graduateBack.updatePdfInfo
import graduateBack.getMyPaper