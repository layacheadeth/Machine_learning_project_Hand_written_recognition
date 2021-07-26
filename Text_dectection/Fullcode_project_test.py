import pygame as pg
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd='/usr/local/Cellar/tesseract/4.1.1/bin/tesseract'

def init():
    global screen
    pg.init()
    screen = pg.display.set_mode((400, 400))
    mainloop()


drawing = False
last_pos = None
w = 10
color = (255, 255, 255)


def draw(event):
    global drawing, last_pos, w
    if event.type == pg.MOUSEMOTION:
        if (drawing):
            mouse_position = pg.mouse.get_pos()
            if last_pos is not None:
                pg.draw.line(screen, color, last_pos, mouse_position, w)
            last_pos = mouse_position
    elif event.type == pg.MOUSEBUTTONUP:
        mouse_position = (0, 0)
        drawing = False
        last_pos = None
    elif event.type == pg.MOUSEBUTTONDOWN:
        drawing = True


def mainloop():
    global screen
    loop = 1
    while loop:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                loop = 0
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_s:
                    pg.image.save(screen, "image.png")
                    img = cv2.imread('image.png')
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

            draw(event)
        pg.display.flip()
    pg.QUIT()


init()
