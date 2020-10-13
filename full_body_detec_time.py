# import numpy as np
import time
import cv2
import datetime


def body_detection(capture_duration):
    # load the required XML classifiers
    face_cascade = cv2.CascadeClassifier('facial_recognition_model.xml')
    low_cascade = cv2.CascadeClassifier('haarcascade_upperbody.xml')
    datetime_ = str(datetime.datetime.now())
    font = cv2.FONT_HERSHEY_SIMPLEX
    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('output2.mp4', fourcc, 20.0, (640, 480))
    is_change_occurred = False
    faces_len = 0
    low_len = 0

    start_time = time.time()
    while int(time.time() - start_time) < capture_duration:
        # capture frame-by-frame
        ret, img = cap.read()
        if ret:
            out.write(img)
            pic = cv2.putText(img, datetime_, (10, 50), font, 1, (255, 255, 0), 1, cv2.LINE_AA)
            out.write(pic)

        # Convert frame to Black white and gray
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        low = low_cascade.detectMultiScale(gray, 1.1, 3)

        # Drawing around the detected "face"
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        for (x, y, w, h) in low:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.imshow('frame', img)

        if len(faces) == len(low) and len(faces) != 0:
            if faces_len != len(faces) or low_len != len(low):
                is_change_occurred = True
            else:
                is_change_occurred = False

            faces_len = len(faces)
            low_len = len(low)

            if is_change_occurred and faces_len >= 1:
                out.write(img)
                cv2.imwrite('intruder.jpg', img)
                pic = cv2.imread('intruder.jpg', 1)
                pic = cv2.putText(img, datetime_, (10, 50), font, 1, (255, 255, 0), 1, cv2.LINE_AA)
                cv2.imwrite('intruder.jpg', pic)
                return True

            if (is_change_occurred == False) and (faces_len == 0):
                return False

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # os.remove('intruder.jpg')
    print(" every thing is ok")
    # Stop recording
    out.release()
    # #Kill all windows
    cap.release()
    cv2.destroyAllWindows()
