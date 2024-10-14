import multiprocessing
import random
import time
from playsound import playsound
import tkinter as tk
import os

global song_name
global orig_colour
song_name=None
SONGS_DIR = "Songs"
class Song:
    def __init__(self, title, file):
        self.title = title
        self.file = file

songs = [
    "16 Chapels", "3500", "90210", "Antidote", "Apple Pie", "Back On It", "Backyard", "Bad Mood Shit On You", "BACC", "Bandz",
    "Basement Freestyle", "beibs in the trap", "Blame", "Blocka La Flame", "coordinate", "Dance On The Moon", "Don't Play", "Drugs You Should Try It",
    "Drive", "First Class", "first take", "goosebumps", "Gree & Purple", "guidance", "Hell Of A Night", "High Fashion", "I Can Tell", "Impossible", "Mamacita", "Maria I'm Drunk", "Naked",
    "Nightcrawler", "Never Catch Me", "Oh My Dis Side", "outside", "Pornography", "Pray 4 Love", "Quintana", "Quintana Pt. 2",
    "sdp interlude", "Serenade", "Skyfall", "sweet sweet", "The Curse", "The Prayer", "the ends", "through the late night", "Up Top", "Upper Echelon", "Uptown", "way back", "wonderful", "Zombies"
]
def resetScore():
    with open("currentScore.txt", "w") as file:  # Open the file in write mode to clear its contents
        file.write("0\n0")  # Write "0" on the first line and "0" on the second line
    
    # Read the values back and update the scoreboard
    with open("currentScore.txt", "r") as file:
        wins1, plays1 = map(int, file.read().splitlines())
    
    with open("LifetimeScore.txt", "r") as file:
        wins2, plays2 = map(int, file.read().splitlines())
    
    global scoreboard
    scoreboard.config(text=f"Current Score: {wins1}/{plays1}\nOverall Score: {wins2}/{plays2}")

def play_again():
    global attempts
    global skips
    global orig_colour
    attempts = 6
    skips = 0
    global song_name
    song_name = chooseSong()
    guess_text1.configure(bg=orig_colour)
    guess_text2.configure(bg=orig_colour)
    guess_text3.configure(bg=orig_colour)
    guess_text4.configure(bg=orig_colour)
    guess_text5.configure(bg=orig_colour)
    guess_text6.configure(bg=orig_colour)
    guess_text1.delete("1.0", tk.END) 
    guess_text2.delete("1.0", tk.END) 
    guess_text3.delete("1.0", tk.END) 
    guess_text4.delete("1.0", tk.END) 
    guess_text5.delete("1.0", tk.END) 
    guess_text6.delete("1.0", tk.END) 
    update_scoreboard()
    
def chooseSong():
    global song_name
    song_name=random.choice(songs)
    return song_name

def update_scoreboard():
    with open("currentScore.txt", "r") as file:
        wins1, plays1 = map(int, file.read().splitlines())
    with open("LifetimeScore.txt", "r") as file:
        wins2, plays2 = map(int, file.read().splitlines())
    with open("analysis.txt", "r") as file:
        one = int(file.readline().strip())
        two = int(file.readline().strip())
        three = int(file.readline().strip())
        four = int(file.readline().strip())
        five = int(file.readline().strip())
        six = int(file.readline().strip())
    scoreboard.config(text=f"Current Score: {wins1}/{plays1}\nOverall Score: {wins2}/{plays2}")
    stats_text.config(text=f"1 Attempt:   {one}\n2 Attempts: {two}\n3 Attempts: {three}\n4 Attempts: {four}\n5 Attempts: {five}\n6 Attempts: {six}")

def play_song(song_name):
    song_name=os.path.join("Songs", song_name)
    p = multiprocessing.Process(target=playsound, args=(song_name+".mp3",))
    p.start()
    global skips
    if skips==0:
        time.sleep(1)
    elif skips==1:
        time.sleep(2.5)
    elif skips==2:
        time.sleep(4.5)
    elif skips==3:
        time.sleep(8)
    elif skips==4:
        time.sleep(16)
    elif skips==5:
        time.sleep(30)
    p.terminate()

