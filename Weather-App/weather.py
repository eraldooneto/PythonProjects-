from cProfile import label
import tkinter as tk
import requests
import time 


# Function to extract data from the API 
def getWeather(canvas):
    city = textfield.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=e67ac427fc8911c67a4517fd8e59885c"

    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%H:%M:%S %p", time.gmtime(json_data['sys']['sunrise'] - 10800))
    sunset = time.strftime("%H:%M:%S %p", time.gmtime(json_data['sys']['sunset'] - 10800))

    final_info = condition + "\n" + str(temp) + "℃" 
    final_data = "\n" + "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" +"\n" + "Pressure: " + str(pressure) + "\n" +"Humidity: " + str(humidity) + "\n" +"Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    
    label1.config(text=final_info)
    label2.config(text=final_data)


# Define the UI

canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")

# Define some fonts to show on the screen 

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

# Get the city name from the user 

textfield = tk.Entry(canvas, font=t)
textfield.pack(pady=20)
textfield.focus()
textfield.bind('<Return>', getWeather)

# Create the labels to show de data

label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()

canvas.mainloop()

