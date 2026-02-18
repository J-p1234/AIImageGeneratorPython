🎨 AI Image Generator – Wallpaper Creator

An elegant desktop AI Image Generator built with Python & Tkinter.
Create unique wallpaper ideas and automatically generate high-quality AI images using OpenAI models.

🚀 Features

🧠 Generates creative wallpaper ideas using GPT

🖼️ Creates high-resolution AI images (1024x1024)

🔄 Browse images with keyboard arrows (← →)

💾 Download & preview generated images

🎨 Clean modern GUI using ttkthemes

⚡ Supports multiple image variants

🛠️ Technologies Used

Python 3

Tkinter (GUI)

ttkthemes

OpenAI API

PIL (Pillow)

Requests


Install dependencies
pip install openai pillow requests ttkthemes

🔑 Setup API Key

Inside the script, replace:

client = openai.OpenAI(api_key = '')


with your OpenAI API key:

client = openai.OpenAI(api_key = 'YOUR_API_KEY_HERE')

🖥️ How It Works

Enter a wallpaper theme (e.g. Cyberpunk city at night)

Choose:

Short → 1 image

Extended → 2 image variants

Click Enter

Browse results using:

→ Right Arrow

← Left Arrow

Click Preview to open the first generated image

🧠 AI Models Used

GPT model for idea generation

Image generation model (gpt-image-1.5 or DALL·E)

📸 Example Prompt Ideas

"Minimalist Japanese landscape"

"Futuristic neon jungle"

"Abstract cosmic waves"

"Dark fantasy castle"

🎯 Future Improvements

Image loading animation

Progress bar while generating

Image gallery grid view

Save custom filenames

Add resolution options

Export history

👨‍💻 Author

Created by JP
AI Enthusiast & Python Developer

<img width="594" height="804" alt="Στιγμιότυπο οθόνης (22)" src="https://github.com/user-attachments/assets/716a33f5-a86f-4966-8b46-69b4a7f69cc5" />

