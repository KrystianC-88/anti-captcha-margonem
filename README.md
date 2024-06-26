# AI Anti-Captcha Margonem

**Trained on a dataset of 150+ captchas**

![for education purposes only](https://img.shields.io/badge/-for%20education%20purposes%20only-red)  

This project is developed for educational purposes only. Usage in the game "Margonem" may result in a ban.

## How to Run the Program

1. Download the model from [here](https://drive.google.com/file/d/17mdh8VxHYL3gipHsBKuCE73uvl9008jF/view?usp=sharing).
2. Place the downloaded model in the `training/models/` directory.

After setting up the model, follow these steps to run the application:

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
4. Inject `margonem-script.js` into the console while in Margonem.

![GIF Image](https://i.imgur.com/MeTmsBM.gif)

## How to Improve the AI

To enhance the AI model, you can train it using Roboflow.

1. Create a project on Roboflow.
2. Upload your captcha photos.
3. Create two tags: "normal" and "upsidedown".

**IMPORTANT:** Create the "normal" tag before the "upsidedown" tag.

4. Select all instances labeled "normal" and "upsidedown".

![Roboflow Image](https://i.imgur.com/7UWjuFP.png)

5. Save the dataset using only the resize option in preprocessing:

![Roboflow Image](https://i.imgur.com/rofMVcj.png)


6. Use `training/train.ipynb` to train the model.
7. Update the model in `captcha.py` to match your new model.

[Watch this video](https://youtu.be/x0ThXHbtqCQ) for more information about training.

Need assistance? Message me on Discord: sffrhs.dev

Discord ID: 515623136805388291
