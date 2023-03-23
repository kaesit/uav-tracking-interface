import cv2
import numpy as np
import math
from math import sqrt
import datetime
import imutils

#cap = cv2.VideoCapture("testvideo5.mp4")
cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

classesFile = "model/classes.txt"

l = 30
t = 3
rt = 1


a = 0
distance = 0
whT = 320

classNames = []
confThreshold = 0.5
nmsThreshold = 0.3

kumanda_aralık=10

width, height = 720, 480 

with open(classesFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

modelConfiguration = 'model/yolov4-obj.cfg'
modelWeigts = 'model/yolov4-obj_last.weights'

net = cv2.dnn.readNet(modelWeigts, modelConfiguration)


fileName = "C:/Users/PC/Desktop/Programlama/Projeler/YapayZeka/Missileme Programı/ds/op.avi"
codec = cv2.VideoWriter_fourcc('W', 'M', 'V', '2')
frameRate = 30
resolution = (width, height)
videoFileOutput = cv2.VideoWriter(fileName, codec, frameRate, resolution)

# net = cv2.dnn.readNetFromDarknet(modelConfiguration,modelWeigts)
# net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
# net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)


def record_start(file_path, codec, frame_rate, resolution, source, img):
     source.write(img)

def record_end(file_path, codec, frame_rate, resolution, source, img):
     source.release()



def findObjects(outputs, img):
    hT, wT, cT = img.shape
    bbox = []
    classIds = []
    confs = []

    for output in outputs:
        for det in output:
            scores = det[5:]
            classId = np.argmax(scores)
            confidence = scores[classId]
            if confidence > confThreshold:
                w, h = int(det[2] * wT), int(det[3] * hT)
                x, y = int((det[0] * wT) - w / 2), int((det[1] * hT) - h / 2)
                bbox.append([x, y, w, h])
                classIds.append(classId)
                confs.append(float(confidence))
    print(len(bbox))
    indices = cv2.dnn.NMSBoxes(bbox, confs, confThreshold, nmsThreshold)
    for i in indices:
        i = i
        box = bbox[i]
        x, y, w, h = box[0], box[1], box[2], box[3]

        x1, y1 = x + w, y + h

        b1, c1 = x + h, y + w 
        cv2.line(img, (x, y), (x + l, y), (0, 0, 255), t)
        cv2.line(img, (x, y), (x, y+l), (0, 0, 255), t)
        cv2.ellipse(img, (x1 + l, y1 + rt), (rt, rt), 180, 0, 90, (0, 0, 255), t)
        # Top Right  x1,y
        cv2.line(img, (x1, y), (x1 - l, y), (0, 0, 255), t)
        cv2.line(img, (x1, y), (x1, y+l), (0, 0, 255), t)
        # Bottom Left  x,y1
        cv2.line(img, (x, y1), (x + l, y1), (0, 0, 255), t)
        cv2.line(img, (x, y1), (x, y1 - l), (0, 0, 255), t)
        # Bottom Right  x1,y1
        cv2.line(img, (x1, y1), (x1 - l, y1), (0, 0, 255), t)
          
        cv2.line(img, (x1, y1), (x1, y1 - l), (0, 0, 255), t)
        cv2.putText(img, f'{classNames[classIds[i - 1]].upper()} %{int(confs[i] * 100)}',
                    (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)


        
        return x, y, w, h


def Start():
     while True:
          success, frame = cap.read()
     
          gray_video = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
     
          blob = cv2.dnn.blobFromImage(frame, 1 / 255, (whT, whT), [0, 0, 0], 1, crop=False)

          net.setInput(blob)

          layerNames = net.getLayerNames()

          outputNames = [layerNames[i - 1] for i in net.getUnconnectedOutLayers()]

          cv2.rectangle(frame, (int(frame.shape[1] / 4), int(frame.shape[0] / 10)),
                         (int(3 * frame.shape[1] / 4), int(9 * frame.shape[0] / 10)), (204, 0, 102), 3)
          cv2.rectangle(frame, (0, 0), (int(frame.shape[1]), int(frame.shape[0])), (0, 153, 76), 4)
          # cv2.circle(frame,(int (frame.shape[1]/2),int (frame.shape[0]/2)))

          cv2.putText(frame, "CFV : Camera Field of View", (10, int(frame.shape[0]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (200, 0, 0),
                         2, cv2.LINE_AA, False)
          cv2.putText(frame, "THA : Target Hit Area", (int(frame.shape[1] / 4) + 5, int(9 * frame.shape[0] / 10) - 10),
                         cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 200), 2, cv2.LINE_AA, False)

          outputs = net.forward(outputNames)

          findObjects(outputs, frame)

          returner = findObjects(outputs, frame)

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
                    print("right")
                    cv2.putText(frame, "Right:"+ ('%.2f' % float((horizantal_difference)/kumanda_aralık)), (int(frame.shape[1] / 4) + 5, int(9 * frame.shape[0] / 10) - 150),
                              cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 200), 2, cv2.LINE_AA, False)
               else:
                    print("left")
                    cv2.putText(frame, "Left:"+ ('%.2f' % float((horizantal_difference*-1)/kumanda_aralık)), (int(frame.shape[1] / 4) + 5, int(9 * frame.shape[0] / 10) - 150),
                              cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 200), 2, cv2.LINE_AA, False)

               vertical_difference = int(returner[1] + returner[3] / 2) - int(frame.shape[0] / 2)

               if vertical_difference > 0:
                    print("down")
                    cv2.putText(frame, "Down:"+ ('%.2f' % float((vertical_difference)/kumanda_aralık)), (int(frame.shape[1] / 4) + 5, int(9 * frame.shape[0] / 10) - 100),
                              cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 200), 2, cv2.LINE_AA, False)
               else:
                    print("up")
                    cv2.putText(frame, "Up:"+ ('%.2f' % float((vertical_difference*-1)/kumanda_aralık)), (int(frame.shape[1] / 4) + 5, int(9 * frame.shape[0] / 10) - 100),
                              cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 200), 2, cv2.LINE_AA, False)

               if int(frame.shape[1] / 4)< returner[0] < int(3 * frame.shape[1] / 4) and int(frame.shape[0] / 10) < returner[1] < int(9 * frame.shape[0] / 10):
                    print("içerdeee")
                    cv2.putText(frame, "Inside",
                              (int(frame.shape[1] / 4) + 5, int(9 * frame.shape[0] / 10) - 250),
                              cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 220, 0), 2, cv2.LINE_AA, False)
               else:
                    print("dışarda")
                    cv2.putText(frame, "Outside",
                              (int(frame.shape[1] / 4) + 5, int(9 * frame.shape[0] / 10) - 250),
                              cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 200), 2, cv2.LINE_AA, False)

               print(distance)
               
               
               
               cv2.circle(frame, (int(frame.shape[1] / 2), int(frame.shape[0] / 2)), 3, (0, 0, 0), 2)
               
               cv2.circle(frame, (int(returner[0] + returner[2] / 2), int(returner[1] + returner[3] / 2)), 3, (0, 0, 255), 2)
               
          

          
          
          cv2.imshow('Image', frame)

          videoFileOutput.write(frame) 
          
          key = cv2.waitKey(1) & 0xFF
          if key == ord("q"):
               break

     cap.release()
     videoFileOutput.release()
     
     cv2.destroyAllWindows()
