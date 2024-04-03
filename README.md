# AI Anti-Captcha Margonem

![for education purposes only](https://img.shields.io/badge/-for%20education%20purposes%20only-red)  

This project is developed for educational purposes only. Usage in the game "Margonem" may result in a ban.

## How to Run the Program

1. Set up a virtual environment:
    ```bash
    python -m venv venv 
    ```
2. Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the application:
    ```bash
    python app.py
    ```
4. Inject 'margonem-script.js' in the console while being in Margonem

![GIF Image](link_to_gif)

## How to Improve the AI

To improve the AI model, you can train it on Roboflow.

1. Create a project on Roboflow.
2. Upload your captcha photos.
3. Create two tags: "normal", "upsidedown".
4. Select all instances labeled "normal" and "upsidedown".
5. Save the data:


**IMPORTANT:** Create the "normal" tag first, then "upsidedown".

[Watch this video](link_to_video) for more information about training.

