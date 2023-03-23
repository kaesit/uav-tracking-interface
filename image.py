import cv2

img = cv2.imread('images/planes.jpg')

with open('model/classes.txt', 'r') as f:
    classes = f.read().splitlines()

net = cv2.dnn.readNet('model/yolov4-obj.cfg', 'model/yolov4-obj_last.weights')
width = 1280
height = 720
model = cv2.dnn_DetectionModel(net)
model.setInputParams(scale=1 / 255, size=(410, 410), swapRB=True)

classIds, scores, boxes = model.detect(img, confThreshold=0.6, nmsThreshold=0.4)


for (classId, score, box) in zip(classIds, scores, boxes):



    text2 = (classes[classIds[0]].upper() + " " + str(int(scores[0] * 100)) + "%")
    if (scores[0] * 100 >= 99.5):
        print("Doğruluk oranı%: 100")
        text2 = (classes[classIds[0]].upper() + " 100%")
    elif (scores[0] * 100 == 84.5):
        print("Doğruluk oranı%:85")
        text2 = (classes[classIds[0]].upper() + " 85%")
    else:
        print("Doğruluk oranı %:", scores[0] * 100)

    #text = '%s: %.2f' % (classes[classId[0]], score)
    print(box[0], box[1])
    print("İkinci oran: ", box[0] + box[2], box[1] + box[3])
    cv2.rectangle(img, (box[0], box[1]), (box[0] + box[2], box[1] + box[3]),
                  color=(230, 242, 155), thickness=3)
    cv2.putText(img, text2, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 1,
                color=(230, 242, 155), thickness=3)
    x, y , w, h = box[0], box[1], box[2], box[3]
    # below circle to denote mid point of center line
    center = (x + w // 2, y + h // 2)
    radius = 10
    cv2.circle(img, center, radius, (36, 236, 12), 2)

scale_percent = 60 # percent of original size

dim = (width, height)

# resize image
img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
winname = "Target Detection"
cv2.namedWindow(winname)        # Create a named window
cv2.moveWindow(winname, 40,30)
cv2.imshow(winname, img)
cv2.waitKey(0)
cv2.destroyAllWindows()
