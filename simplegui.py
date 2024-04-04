#import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
#import PYSimpleGUI as simplegui

import simpleguitk as simplegui
import random

r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)

def draw_handler(canvas):
    txtcolor = "RGB( " + str(r-80) + ", " + str(g-80) + ", " + str(b-80) + ")"
    canvas.draw_text("Student Portfolio", (100, 80), 20, txtcolor)
    backg = "RGB( " + str(r) + ", " + str(g) + ", " + str(b) + ")"
    frame.set_canvas_background(backg)

frame = simplegui.create_frame("Python Portfolio", 400, 150)
frame.set_draw_handler(draw_handler)
                     
frame.start()