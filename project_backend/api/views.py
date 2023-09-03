from django.shortcuts import render

from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from pydantic import BaseModel
import os
from . import config
import requests
# Create your views here.
# Define the data model for the request (the prompt)
class TextPrompt(BaseModel):
    prompt: str

@api_view(["POST"])
def generate(request):
    api_host = os.getenv('API_HOST', 'https://api.stability.ai')
    api_key = config.api_key
    engine_id = "stable-diffusion-xl-beta-v2-2-2"

    data = request.data
    prompt = data['prompt']
    print(prompt)
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
                        "text": prompt #prompt.prompt
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
            return Response({'status_code':500, 'detail':"Image generation failed"})
        data = response.json()
        image_data = data["artifacts"][0]["base64"]

        return Response({"status":200, "image_data": image_data})
    except Exception as e:
        print(e)
        return Response({'status_code':500, 'detail':'got an error'})
