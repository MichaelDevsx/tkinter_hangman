import tkinter as tk
from tkinter import Text, WORD, END
import customtkinter
from PIL import Image
import os
import random

img_blur_list = []
hide_word = []




def random_pick_blur():
    #random pick img-blur
    img_blur = "Hangman/assets/blur"
    for filename in os.listdir(img_blur):
        if filename.endswith(".jpg"):
            name = os.path.splitext(filename)[0]
            img_blur_list.append(name)
    img_blur_random = random.choice(img_blur_list)
    img_blur_list.remove(img_blur_random)

    return img_blur_random

def new_pick_blur():
    pick_img = random_pick_blur()
    random_img = customtkinter.CTkImage(dark_image=Image.open(f"Hangman/assets/blur/{pick_img}.jpg"), size=(300,300))
    return img.configure(image = random_img)



root = customtkinter.CTk()
root.title("Hangman Project")
user_life = tk.IntVar(value=0)

def on_start():
    my_text.insert(END,
    """
    **Rules**

    You have to guess the picture sending
    letter by letter.
    If your try to guess the complet word and it isnt 
    correct you will fail and lost all of your chances.

    -You have 3 lifes, 
    its mean that you have 3 chances to guess.

    -If you are ready. Type Ready and submit it..

    The Game will automatically start

    Enjoy!.
    """
    )
    sframe.pack(padx=5, pady=15)
    btn_reset.grid(row=0, column=1, padx=10, pady=5)
    submit.grid(row=1, column=2, sticky="w")

letters_guessed = []

def start_game(guess=None):
    global letters_guessed
    hide_word = []
    submit.grid_forget()
    btn_submit.grid(row=1, column=1, sticky="w")
    my_text.delete(1.0, END)
    img.grid(row=0, column=1, padx=10, pady=5)
    img_blur_random = pick_img
    my_text.insert(END,f"""Try to guess the name of the movie
        it has {len(img_blur_random)} letters\n\n""")
    for i in range(len(img_blur_random)):
        hide_word.append("_")
    hide = " ".join(hide_word)
    my_text.insert(END,f"{hide}\n\n")
    if guess is not None and len(guess) == 1:
        if guess in img_blur_random:
            for i in range(len(img_blur_random)):
                if img_blur_random[i] == guess:
                    hide_word[i] = guess
                    if guess not in letters_guessed:
                        letters_guessed.append(guess)
            hide = ""
            for letter in img_blur_random:
                if letter in letters_guessed:
                    hide += f"{letter} "
                else:
                    hide += "_ "
            my_text.delete(1.0, END)
            my_text.insert(END,f"{hide}\n\n")

            if "_" not in hide:
                my_text.insert(END, "¡Felicidades, has ganado el juego!")
                img.configure(image=normal_img)
                btn_submit.grid_forget()
                btn_start.grid_forget()

        else:
            my_text.delete(1.0, END)
            my_text.insert(END,f"The letter is not in the word. Try again!\n\n")
            user_life.set(user_life.get()-1)

    if user_life.get() == 0:
        my_text.insert(END, "Game Over! ")
        img.configure(image=normal_img)
        btn_submit.grid_forget()
        btn_start.grid_forget()

    elif guess is not None and len(guess) > 1:
        if guess == img_blur_random:
            hide_word = list(guess)
            hide = " ".join(hide_word)
            my_text.delete(1.0, END)
            my_text.insert(END,f"{hide}\n\n")
            my_text.insert(END, "¡Felicidades, has ganado el juego!")
            img.configure(image=normal_img)
            btn_submit.grid_forget()
            btn_start.grid_forget()

        else:
            user_life.set(user_life.get() - 1)


    
    # hide = " ".join(hide_word)
    # my_text.insert(END,f"{hide}\n\n")





