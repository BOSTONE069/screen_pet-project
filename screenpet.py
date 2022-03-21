from tkinter import Tk, HIDDEN , NORMAL , Canvas

win = Tk()

c = Canvas(win , width=400, height=400)
c.configure(bg='dark blue', highlightthickness=0) #This is defining the backgroung color

c.body_color = 'SkyBlue1'

body = c.create_oval(35,20,365,350,outline=c.body_color, fill=c.body_color)#This is definign the how the pet is supposed to look like.
foot_left = c.create_oval( 65, 320, 145, 360, outline=c.body_color, fill=c.body_color)
foot_right = c.create_oval(250, 320,330,360, outline=c.body_color, fill=c.body_color)

ear_left = c.create_polygon(75,80,75,10,165,70, outline=c.body_color, fill=c.body_color)
ear_left = c.create_polygon(255,45,325,10,320,70,outline=c.body_color, fill=c.body_color)

eye_left = c.create_oval(130,110,160,170,outline='black' , fill='white')
pupil_left = c.create_oval(140,145,150,155, outline='black', fill='black')
eye_right = c.create_oval(230,110,260, 170, outline='black', fill='white')
pupil_right = c.create_oval(240, 145, 250, 155, outline='black', fill='black')

c.pack()

win.mainloop()
