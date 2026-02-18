from tkinter import *
from ttkthemes import ThemedTk
from tkinter.ttk import *
from tkinter import ttk
import openai
import requests
import base64
import os
from PIL import Image, ImageTk

window = ThemedTk(theme='breeze')
window.title(' AI Image generator created by JP')
window.geometry('600x780')
window.resizable(False, False)
window.configure(bg='#449DD1')
cIndex = 0
image_paths = []
client = openai.OpenAI(api_key = '')

OUTPUT_DIR = "outputs"

def showImage(ind):
    global imagePreview, image_paths

    img = Image.open(image_paths[ind])
    img = img.resize((400,400), Image.Resampling.LANCZOS)
    imagePreview = ImageTk.PhotoImage(img)
    image_label.config(image=imagePreview)

def nextImg(event=None):
    global cIndex

    if not image_paths:
        return

    cIndex = (cIndex + 1) % len(image_paths)
    showImage (cIndex)

def prevImg(event=None):
    global cIndex

    if not image_paths:
        return

    cIndex = (cIndex - 1) % len(image_paths)
    showImage (cIndex)

def preview_first():
    if image_paths:
        os.startfile(image_paths[0])

def download_image(url, filepath):
    img_data = requests.get(url).content
    with open(filepath, "wb") as f:
        f.write(img_data)

def generate_ideas(user_text,n):
    prompt =(
        f"Generate {n} unique, creative ideas for wallpaper about:{user_text}\n"
        f"Return ONLY a numbered list from 1 to {n}. One idea per line."
    )
    resp = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.9,
    )

    ideas = []
    for line in resp.choices[0].message.content.splitlines():
        print(line)
        line = line.strip()
        if line !="":
            ideas.append(line)
    return ideas[:n]

def generate_images_from_ideas(ideas):
    paths = []

    for i in range(len(ideas)):
        idea = ideas[i]

        img = client.images.generate(
            model="dall-e-3",
            prompt=idea,
            size="1024x1024",
            n=1
        )

        url = img.data[0].url
        print(url)
        filepath= OUTPUT_DIR +"/request"+ str(i+1)+ ".jpg"
        download_image(url,filepath)

def generate_images_from_ideas2(ideas):
    paths = []

    for i in range(len(ideas)):
        img = client.images.generate(
            model="gpt-image-1.5",  # newest quality
            prompt=ideas[i],
            size="1024x1024",
            n=1,
            output_format="jpeg"  # png / webp / jpeg
        )
        filepath = os.path.join(OUTPUT_DIR, f"request_{i+1}.jpg")

        b64 = img.data[0].b64_json
        print(b64)
        with open(filepath,"wb") as f:
            f.write(base64.b64decode(b64))

        paths.append(filepath)
    return paths

def process():
    global user,n, image_paths,cIndex
    user = txt1.get().strip()
    if rb.get() == "Choice1":
        n=1
    else:
        n=2
    ideas = generate_ideas(user,n)
    image_paths = generate_images_from_ideas2(ideas)
    showImage(0)
    cIndex = 0


lbl1 = ttk.Label(window, text= 'AI Image Generator',background='#449DD1', font=( 'Impact',30))
lbl1.pack()
lbl2 = ttk.Label(window, text= 'An AI Image Generator for wallpaper ideas',background='#449DD1', font=( 'Impact',15))
lbl2.pack()
image_label = ttk.Label(window, text='')
image_label.place(x=100,y=300)
txt1 = ttk.Entry(window, font=('Impact',15))
txt1.pack(pady=100)
rb = StringVar(value="Choice1")
rad1 = ttk.Radiobutton(window, text="Short [1 variants]", value="Choice1", variable=rb)
rad1.place(x=150,y=100)
rad2 = ttk.Radiobutton(window, text="Extended [2 Variants]", value="Choice3", variable=rb)
rad2.place(x=300,y=100)
btnprev = ttk.Button(window,text= 'Preview', command=preview_first)
btnprev.place(x=150,y=250)
btnent = ttk.Button(window,text= 'Enter', command=process)
btnent.place(x=350,y=250)


window.bind("<Right>",nextImg)
window.bind("<Left>",prevImg)

window.mainloop()