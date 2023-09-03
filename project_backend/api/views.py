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

pre_prompt="Provide a summarized and detailed description of characters or events featured in african literature text in not more than 25 words. "
def return_output(prompt_input):
    output = replicate.run(
        "replicate/llama-2-70b-chat:2796ee9483c3fd7aa2e171d38f4ca12251a30609463dcfd4cd76703f22e96cdf",
         input={"prompt": f"{pre_prompt} {prompt_input} Assistant: ", # Prompts
                "temperature":0.1, "top_p":0.9, "max_length":128, "repetition_penalty":1})  # Model parameters
    full_response = ""
    for item in output:
        full_response += item
    return full_response

@api_view(["POST"])
def generate(request):
    api_host = os.getenv('API_HOST', 'https://api.stability.ai')
    api_key = config.api_key
    engine_id = "stable-diffusion-xl-beta-v2-2-2"

    data = request.data
    prompt = return_output(data['prompt'])
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