def guess(guess_entry, song_name):
    global guess_text1
    global guess_text2
    global guess_text3
    global guess_text4
    global guess_text5
    global guess_text6
    guess_str = guess_entry.get()
    guess_entry.delete(0, tk.END)
    
    global attempts
    guessed_song=None
    for song in songs:
        if guess_str.lower().strip("'") == song.lower().strip("'"):
            guessed_song = song
            attempts-=1
            break

    if guessed_song is None:
        if 6-attempts==0:
            guess_text1.delete("1.0", tk.END)  
            guess_text1.tag_config('colour', background="yellow", foreground="blue")
            guess_text1.configure(bg="yellow")
            guess_text1.insert(tk.END, " Song not found. Try Again\n", 'colour')
        elif 6-attempts==1:
            guess_text2.delete("1.0", tk.END)  
            guess_text2.tag_config('colour', background="yellow", foreground="blue")
            guess_text2.configure(bg="yellow")
            guess_text2.insert(tk.END, " Song not found. Try Again\n", 'colour')
        elif 6-attempts==2:
            guess_text3.delete("1.0", tk.END)  
            guess_text3.tag_config('colour', background="yellow", foreground="blue")
            guess_text3.configure(bg="yellow")
            guess_text3.insert(tk.END, " Song not found. Try Again\n", 'colour')
        elif 6-attempts==3:
            guess_text4.delete("1.0", tk.END)  
            guess_text4.tag_config('colour', background="yellow", foreground="blue")
            guess_text4.configure(bg="yellow")
            guess_text4.insert(tk.END, " Song not found. Try Again\n", 'colour')
        elif 6-attempts==4:
            guess_text5.delete("1.0", tk.END)  
            guess_text5.tag_config('colour', background="yellow", foreground="blue")
            guess_text5.configure(bg="yellow")
            guess_text5.insert(tk.END, " Song not found. Try Again\n", 'colour')
        elif 6-attempts==5:
            guess_text6.delete("1.0", tk.END)  
            guess_text6.tag_config('colour', background="yellow", foreground="blue")
            guess_text6.configure(bg="yellow")
            guess_text6.insert(tk.END, " Song not found. Try Again\n", 'colour') 
        return
    
    if guessed_song.lower()==song_name.lower():
        if 6-attempts==1:
            guess_text1.delete("1.0", tk.END)  
            guess_text1.tag_config('colour', background="green", foreground="white")
            guess_text1.configure(bg="green")
            guess_text1.insert(tk.END, f" Congratulations! You guessed {song_name} in 1 try!\n", 'colour')
        elif 6-attempts==2:
            guess_text2.delete("1.0", tk.END)  
            guess_text2.tag_config('colour', background="green", foreground="white")
            guess_text2.configure(bg="green")
            guess_text2.insert(tk.END, f" Congratulations! You guessed {song_name} in 2 tries!\n", 'colour')
        elif 6-attempts==3:
            guess_text3.delete("1.0", tk.END)  
            guess_text3.tag_config('colour', background="green", foreground="white")
            guess_text3.configure(bg="green")
            guess_text3.insert(tk.END, f" Congratulations! You guessed {song_name} in 3 tries!\n", 'colour')
        elif 6-attempts==4:
            guess_text4.delete("1.0", tk.END)  
            guess_text4.tag_config('colour', background="green", foreground="white")
            guess_text4.configure(bg="green")
            guess_text4.insert(tk.END, f" Congratulations! You guessed {song_name} in 4 tries!\n", 'colour')
        elif 6-attempts==5:
            guess_text5.delete("1.0", tk.END)  
            guess_text5.tag_config('colour', background="green", foreground="white")
            guess_text5.configure(bg="green")
            guess_text5.insert(tk.END, f" Congratulations! You guessed {song_name} in 5 tries!\n", 'colour') 
        elif 6-attempts==6:
            guess_text6.delete("1.0", tk.END)  
            guess_text6.tag_config('colour', background="green", foreground="white")
            guess_text6.configure(bg="green")
            guess_text6.insert(tk.END, f" Congratulations! You guessed {song_name} in 6 tries!\n", 'colour')   
        with open("currentScore.txt", "r+") as file:
            wins, plays = map(int, file.read().splitlines())
            file.seek(0)
            file.write(f"{wins + 1}\n{plays + 1}")
        with open("LifetimeScore.txt", "r+") as file:
            wins, plays = map(int, file.read().splitlines())
            file.seek(0)
            file.write(f"{wins + 1}\n{plays + 1}")
        with open("analysis.txt", "r") as file:
            lines=file.readlines()
            line_number=6-attempts
            lines[line_number-1]=str(int(lines[line_number-1])+1)+"\n"
        with open("analysis.txt", "w") as file:
            file.writelines(lines)
        return
    else:
        if 6-attempts==1:
            guess_text1.delete("1.0", tk.END)  
            guess_text1.tag_config('colour', background="red", foreground="white")
            guess_text1.configure(bg="red")
            guess_text1.insert(tk.END, f" {guessed_song}: Incorrect. Try Again. {attempts} attempt(s) remaining\n", 'colour')
        elif 6-attempts==2:
            guess_text2.delete("1.0", tk.END)  
            guess_text2.tag_config('colour', background="red", foreground="white")
            guess_text2.configure(bg="red")
            guess_text2.insert(tk.END, f" {guessed_song}: Incorrect. Try Again. {attempts} attempt(s) remaining\n", 'colour')
        elif 6-attempts==3:
            guess_text3.delete("1.0", tk.END)  
            guess_text3.tag_config('colour', background="red", foreground="white")
            guess_text3.configure(bg="red")
            guess_text3.insert(tk.END, f" {guessed_song}: Incorrect. Try Again. {attempts} attempt(s) remaining\n", 'colour')
        elif 6-attempts==4:
            guess_text4.delete("1.0", tk.END)  
            guess_text4.tag_config('colour', background="red", foreground="white")
            guess_text4.configure(bg="red")
            guess_text4.insert(tk.END, f" {guessed_song}: Incorrect. Try Again. {attempts} attempt(s) remaining\n", 'colour')
        elif 6-attempts==5:
            guess_text5.delete("1.0", tk.END)  
            guess_text5.tag_config('colour', background="red", foreground="white")
            guess_text5.configure(bg="red")
            guess_text5.insert(tk.END, f" {guessed_song}: Incorrect. Try Again. {attempts} attempt(s) remaining\n", 'colour')
        elif 6-attempts==6:
            guess_text6.delete("1.0", tk.END)  
            guess_text6.tag_config('colour', background="red", foreground="white")
            guess_text6.configure(bg="red")
            guess_text6.insert(tk.END, f" {guessed_song}: Incorrect. Try Again. {attempts} attempt(s) remaining\n", 'colour')
    
    if attempts == -1:
        guess_text6.insert(tk.END, f"{guessed_song}. Sorry, you've run out of guesses. The correct song was: {song_name}\n")
        guess.text.configure(font = ("red"))
        with open("currentScore.txt", "r+") as file:
            wins, plays = map(int, file.read().splitlines())
            file.seek(0)
            file.write(f"{wins}\n{plays + 1}")
        with open("LifetimeScore.txt", "r+") as file:
            wins, plays = map(int, file.read().splitlines())
            file.seek(0)
            file.write(f"{wins}\n{plays + 1}")

