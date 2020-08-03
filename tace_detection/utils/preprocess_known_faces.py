import os

import face_recognition
from tqdm import tqdm

PRESENT_PEOPLE = ['Samos', 'chachou', 'pocket']


def _create_known_face_name_and_encoding(known_faces_path):
    known_face_names = []
    known_face_encodings = []
    for profile in tqdm(os.listdir(known_faces_path)):
        ngram = profile.split('.')[0]
        if profile.endswith('.png'):  # and ngram in PRESENT_PEOPLE:
            image = face_recognition.load_image_file(known_faces_path / profile)
            try:
                encoding = face_recognition.face_encodings(image)[0]  # embedding in vector 128
                known_face_encodings.append(encoding)
                known_face_names.append(ngram)
            except IndexError:
                print(f'No face found for {ngram}')
    return known_face_names, known_face_encodings
