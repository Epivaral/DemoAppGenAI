# DALL-E 3 requires version 1.0.0 or later of the openai-python library.
import os
import requests
from openai import AzureOpenAI
import json

# You will need to set these environment variables or edit the following values.
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT", "<your_azure_openai_endpoint_here>")  # Replace with your Azure OpenAI endpoint
api_version = os.getenv("OPENAI_API_VERSION", "2024-04-01-preview")
deployment = os.getenv("DEPLOYMENT_NAME", "dall-e-3")
api_key = "<your_api_key_here>"  # Replace with your actual API key

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=api_key,
)

# Fetch all books from the API
books_api = "https://lemon-pebble-088965b1e.1.azurestaticapps.net/data-api/api/Books"
response = requests.get(books_api)
response.raise_for_status()
books = response.json()
if isinstance(books, dict) and "value" in books:
    books = books["value"]

# Ensure images directory exists
os.makedirs("images", exist_ok=True)

for book in books:
    title = book.get("Title", "")
    author = book.get("Author", "")
    genre = book.get("Genre", "")
    description = book.get("Description", "")
    prompt = f"Please generate the front book cover for this book, it will be used for an online bookstore, so the book title and book author must be clearly visible, Please do not made up the book title and name, use the exact ones provided here.\nUse the description as a guide for the image.\n\nTitle: {title}\nAuthor: {author}\nGenre: {genre}\nDescription: {description}."
    try:
        result = client.images.generate(
            model=deployment,
            prompt=prompt,
            n=1,
            style="vivid",
            quality="standard",
        )
        image_url = json.loads(result.model_dump_json())["data"][0]["url"]
        # Download the image
        img_data = requests.get(image_url).content
        # Save image to images folder
        safe_title = "_".join(title.split())
        filename = f"images/{safe_title}.png"
        with open(filename, "wb") as f:
            f.write(img_data)
        print(f"Saved: {filename}")
    except Exception as e:
        print(f"Skipping '{title}' due to error: {e}")