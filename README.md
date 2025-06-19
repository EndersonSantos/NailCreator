# NailCreator

This project lets you create nail design images using OpenAI's image generation tools. You can run it as a script or via the included Django web application.

## Requirements
Install dependencies:
```bash
pip install -r requirements.txt
```
Set the environment variables `OPENAI_API_KEY` (and optionally `DJANGO_SECRET_KEY`). A `.env` file can also be used.

## CLI Usage
```bash
python nail_creator.py
```
Follow the prompts to generate images. They will be saved as `nail_design.png` (or numbered files if generating multiple images).

## Web Application
To use the Django web interface:
```bash
python manage.py migrate  # create the database
python manage.py runserver
```
Open `http://localhost:8000` and enter how you want the nails to look and feel. Generated images will appear below the form.
