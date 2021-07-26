from tkinter import *

width = 200
height = 200
center = height//2

current_x,current_y=0,0
color='black'

def locate_xy(event):
    global current_x,current_y
    current_x,current_y=event.x,event.y



def addline(event):
    global current_x,current_y
    cv.create_line((current_x,current_y,event.x,event.y),fill=color)
    current_x, current_y = event.x, event.y
    print(current_x,current_y)

def show_color(new_color):
    global color
    color=new_color

def new_canvas():
    cv.delete("all")
    display_pallete()

def save():
    pass


root = Tk()

menubar=Menu(root)
root.config(menu=menubar)
submenu=Menu(menubar,tearoff=0 )



menubar.add_cascade(label='File',menu=submenu)
submenu.add_command(label='New Canvas',command=new_canvas)


# Tkinter create a canvas to draw on
cv = Canvas(root, width=width, height=height, bg='white')
cv.bind('<Button-1>',locate_xy)
cv.bind('<B1-Motion>',addline)




cv.pack(expand=YES, fill=BOTH)

button=Button(text="save", width=10, bg='blue')
button.pack()

def display_pallete():
    id=cv.create_rectangle((10,10,30,30),fill='black')
    cv.tag_bind(id,'<Button-1>',lambda x: show_color('black'))

    id=cv.create_rectangle((10,40,30,60),fill='gray')
    cv.tag_bind(id,'<Button-1>',lambda x: show_color('gray'))

    id=cv.create_rectangle((10,70,30,90),fill='brown4')
    cv.tag_bind(id,'<Button-1>',lambda x: show_color('brown4'))

    id=cv.create_rectangle((10,100,30,120),fill='red')
    cv.tag_bind(id,'<Button-1>',lambda x: show_color('red'))

    id=cv.create_rectangle((10,130,30,150),fill='orange')
    cv.tag_bind(id,'<Button-1>',lambda x: show_color('orange'))

    id=cv.create_rectangle((10,160,30,180),fill='yellow')
    cv.tag_bind(id,'<Button-1>',lambda x: show_color('yellow'))

    id=cv.create_rectangle((10,190,30,210),fill='green')
    cv.tag_bind(id,'<Button-1>',lambda x: show_color('green'))

    id=cv.create_rectangle((10,220,30,240),fill='blue')
    cv.tag_bind(id,'<Button-1>',lambda x: show_color('blue'))

    id=cv.create_rectangle((10,250,30,270),fill='purple')
    cv.tag_bind(id,'<Button-1>',lambda x: show_color('purple'))



display_pallete()
cv.pack()


root.mainloop()
