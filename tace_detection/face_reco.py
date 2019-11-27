import cv2
import face_recognition

from tace_detection.utils.preprocess_known_faces import _create_known_face_name_and_encoding

process_this_frame = True
known_face_names, known_face_encodings = _create_known_face_name_and_encoding('./pics/')
video_capture = cv2.VideoCapture(0)

while True:
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

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

    process_this_frame = not process_this_frame
    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        cv2.rectangle(frame, (left, top), (right, bottom), (210, 188, 93), 2)
        cv2.rectangle(frame, (left, top + 30), (right, top), (210, 188, 93), cv2.FILLED)
        cv2.rectangle(frame, (left, bottom - 30), (right, bottom), (210, 188, 93), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, top + 24), font, 0.7, (255, 255, 255), 1)

    cv2.imshow('Watcher du TURFU', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
