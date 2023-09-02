from tkinter import *
import random

# Our Variables

player_score = 0
player_x = 0
player_y = 400

target_x = 250
target_y = 250

time_counter = 0
point_time = 5


def display_score():
    score_label = Label(root, text="Score: {}".format(player_score), font=("arial", 18, "bold"))
    score_label.place(x=370, y=0, width=130, height=50)


def display_time():
    time_label = Label(root, text="remaining Time: {}".format(point_time - time_counter))
    time_label.place(x=0, y=0)
    return time_label


def display_player():
    player_label = Label(root, image=photo_image1)
    player_label.place(x=player_x, y=player_y, width=100, height=100)


def display_target():
    target_label = Label(root, image=photo_image2)
    target_label.place(x=target_x, y=target_y, width=40, height=40)


def display_game_over():
    game_over_label = Label(root, text="Game Over", font=("arial", 30, "bold"), fg="red")
    game_over_label.place(x=0, y=50, width=500, height=450)


def randomize_target_location():
    global target_x, target_y
    target_x = random.randrange(0, 400)
    target_y = random.randrange(0, 400)


def player_gain_point():
    global player_score, time_counter
    player_score += 1
    time_counter = 0


def player_lost_point():
    global player_score, time_counter
    player_score -= 1
    time_counter = 0


def counter_fun(label):
    def count():
        global time_counter, player_score
        time_counter += 1
        if point_time - time_counter == -1:
            player_lost_point()
            display_score()
        display_time()
        if player_score == -1:
            display_game_over()
        label.after(1000, count)
    count()


root = Tk()

root.title("Eat Fruit")
root.geometry("500x500")
root.geometry("+500+50")
root.configure(bg="#346934")

display_time()
counter_fun(display_time())

display_score()

# Player Character initial Place
player_photo = PhotoImage(file=r"C:\Users\Seif El-Deen\Pictures\bird.png")
photo_image1 = player_photo.subsample(1)
display_player()

# Target Character initial Place
target_photo = PhotoImage(file=r"C:\Users\Seif El-Deen\Pictures\apple.png")
photo_image2 = target_photo.subsample(1, 1)
display_target()


def clear_screen():
    # Remove all widgets from the root window
    for widget in root.winfo_children():
        if widget["text"] != "":
            continue
        widget.destroy()


def key_pressed(event):
    global player_x, player_y, target_x, target_y, player_score, time_counter

    if event.keysym == "Up":
        player_y -= 10
    if event.keysym == "Down":
        player_y += 10
    if event.keysym == "Left":
        player_x -= 10
    if event.keysym == "Right":
        player_x += 10

    clear_screen()
    display_target()

    display_player()

    if target_x <= player_x + 50 <= target_x + 50 and target_y + 50 >= player_y + 50 >= target_y:
        player_gain_point()

        display_time()
        display_score()

        randomize_target_location()


root.bind("<Key>", key_pressed)
root.mainloop()
