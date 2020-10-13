import cv2
import datetime
import os
import time


def Photo():
    # starting the video
    cap = cv2.VideoCapture(0)
    # width = 640
    cap.set(3, 640)
    # height = 480
    cap.set(4, 480)
    # setting the date
    datetime_ = str(datetime.datetime.now())
    # setting the font
    font = cv2.FONT_HERSHEY_SIMPLEX
    if cap.isOpened():
        # stop the video on a single frame for the next processes
        _, frame = cap.read()
        # releasing camera immediately after capturing picture
        cap.release()
        print("the camera finished to take the photo")
        # creating the file
        cv2.imwrite('img.jpg', frame)
        print("now its a file")
        # reading image
        frame = cv2.imread('img.jpg', 1)
        # shoving into the image the date and time
        # if its an video you need to mange it like an image, frame by frame
        frame = cv2.putText(frame, datetime_, (10, 50), font, 1, (255, 255, 0), 1,
                            cv2.LINE_AA)
        # rewriting the image with the new params
        cv2.imwrite('img.jpg', frame)
        print("now its a rewriting file")


def make_sound():
    file = "Alarm.mp3"
    print("alarm alarm")
    os.system("mpg123 " + file)


def Video(capture_duration):
    # starting the camera
    cap = cv2.VideoCapture(0)
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    # write the frame
    out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))

    start_time = time.time()
    while int(time.time() - start_time) < capture_duration:
        ret, frame = cap.read()
        if ret:
            # creating the file
            out.write(frame)
        else:
            break
    # # Release everything if job is finished
    out.release()
    cap.release()
    cv2.destroyAllWindows()
