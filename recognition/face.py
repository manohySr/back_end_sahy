"""
    subject: get 2 images, each images should be encoded before being compared


    Having a collection of a known people: set

    #1 function which add known people encoded in the collection: list 
    
    #2 function which take the image and encode it (return the encoded image)

    #3 function who compare 2 images (the reference one and the unknown one) (return boolean)

    #4 function who loop all the image(reference) use the function #3 (return the name of the person)

"""
import face_recognition
import os

import face_recognition
def encode_image(image_path):
    image = face_recognition.load_image_file(image_path)
    encoded_image = face_recognition.face_encodings(image)[0]
    return encoded_image


def compare_faces(image_encoded_unknown, image_encoded_known):
    result = face_recognition.compare_faces([image_encoded_known], image_encoded_unknown)
    return result

def make_collection(image_path):
    file_name = os.path.basename(image_path)
    person_name = os.path.splitext(file_name)[0]

    face_encoded = encode_image(image_path)
    return [person_name, face_encoded]

def recognition(image_unknown, collection_of_known_people):

    image_encoded_unknown = encode_image(image_unknown)
    for person_data in collection_of_known_people:
        result = compare_faces(image_encoded_unknown, person_data[1])[0]
        if result:
            return person_data[0]

    return False
        
"""
    I use those function in my main app:
        make_collection(collection, image_path) -> collection ['Name of file', the encoded image]
        recognition(image_unknown, collection_of_known_people) -> 'Name of file' or False

"""



# collection = []
# collection = [make_collection("./known/Manohy.jpg")]
# collection.append(make_collection("./known/Danielyh.jpg"))


# print(recognition("./unknown/Manohy.jpg", collection))
# print(recognition("./unknown/6.jpg", collection))
