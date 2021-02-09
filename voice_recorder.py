import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import time
import winsound
# Sampling frequency 
sampling = 16000

# Recording duration 
duration = 1

i=1
print('Hiya! Recording will be starting in 3 seconds')
for j in range(0,3):
    print('recording in', + j, 'seconds')
    time.sleep(1)
freq=16000
dur=100
for i in range(0,10):
    print("Speak up")
    winsound.Beep(freq,dur)
    time.sleep(1)
    record = sd.rec(int(duration * sampling), 
				samplerate=sampling, channels=2) 
    sd.wait() 
    wv.write("recording{}.wav".format(i), record, sampling, sampwidth=2)




