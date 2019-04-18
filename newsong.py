# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 21:45:59 2019

@author: chaitu
"""

from __future__ import print_function
import librosa
import math
import IPython.display as ipd
import pandas as pd
import numpy as np

file='C:/Users/admin/Desktop/songs/'

nameOfSong="000005.mp3"            
audio_path = file+nameOfSong
x , sr = librosa.load(audio_path)
ipd.Audio(audio_path)
hashmap={}

def distance(p1,p2,p3,p4,p5,a1,a2,a3,a4,a5):
	return math.sqrt(
                (p1-a1)**2+(p2-a2)**2+(p3-a3)**2+(p4-a4)**2+(p5-a5)**2
                )

def nextSongRecommendationModule(newSong):
    csv_file_name="cluster"+hashmap[newSong]+".csv"
    df = pd.read_csv(csv_file_name)
    songs=df.filename;
    #will fail for cluster11.csv BEWARE
    clusterId=csv_file_name[7]
    for songName in songs:
        #s.add( ("songName",clusterId) )
        hashmap[songName]=clusterId
    #if s.contains(newSong):
    y, sr = librosa.load(newSong)
    [a,b,c,d,e]=features(y,sr)
    if newSong in hashmap:
        clusterId= hashmap[newSong]
        df = pd.read_csv("cluster"+clusterId+".csv")
        name=df.filename
        f1 = df.tonnetz
        f2 =df.mfcc
        f3=df.chroma
        f4 =df.mel
        f5 =df.contrast
        minimum=1000000000;
        nearestSong="new song";
        for (songname,v1,v2,v3,v4,v5) in zip(name,f1,f2,f3,f4,f5):
            dist=distance(a,b,c,d,e,v1,v2,v3,v4,v5)
            if(dist<minimum):
                minimum = dist
                nearestSong=songname
        print("the next song is"+nearestSong)
    audio_path1 = file+nearestSong
    x , sr = librosa.load(audio_path1)
    ipd.Audio(audio_path1)
            
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



#fetch data from column names of 6 csv files
for i in range(1,7):
    csv_file_name="cluster"+str(i)+".csv"
    df = pd.read_csv(csv_file_name)
    songs=df.filename;
    #will fail for cluster11.csv BEWARE
    clusterId=csv_file_name[7]
    for songName in songs:
        #s.add( ("songName",clusterId) )
        hashmap[songName]=clusterId  


nextSongRecommendationModule(nameOfSong)

