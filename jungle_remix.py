from pydub import AudioSegment

# 1. Load your clean sample
sample = AudioSegment.from_wav("samples/cool_down_pace_sample.wav")

# 2. Slice out 4 distinct beats based on detect.py
beat1 = sample[0:400]  # From 0ms to the first hit
beat2 = sample[400:800]  # From 400ms to the second hit
beat3 = sample[800:1150]  # From 800ms to the third hit
beat4 = sample[1150:1450]  # From 1150ms to the fourth hit

final_loop = beat1 + beat2 + beat3 + (beat4.reverse() * 2)

# export
final_loop.export("samples/jungle_chop.wav", format="wav")
