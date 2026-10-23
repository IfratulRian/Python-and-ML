import turtle
import random

# ---------- Settings (change these) ----------
WIDTH, HEIGHT = 500, 620
STEP = 20                 # size of each move
SPEED_LEVELS = {          # milliseconds per move (bigger = slower)
    "1": 300,             # slow
    "2": 220,             # normal
    "3": 150,             # fast
}
START_DELAY = SPEED_LEVELS["1"]
SPEEDUP_PER_FOOD = 0      # set to e.g. 4 to get faster as you eat
MIN_DELAY = 100

# Play area (grid aligned). The score panel is ABOVE Y_TOP, so the snake can't enter it.
X_LIMIT = 240
Y_TOP, Y_BOTTOM = 200, -280
PANEL_BOTTOM = Y_TOP + 20 + 4   # panel starts just above the play area border

# ---------- Window ----------
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(WIDTH, HEIGHT)
screen.tracer(0)


def draw_rect(t, x1, y1, x2, y2):
    """Draw a rectangle from top-left (x1,y1) to bottom-right (x2,y2)."""
    t.penup()
    t.goto(x1, y1)
    t.setheading(0)
    t.pendown()
    for w, h in ((x2 - x1, 0), (0, y2 - y1), (x1 - x2, 0), (0, y1 - y2)):
        t.goto(t.xcor() + w, t.ycor() + h)
    t.penup()


# ---------- Score panel (top) ----------
panel = turtle.Turtle()
panel.hideturtle()
panel.speed(0)
panel.color("#f0f0f0")
panel.begin_fill()
draw_rect(panel, -WIDTH // 2, HEIGHT // 2, WIDTH // 2, PANEL_BOTTOM)
panel.end_fill()

# ---------- Play-area border ----------
border = turtle.Turtle()
border.hideturtle()
border.speed(0)
border.pensize(3)
border.color("#555555")
draw_rect(border, -X_LIMIT - STEP // 2, Y_TOP + STEP // 2,
          X_LIMIT + STEP // 2, Y_BOTTOM - STEP // 2)

score_pen = turtle.Turtle()
score_pen.hideturtle()
score_pen.penup()
score_pen.color("black")

message_pen = turtle.Turtle()
message_pen.hideturtle()
message_pen.penup()
message_pen.color("white")

# ---------- Game state ----------
segments = []
direction = "stop"
next_direction = "stop"
score = 0
high_score = 0
delay = START_DELAY
game_over = False

# ---------- Food ----------
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.shapesize(0.8, 0.8)
food.penup()


def update_score():
    score_pen.clear()
    score_pen.goto(0, PANEL_BOTTOM + 20)
    score_pen.write(f"Score:{score}", align="center", font=("Courier", 30, "normal"))
    score_pen.goto(WIDTH // 2 - 10, PANEL_BOTTOM + 6)
    score_pen.write(f"Best:{high_score}", align="right", font=("Courier", 11, "normal"))
    score_pen.goto(-WIDTH // 2 + 10, PANEL_BOTTOM + 6)
    speed_name = {300: "Slow", 220: "Normal", 150: "Fast"}.get(delay, f"{delay}ms")
    score_pen.write(f"Speed:{speed_name}", align="left", font=("Courier", 11, "normal"))


def new_segment(x, y):
    seg = turtle.Turtle()
    seg.shape("square")
    seg.color("lime")
    seg.penup()
    seg.goto(x, y)
    segments.append(seg)


def place_food():
    occupied = {(round(s.xcor()), round(s.ycor())) for s in segments}
    while True:
        x = random.randrange(-X_LIMIT, X_LIMIT + 1, STEP)
        y = random.randrange(Y_BOTTOM, Y_TOP + 1, STEP)
        if (x, y) not in occupied:
            food.goto(x, y)
            return


def reset_game():
    global direction, next_direction, score, game_over
    for s in segments:
        s.goto(1000, 1000)
        s.hideturtle()
    segments.clear()
    message_pen.clear()

    new_segment(-200, -100)
    new_segment(-200, -120)
    new_segment(-200, -140)

    direction = "stop"
    next_direction = "stop"
    score = 0
    game_over = False
    place_food()
    update_score()
    message_pen.goto(0, -20)
    message_pen.write("Press an arrow key / WASD to start\nKeys 1 / 2 / 3 = speed",
                      align="center", font=("Arial", 13, "normal"))


def end_game():
    global game_over, high_score
    game_over = True
    high_score = max(high_score, score)
    message_pen.clear()
    message_pen.goto(0, 0)
    message_pen.write("GAME OVER", align="center", font=("Arial", 28, "bold"))
    update_score()
    screen.ontimer(reset_game, 1500)


# ---------- Controls ----------
def go_up():
    global next_direction
    if direction != "down":
        next_direction = "up"


def go_down():
    global next_direction
    if direction != "up":
        next_direction = "down"


def go_left():
    global next_direction
    if direction != "right":
        next_direction = "left"


def go_right():
    global next_direction
    if direction != "left":
        next_direction = "right"


def set_speed(level):
    def _set():
        global delay
        delay = SPEED_LEVELS[level]
        update_score()
    return _set


screen.listen()
for key in ("Up", "w"):
    screen.onkeypress(go_up, key)
for key in ("Down", "s"):
    screen.onkeypress(go_down, key)
for key in ("Left", "a"):
    screen.onkeypress(go_left, key)
for key in ("Right", "d"):
    screen.onkeypress(go_right, key)
for level in SPEED_LEVELS:
    screen.onkeypress(set_speed(level), level)


# ---------- Main loop ----------
def game_loop():
    global direction, score, delay

    if not game_over:
        direction = next_direction

        if direction != "stop":
            message_pen.clear()
            head = segments[0]
            x, y = head.xcor(), head.ycor()
            if direction == "up":
                y += STEP
            elif direction == "down":
                y -= STEP
            elif direction == "left":
                x -= STEP
            elif direction == "right":
                x += STEP

            hit_wall = abs(x) > X_LIMIT or y > Y_TOP or y < Y_BOTTOM
            hit_self = any(round(s.xcor()) == round(x) and round(s.ycor()) == round(y)
                           for s in segments[:-1])

            if hit_wall or hit_self:
                end_game()
            else:
                ate = round(x) == round(food.xcor()) and round(y) == round(food.ycor())
                tail_x, tail_y = segments[-1].xcor(), segments[-1].ycor()

                for i in range(len(segments) - 1, 0, -1):
                    segments[i].goto(segments[i - 1].xcor(), segments[i - 1].ycor())
                head.goto(x, y)

                if ate:
                    new_segment(tail_x, tail_y)
                    score += 10
                    if SPEEDUP_PER_FOOD:
                        delay = max(MIN_DELAY, delay - SPEEDUP_PER_FOOD)
                    update_score()
                    place_food()

    screen.update()
    screen.ontimer(game_loop, delay)


reset_game()
game_loop()
screen.mainloop()