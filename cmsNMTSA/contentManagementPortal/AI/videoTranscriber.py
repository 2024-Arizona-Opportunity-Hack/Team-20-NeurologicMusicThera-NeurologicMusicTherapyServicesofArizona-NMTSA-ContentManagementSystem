import ffmpeg
import librosa
import numpy as np
from io import BytesIO
from transformers import pipeline
from django.core.files.uploadedfile import InMemoryUploadedFile
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
whisper_asr = pipeline(task="automatic-speech-recognition", model="openai/whisper-base", device=0 if torch.cuda.is_available() else -1)

def video_to_audio_chunks(uploaded_file, chunk_duration=300):

    try:
        out, _ = (
            ffmpeg
            .input("pipe:0")
            .output("pipe:", format="wav", acodec="pcm_s16le", ac=1, ar="16k")
            .run(input=uploaded_file.read(), capture_stdout=True, capture_stderr=True)
        )

        audio_data = BytesIO(out)
        full_audio, sr = librosa.load(audio_data, sr=16000, mono=True)

        total_duration = len(full_audio) / sr
        for start_time in range(0, int(total_duration), chunk_duration):
            end_time = min(start_time + chunk_duration, int(total_duration))
            yield full_audio[int(start_time * sr):int(end_time * sr)]

    except Exception as e:
        raise ValueError(f"Failed to process video: {e}")

def get_transcripts(uploaded_file):

    if not isinstance(uploaded_file, InMemoryUploadedFile):
        raise ValueError("Invalid file type: must be an uploaded file")

    transcription_result = []

    for chunk in video_to_audio_chunks(uploaded_file):
        transcription = whisper_asr(chunk)
        transcription_result.append(transcription['text'])

    return " ".join(transcription_result)
