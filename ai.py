import cv2
import numpy as np
import time
import sys

net = cv2.dnn.readNet("model2/yolov4-obj_last.weights", "model2/yolov4-obj.cfg")
model = cv2.dnn_DetectionModel(net)
model.setInputParams(scale= 1 / 255, size=(410, 410), swapRB=True)
model.setInputScale(1.0/ 127.5)
model.setInputMean((127.5, 127.5, 127.5))
model.setInputSwapRB(True)
width, height = 720, 480 
# Sınıfları eklemek


classes = []
with open("model2/classes.txt", "r") as file_object:
	for class_name in file_object.readlines():
		class_name = class_name.strip()
		classes.append(class_name)
print(classes)

thresh = 0.6
nms_threshold = 0.4
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

fileName = "C:/Users/PC/Desktop/Programlama/Projeler/YapayZeka/Drone/ds/ds.avi"
codec = cv2.VideoWriter_fourcc('W', 'M', 'V', '2')
frameRate = 30
resolution = (width, height)
videoFileOutput = cv2.VideoWriter(fileName ,codec, frameRate, resolution)

"""def fancyDraw(frame, bbox, l=30, t=5, rt= 1):
	x, y, w, h = bbox
	x1, y1 = x + w, y + h

	
	cv2.rectangle(img, (x,y),(x+w,h+y), color=(0, 0, 255), thickness=2)
	# Top Left  x,y
	cv2.line(img, (x, y), (x + l, y), (0, 0, 255), t)
	cv2.line(img, (x, y), (x, y+l), (0, 0, 255), t)
     # Top Right  x1,y
	cv2.line(img, (x1, y), (x1 - l, y), (0, 0, 255), t)
	cv2.line(img, (x1, y), (x1, y+l), (0, 0, 255), t)
     # Bottom Left  x,y1
	cv2.line(img, (x, y1), (x + l, y1), (0, 0, 255), t)
	cv2.line(img, (x, y1), (x, y1 - l), (0, 0, 255), t)
     # Bottom Right  x1,y1
	cv2.line(img, (x1, y1), (x1 - l, y1), (0, 0, 255), t)
	cv2.line(img, (x1, y1), (x1, y1 - l), (0, 0, 255), t)
	return img
"""

l = 30
t = 1
rt = 1



class AI():
	def __init__(self):
		
		while True:
			# Pencereler

			ret, frame = cap.read()
			fps = cap.get(cv2.CAP_PROP_FPS)
			
			#threshframe = cv2.threshold(frame, 70,255,cv2.THRESH_BINARY)
			# Nesne Tespiti
			
			(class_ids, scores, bboxes) = model.detect(frame, confThreshold=thresh, nmsThreshold=nms_threshold)
			for class_id, score, bbox in zip(class_ids, scores, bboxes):
				(x, y, w, h) = bbox
				print(x, y, w, h)
				bboxes = list(bboxes)
				scores = list(np.array(scores).reshape(1,-1)[0])
				scores = list(map(float, scores))

				indices = cv2.dnn.NMSBoxes(bboxes, scores, thresh, nms_threshold)
				
				#cv2.rectangle (frame, (x, y), (x + w, y + h), cv2.COLOR_BAYER_GR2RGB, 3)
				for i in indices:
					print("FPS: ", cap.get(cv2.CAP_PROP_FPS)) 
					i = i[0]
					box = bboxes[i] 
					x,y,w,h = box[0],box[1],box[2],box[3]
					text2 = (classes[class_ids[i][0]-1].upper() + " " + str(int(score[0] * 100)) + "%")
					if (score[0] * 100 >= 99.5):
						print("Accuracy rate %:100")
						text2 = (classes[class_ids[i][0]-1].upper() + " 100%")
					elif (score[0] * 100 == 84.5):
						print("Accuracy rate %:85")
						text2 = (classes[class_ids[i][0]-1].upper() + " 85%")
					else:
						print("Accuracy rate %:", score[0] * 100)
					
					
					x1, y1 = x + w, y + h

					b1, c1 = x + h, y + w 
					
					#frame = fancyDraw(frame, i, bboxes, bbox)
					text = '%s: %.2f' % (classes[class_ids[i][0]-1].upper(), score[0])
					
					#cv2.putText (frame, text, (x, y - 10), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 250), 2)
					# color=(134, 71, 230)
					#cv2.rectangle(frame, (x, y), (x+w,h+y), color=(255, 255, 255), thickness=1)

					center = (x + w // 2, y + h // 2)
					radius = 2
					cv2.circle(frame, center, radius, (36, 236, 12), 2)
					
					cv2.putText(frame, text2, (box[0] + 10, box[1] + 30),
					cv2.FONT_HERSHEY_COMPLEX, 1, (129, 194, 0), 1)

					# Top Left x, y
					#! color purple (134, 71, 230)
					#? color WhatsApp (18, 140, 126)
					#** color green (129, 194, 0)

					cv2.line(frame, (x, y), (x + l, y), (129, 194, 0), t)
					cv2.line(frame, (x, y), (x, y+l), (129, 194, 0), t)
					cv2.ellipse(frame, (x1 + l, y1 + rt), (rt, rt), 180, 0, 90, (129, 194, 0), t)
					# Top Right  x1,y
					cv2.line(frame, (x1, y), (x1 - l, y), (129, 194, 0), t)
					cv2.line(frame, (x1, y), (x1, y+l), (129, 194, 0), t)
					# Bottom Left  x,y1
					cv2.line(frame, (x, y1), (x + l, y1), (129, 194, 0), t)
					cv2.line(frame, (x, y1), (x, y1 - l), (129, 194, 0), t)
					# Bottom Right  x1,y1
					cv2.line(frame, (x1, y1), (x1 - l, y1), (129, 194, 0), t)
					cv2.line(frame, (x1, y1), (x1, y1 - l), (129, 194, 0), t)

					

					#cv2.line(frame, (x1, y1), (x1, b1 - l), (0, 0, 255), t)
				
			dim = (width, height)
			frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
			
			cv2.imshow("Frame", frame)
			videoFileOutput.write(frame)
			key = cv2.waitKey(1) & 0xFF
			if key == ord("q"):
				break

		cap.release()
		videoFileOutput.release()
		cv2.destroyAllWindows()