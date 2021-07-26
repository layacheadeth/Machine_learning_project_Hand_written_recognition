import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd='/usr/local/Cellar/tesseract/4.1.1/bin/tesseract'
img=cv2.imread('image.png')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# print the text from image
# print(pytesseract.image_to_string(img))
# print the bounding boxes of each charactor such as x,y,and diagonal point of bounding box(w,h)
print(pytesseract.image_to_boxes(img))
# Dectection charactors
# hImg,wImg,_=img.shape
# boxes=pytesseract.image_to_boxes(img)
# for b in boxes.splitlines():
#     b=b.split(' ')
#     print(b)
#     x,y,w,h=int(b[1]),int(b[2]),int(b[3]),int(b[4])
#     # draw a circle around each charactor to look as a visualize detection
#     cv2.rectangle(img,(x,hImg-y),(w,hImg-h),(0,0,255),3)
#     #print the text along with its detection
#     cv2.putText(img,b[0],(x,hImg-y+25),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)

# # Detect word
boxes1=pytesseract.image_to_data(img)
for x,b in enumerate(boxes1.splitlines()):
    if x!=0:
        b=b.split()
        print(b)
        if len(b)==12:
            # because the data given by image_to_data function is in those 6,7,8,9 columns
            x,y,w,h=int(b[6]),int(b[7]),int(b[8]),int(b[9])
            # drawing a rectangle around those detected word
            cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,255),3)
            # write a letter accordinly to the detected word
            cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)
# detect only digit
hImg,wImg,_=img.shape
# this oem has many type detection, so does the psm which is page segmentation mode.(also has many page layout type).
cong=r'--oem 3 --psm 6 outputbase digits'
boxes1=pytesseract.image_to_data(img,config=cong)
for x,b in enumerate(boxes1.splitlines()):
    if x!=0:
        b=b.split()
        print(b)
        if len(b)==12:
            # because the data given by image_to_data function is in those 6,7,8,9 columns
            x,y,w,h=int(b[6]),int(b[7]),int(b[8]),int(b[9])
            # drawing a rectangle around those detected word
            cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,255),3)
            # write a letter accordinly to the detected word
            cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)
#     the result in this code show nothing significant since our image has no number. If it has, it will detect and draw the detection right away.


cv2.imshow('result',img)
cv2.waitKey(0)