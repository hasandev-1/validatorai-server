from fastapi import APIRouter,HTTPException,status
from fastapi.responses import Response
from app.schemas.tts import TTSRequest
from app.services.tts_service import generate_tts 


tts_router = APIRouter(prefix="/tts",tags=["Text-To-Speech"]) 


@tts_router.post("/generate")
def generate_audio(request:TTSRequest):
    try:
        audio_bytes = generate_tts(request.text,request.voice)
        return Response(content=audio_bytes,media_type="audio/wav")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=f"Failed to generate audio: {str(e)}") 