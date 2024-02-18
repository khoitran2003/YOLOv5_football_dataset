import cv2
import random
import os


test_path = "dataset/football_test/Match_1864_1_0_subclip/Match_1864_1_0_subclip.mp4"

model_path = "yolo/best.pt"

root = "yolov5/football_yolo"
file_id = [
    file_id.replace(".jpg", "")
    for file_id in os.listdir(os.path.join(root, "images", "train"))
]
random_id = random.choice(file_id)

image = cv2.imread(os.path.join(root, "images", "train", "{}.jpg".format(random_id)))
resized_image = cv2.resize(image, (2048, 2048))

