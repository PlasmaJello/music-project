from pydub import AudioSegment

# 1. Load your 6-second padded sample
sample = AudioSegment.from_wav("cool_down_pace_sample.wav")

# 2. Define what "loud" means.
# Pydub measures volume in dBFS (decibels relative to full scale).
# 0 is the loudest possible digital sound. Silence is around -100.
LOUDNESS_THRESHOLD = -15.0

# this is our filter window (ignore everything for 300ms after a spike)
COOLDOWN_MS = 300
last_detected_time = -COOLDOWN_MS  # start negative so the first spike can be detected

print("Filtering transients into clean chops...")
print("-------------------------------------------------------")

# 3. Loop through the audio in 50ms steps (chunks)
chunk_size = 50

for i in range(0, len(sample), chunk_size):
    chunk = sample[i : i + chunk_size]

    # Check the loudness of this specific chunk
    if chunk.dBFS > LOUDNESS_THRESHOLD:
        # Check if enough time has passed since the last detected spike
        if i - last_detected_time >= COOLDOWN_MS:
            print(f"🎵 Clean Hit Found at: {i} ms")
            last_detected_time = i
