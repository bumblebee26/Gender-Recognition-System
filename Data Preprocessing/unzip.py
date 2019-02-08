import os
import tarfile

source = 'C:\\Users\\Atulya\\Documents\\GitHub\\gender-classifier-using-voice\\Data Preprocessing\\raw_zipped\\'
destination = 'C:\\Users\\Atulya\\Documents\\GitHub\\gender-classifier-using-voice\\Data Preprocessing\\raw\\'

for f in os.listdir(source):
    if f.endswith('.tgz'):
        tar = tarfile.open(os.path.join(source, f))
        tar.extractall(destination)
        tar.close()