import base64
from openai import OpenAI
import os
from dotenv import load_dotenv


def generate_nail_image(description: str, feelings: str = "", n: int = 1) -> list[str]:
    """Generate one or more nail design images using the OpenAI Responses API.

    Parameters
    ----------
    description : str
        Basic description including colors or themes.
    feelings : str, optional
        Additional mood or feeling words.
    n : int, optional
        Number of images to generate (default is 1).

    Returns
    -------
    list[str]
        List of base64-encoded image data strings.
    """

    # Load environment variables from .env file
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not set in environment or .env file.")
    client = OpenAI(api_key=api_key)

    prompt = (
        f"Generate an image of a nail design with the following description: {description}."
    )
    if feelings:
        prompt += f" Include the following feelings or mood: {feelings}."

    # Generate n images by making n requests (since the current API may not support n>1 in a single call)
    images = []
    for i in range(n):
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=prompt,
            tools=[{"type": "image_generation"}],
        )
        image_data = [
            output.result for output in response.output if output.type == "image_generation_call"
        ]
        if image_data:
            images.append(image_data[0])
    return images


def main():
    print("Describe how you want your nails (colors, themes, etc.):")
    description = input().strip()
    print(
        "Optionally add feelings or moods (comma-separated, e.g., 'powerful, cheerful'):"
    )
    feelings = input().strip()
    print("How many images do you want to generate? (default 1):")
    try:
        n = int(input().strip() or "1")
    except ValueError:
        print("Invalid number, defaulting to 1 image.")
        n = 1

    try:
        images_base64 = generate_nail_image(description, feelings, n)
    except Exception as exc:
        print("Error contacting OpenAI API:", exc)
        return

    if images_base64:
        for idx, image_base64 in enumerate(images_base64, 1):
            filename = f"nail_design_{idx}.png" if n > 1 else "nail_design.png"
            with open(filename, "wb") as f:
                f.write(base64.b64decode(image_base64))
            print(f"Image saved as {filename}")
    else:
        print("No image returned by the API.")


if __name__ == "__main__":
    main()
