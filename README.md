# NailCreator

This project allows a nail stylist to describe desired nail designs using colors, themes, and feelings. It uses the OpenAI Responses API with the image generation tool to create a sample design image.

## Usage

1. Install dependencies (requires the `openai` library):
   ```bash
   pip install openai
   ```
2. Set your `OPENAI_API_KEY` environment variable.
3. Run the script:
   ```bash
   python nail_creator.py
   ```
4. Provide the description and optional feelings when prompted. The script will generate an image saved as `nail_design.png`.