def insert_song(guess_entry):
    selected_song = listbox.get(listbox.curselection())
    guess_entry.delete(0, tk.END)
    guess_entry.insert(0, selected_song)
    
def filter_songs(event, guess_entry):
    global songs
    global listbox
    entered_letter = guess_entry.get().strip().lower()
    filtered_songs = [song for song in songs if song.lower().startswith(entered_letter)]
    listbox.delete(0, tk.END)
    for song in filtered_songs:
        listbox.insert(tk.END, song)
    
def skip():
    global attempts
    global guess_text1
    global guess_text2
    global guess_text3
    global guess_text4
    global guess_text5
    global guess_text6
    global skip_button
    attempts -= 1
    global skips
    global guess_entry
    skips+=1
    if 6-attempts==1:
        guess_text1.delete("1.0", tk.END)  
        guess_text1.tag_config('colour', background="yellow", foreground="blue")
        guess_text1.configure(bg="yellow")
        guess_text1.insert(tk.END, f" Skipped. {attempts} attempt(s) remaining\n", 'colour')
    elif 6-attempts==2:
        guess_text2.delete("1.0", tk.END)  
        guess_text2.tag_config('colour', background="yellow", foreground="blue")
        guess_text2.configure(bg="yellow")
        guess_text2.insert(tk.END, f" Skipped. {attempts} attempt(s) remaining\n", 'colour')
    elif 6-attempts==3:
        guess_text3.delete("1.0", tk.END)  
        guess_text3.tag_config('colour', background="yellow", foreground="blue")
        guess_text3.configure(bg="yellow")
        guess_text3.insert(tk.END, f" Skipped. {attempts} attempt(s) remaining\n", 'colour')
    elif 6-attempts==4:
        guess_text4.delete("1.0", tk.END)  
        guess_text4.tag_config('colour', background="yellow", foreground="blue")
        guess_text4.configure(bg="yellow")
        guess_text4.insert(tk.END, f" Skipped. {attempts} attempt(s) remaining\n", 'colour')
    elif 6-attempts==5:
        guess_text5.delete("1.0", tk.END)  
        guess_text5.tag_config('colour', background="yellow", foreground="blue")
        guess_text5.configure(bg="yellow")
        guess_text5.insert(tk.END, f" Skipped. {attempts} attempt(s) remaining\n", 'colour')
    if attempts <= 0:
        guess_text6.delete("1.0", tk.END)  
        guess_text6.tag_config('colour', background="yellow", foreground="blue")
        guess_text6.configure(bg="yellow")
        guess_text6.insert(tk.END, " No more skips\n", 'colour')
        skip_button.pack_forget()
        attempts+=1

