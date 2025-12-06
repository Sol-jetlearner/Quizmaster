import pgzrun
from pygame import Rect
WIDTH=800
HEIGHT=700
marquee_box=Rect(0,0,800,60)
question_box=Rect(20,80,500,140)
timer_box=Rect(570,80,140,140)
skip_box=Rect()
ans_box1=Rect()
ans_box2=Rect()
ans_box3=Rect()
ans_box4=Rect()

#answer_boxes=[ans_box1,ans_box2,ans_box3,ans_box4]
def draw():
    screen.fill("black")
    screen.draw.filled_rect(marquee_box,"blue")
    screen.draw.filled_rect(question_box,"red")
    screen.draw.filled_rect(timer_box,"purple")



def update():
    pass

def move_marquee():
    pass

def read_question_file():
    pass

def read_next_ques():
    pass

def on_mouse_down():
    pass

def correct_answer():
    pass

def game_over():
    pass

def skip_question():
    pass

def update_time_left():
    pass

pgzrun.go()