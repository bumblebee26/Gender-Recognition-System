import pandas as pd
import os
from pitch import get_pitch
#from frequencies import get_frequencies,get_features
from mfcc import get_mfcc
import librosa
import  scipy.io.wavfile as wav

path_male = "C:\\Users\\Atulya\\Documents\\GitHub\\gender-classifier-using-voice\\Data Preprocessing\\Male\\";
path_female = "C:\\Users\\Atulya\\Documents\\GitHub\\gender-classifier-using-voice\\Data Preprocessing\\Female\\";
freq_col=['pitch']
mfcc_col=['mfcc'+str(i+1) for i in list(range(110))]
col = freq_col+mfcc_col+['label']

def main(path,gender):
    df = pd.DataFrame()
    print('Extracting features for '+gender)
   
    directory=os.listdir(path)
    for wav_file in directory:
        write_features=[]
        y, sr = librosa.load(path+wav_file)
        fs,x = wav.read(path+wav_file)
        print(wav_file)
        
        pitch=get_pitch(fs,x)
        #frequencies=get_frequencies(y,sr)
        #freq_features=get_features(frequencies)
        mfcc_features=get_mfcc(y,sr)
        
        #write_features=[pitch]+freq_features+mfcc_features.tolist()[0]+[gender]
        write_features=[pitch]+mfcc_features.tolist()[0]+[gender]
        df = df.append([write_features])
        #if wav_file=='00001.wav':
            #break #remove break to execute for all files
    df.columns = col
    df.to_csv(gender+'_features.csv')

main(path_male,'male')
main(path_female,'female')

maledf=pd.read_csv('male_features.csv')
maledf=maledf.iloc[:, 1:] #removing extra row index

femaledf=pd.read_csv('female_features.csv')
femaledf=femaledf.iloc[:, 1:] #removing extra row index

finaldf=maledf.append(femaledf)
finaldf.to_csv('features.csv')
