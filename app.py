import base64
from io import BytesIO
from flask import Flask, jsonify, request
from flask_cors import CORS
from PIL import Image
from captcha import CaptchaSolver
from datetime import datetime
import random
import string
app = Flask(__name__)
CORS(app)

def scale_image(img, target_width, target_height):
    img = img.resize((target_width, target_height), Image.LANCZOS)
    return img

def generate_filename():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    random_letters = ''.join(random.choices(string.ascii_lowercase, k=5))
    return f"captchaphotos/{timestamp}_{random_letters}.jpg"

@app.route('/solve', methods=['POST', 'GET'])
def solver():
    data = request.get_json()
    rimg = data['image'].replace('data:image/jpg;base64,', '')
    image_data = base64.b64decode(rimg)
    img = Image.open(BytesIO(image_data))
    
    #saves captcha
    filename = generate_filename()
    img.save(filename)
    img = scale_image(img, 640, 640)
    
    solver = CaptchaSolver(img)
    result = solver.predict()
    answer = solver.get_answer(result)
    return jsonify({"answer":answer})
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)