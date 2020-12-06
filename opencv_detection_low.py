import cv2

c = cv2.VideoCapture('Traffic_low.mp4')
cc = cv2.CascadeClassifier('cars.xml')

while True:
    ret, f = c.read()
    if not ret:
        break

    if len(cc.detectMultiScale(cv2.cvtColor(f, cv2.COLOR_BGR2GRAY), 1.1, 9)) > 0:
<<<<<<< HEAD
        print("At this time of the video " + str(c.get(cv2.CAP_PROP_POS_MSEC)))
=======
        print(At this time of the video  + str(c.get(cv2.CAP_PROP_POS_MSEC)))
>>>>>>> 19d1d8069aa08d7b289ab19e186c7dd3451d5d21
