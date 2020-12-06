import cv2

cap = cv2.VideoCapture('Traffic_low.mp4')
car_cascade = cv2.CascadeClassifier('cars.xml')

while True:
    ret, frames = cap.read()
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.1, 9)

    for (x,y,w,h) in cars:
        plate = frames[y:y + h, x:x + w]
        cv2.rectangle(frames,(x,y),(x +w, y +h) ,(51 ,51,255),2)
        cv2.rectangle(frames, (x, y - 40), (x + w, y), (51,51,255), -2)
        cv2.putText(frames, 'Car', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        cv2.imshow('car',plate)
        
        if len(car_cascade.detectMultiScale(cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY), 1.1, 9)) > 0:
            print("At this time of the video: " + str(cap.get(cv2.CAP_PROP_POS_MSEC)))

    frames = cv2.resize(frames,(600,400))
    cv2.imshow('Car Detection System', frames)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
