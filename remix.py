from pydub import AudioSegment

print("loading the massive audio file...")

# Load the mp3 file
radio_show = AudioSegment.from_mp3("reggae_radio.mp3")

print("file loaded, extracting sample...")

# slice out 4 second sample
start_time = 554000
end_time = start_time + 4000
sample = radio_show[start_time:end_time]

# Export the sample to a new wav file to avoid compression
sample.export("cool_down_pace_sample.wav", format="wav")

print("success, 'cool_down_pace_sample.wav' created")
