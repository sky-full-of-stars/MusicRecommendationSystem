import Tkinter
import tempfile
import os
from tkFileDialog import askopenfilename , asksaveasfilename    
import ttk
import tkMessageBox
from Tkconstants import *
import random
import pyaudio
import wave

#############################################################################
#This code has been taken from https://gist.github.com/sloria/5693955 by sloria
class Recorder(object):
    '''A recorder class for recording audio to a WAV file.
    Records in mono by default.
    '''

    def __init__(self, channels=1, rate=44100, frames_per_buffer=1024):
        self.channels = channels
        self.rate = rate
        self.frames_per_buffer = frames_per_buffer

    def open1(self, fname, mode='wb'):
        return RecordingFile(fname, mode, self.channels, self.rate,
                            self.frames_per_buffer)

class RecordingFile(object):
    def __init__(self, fname, mode, channels, 
                rate, frames_per_buffer):
        self.fname = fname
        self.mode = mode
        self.channels = channels
        self.rate = rate
        self.frames_per_buffer = frames_per_buffer
        self._pa = pyaudio.PyAudio()
        self.wavefile = self._prepare_file(self.fname, self.mode)
        self._stream = None

    def __enter__(self):
        return self

    def __exit__(self, exception, value, traceback):
        self.close()

    def record(self, duration):
        # Use a stream with no callback function in blocking mode
        self._stream = self._pa.open(format=pyaudio.paInt16,
                                        channels=self.channels,
                                        rate=self.rate,
                                        input=True,
                                        frames_per_buffer=self.frames_per_buffer)
        for _ in range(int(self.rate / self.frames_per_buffer * duration)):
            audio = self._stream.read(self.frames_per_buffer)
            self.wavefile.writeframes(audio)
        return None

    def start_recording(self):
        # Use a stream with a callback in non-blocking mode
        self._stream = self._pa.open(format=pyaudio.paInt16,
                                        channels=self.channels,
                                        rate=self.rate,
                                        input=True,
                                        frames_per_buffer=self.frames_per_buffer,
                                        stream_callback=self.get_callback())
        self._stream.start_stream()
        return self

    def stop_recording(self):
        self._stream.stop_stream()
        return self

    def get_callback(self):
        def callback(in_data, frame_count, time_info, status):
            self.wavefile.writeframes(in_data)
            return in_data, pyaudio.paContinue
        return callback


    def close(self):
        self._stream.close()
        self._pa.terminate()
        self.wavefile.close()

    def _prepare_file(self, fname, mode='wb'):
        wavefile = wave.open(fname, mode)
        wavefile.setnchannels(self.channels)
        wavefile.setsampwidth(self._pa.get_sample_size(pyaudio.paInt16))
        wavefile.setframerate(self.rate)
        return wavefile

#############################################################################
banglakey=Tkinter.Tk()

banglakey.title('Music player 1.3')
"""song=StringVar()
label=Label(banglakey,text="Hii there! How are you doing ? Wanna listen some music?",fg="black",font='times 36')
label.pack()
search=Entry(banglakey,textvariable=song,bg="beige",fg="purple",font='times 24')
search.pack()
songname=song.get()+'.mp3' """

class dummypygame:#class object to be used in place of pygame if not available    
        def play(self): pass
        class mixer:#class object to be used in place of pygame.mixer if not available
                True
                def get_init():
                    True
                """class Sound(file):#class object to be used in place of pygame.mixer.Sound if not available"""
                    class play: 
        class quit: pass
        def load_sound(file):
                print ('Warning, no sound')
                pygame.mixer = None
        class init: pass#class object to be used in place of pygame if not available
        class error: False

import pygame
pygame.init()
nam=Tkinter.StringVar()
name=''
sound=''
pause=Tkinter.BooleanVar()
pause.set(False)

def u78(event=None):
    
    global name
    name= "000005.mp3"
    if name!='':
        load_sound(name)
        nam.set(name)
        pause.set(False)
    if pygame.mixer and not pygame.mixer.get_init():
        print ('Warning, no sound')
        pygame.mixer = None
        
def helpe(event=None):
    tkMessageBox.showinfo('Help')