def main():
    # Pick a random song
    global song_name
    global play_again_button
    global skip_button
    global orig_colour
    song_name = chooseSong()
    global skips
    skips=0
    global root
    global attempts
    global guess_text1
    global guess_text2
    global guess_text3
    global guess_text4
    global guess_text5
    global guess_text6
    global listbox
    attempts = 6

    # Create the main window
    root = tk.Tk()
    root.geometry("1500x900")
    root.title("Travis Scott Heardle")
    
    frame=tk.Frame(root)
    scrollbar=tk.Scrollbar(frame, orient=tk.VERTICAL)

    # Create widgets
    listbox=tk.Listbox(frame, width=225, yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)
    
    
    label_guess = tk.Label(root, text="Guess the song:")
    guess_entry = tk.Entry(root, font=("Helvetica", 30))
    button_guess = tk.Button(root, text="Guess", command=lambda: guess(guess_entry, song_name))
    play_image = tk.PhotoImage(file="play.png").subsample(2, 2)
    skip_button=tk.Button(root, text="Skip", command=skip)
    
    guess_text1 = tk.Text(root, wrap=tk.WORD, width=130, height=75, font=("Helvetica", 48))
    guess_text2 = tk.Text(root, wrap=tk.WORD, width=130, height=75, font=("Helvetica", 48))
    guess_text3 = tk.Text(root, wrap=tk.WORD, width=130, height=75, font=("Helvetica", 48))
    guess_text4 = tk.Text(root, wrap=tk.WORD, width=130, height=75, font=("Helvetica", 48))
    guess_text5 = tk.Text(root, wrap=tk.WORD, width=130, height=75, font=("Helvetica", 48))
    guess_text6 = tk.Text(root, wrap=tk.WORD, width=130, height=75, font=("Helvetica", 48))
    orig_colour = guess_text1.cget("background")
    
    # Create a button with the image
    play_button = tk.Button(root, image=play_image, command=lambda: play_song(song_name))
    
    play_again_button = tk.Button(root, text="Play Again", command=play_again)
    global scoreboard
    global stats_text
    
    with open("currentScore.txt", "r") as file:
        wins1 = int(file.readline().strip())
        plays1 = int(file.readline().strip())
    with open("LifetimeScore.txt", "r") as file:
        wins2 = int(file.readline().strip())
        plays2 = int(file.readline().strip())
    with open("Analysis.txt", "r") as file:
        one = int(file.readline().strip())
        two = int(file.readline().strip())
        three = int(file.readline().strip())
        four = int(file.readline().strip())
        five = int(file.readline().strip())
        six = int(file.readline().strip())
    
    scoreboard = tk.Label(root, text=f"Current Score: {wins1}/{plays1}\nOverall Score: {wins2}/{plays2}")
    stats_text=tk.Label(root, text=f"1 Attempt:   {one}\n2 Attempts: {two}\n3 Attempts: {three}\n4 Attempts: {four}\n5 Attempts: {five}\n6 Attempts: {six}")
    resetScoreButton=tk.Button(root, text="Reset Current Score", command=resetScore)


    # Place widgets on the window
    play_button.place(width=80, height=80, x=665, y=483)
    label_guess.place(width=300, height=45, x=57, y=840)
    scoreboard.place(width=150, height=30, x=1300, y=630)
    stats_text.place(width=150, height=150, x=1300, y=660)
    guess_entry.place(width=700, height=50, x=150, y=800)
    button_guess.place(width=125, height=52, x=25, y=800)
    guess_text1.place(width=1450, height=75, x=25, y=30)
    guess_text2.place(width=1450, height=75, x=25, y=105)
    guess_text3.place(width=1450, height=75, x=25, y=180)
    guess_text4.place(width=1450, height=75, x=25, y=255)
    guess_text5.place(width=1450, height=75, x=25, y=330)
    guess_text6.place(width=1450, height=75, x=25, y=405)
    play_again_button.place(width=140, height=60, x=27, y=483)
    resetScoreButton.place(width=170, height=35, x=1290, y=800)
    skip_button.place(width=140, height=60, x=1332, y=483)
    scrollbar.pack(side=tk.RIGHT, fill="y", pady=10)
    frame.place(width=700, height=250, x=150, y=600)
    listbox.pack(pady=15)
    for song in songs:
        listbox.insert(tk.END, song)
    
    listbox.bind('<<ListboxSelect>>', lambda event: insert_song(guess_entry))
    guess_entry.bind('<KeyRelease>', lambda event: filter_songs(event, guess_entry))
    root.mainloop()


if __name__ == "__main__":
    main()
