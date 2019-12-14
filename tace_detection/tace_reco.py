from datetime import datetime

import cv2
import face_recognition
import pandas as pd
import requests

from tace_detection import detector_path
from tace_detection.utils.octopod_info import get_octopod_info, base_octopod_url, token
from tace_detection.utils.preprocess_known_faces import _create_known_face_name_and_encoding

FONT = cv2.FONT_HERSHEY_DUPLEX

process_this_frame = True
known_face_names, known_face_encodings = _create_known_face_name_and_encoding(detector_path / 'octo')
video_capture = cv2.VideoCapture(0)
detected_octo = pd.DataFrame(columns=['NICKNAME', 'ID', 'TACE'])
df_octo = get_octopod_info()

while True:
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]  # BGR to RGB

    if process_this_frame:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = 'Unknown'

            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            face_names.append(name)

            if name not in detected_octo['NICKNAME'].values and name != 'Unknown':
                id_name = df_octo[df_octo['nickname'] == name.upper()]['id'].iloc[0]
                year = datetime.today().strftime('%Y')
                month = datetime.today().strftime('%m')
                day = datetime.today().strftime('%d')
                url = f'/activity_rate?from_date=01%2F01%2F{year}&to_date={day}%2F{month}%2F{year}&include_pipe=false'
                tace_response = requests.get(base_octopod_url + '/people/' + str(id_name) + url, token)
                tace_name = tace_response.json()['value']
                detected_octo = detected_octo.append({'NICKNAME': name, 'ID': id_name, 'TACE': tace_name},
                                                     ignore_index=True)

    process_this_frame = not process_this_frame

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        rectangle_color = (210, 188, 93)
        cv2.rectangle(frame, (left, top), (right, bottom), rectangle_color, 2)
        cv2.rectangle(frame, (left, top + 30), (right, top), rectangle_color, cv2.FILLED)
        cv2.rectangle(frame, (left, bottom - 30), (right, bottom), rectangle_color, cv2.FILLED)

        text_color = (255, 255, 255)
        if name != 'Unknown':
            tace_raw = detected_octo[detected_octo['NICKNAME'] == name]['TACE'].values[0] * 100
            tace_text = 'TACE: ' + '{0:.2f}%'.format(tace_raw)
            if tace_raw < 70:
                text_color = (0, 0, 255)
            elif tace_raw < 80:
                text_color = (0, 130, 255)
            cv2.putText(frame, name, (left + 6, top + 24), FONT, 0.7, text_color, 1)
            cv2.putText(frame, tace_text, (right - 160, bottom - 8), FONT, 0.7, text_color, 1)

        else:
            cv2.putText(frame, name, (left + 6, top + 24), FONT, 0.7, text_color, 1)

    cv2.imshow('TACE Detector', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
