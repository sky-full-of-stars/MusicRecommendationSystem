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
import os

file='C:/Users/admin/Desktop/dataset/'

def distance(p1,p2,p3,p4,p5,a1,a2,a3,a4,a5):
	return math.sqrt(
                (p1-a1)**2+(p2-a2)**2+(p3-a3)**2+(p4-a4)**2+(p5-a5)**2
                )

def nextSongRecommendationModule(current_song,hashmap):
    newSong=current_song
    newSong=os.path.basename(newSong)
    y, sr = librosa.load('C:/Users/admin/Desktop/dataset/'+newSong)
    [a,b,c,d,e]=features(y,sr)
    clusterId= hashmap[newSong]
    print("the path is yoooooo"+newSong)
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
    current_song='C:/Users/admin/Desktop/dataset/'+nearestSong
    return current_song
            
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

