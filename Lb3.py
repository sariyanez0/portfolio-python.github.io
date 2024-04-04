#speaking
import play
w=1000
h=1000
@play.when_program_starts
def do():
    play.screen.width = w
    play.screen.height = h

play.set_backdrop((176,224,230))
#background box
box=play.new_box(
  color=(255,182,193),
  x=-184,
  y=89,
  width=300,
  height=300,
)
#face starts
s_head = play.new_circle(
 color = (203, 195, 227),
  x = -266,
  y = 4,
  radius = 50,
)
sl_eye = play.new_circle(
  color = "black",
  x = -287,
  y = 18,
  radius = 10,
)
sr_eye = play.new_circle(
  color = "black",
  x = -245,
  y = 18,
radius = 10,
)
s_nose = play.new_circle(
  color ="black",
  x = -265,
  y = -1,
  radius = 5,
)

s_nose = play.new_circle(
  color="pink",
  x=-265,
  y=0,
  radius=4,
)

s_mouth4 = play.new_box(
  color = "red",
  x = -270,
  y = -26,
  width = 13,
  height = 16,
)
s_mouth = play.new_box(
  color = "black",
  x = -265,
  y = -21,
  width = 26,
  height = 5,
)
s_mouth2 = play.new_box(
  color = "black",
  x = -278,
  y = -19,
  width = 5,
  height = 5,
)
s_mouth3 = play.new_box(
  color = "black",
  x = -252,
  y = -19,
  width = 5,
  height = 5,
)
#text starts first one
text = play.new_text(
   color=  "black",
   words = "I am so hungry ",
   x = -173,
   y = 54,
   font_size = 20,
 )
#text starts second one
@play.repeat_forever
async def speak_slowly():
  await play.timer(seconds = 5)
  text.words="I am still hungry :("

#to show where mouse is the cords
mouse_text=play.new_text(
  color="red",
  words = "blank",
   x = -173,
   y = 54,
   font_size = 20,
)
@play.repeat_forever
def mouse_coord():
  mouse_text.go_to(play.mouse)
  mouse_text.words = str(int(play.mouse.x))+", "+str(int(play.mouse.y))


play.start_program()