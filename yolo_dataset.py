import os
import shutil
import cv2
import glob
import json

if __name__ == "__main__":
    root = "dataset/football_test"
    output_dir = "yolo/football_yolo"
    width = 3840
    height = 1200
    # if os.path.isdir(output_dir):
    #     shutil.rmtree(output_dir)
    # os.makedirs(output_dir)
    # os.makedirs(os.path.join(output_dir, "images"))
    # os.makedirs(os.path.join(output_dir, "images", "train"))
    # os.makedirs(os.path.join(output_dir, "images", "val"))
    # os.makedirs(os.path.join(output_dir, "labels"))
    # os.makedirs(os.path.join(output_dir, "labels", "train"))
    # os.makedirs(os.path.join(output_dir, "labels", "val"))
    video_path = list(glob.iglob("{}/*/*.mp4".format(root)))
    video_path = [video_path.replace(".mp4", "") for video_path in video_path]
    anno_path = list(glob.iglob("{}/*/*.json".format(root)))
    anno_path = [anno_path.replace(".json", "") for anno_path in anno_path]
    paths = set(video_path) & set(anno_path)

    for vid_id, path in enumerate(paths):
        count = 1
        video = cv2.VideoCapture("{}.mp4".format(path))
        with open ("{}.json".format(path), "r") as json_file:
            json_data = json.load(json_file)
        while video.isOpened():
            flag, frame = video.read()
            if not flag:
                break
            cv2.imwrite(os.path.join(output_dir, "images", "val", "{}_{}.jpg".format(vid_id+1, count)), frame)
            current_players_bbox = [obj["bbox"] for obj in json_data["annotations"] if 
                           obj["image_id"] == count and obj["category_id"] == 4]
            with open(os.path.join(output_dir, "labels", "val", "{}_{}.txt".format(vid_id+1, count)), "w") as text_file:
                for player in current_players_bbox:
                    xmin, ymin, w, h = player
                    xcent = (xmin + w/2) / width
                    ycent = (ymin + h/2) / height
                    w /= width
                    h /= height
                    text_file.write("0 {:.6f} {:.6f} {:.6f} {:.6f}\n".format(xcent, ycent, w, h))
            count += 1