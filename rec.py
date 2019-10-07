import pyaudio
import numpy
import wave

WAVE_OUTPUT_FILENAME = "sample.wav"
iDeviceIndex = 2

def MakeWavFile(FileName = "sample.wav", Record_Seconds = 2):
  chunk = 1024
  FORMAT = pyaudio.paInt16

  CHANNELS = 1
  RATE = 44100

  p = pyaudio.PyAudio()

  stream = p.open(format = FORMAT, channels = CHANNELS, rate = RATE, input = True, frames_per_buffer = chunk)

  print("Now Recording...")
  all = []
  for i in range(0, int(RATE / chunk * Record_Seconds)):
    data = stream.read(chunk)
    all.append(data)
  
  print("Finished Recording.")
  
  stream.close()
  p.terminate()
  wavFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
  wavFile.setnchannels(CHANNELS)
  wavFile.setsampwidth(p.get_sample_size(FORMAT))
  wavFile.setframerate(RATE)
  wavFile.writeframes(b''.join(all))
  
  wavFile.close()

if __name__ == '__main__':
  MakeWavFile("sample.wav", Record_Seconds = 2) 
