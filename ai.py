import cv2
import numpy as np
import time
import sys
import os
from gui_buttons import Buttons


net = cv2.dnn.readNet("model/yolov4-obj_last.weights", "model/yolov4-obj.cfg")
model = cv2.dnn_DetectionModel(net)
model.setInputParams(scale= 1 / 255, size=(410, 410), swapRB=True)
model.setInputScale(1.0/ 127.5)
model.setInputMean((127.5, 127.5, 127.5))
model.setInputSwapRB(True)
width, height = 720, 480 
# Sınıfları eklemek


classes = []
with open("model/classes.txt", "r") as file_object:
     for class_name in file_object.readlines():
          class_name = class_name.strip()
          classes.append(class_name)
print(classes)

thresh = 0.5
nms_threshold = 0.3
kumanda_aralık=10
a = 0
distance = 0
whT = 320

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

fileName = "C:/Users/PC/Desktop/Programlama/Projeler/YapayZeka/Missileme Programı/ds/ds.avi"
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
t = 3
rt = 1


def click_button(event, x, y, flags, params):
     global button_person
     if event == cv2.EVENT_LBUTTONDOWN:
          button.button_click(x, y)
          return 0





class AI():
     def __init__(self):
          cv2.namedWindow("Frame")
          cv2.setMouseCallback("Frame", click_button)
          while True:
               # Pencereler

               ret, frame = cap.read()
               
               
               
               dim = (width, height)
               #frame = cv2.resize(frame, dim)
               #threshframe = cv2.threshold(frame, 70,255,cv2.THRESH_BINARY)
               # Nesne Tespiti

               blob = cv2.dnn.blobFromImage(frame, 1 / 255, (whT, whT), [0, 0, 0], 1, crop=False)

               net.setInput(blob)

               layerNames = net.getLayerNames()
               
               outputNames = [layerNames[i - 1] for i in net.getUnconnectedOutLayers()]

               cv2.rectangle(frame, (int(frame.shape[1] / 4), int(frame.shape[0] / 10)), (int(3 * frame.shape[1] / 4), int(9 * frame.shape[0] / 10)), (204, 0, 102), 3)
               
               cv2.rectangle(frame, (0, 0), (int(frame.shape[1]), int(frame.shape[0])), (0, 153, 76), 3)

               cv2.putText(frame, "Kamera Gorus Alani", (10, int(frame.shape[0]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (200, 0, 0), 1, cv2.LINE_AA, False)
               
               cv2.putText(frame, "Hedef Vurus Alani", (int(frame.shape[1] / 4) + 5, int(9 * frame.shape[0] / 10) - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 200), 1, cv2.LINE_AA, False)
               
               (class_ids, scores, bboxes) = model.detect(frame, confThreshold=thresh, nmsThreshold=nms_threshold)
               for class_id, score, bbox in zip(class_ids, scores, bboxes):
                    (x, y, w, h) = bbox
                    
                    x1, y1 = x + w, y + h

                    b1, c1 = x + h, y + w 
                         
                    #frame = fancyDraw(frame, i, bboxes, bbox)
                    #text = '%s: %.2f' % (classes[class_ids[i][0]-1].upper(), score[0])
                         
                    #cv2.putText (frame, text, (x, y - 10), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 250), 2)
                    # color=(134, 71, 230)
                    #cv2.rectangle(frame, (x, y), (x+w,h+y), color=(255, 255, 255), thickness=1)

                    center = (x + w // 2, y + h // 2)
                    radius = 8
                    #cv2.circle(frame, center, radius, (230, 242, 155), 2)
                         
                         

                         
                    outputs = net.forward(outputNames)

                    self.findObjects(outputs, frame)
                         

                    #cv2.line(frame, (x1, y1), (x1, b1 - l), (0, 0, 255), t)
                    returner = self.findObjects(outputs, frame)

                    print(returner)
                    
                    
                    
                    if returner is not None:
                         
                         cv2.line(frame, (int(frame.shape[1] / 2), int(frame.shape[0] / 2)),
                                        (int(returner[0] + returner[2] / 2), int(returner[1] + returner[3] / 2)), (0, 255, 0), 2)
                         roi_frame = frame[returner[1]:returner[1] + returner[3], returner[0]:returner[0] + returner[2]]
                         # cv2.imshow('Image2', roi_frame)

                         # frame[0: returner[3],0: returner[2]] = roi_frame
                         # roi_frame2 = frame[returner[1]:returner[1] + 100, returner[0]:returner[0] + 100]

                         # dronu daha küçük bir alanda bulmak
                         # roi_drone = frame[returner[1]+100 :returner[1] + returner[3] + 100, returner[0]-100 :returner[0] + returner[2]+ 100]
                         # findObjects(outputs, roi_drone)

                         # cv2.imshow('Image2', roi_frame2)

                         distance = ((returner[0] - int(frame.shape[0] / 2)) ** 2 + (returner[1] - int(frame.shape[0] / 2) ** 2))
                         #print(math.sqrt(distance))
                         #cv2.putText(frame, "Distance:" + ('%d' % int(distance)), (200, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 200),
                         #2, cv2.LINE_AA, False)

                         # sağ yada sol taraftamı ona bakan bir algoritma yaz
                         # üst taraftamı alt taraftamı ona bakan bir algoritma
                         horizantal_difference = int(returner[0] + returner[2] / 2) - int(frame.shape[1] / 2)
                         if horizantal_difference  > 0:
                              print("RIGHT")
                              cv2.putText(frame, "Right:"+ ('%.2f' % float((horizantal_difference)/kumanda_aralık)), (int(frame.shape[1] / 4) + 5, int(9 * frame.shape[0] / 10) - 150),
                                             cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 200), 2, cv2.LINE_AA, False)
                         else:
                              print("LEFT")
                              cv2.putText(frame, "Left:"+ ('%.2f' % float((horizantal_difference*-1)/kumanda_aralık)), (int(frame.shape[1] / 4) + 5, int(9 * frame.shape[0] / 10) - 150),
                                             cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 200), 2, cv2.LINE_AA, False)

                         vertical_difference = int(returner[1] + returner[3] / 2) - int(frame.shape[0] / 2)

                         if vertical_difference > 0:
                              print("DOWN")
                              cv2.putText(frame, "Down:"+ ('%.2f' % float((vertical_difference)/kumanda_aralık)), (int(frame.shape[1] / 4) + 5, int(9 * frame.shape[0] / 10) - 100),
                                             cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 200), 2, cv2.LINE_AA, False)
                         else:
                              print("UP")
                              cv2.putText(frame, "Up:"+ ('%.2f' % float((vertical_difference*-1)/kumanda_aralık)), (int(frame.shape[1] / 4) + 5, int(9 * frame.shape[0] / 10) - 100),
                                             cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 200), 2, cv2.LINE_AA, False)

                         if int(frame.shape[1] / 4)< returner[0] < int(3 * frame.shape[1] / 4) and int(frame.shape[0] / 10) < returner[1] < int(9 * frame.shape[0] / 10):
                              print("INSIDE")
                              cv2.putText(frame, "Inside",
                                             (int(frame.shape[1] / 4) + 5, int(9 * frame.shape[0] / 10) - 250),
                                             cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 220, 0), 2, cv2.LINE_AA, False)
                         else:
                              print("OUTSIDE")
                              cv2.putText(frame, "Outside",
                                             (int(frame.shape[1] / 4) + 5, int(9 * frame.shape[0] / 10) - 250),
                                             cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 200), 2, cv2.LINE_AA, False)
                         print(distance)

                         cv2.circle(frame, (int(frame.shape[1] / 2), int(frame.shape[0] / 2)), 3, (0, 0, 0), 2)
                         cv2.circle(frame, (int(returner[0] + returner[2] / 2), int(returner[1] + returner[3] / 2)), 3, (0, 0, 255), 2)
                         
                         if key == 27:
                              break
                    else:
                         pass

               cv2.imshow("Frame", frame)
               videoFileOutput.write(frame)
               key = cv2.waitKey(1) & 0xFF
               if key == ord('q'):
                    break

          cap.release()
          videoFileOutput.release()
          cv2.destroyAllWindows()
     
     def findObjects(self, outputs, img):
          hT, wT, cT = img.shape
          bbox = []
          classIds = []
          confs = []

          for output in outputs:
               for det in output:
                    scores = det[5:]
                    classId = np.argmax(scores)
                    confidence = scores[classId]
                    if confidence > thresh:
                         w, h = int(det[2] * wT), int(det[3] * hT)
                         x, y = int((det[0] * wT) - w / 2), int((det[1] * hT) - h / 2)
                         bbox.append([x, y, w, h])
                         classIds.append(classId)
                         confs.append(float(confidence))
          print(len(bbox))
          indices = cv2.dnn.NMSBoxes(bbox, confs, thresh, nms_threshold)
          for i in indices:
               i = i
               box = bbox[i]
               x, y, w, h = box[0], box[1], box[2], box[3]

               x1, y1 = x + w, y + h
               text2 = (classes[classIds[i - 1]].upper() + " " + str(int(confs[0] * 100)) + "%")
               b1, c1 = x + h, y + w 
               # Top Left x, y
               #! color purple (134, 71, 230)
               #? color WhatsApp (18, 140, 126)
               #** color green (129, 194, 0)

               cv2.line(img, (x, y), (x + l, y), (230, 242, 155), t)
               cv2.line(img, (x, y), (x, y+l), (230, 242, 155), t)
               cv2.ellipse(img, (x1 + l, y1 + rt), (rt, rt), 180, 0, 90, (230, 242, 155), t)
               # Top Right  x1,y
               cv2.line(img, (x1, y), (x1 - l, y), (230, 242, 155), t)
               cv2.line(img, (x1, y), (x1, y+l), (230, 242, 155), t)
               # Bottom Left  x,y1
               cv2.line(img, (x, y1), (x + l, y1), (230, 242, 155), t)
               cv2.line(img, (x, y1), (x, y1 - l), (230, 242, 155), t)
               # Bottom Right  x1,y1
               cv2.line(img, (x1, y1), (x1 - l, y1), (230, 242, 155), t)
               cv2.line(img, (x1, y1), (x1, y1 - l), (230, 242, 155), t)
               cv2.putText(img, f'{classes[classIds[i - 1]].upper()} {int(confs[i] * 100)}%', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (230, 242, 155), 2)
               print("Accuracy Rate: ", f'{int(confs[i] * 100)}%')
               return x, y, w, h
     