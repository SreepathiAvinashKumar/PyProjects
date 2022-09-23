import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)


try:
 while True:
    _,image=cap.read()
    image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(image_gray,1.3,5)
    for x,y,width,height in faces:
         cv2.rectangle(image,(x,y),(x+width,y+height),color=(255,0,0),thickness=3)
         cv2.imshow('FaceDetection',image)
    if cv2.waitKey(1)==ord('q'):
            break
 cap.release()    
 cv2.destroyAllWindows()        
except KeyboardInterrupt:
    print("Exception Occured")
  
