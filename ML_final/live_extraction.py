import pandas as pd
import os
from pitch import get_pitch
from mfcc import get_mfcc
import librosa
import  scipy.io.wavfile as wav


def extract_features(path):
    df = pd.DataFrame()
    print('Extracting features')
   
    freq_col=['pitch']
    mfcc_col=['mfcc'+str(i+1) for i in list(range(110))]
    col = freq_col+mfcc_col

    
    directory=os.listdir(path+"recorded_audio\\")
    print(directory)
    for wav_file in directory:
        write_features=[]
        y, sr = librosa.load(path+"recorded_audio\\"+wav_file)
        fs,x = wav.read(path+"recorded_audio\\"+wav_file)
        
        pitch=get_pitch(fs,x)
        mfcc_features=get_mfcc(y,sr)
        
        write_features=[pitch]+mfcc_features.tolist()[0]
        df = df.append([write_features])
    df.columns = col
    df.to_csv('recorded_audio_features.csv')