from pydub import AudioSegment

# 1. Load the wav sample
sample = AudioSegment.from_wav("samples/cool_down_pace_sample.wav")

# 2. Define the start and end times (in milliseconds)
# E.g., isolating the section between the hits at 400ms and 1150ms
start_ms = 2600
end_ms = 5900

# 3. Slice the audio
isolated_section = sample[start_ms:end_ms]

# 4. Loop the isolated section 4 times
looped_section = isolated_section * 4

# 5. Export the looped segment
looped_section.export("samples/isolated_section_looped.wav", format="wav")
print("Looped section exported successfully to 'samples/isolated_section_looped.wav'!")
