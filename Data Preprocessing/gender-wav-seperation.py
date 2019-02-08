import os
import time
import shutil
import random

#Note : Male and Female should already be created at path x

x='C:/Users/Atulya/Documents/GitHub/gender-classifier-using-voice/Data Preprocessing'
address=x+'/raw'
j=0
print(len(os.listdir(address)))
data=os.listdir(address)

for file in data:
    try:
        print('counter=',j)
        print(file)

        if file=='.DS_Store':
            continue
        i=address+'/'+str(file)
        os.chdir(i+'/etc')
        fhand=open('README')
        for line in fhand:
            if line.startswith('Gender:'):
                if line[8:].strip()=='Male' or line[8:].strip()=='male':
                    j=j+1
                    print(line[8:].strip())
                    os.chdir(i+'/wav')
                    for audio in os.listdir(i+'/wav'):
                        u=str(time.time()+random.random()).replace('.','')+'.wav'
                        os.rename(audio,u)
                        shutil.copy(u,x+'/Male')
                elif line[8:].strip()=='Female' or line[8:].strip()=='female':
                    j=j+1
                    print(line[8:].strip())
                    os.chdir(i+'/wav')
                    for audio in os.listdir(i+'/wav'):
                        u=str(time.time()+random.random()).replace('.','')+'.wav'
                        os.rename(audio,u)
                        shutil.copy(u,x+'/Female')
    except:
        pass
