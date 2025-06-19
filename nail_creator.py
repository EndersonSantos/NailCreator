import base64
from openai import OpenAI


def generate_nail_image(description: str, feelings: str = "") -> str:
    """Generate a nail design image using the OpenAI Responses API.

    Parameters
    ----------
    description : str
        Basic description including colors or themes.
    feelings : str, optional
        Additional mood or feeling words.

    Returns
    -------
    str
        Base64-encoded image data or ``None`` if no image was returned.
    """

    client = OpenAI()

    prompt = (
        f"Generate an image of a nail design with the following description: {description}."
    )
    if feelings:
        prompt += f" Include the following feelings or mood: {feelings}."

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt,
        tools=[{"type": "image_generation"}],
    )

    image_data = [
        output.result for output in response.output if output.type == "image_generation_call"
    ]
    return image_data[0] if image_data else None


def main():
    print("Describe how you want your nails (colors, themes, etc.):")
    description = input().strip()
    print(
        "Optionally add feelings or moods (comma-separated, e.g., 'powerful, cheerful'):"
    )
    feelings = input().strip()

    try:
        image_base64 = generate_nail_image(description, feelings)
    except Exception as exc:
        print("Error contacting OpenAI API:", exc)
        return

    if image_base64:
        filename = "nail_design.png"
        with open(filename, "wb") as f:
            f.write(base64.b64decode(image_base64))
        print(f"Image saved as {filename}")
    else:
        print("No image returned by the API.")


if __name__ == "__main__":
    main()
