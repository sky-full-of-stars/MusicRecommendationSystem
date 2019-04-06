# -*- coding: utf-8 -*-
"""
Author: Akshay
Date: 14th oct 2018
Time: 5:00am
Obj: to try to get features for inbuilt song dataset
source :
"""

from __future__ import print_function
import librosa
import numpy as np

# 1. Get the file path to the included audio example
filename = librosa.util.example_audio_file()
print(filename)
# 2. Load the audio as a waveform `y`
#    Store the sampling rate as `sr`
y, sr = librosa.load(filename)
y = librosa.effects.harmonic(y)

import soundfile as sf
"""
X, sample_rate = sf.read(filename, dtype='float32')
if X.ndim > 1:
        X = X[:,0]
        X = X.T
        
"""

tonnetz = np.mean(librosa.feature.tonnetz(y=y, sr=sr))
print("tonnetz: ", tonnetz)
print("______________________________________________________")



mfccs = np.mean(librosa.feature.mfcc(y=y, sr=sr))
print("mfcc: ",mfccs)
print("______________________________________________________")



#stft = np.abs(librosa.stft(X))
chroma = np.mean(librosa.feature.chroma_stft(y=y, sr=sr))
print("chroma: ",chroma)
print("______________________________________________________")



mel = np.mean(librosa.feature.melspectrogram(y=y, sr=sr))
print("mel: ",mel)
print("______________________________________________________")



contrast = np.mean(librosa.feature.spectral_contrast(y=y,sr=sr))
print("contrast: ",contrast)
print("______________________________________________________")

