from pyimagesearch.sdetect import shapedetect
import imutils
import cv2


image = cv2.imread(input("Enter name of the file to be loaded.extension)\n(Make sure it is in the same directory as this project):\n\n"))
resized = imutils.resize(image, width=300)
ratio = image.shape[0] / float(resized.shape[0])
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
cv2.imshow("THREHSOLD",thresh)
cv2.waitKey(0)
cnts = cv2.findContours(thresh.copy(), 2,1)

cnts = cnts[1]
sd = shapedetect()

for c in cnts:

    M = cv2.moments(c)
    cX = int((M["m10"] / M["m00"]) * ratio)
    cY = int((M["m01"] / M["m00"]) * ratio)
    shape = sd.detect(c)
    c = c.astype("float")
    c *= ratio
    c = c.astype("int")
    cv2.drawContours(image, [c], -1, (0, 225, 0), 2)
    cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
		0.5, (180, 180, 180), 2)
    cv2.imshow("PRESS Q OR ESC TO PROCEED", image)
    cv2.waitKey(0)
k=cv2.waitKey()   
if k == 27 or ord('q'):
    cv2.destroyAllWindows()
     


















