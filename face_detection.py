import sys, cv2 as cv
Mode = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
Mode1 = cv.CascadeClassifier('haarcascade_profileface.xml')
number = 0
cap = cv.VideoCapture(0)
while True:
    ok, img = cap.read()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    students = Mode.detectMultiScale(gray, 1.3, 5)
    students1 = Mode1.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in students1:
        cv.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)
        roi_gray1 = gray[y:y+h, x:x+w]
        roi_color1 = img[y:y+h, x:x+w]
    number = len(students)+len(students1)
    cv.putText(img,"Detected:"+str(number),(23,40), cv.FONT_HERSHEY_PLAIN, 1.0, (0,0,0),2)
    cv.putText(img,"Detected:"+str(number),(20,40), cv.FONT_HERSHEY_PLAIN, 1.0, (255,255,255),2)
    for (x,y,w,h) in students:
            cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
    number = len(students)
    cv.imshow('img',img)
    if cv.waitKey(1) == 27:
        break
cv.destroyAllWindows()
number = str(number)
f = open('log.txt', 'w')
f.write(number)
f.close()
