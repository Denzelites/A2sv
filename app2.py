import os
import requests
import config
import base64

api_host = os.getenv('API_HOST', 'https://api.stability.ai')
api_key = config.api_key
engine_id="stable-diffusion-xl-beta-v2-2-2"


# Do something with the payload...

def get_model():
    url = f"{api_host}/v1/engines/list"
    response = requests.get(url, headers={
    "Authorization": f"Bearer {api_key}"})
    
    if response.status_code != 200:
        raise Exception("Non-200 response: " + str(response.text))
    payload = response.json()


def generate_image(prompt):
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
                "text": f"{prompt}"
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
        raise Exception("Non-200 response: " + str(response.text))
    else:
        data = response.json()

        for i, image in enumerate(data["artifacts"]):
            with open(f"v1_txt2img_{i}.png", "wb") as f:
                f.write(base64.b64decode(image["base64"]))

generate_image([input("Input a prompt:")]) 