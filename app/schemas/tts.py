from pydantic import BaseModel 


class TTSRequest(BaseModel):

    text:str 
    voice:str="Kore" #(kore is default voice)