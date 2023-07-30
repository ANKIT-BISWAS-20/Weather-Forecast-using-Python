import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image,ImageTk
import ttkbootstrap


API_KEY="37a7723afda34c7c0c25f011a89ce114"
BASE_URL="https://api.openweathermap.org/data/2.5/weather?"

def weather(CITY):
    url=BASE_URL+"q="+CITY+"&appid="+API_KEY
    responce=requests.get(url).json()
    temparature=int((responce["main"]["temp"]-273)//1)
    description=responce['weather'][0]["description"]
    humidity=int((responce["main"]["humidity"])//1)
    icon_id=responce['weather'][0]['icon']
    icon_url=f"http://openweathermap.org/img//wn/{icon_id}@2x.png"
    result = [CITY , temparature, humidity , description , icon_url]
    return(result)


def search():
    CITY=entry.get()
    output=weather(CITY)
    if output == None:
        return
    CITY = output[0]
    temparature = output[1]
    humidity = output[2]
    description = output[3]
    icon_url =  output[4]
    city.configure(text=f"City Name : {CITY}")
    temparature_label.configure(text=f"TEMPARATURE : {temparature}°C")
    humidity_label.configure(text=f"HUMIDITY : {humidity}")
    description_label.configure(text=f"DESCRIPTION : {description}")
    image=Image.open(requests.get(icon_url,stream=True).raw)
    icon = ImageTk.PhotoImage(image)
    icon_label.configure(image=icon)
    icon_label.image = icon


root = ttkbootstrap.Window(themename = "vapor")
root.title("WEATHER FORECAST")
root.geometry("400x600")

heading = tk.Label(root, font="Helvetica, 24")
heading.configure(text="WEATHER FORECAST")
heading.pack(pady=20)


entry = ttkbootstrap.Entry(root, font="Helvetica, 18")
entry.pack(pady=10)

search_button = ttkbootstrap.Button(root, text="Search",command=search,bootstyle="green")
search_button.pack(pady=10)

city = tk.Label(root, font="Helvetica, 25")
city.pack(pady=20)

icon_label = tk.Label(root)
icon_label.pack()

temparature_label = tk.Label(root, font="Helvetica, 20")
temparature_label.pack()

humidity_label = tk.Label(root, font="Helvetica, 20")
humidity_label.pack()

description_label = tk.Label(root, font="Helvetica, 20")
description_label.pack()

root.mainloop()