import requests

API_URL = "https://api.sora.com/v1/nail-ideas"


def generate_nail_ideas(description: str, feelings: str = "", num_ideas: int = 4):
    """Call Sora API to generate nail design ideas.

    Parameters
    ----------
    description : str
        Basic description including colors or themes.
    feelings : str, optional
        Additional mood or feeling words.
    num_ideas : int, optional
        Number of ideas to request from the API (default is 4).
    """
    payload = {
        "description": description,
        "feelings": feelings,
        "num_ideas": num_ideas,
    }
    response = requests.post(API_URL, json=payload)
    response.raise_for_status()
    data = response.json()
    return data.get("ideas", [])


def main():
    print("Describe how you want your nails (colors, themes, etc.):")
    description = input().strip()
    print("Optionally add feelings or moods (comma-separated, e.g., 'powerful, cheerful'):")
    feelings = input().strip()

    try:
        ideas = generate_nail_ideas(description, feelings)
    except requests.RequestException as exc:
        print("Error contacting Sora API:", exc)
        return

    if ideas:
        print("Here are some ideas:")
        for i, idea in enumerate(ideas, 1):
            print(f"{i}. {idea}")
    else:
        print("No ideas returned by the API.")


if __name__ == "__main__":
    main()
