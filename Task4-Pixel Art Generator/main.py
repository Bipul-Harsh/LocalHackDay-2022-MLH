import cv2
import numpy as np
import argparse

parser = argparse.ArgumentParser(description="Can check pixel value of any point in given photo.")
parser.add_argument('--input_file', type=str, default="./assets/sample.jpg", help="(Required) the image file you want to read")
parser.add_argument('--wt_ratio', type=float, default=1, help="width ratio to resize frame horizontally")
parser.add_argument("--ht_ratio", type=float, default=1, help="height ratio to resize frame veritcally")
parser.add_argument("--wt_size", type=int, default=0, help="to provide the frame width size in pixels")
parser.add_argument("--ht_size", type=int, default=0, help="to provide the frame height size in pixels")
parser.add_argument("--blur", type=float, default=0.08, help="Add blur ratio in float")

args = parser.parse_args()

INPUT_FILE = args.input_file
assert INPUT_FILE != None, "Please provide a image file"
WT_RATIO = args.wt_ratio
HT_RATIO = args.ht_ratio
HT_SIZE = args.ht_size
WT_SIZE = args.wt_size
WINDOW_NAME = "Color Picker"
BLUR = args.blur

image = cv2.imread(INPUT_FILE)
image = cv2.resize(image, (WT_SIZE,HT_SIZE), fx=WT_RATIO, fy=HT_RATIO)
assert type(image) != type(None), "Please provide valid image location"

width,height = image.shape[1], image.shape[0]
w, h = (int(width*BLUR), int(height*BLUR))
temp = cv2.resize(image, (w, h), interpolation=cv2.INTER_LINEAR)
updated_image = cv2.resize(temp, (int(w * 1/BLUR), int(h * 1/BLUR)),interpolation=cv2.INTER_NEAREST)

cv2.namedWindow(WINDOW_NAME)

while(True):
    cv2.imshow(WINDOW_NAME, updated_image)

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()