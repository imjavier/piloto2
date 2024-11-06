from urllib import response
from spleeter.separator import Separator
from io import BytesIO
import os
import tempfile
from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.responses import StreamingResponse
from pathlib import Path
import tensorflow as tf
import multiprocessing
import os
from fastapi.middleware.cors import CORSMiddleware

def start_basic_configuration():
    multiprocessing.freeze_support()
    os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
    os.environ['TF_ENABLE_MLIR'] = '1'
    tf.compat.v1.ConfigProto()
    tf.compat.v1.RunOptions(report_tensor_allocations_upon_oom=True)

def start_spleeter():
    return Separator('spleeter:2stems')
    
parent_directory = Path(__file__).resolve().parent.parent
UPLOAD_FOLDER = parent_directory / 'audios'
UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas las fuentes, o especificar dominios
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos los encabezados
)
@app.post("/upload/")
async def upload_file(cancion: UploadFile = File(...), modelo: str = Form(...)):
    
    song_buffer = BytesIO(await cancion.read())
    print("SE LLEGA HASTA AQUí SIN PROBLEMA")
    separator = start_spleeter()
    with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as temp_audio:
        temp_audio.write(song_buffer.getvalue())
        temp_audio.flush()
        temp_audio_path = temp_audio.name
    try:

        separator.separate_to_file(temp_audio_path, UPLOAD_FOLDER)
    except:
        raise HTTPException(status_code=400, detail="El parámetro debe ser un número positivo.")
    print('DESPUES DE LA TRANSFORMACIÓN LLEGA SIN PROBLEMA')
    filename = os.path.basename(temp_audio_path)
    file_base_name = filename.split(".")[0] 
    vocals_path = UPLOAD_FOLDER / file_base_name / 'vocals.wav'
    accompaniment_path = UPLOAD_FOLDER / file_base_name / 'accompaniment.wav'

    print("SE LLEGA HASTA AQUí SIN PROBLEMA")
    if modelo == 'model_music':
        return StreamingResponse(
            open(accompaniment_path, "rb"), 
            media_type="audio/wav", 
            headers={
                "Content-Disposition": f"attachment; filename={accompaniment_path.name}"
            }
        )
    
    return StreamingResponse(
        open(vocals_path, "rb"), 
        media_type="audio/wav",
        headers={
            "Content-Disposition": f"attachment; filename={vocals_path.name}"
        }
    )