def on_reset():
    global letters_guessed
    # Limpiar variables y elementos visuales
    letters_guessed = []
    hide_word.clear()
    my_text.delete(1.0, END)
    chat_entry.delete(0, END)
    sframe.pack_forget()
    btn_reset.grid_forget()
    img.grid_forget()
    btn_submit.grid_forget()
    btn_start.grid(row=0, column=0, padx=10, pady=5)



def on_submit():
    user_life.set(3)
    user = chat_entry.get().lower()
    chat_entry.delete(0, END)
    if user == "ready":
        start_game()
    elif user == "quit":
        root.quit()
    else:
        my_text.delete(1.0, END)
        my_text.insert(END,f"""{user} is not a valid word. Please Type Ready or quit to finish the game.""")


def game_submit():
    guess = chat_entry.get()
    chat_entry.delete(0, END)
    start_game(guess)







#set color
customtkinter.set_appearance_mode("dark") #dark, light, system
customtkinter.set_default_color_theme("dark-blue")


#creating frame for the first line
fframe = customtkinter.CTkFrame(root,fg_color="transparent")
fframe.pack(pady=10)

customtkinter.CTkLabel(
    fframe,
    text="UserName",
    fg_color="transparent"
).grid(row=0, column=0, padx=5, pady=5)

user_entry = tk.StringVar()
customtkinter.CTkEntry(
    fframe,
    placeholder_text="Write yor name",
    textvariable=user_entry
).grid(row=0, column=1, columnspan=2, padx=5, pady=5)

customtkinter.CTkLabel(
    fframe,
    text="LIFE",
    fg_color="transparent"
).grid(row=0, column=3, padx=15)


customtkinter.CTkEntry(
    fframe,
    placeholder_text="Write yor name",
    textvariable= user_life,
    width=30,
    corner_radius=10,
    state="readonly"
).grid(row=0, column=4 ,padx=5, pady=5)


sframe = customtkinter.CTkFrame(root,fg_color="transparent")
sframe.pack_forget()

#text widget to get the answer of the game

my_text = Text(
    sframe,
    bg="#343638",
    width=60,
    bd=1,
    fg="#d6d6d6",
    relief="flat",
    wrap=WORD,
    selectbackground="#1f538d"
)
my_text.grid(row=0, column=0, padx=10, pady=10)

#random img
pick_img = random_pick_blur()
random_img = customtkinter.CTkImage(dark_image=Image.open(f"Hangman/assets/blur/{pick_img}.jpg"), size=(300,300))
normal_img = customtkinter.CTkImage(dark_image=Image.open(f"Hangman/assets/normal/{pick_img}.jpg"), size=(300,300))

img = customtkinter.CTkLabel(
    sframe,
    text="",
    image=random_img,
    fg_color="transparent"
)
img.grid_forget()

chat_entry = customtkinter.CTkEntry(
    sframe,
    placeholder_text="Type to Guess the picture",
    width=400,
    height=50,
    border_width=2
)
chat_entry.grid(row=1, column=0, pady=10)

#configuration and button to submit words to guess

img_submit = customtkinter.CTkImage(dark_image=Image.open("Hangman/assets/submit.png"), size=(40,40))

btn_submit = customtkinter.CTkButton(
    sframe,
    text="",
    width=3,
    image=img_submit,
    fg_color="transparent",
    command=game_submit
)
btn_submit.grid_forget()

#button to submit information
submit = customtkinter.CTkButton(
    sframe,
    text="Submit",
    command= on_submit
)
submit.grid(row=1, column=2, sticky="w")

bframe = customtkinter.CTkFrame(root, fg_color="transparent")
bframe.pack(side="bottom", padx=5, pady=5)

#start button

btn_start = customtkinter.CTkButton(
    bframe,
    text="Start",
    command=on_start,
)
btn_start.grid(row=0, column=0, padx=10, pady=5)

#reset button
btn_reset = customtkinter.CTkButton(
    bframe,
    text="Reset",
    command=on_reset,
)
btn_reset.grid_forget()


root.mainloop()