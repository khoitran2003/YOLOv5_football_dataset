import cv2
import os
import random

root = "yolo/football_yolo"
file_id = [file_id.replace(".jpg", "") for file_id in os.listdir(os.path.join(root, "images", "train"))]
random_id = random.choice(file_id)

image = cv2.imread(os.path.join(root, "images", "train", "{}.jpg". format(random_id)))
height, width, _ = image.shape

with open(os.path.join(root, "labels", "train", "{}.txt". format(random_id))) as f:
    data = f.readlines()
    data = [data.strip().split() for data in data]
    data = [list(map(float, data)) for data in data]
    for bbox in data:
        _, xcent, ycent, w, h = bbox
        xcent *= width
        w *= width
        ycent *= height
        h *= height
        cv2.rectangle(image, (int(xcent - w/2), int(ycent - h/2)), (int(xcent + w/2), int(ycent + h/2)), (0, 0, 255), 2)
cv2.imwrite("yolo/test_image.jpg", image)

