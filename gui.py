# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 03:20:57 2019

@author: rohit
"""

#imports
import tkinter.messagebox
from tkinter import *
from pygame import mixer
from tkinter import filedialog
from mutagen.mp3 import MP3
from os import listdir
import os
import threading
import time

#intializing root
root=Tk()
root.title("Music Recommender")
root.iconbitmap("C:/Users/admin/Desktop/music_player_QXR_icon.ico")

#intializing menu bar
menubar = Menu(root)
root.config(menu=menubar)
subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=subMenu)


#implement browsing from the menu
def browse_file():
    global filename
    filename = filedialog.askopenfilename()

#the about us stuff
def about_us():
    tkinter.messagebox.showinfo('About Music Recommender', 'This is a music player built by students of BMSCE')


#keeping these here as i can't call funmction if they are down
subMenu.add_command(label="Open", command=browse_file)
subMenu.add_command(label="Exit",command=root.destroy)
subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=subMenu)
subMenu.add_command(label="About Us",command=about_us)

#intializing mixer
mixer.init()
global playlist
playlist=[]

def listbox_init():
    index=0
    file = 'C:/Users/admin/Desktop/dataset'
    for song in listdir(file):
        Lb1.insert(index, song)
        index+=1

def playlist_init():
    playlist[:]=[]
    index=0
    file = 'C:/Users/admin/Desktop/dataset'
    for song in listdir(file):
        index+=1
        playlist.insert(index,file+'/'+song)
    


#keeping this here as i can't call funmction if they are down same reason
def search_text():
    global playlist
    print("hello")
    temp=[]
    index=0
    if searchText.get()=='':
        Lb1.delete(0, END)
        playlist_init()
        for song in playlist:
            Lb1.insert(index,os.path.basename(song))
            index+=1
        tkinter.messagebox.showinfo('No text entered')
        #listbox_init()
    else:
        Lb1.delete(0, END)
        word=searchText.get()
        for song in playlist:
            if word in song:
                Lb1.insert(index,os.path.basename(song))
                temp.insert(index,song)
                index+=1
        playlist[:]=[]
        playlist=temp[:]
        
    
#created 2 frames left and right
leftframe = Frame(root)
leftframe.pack(side=LEFT, padx=30)

#entry text
searchText = Entry(leftframe)
searchText.grid(row=0,column=0,padx=15)

#entry button
searchButton = Button(leftframe,text="search",command=search_text)
searchButton.grid(row=0,column=1,pady=15)

#created a list cause ill use this in future to take the song


#created scrollbar and listbox, btw gotta check if this works
scrollbar = Scrollbar(leftframe)
Lb1 = Listbox(leftframe, yscrollcommand = scrollbar.set)
index=0
file = 'C:/Users/admin/Desktop/dataset'

for song in listdir(file):
    Lb1.insert(index, song)
    index+=1
    playlist.insert(index,file+'/'+song)
    
Lb1.grid(row=1,column=0,pady=30)
scrollbar.config( command = Lb1.yview )
scrollbar.grid(row=1,column=0,sticky=E)


#created right frame
rightframe = Frame(root)
rightframe.pack()

#in right frame, top , middle and bottom
topframe = Frame(rightframe)
topframe.pack()


filelabel = Label(topframe, text='Welcome')
filelabel.pack(pady=10)

lengthlabel = Label(topframe, text='Total Length : --:--')
lengthlabel.pack()

currenttimelabel = Label(topframe, text='Current Time : --:--', relief=GROOVE)
currenttimelabel.pack()






def show_details(play_song):
    filelabel['text'] = "Playing"+ '-' + os.path.basename(play_song)
    file_data = os.path.splitext(play_song)
    print(file_data)

    if file_data[1] == '.mp3':
        audio = MP3(play_song)
        total_length = audio.info.length
    else:
        a = mixer.Sound(play_song)
        total_length = a.get_length()
    print(total_length)
    # div - total_length/60, mod - total_length % 60
    mins, secs = divmod(total_length, 60)
    mins = round(mins)
    secs = round(secs)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    lengthlabel['text'] = "Total Length" + ' - ' + timeformat

    t1 = threading.Thread(target=start_count, args=(total_length,))
    t1.start()


def start_count(t):
    global paused
    current_time = 0
    while current_time <= t and mixer.music.get_busy():
        if paused:
            continue
        else:
            mins, secs = divmod(current_time, 60)
            mins = round(mins)
            secs = round(secs)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            currenttimelabel['text'] = "Current Time" + ' - ' + timeformat
            time.sleep(1)
            current_time += 1


def play_music():
    global paused
    if paused:
        mixer.music.unpause()
        paused = FALSE
    else:
        try:
            stop_music()
            time.sleep(1)
            selected_song=Lb1.curselection()
            selected_song = int(selected_song[0])
            play_song=playlist[selected_song]
            mixer.music.load(play_song)
            mixer.music.play()
            playlist_init()
            show_details(play_song)
        except:
            tkinter.messagebox.showerror('File not found', 'Music Recommender could not find the file. Please check again.')
   
        


def stop_music():
    mixer.music.stop()


paused = FALSE

def pause_music():
    global paused
    paused = TRUE
    mixer.music.pause()

def rewind_music():
    play_music()


def set_vol(val):
    volume = int(val) / 100
    mixer.music.set_volume(volume)


muted = FALSE


def mute_music():
    global muted
    if muted:  # Unmute the music
        mixer.music.set_volume(0.7)
        volumeBtn.configure(image=volumePhoto)
        scale.set(70)
        muted = FALSE
    else:  # mute the music
        mixer.music.set_volume(0)
        volumeBtn.configure(image=mutePhoto)
        scale.set(0)
        muted = TRUE


middleframe = Frame(rightframe)
middleframe.pack(pady=10)

photoplay = PhotoImage(file='C:/Users/admin/Desktop/play-button (3).png')
btnplay = Button(middleframe, image=photoplay, command=play_music)
btnplay.grid(row=0, column=0, padx=10)

photostop = PhotoImage(file='C:/Users/admin/Desktop/stop.png')
btnstop = Button(middleframe, image=photostop, command=stop_music)
btnstop.grid(row=0, column=1, padx=10)

pausePhoto = PhotoImage(file='C:/Users/admin/Desktop/pause.png')
pauseBtn = Button(middleframe, image=pausePhoto, command=pause_music)
pauseBtn.grid(row=0, column=2, padx=10)


bottomframe = Frame(rightframe)
bottomframe.pack()

rewindPhoto = PhotoImage(file='C:/Users/admin/Desktop/rewind.png')
rewindBtn = Button(bottomframe, image=rewindPhoto, command=rewind_music)
rewindBtn.grid(row=0,column=0)

mutePhoto = PhotoImage(file='C:/Users/admin/Desktop/mute.png')
volumePhoto = PhotoImage(file='C:/Users/admin/Desktop/speaker.png')
volumeBtn = Button(bottomframe, image=volumePhoto, command=mute_music)
volumeBtn.grid(row=0, column=1)


scale = Scale(bottomframe, from_=0, to=100, orient=HORIZONTAL, command=set_vol)
scale.set(70)
mixer.music.set_volume(0.7)
scale.grid(row=0,column=2,pady=15,padx=30)


def on_closing():
    stop_music()
    root.destroy()


root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
