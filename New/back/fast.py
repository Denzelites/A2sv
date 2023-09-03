# main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import requests
import config
import base64

app = FastAPI()

# Define the data model for the request (the prompt)
class TextPrompt(BaseModel):
    prompt: str

@app.post("/generate-image/")
async def generate_image(prompt: TextPrompt):
    api_host = os.getenv('API_HOST', 'https://api.stability.ai')
    api_key = config.api_key
    engine_id = "stable-diffusion-xl-beta-v2-2-2"

    try:
        response = requests.post(
            f"{api_host}/v1/generation/{engine_id}/text-to-image",
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json",
                "Authorization": f"Bearer {api_key}"
            },
            json={
                "text_prompts": [
                    {
                        "text": prompt.prompt
                    }
                ],
                "cfg_scale": 7,
                "height": 512,
                "width": 512,
                "samples": 1,
                "steps": 30,
            },
        )

        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Image generationsdadasda failed")

        data = response.json()
        image_data = data["artifacts"][0]["base64"]

        return {"image_data": image_data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
