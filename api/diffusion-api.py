"""
Use GPU/CPU with pretrained model to generate images from text prompts
"""

# fastapi
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware

# torch & diffusers
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline

# image processing
from io import BytesIO
import base64 

# dotenv
import os
from dotenv import load_dotenv
load_dotenv()

# check if GPU is available
if not torch.cuda.is_available():
    raise RuntimeError("No cuda GPU available")

# get auth token
auth_token = os.getenv("AUTH_TOKEN")
device = 'cuda'

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["POST", "GET"],
    allow_headers=["*"]
)

model_id = "CompVis/stable-diffusion-v1-4" # https://huggingface.co/CompVis/stable-diffusion-v1-4

# use pretrained model
pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    revision="fp16", # pick fp16 for GPU to use less memory
    torch_dtype=torch.float16,
    use_auth_token=auth_token,
)

# move model to GPU
pipe.to(device)

@app.get("/")
def generate(prompt: str):
    try:
        with autocast(device):
            image = pipe(prompt, guidance_scale=8.5).images[0] # generate image

        image.save("generated.png")
        buffer = BytesIO()
        image.save(buffer, format="PNG")
        imgstr = base64.b64encode(buffer.getvalue())

        return Response(content=imgstr, media_type="image/png", status_code=200)
    except:
        return Response(content="Error", media_type="text/plain", status_code=500)