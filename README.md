# Smart-Security-Camera :camera:

Raspberry Pi security camera running open-cv for object detection.

The camera will send an alert with a photo and video of all the objects it detects.

The alert will be received in the TELEGRAM app. :iphone:

The detection is done with the help of a motion sensor (HC-SR501).

<h2> To-do list before: :page_facing_up: </h2>

<li>

1. This project uses a Raspberry Pi Camera to stream video. make sure to configure the raspberry pi camera on your device.

2. You can install openCV on your raspberry pi by using the following [tutorial](https://www.pyimagesearch.com/2016/04/18/install-guide-raspberry-pi-3-raspbian-jessie-opencv-3/) .

</li>

<h2>:fire: How It Works:</h2> 

The goal was to use it when a person leaves his house and he wants to feel safe, so he runs the system:

The system knows how to communicate with the application and send it commands such as:

Get a time and date, read the last email we received, get a live photo, get a live video.

Once the sensor detects movement in its space the camera starts detecting, if a person's torso is detected and also his face, the camera sends an alert to the app in addition to getting a picture and a short video to see what is happening.

:sound:
Then there is the option to send a command that will sound an alarm to keep the person away from the door.
