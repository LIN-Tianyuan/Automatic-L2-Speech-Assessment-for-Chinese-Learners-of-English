import whisper
import os
import pandas as pd

AUDIO_DIR = "ICNALE_WAV/"
OUTPUT_DIR = "whisper_transcriptions/"
os.makedirs(OUTPUT_DIR, exist_ok=True)

model = whisper.load_model("medium")

results = []

for file in os.listdir(AUDIO_DIR):
    if file.endswith(".wav"):
        audio_path = os.path.join(AUDIO_DIR, file)
        print(f"Processing: {file}")

        result = model.transcribe(audio_path)
        text = result["text"]

        output_txt = os.path.join(OUTPUT_DIR, file.replace(".wav", ".txt"))
        with open(output_txt, "w") as f:
            f.write(text)

        results.append({"file": file, "transcription": text})

df = pd.DataFrame(results)
df.to_csv(os.path.join(OUTPUT_DIR, "whisper_results.csv"), index=False)
print("All transcriptions saved!")



