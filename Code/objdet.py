import cvlib as cv
from cvlib.object_detection import draw_bbox
import sys
import cv2


image = cv2.imread('Images\\input1.jpg')


bbox, label, conf = cv.detect_common_objects(image)

print(bbox, label, conf)
x = len(label)

print("Total objects count:",x)
out = draw_bbox(image, bbox, label, conf)

        
cv2.imshow("object_detection", out)
cv2.waitKey()


cv2.imwrite("object_detection.jpg", out)


#cv2.destroyAllWindows()
