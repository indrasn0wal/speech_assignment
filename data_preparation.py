import os
import shutil

# --- Configuration ---
WAV_DIR = "wav"
TRANSCRIPT_DIR = "transcripts"
OUTPUT_DIR = "mfa_corpus"
# ---------------------

# Create the target directory structure
target_speaker_dir = os.path.join(OUTPUT_DIR)
os.makedirs(target_speaker_dir, exist_ok=True)

print(f"Setting up corpus in: {target_speaker_dir}")

# 1. Copy all .wav files
for wav_file in os.listdir(WAV_DIR):
    if wav_file.lower().endswith(".wav"):
        source_path = os.path.join(WAV_DIR, wav_file)
        target_path = os.path.join(target_speaker_dir, wav_file)
        shutil.copy(source_path, target_path)

# 2. Copy transcript files and normalize to .txt extension
for transcript_file in os.listdir(TRANSCRIPT_DIR):
    if transcript_file.lower().endswith(".txt"):
        base_name = os.path.splitext(transcript_file)[0]
        source_path = os.path.join(TRANSCRIPT_DIR, transcript_file)
        target_path = os.path.join(target_speaker_dir, f"{base_name}.txt")
        shutil.copy(source_path, target_path)

print("Data preparation complete.")
print(f"Total files in target: {len(os.listdir(target_speaker_dir))}")