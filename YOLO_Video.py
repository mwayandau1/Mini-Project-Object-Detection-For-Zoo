from ultralytics import YOLO
import cv2
import math

def video_detection(path_x):
    video_capture = path_x
    #Create a Webcam Object
    cap=cv2.VideoCapture(video_capture)
    frame_width=int(cap.get(3))
    frame_height=int(cap.get(4))
    #out=cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M', 'J', 'P','G'), 10, (frame_width, frame_height))

    model=YOLO("YOLO-Weights/best.pt")
    classNames = ['Bird', 'Cat', 'Cow', 'Deer', 'Dog', 'Elephant', 'Giraffle', 'Person', 'Pig', 'Sheep']
    while True:
        success, img = cap.read()
        results=model(img,stream=True)
        for r in results:
            boxes=r.boxes
            for box in boxes:
                x1,y1,x2,y2=box.xyxy[0]
                x1,y1,x2,y2=int(x1), int(y1), int(x2), int(y2)
                print(x1,y1,x2,y2)
                conf=math.ceil((box.conf[0]*100))/100
                cls=int(box.cls[0])
                class_name=classNames[cls]
                label=f'{class_name}{conf}'
                t_size = cv2.getTextSize(label, 0, fontScale=1, thickness=2)[0]
                print(t_size)
                c2 = x1 + t_size[0], y1 - t_size[1] - 3
                if class_name == 'Bird':
                    color=(49, 50, 56)
                elif class_name == "Cat":
                    color = (64, 13, 61)
                elif class_name == "Cow":
                    color = (92, 4, 27)
                elif class_name == "Deer":
                    color = (46, 51, 24)

                elif class_name == "Dog":
                    color = (14, 43, 37)
                elif class_name == "Elephant":
                    color = (214, 153, 139)
                elif class_name == "Giraffle":
                    color = (30, 35, 66)
                elif class_name == "Person":
                    color = (30, 35, 66)
                elif class_name == "Pig":
                    color = (65, 113, 115)              

                else:
                    color = (85,45,255)

                if conf>0.5:
                    cv2.rectangle(img, (x1,y1), (x2,y2), color,3)
                    cv2.rectangle(img, (x1,y1), c2, color, -1, cv2.LINE_AA)  # filled
                    cv2.putText(img, label, (x1,y1-2),0, 1,[255,255,255], thickness=1,lineType=cv2.LINE_AA)

        yield img
        #out.write(img)
        #cv2.imshow("image", img)
        #if cv2.waitKey(1) & 0xFF==ord('1'):
            #break
    #out.release()
cv2.destroyAllWindows()