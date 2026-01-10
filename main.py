import pgzrun
from pygame import Rect
WIDTH=800
HEIGHT=700
marquee_box=Rect(0,0,800,60)
question_box=Rect(20,80,500,140)
timer_box=Rect(570,80,140,140)
skip_box=Rect(550,275,175,315)
ans_box1=Rect(40,275,200,140)
ans_box2=Rect(40,450,200,140)
ans_box3=Rect(260,275,200,140)
ans_box4=Rect(260,450,200,140)

answer_boxes=[ans_box1,ans_box2,ans_box3,ans_box4]
score = 0
is_game_over = False
marquee_message = ""
time_left=10

def draw():
    screen.fill("black")
    screen.draw.filled_rect(marquee_box,"black")
    screen.draw.filled_rect(question_box,"red")
    screen.draw.filled_rect(timer_box,"purple")
    screen.draw.filled_rect(skip_box,"yellow")
    #to add answer boxes
    for ans_box in answer_boxes:
        screen.draw.filled_rect(ans_box,"orange")

    #adding text to marquee box
    marquee_message="Welcome to Quiz Master"
    marquee_message += f"Q:{question_index} of {question_count}"
    screen.draw.textbox(marquee_message, marquee_box, 
                        color="white")

    #adding text to the timer box
    screen.draw.textbox(str(time_left), timer_box, color="white", shadow=(0.5,0.5),scolor="grey")

    #adding a text to a skip box
    screen.draw.textbox("skip", skip_box, color="black", 
                        angle=-90)
    
    #adding text to the question box
    screen.draw.textbox(question[0].strip(), question_box, 
            color="white", shadow=(0.5,0.5), 
            scolor="dim grey")

    #adding text to the answer boxes
    index=1
    for ans_box in answer_boxes:
        screen.draw.textbox(question[index].strip(), ans_box, color="black")
        index = index + 1 
def update():
    move_marquee()

def move_marquee():
    marquee_box.x-=2
    if marquee_box.right<0:
        marquee_box.left=WIDTH

question_file_name="Quiz master\questions.txt"
questions=[]
question_count=0
question_index=0

def read_question_file():
    global question_count,questions
    q_file=open(question_file_name,"r")
    for question in q_file:
        questions.append(question)
        question_count+=1
    q_file.close()

def read_next_ques():
    global question_index
    question_index += 1
    return questions.pop(0).split("|")

def on_mouse_down(pos):
    index=1
    for box in answer_boxes:
        if box.collidepoint(pos):
            if index == int(question[5]):
                correct_answer()
            else:
                game_over()
    if skip_box.collidepoint(pos):
        skip_question()

def correct_answer():
    global score,question,time_left,questions
    score += 1
    if questions:
        question = read_next_ques()
        time_left = 10
    else:
        game_over()

def game_over():
    global question,time_left,is_game_over
    message = f"Game over!\nYou got {score} questions correct!"
    question = [message,"-","-","-","-",5]
    time_left = 0
    is_game_over = True

def skip_question():
    global question,time_left
    if questions and not is_game_over:
        question=read_next_ques()
        time_left=10
    else:
        game_over()

def update_time_left():
    global time_left
    if time_left:
        time_left=time_left-1
    else:
        game_over()

read_question_file()
question = read_next_ques()
clock.schedule_interval(update_time_left,1)

pgzrun.go()
