
"""
Created on Sat Mar  2 14:03:46 2019

@author: Akshay
aim: everything before kmeans

"""
#1st part
#imports and similar stuff
from __future__ import print_function
import csv
import numpy as np
import librosa
from os import listdir




#2nd part
#aim: to extract features of songs
def features(y,sr):
    print("inside features")
    tonnetz = np.mean(librosa.feature.tonnetz(y=y, sr=sr))
    print("tonnetz: ", tonnetz)
    print("_______________________________________________")
    
    mfccs = np.mean(librosa.feature.mfcc(y=y, sr=sr))
    print("mfcc: ",mfccs)
    print("________________________________________________")
    
    chroma = np.mean(librosa.feature.chroma_stft(y=y, sr=sr))
    print("chroma: ",chroma)
    print("________________________________________________")
    
    mel = np.mean(librosa.feature.melspectrogram(y=y, sr=sr))
    print("mel: ",mel)
    print("________________________________________________")
    
    contrast = np.mean(librosa.feature.spectral_contrast(y=y,sr=sr))
    print("contrast: ",contrast)
    print("_________________________________________________")
    
    print("done with part 2")
    return [tonnetz,mfccs,chroma,mel,contrast]




#3rd part
#initialize file to write data into
#some csv stuff
def init_file():
    header = 'filename tonnetz mfcc chroma mel contrast'
    header = header.split()
    file = open('data.csv', 'w', newline='')
    with file:
        writer = csv.writer(file)
        writer.writerow(header)



#4th part
#writing data into file
def write(songname,tonnetz,mfccs,chroma,mel,contrast):
    print("inside write")
    to_append = f'{songname} {tonnetz} {mfccs} {chroma} {mel} {contrast} '
    file = open('data.csv', 'a', newline='')
    with file:
        writer = csv.writer(file)
        writer.writerow(to_append.split())
        



#5th part
#process all songs
#extract their features (fun call)
#write features to file (fun call)
def process_songs():
    directory="C:/Users/Akshay/Desktop/dataset"
    for songs in listdir(directory):
       x="/";
       path=directory+x+songs
       print(path);
       y, sr = librosa.load(path)
       if(y.size==0):
           continue;
       y = librosa.effects.harmonic(y)
       tonnetz,mfccs,chroma,mel,contrast = features(y,sr)
       write(songs,tonnetz,mfccs,chroma,mel,contrast)
    print("1st dir done");
    
    directory="E:/Songs/mySongs"
    for songs in listdir(directory):
       x="/";
       path=directory+x+songs
       print(path);
       y, sr = librosa.load(path)
       if(y.size==0):
           continue;
       y = librosa.effects.harmonic(y)
       tonnetz,mfccs,chroma,mel,contrast = features(y,sr)
       write(songs,tonnetz,mfccs,chroma,mel,contrast)
    print("2nd dir done");
    
    directory="E:/Songs/MakesYouHappy"
    for songs in listdir(directory):
       x="/";
       path=directory+x+songs
       print(path);
       y, sr = librosa.load(path)
       if(y.size==0):
           continue;
       y = librosa.effects.harmonic(y)
       tonnetz,mfccs,chroma,mel,contrast = features(y,sr)
       write(songs,tonnetz,mfccs,chroma,mel,contrast)
    print("3rd dir done"); 
       



#6th part
#start of the program
#TODO: see if you can optimimze funcion calls
def main():
    init_file()
    process_songs()




   
main()



#print(tonnetz)



 