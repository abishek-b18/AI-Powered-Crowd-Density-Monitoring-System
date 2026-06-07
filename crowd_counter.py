from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    results = model(frame)

    count = 0

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])

            if cls == 0:
                count += 1

    print("People Count:", count)

    cv2.imshow("Crowd Counter", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()