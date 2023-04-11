import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename

from collection import save_image_known_in_database, get_collection
from recognition.face import make_collection, recognition
from person import Person
import base64
import imghdr

UPLOAD_FOLDER = 'recognition/known'
UPLOAD_FOLDER_UNKNOWN = 'recognition/unknown'

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.secret_key = "secret key"
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_FOLDER_UNKNOWN'] = UPLOAD_FOLDER_UNKNOWN
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024



ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/add_person', methods=['POST'])
def create_person():
    # extract information from request
    last_name = request.form.get('last_name')
    first_name = request.form.get('first_name')
    address = request.form.get('address')
    email = request.form.get('email')
    birthday = request.form.get('birthday')
    description = request.form.get('description')
    filename = ""
    
    collection = []
    file = request.files['file']
    if file and allowed_file(file.filename):
        # collection = get_collection()
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        collection = make_collection(f'{UPLOAD_FOLDER}/{filename}')
        save_image_known_in_database(collection)

    person = Person(last_name=last_name, first_name=first_name, address=address, email=email, birthday=birthday, description=description, photo_filename=filename)
    person.save_to_database()
    
    return jsonify({'message': 'Person created successfully'}), 201

@app.route('/recognition', methods=['POST'])
def recognition_faces():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER_UNKNOWN'], filename))
        collection = get_collection()
        face = recognition(f'{UPLOAD_FOLDER_UNKNOWN}/{filename}', collection)
        if face:
            result = Person.get_info_from_database(face)
            filename = f'{UPLOAD_FOLDER}/{result[6]}'
            with open(filename, 'rb') as f:
                image_data = f.read()
            mime_type = 'image/' + imghdr.what(None, h=image_data)
            return jsonify({
                'last_name': result[0],
                'first_name': result[1],
                'address': result[2],
                'email': result[3],
                'birthday': result[4],
                'description': result[5],
                'filename': base64.b64encode(image_data).decode('utf-8'),
                'mime_type': mime_type
                }), 201
        else:
            return jsonify({'message': 'Cette personne n\' est pas dans la base de donnée'})


if __name__ == "__main__": 
    app.run()