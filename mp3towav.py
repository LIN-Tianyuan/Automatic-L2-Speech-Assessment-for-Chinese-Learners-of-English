import os
import ffmpeg

INPUT_DIR = "ICNALE_SM_CHN_N600/"  # mp3
OUTPUT_DIR = "ICNALE_WAV"  # wav
os.makedirs(OUTPUT_DIR, exist_ok=True)

for file in os.listdir(INPUT_DIR):
    if file.endswith(".mp3"):
        input_path = os.path.join(INPUT_DIR, file)
        output_path = os.path.join(OUTPUT_DIR, file.replace(".mp3", ".wav"))

        # change
        (
            ffmpeg
            .input(input_path)
            .output(output_path, format="wav", acodec="pcm_s16le", ar="16000")  # 16kHz, PCM 16-bit
            .run(overwrite_output=True)
        )
        print(f"Converted: {file} -> {output_path}")

print("All MP3 files have been successfully converted to WAV format!")