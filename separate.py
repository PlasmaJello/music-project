import os
import shutil
import subprocess
import sys

def main():
    input_file = "samples/isolated_section.wav"
    output_dir = "samples/separated"
    
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        sys.exit(1)
        
    print(f"Splitting '{input_file}' using Demucs...")
    print("This might take a minute depending on your hardware...")
    
    # 1. Run demucs using the current Python interpreter
    cmd = [
        sys.executable, "-m", "demucs.separate",
        "-o", output_dir,
        input_file
    ]
    
    result = subprocess.run(cmd)
    
    if result.returncode != 0:
        print("Error: Demucs separation failed.")
        sys.exit(1)
        
    # Demucs places files inside: {output_dir}/{model_name}/{input_filename_without_ext}/
    model_name = "htdemucs"
    track_name = "isolated_section"
    separated_path = os.path.join(output_dir, model_name, track_name)
    
    # Target file paths
    drums_src = os.path.join(separated_path, "drums.wav")
    bass_src = os.path.join(separated_path, "bass.wav")
    
    drums_dest = "samples/isolated_drums.wav"
    bass_dest = "samples/isolated_bass.wav"
    
    # 2. Move and rename the drums and bass files
    if os.path.exists(drums_src):
        shutil.move(drums_src, drums_dest)
        print(f"✅ Drums component saved to: {drums_dest}")
    else:
        print("Warning: Drums stem not found.")
        
    if os.path.exists(bass_src):
        shutil.move(bass_src, bass_dest)
        print(f"✅ Bass component saved to: {bass_dest}")
    else:
        print("Warning: Bass stem not found.")
        
    # 3. Clean up the rest of the separated folder to keep things tidy
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
        print("🧹 Cleaned up temporary Demucs directories.")

if __name__ == "__main__":
    main()
