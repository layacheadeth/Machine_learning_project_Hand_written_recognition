import cv2
import pytesseract

def text_detecttion(image):
    pytesseract.pytesseract.tesseract_cmd = '/usr/local/Cellar/tesseract/4.1.1/bin/tesseract'
    img = cv2.imread(image)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    boxes1 = pytesseract.image_to_data(img)
    for x, b in enumerate(boxes1.splitlines()):
        if x != 0:
            b = b.split()
            print(b)
            if len(b) == 12:
                # because the data given by image_to_data function is in those 6,7,8,9 columns
                x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                # drawing a rectangle around those detected word
                cv2.rectangle(img, (x, y), (w + x, h + y), (0, 0, 255), 3)
                # write a letter accordinly to the detected word
                cv2.putText(img, b[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2)

    cv2.imshow('result', img)
    cv2.waitKey(0)