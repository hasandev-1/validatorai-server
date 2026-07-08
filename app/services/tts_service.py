from google import genai 
import wave 
import io 
import base64


client = genai.Client()

# https://ai.google.dev/gemini-api/docs/speech-generation 
def generate_tts(text:str,voice:str) -> bytes:
    interaction = client.interactions.create(
        model="gemini-3.1-flash-tts-preview",
        input=text,
        response_format={"type":"audio"},
        generation_config={
            "speech_config": [
                {"voice":voice}
            ]
        }
    )
    pcm_audio_data = base64.b64decode(interaction.output_audio.data) # raw pcm bytes 
    wav_io = io.BytesIO() # wav raw byte
    with wave.open(wav_io,"wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(24000)
        wf.writeframes(pcm_audio_data)
    return wav_io.getvalue()