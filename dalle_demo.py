import openai
import requests
from PIL import Image
from io import BytesIO
import os

# Initialize OpenAI API with your API key

def generate_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    return response['data'][0]['url']

def display_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show()

def save_image(url, filename):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
    img.save(os.path.join(downloads_path, filename))

# Prompts to generate images
prompts = [
    "a futuristic folkart painting",
    "a cute cat wearing a spacesuit",
    "an ancient castle on the edge of a mountain",
    "a robot painting a picture in a modern art gallery",
    "a blue elephant eating goose berries over mars planet"
]

# Generate and display images
for i, prompt in enumerate(prompts):
    print(f"Generating image for prompt: '{prompt}'")
    image_url = generate_image(prompt)
    display_image(image_url)
    save_image(image_url, f"generated_image_{i+1}.png")
    print(f"Image saved as 'generated_image_{i+1}.png' in Downloads folder.")
