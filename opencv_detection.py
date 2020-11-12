import cv2

my_cascade = cv2.CascadeClassifier('toy.xml')

def detect(gray, frame):
    toys= my_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in toys:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        print("Toy Detected at: "+str(video_capture.get(cv2.CAP_PROP_POS_MSEC)))
    return frame 

video_capture = cv2.VideoCapture('home.mp4')
cv2.startWindowThread()
while True: 
    _, frame = video_capture.read() 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    canvas = detect(gray, frame) 
    cv2.imshow('Video', canvas) 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()