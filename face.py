import cv2
import os

a = 0   
id = 0
objek1 ="ooka"
objek2 ="pratama" 
video = cv2.VideoCapture('tes.mp4')

detection = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('DataSet/training.xml')
 
while True:
	a = a + 1
	
	ret, frame = video.read()
	warna = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	face = detection.detectMultiScale(warna,1.3,5)
	for (x,y,w,h) in face:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)
		id, conf = recognizer.predict(warna[y:y+h,x:x+w])
		if (id==1):
			id = objek1
		elif (id==2):
				id = objek2

		cv2.putText(frame,str(id),(x+40,y-10),cv2.FONT_HERSHEY_DUPLEX,1.5,(0,255,0))
	cv2.imshow("Face Recognition", frame)
	if (cv2.waitKey(90)==ord('p')) :
		break
video.release()
cv2.destroyAllWindows()