def About():
    tkMessageBox.showinfo('About','This is Music player 1.3')

def Record():
        banglakey.record=Tkinter.Toplevel()
        banglakey.record.title("Record Sound")
        banglakey.record.transient(banglakey)
        record=Tkinter.BooleanVar()

        rec = Recorder(channels=2)
        f = asksaveasfilename(defaultextension=".wav",filetypes=[("sound files", ".wav")])
        recfile2 = rec.open1(f, 'wb')
                
        def start(event=None):
                    
                    p61.start()
                    recfile2.start_recording()
                

        def stop(event=None):
                
                recfile2.stop_recording()
                recfile2.close()
                p61.stop()
                banglakey.record.destroy()

        b61=Tkinter.Button(banglakey.record, text =u'Start', command = start,relief="groove",bg="#0060FF",fg="white",font=("arial",16))
        b62=Tkinter.Button(banglakey.record, text =u'Stop', command = stop,relief="groove",bg="#0060FF",fg="white",font=("arial",16))
        p61=ttk.Progressbar(banglakey.record,orient='horizontal',mode='indeterminate',length=200)
        b61.pack(side=Tkinter.TOP)
        b62.pack(side=Tkinter.TOP)
        p61.pack(side=Tkinter.TOP)
        banglakey.record.mainloop()

menu = Tkinter.Menu(banglakey)
banglakey.config(menu=menu)
filemenu = Tkinter.Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Open...", command=u78)
filemenu.add_command(label="Record...", command=Record)
filemenu.add_separator()
filemenu.add_command(label="Exit",activebackground='red', command=banglakey.destroy)

helpmenu = Tkinter.Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)
helpmenu.add_command(label="Help file",activebackground='purple', command=helpe)

class dummysound:#class object to be used in place of pygame.mixer.Sound if not available
        def play(self): pass
        def mixer(self): pass

def load_sound(name):
        if not pygame.mixer: return dummysound()
        try:
            name = os.path.join(name)
            print (name)
            pygame.mixer.music.load(name)
        except pygame.error:
            print ('Warning, unable to load, %s' % name)
            return dummysound()

         
b51=Tkinter.Button(banglakey, text =u'OPEN', command = u78,relief="groove",bg="#0060FF",fg="white",font=("arial",16))


l12=Tkinter.Label(banglakey, textvariable= nam ,font=("times new roman",11),relief="flat",borderwidth=1,bg="#109070",fg="white")


p51=ttk.Progressbar(orient='horizontal',mode='indeterminate',length=200)

def update_timeText():
        if not pygame.mixer.music.get_busy():
                    p51.stop()
                    b54.config(state='disabled')
        
        banglakey.after(1000, update_timeText)
        
def u77(event=None):
    #load the sound effects
    if pygame.mixer:
            pygame.mixer.init()
            b54.config(state='normal')
            p51.start()
            if pause.get()==False:
                    pygame.mixer.music.play(1)
                    update_timeText()
                    
            elif pause.get()==True:
                    pygame.mixer.music.unpause()
                    p51.start()
                    
            
        
b52=Tkinter.Button(banglakey, text =u'PLAY', command = u77,relief="groove",bg="#0060FF",fg="white",font=("arial",16))


def u76(event=None):
       pygame.mixer.music.stop()
       p51.stop()
       pause.set(False)
       
b53=Tkinter.Button(banglakey, text =u'STOP', command = u76,relief="groove",bg="#0060FF",fg="white",font=("arial",16))

def u78(event=None):
        pygame.mixer.music.pause()
        pause.set(True)
        p51.stop()
        b54.config(state='disabled')
b54=Tkinter.Button(banglakey, text =u'PAUSE',state='disabled', command = u78,relief="groove",bg="#0060FF",fg="white",font=("arial",16))


b51.pack(side=Tkinter.TOP)
b52.pack(side=Tkinter.TOP)
b54.pack(side=Tkinter.TOP)
b53.pack(side=Tkinter.TOP)
p51.pack(side=Tkinter.TOP)
l12.pack(side=Tkinter.TOP)

banglakey.mainloop()
pygame.quit()
