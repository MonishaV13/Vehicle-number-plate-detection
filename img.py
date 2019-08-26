
import pytesseract
import imutils
from PIL import Image, ImageEnhance, ImageFilter
import cv2
import numpy as np
from matplotlib import pyplot as plt
pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
cnts=0
image = cv2.imread("./car_num.jpg")
if image is None:
	print("No image")
else:
	image=imutils.resize(image,width=500)
	cv2.waitKey(0)

	gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	cv2.imshow("Greyscale conversion",gray)
	cv2.waitKey(0)

	gray=cv2.bilateralFilter(gray,11,17,17)
	cv2.imshow("BilateralFilter",gray)
	cv2.waitKey(0)

	edged=cv2.Canny(gray,170,200)
	cv2.imshow("Canny Edges",edged)
	cv2.waitKey(0)

	cnts, new=cv2.findContours(edged.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

	img1=image.copy()
	cv2.drawContours(img1,cnts,-1,(0,255,0),3)
	cv2.imshow("All Contours",img1)
	cv2.waitKey(0)

	cnts=sorted(cnts, key=cv2.contourArea,reverse = True)[:30]
	NumberPlateCnt=None

	img2=image.copy()
	cv2.drawContours(img2,cnts,-1,(0,255,0),3)
	cv2.imshow("Top 30 Contours",img2)
	cv2.waitKey(0)

c=0
idk=9997
for c in cnts:
	peri=cv2.arcLength(c,True)
	approx=cv2.approxPolyDP(c,0.02 * peri, True)

	if len(approx) == 4:
		NumberPlateCnt = approx
		x,y,w,h = cv2.boundingRect(c)
		new_img = image[y:y + h,x:x + w]
		cv2.imwrite('./Images/' + str(idk) + '.jpg' , new_img)
		idk+=1

		break

cv2.drawContours(image, [NumberPlateCnt], -1, (0,255,0), 3)
cv2.waitKey(0)

Cropped_img_loc=cv2.imread('C:\\Users\\KANAK\\python_work\\argparse\\Images\\9997.jpg')
cv2.waitKey(0)



if Cropped_img_loc is None:
 	print("No image")
else:
 	ima=imutils.resize(Cropped_img_loc,width=500)
 	cv2.imshow("imo",ima)
 	cv2.waitKey(0)

imo = cv2.imread('C:\\Users\\KANAK\\python_work\\argparse\\Images\\9997.jpg')
text=pytesseract.image_to_string(Image.fromarray(imo))
print("Number is :",text)





