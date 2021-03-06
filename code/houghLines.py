import cv2
import os
import math

def main():

	directory = os.path.dirname(__file__)
	picLoc = os.path.join(directory, "../video-image/1m50s.png")

	image = cv2.imread(picLoc)
	print "sending image to houghLines.py"
	a = hough(image)
	cv2.imshow("", a)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def hough(image):
	#image = cv2.GaussianBlur(image, (11,11),0)
	image = cv2.blur(image, (5,7))
	image = cv2.cvtColor( image, cv2.COLOR_BGR2LAB )
	canny = cv2.Canny(image, 20, 175 )
	color_image = cv2.cvtColor(canny, cv2.COLOR_GRAY2BGR)
	houghLines = cv2.HoughLinesP(canny, 1, math.pi/180, 100, minLineLength = 250, maxLineGap = 100)
	print len(houghLines[0])
	for x in range(len(houghLines[0])):
		pt1 = (houghLines[0][x][0], houghLines[0][x][1])
		pt2 = (houghLines[0][x][2], houghLines[0][x][3])
		cv2.line(color_image, pt1, pt2, (0,0,255), 3)
	return color_image

main()
