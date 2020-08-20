from flask import Flask, render_template, request, send_file

from getnewimage import getnewImage
import base64
from io import BytesIO
import dnnlib
from PIL import Image
import os
import gdown

# get pretrained pkl from google drive server if it isn't there already

url = "https://drive.google.com/uc?id=19wQe12syOYopUVA_eEHUdiqtdIKl4m7L"
output = 'pretrained/masks-early.pkl'
if os.path.isfile(output) is False:
    print('file not found, downloading from google drive')
    gdown.download(url, output)



# initialize tensorflow session

dnnlib.tflib.init_tf()


# initialize app

app = Flask(__name__)


# convert returned image
def serve_pil_image(pil_img):
    img_io = BytesIO()
    pil_img.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')

# serve index page
@app.route('/')
def dynamic_page():
    return render_template('index.html')

# serve image
@app.route('/generate', methods=['POST', 'GET'])
def getimage():
    data = getnewImage()
    return serve_pil_image(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=True, threaded=False)