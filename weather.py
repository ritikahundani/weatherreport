#importing modules
import time
from tkinter import *
from tkinter import messagebox as mb
import requests
from plyer import notification


def getNotification():
    cityName = place.get()  # getting input of name of the place from user
    baseUrl = "http://api.openweathermap.org/data/2.5/weather?"  # base URL from where we extract weather report
    try:
        # This is the complete URL to get weather conditions of a city
        url = baseUrl + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + cityName
        response = requests.get(url)  # requesting the content of the URL
        x = response.json()  # converting it into JSON

        if x["cod"] != 200:  # Check if the response contains an error
            raise Exception(x.get("message", "Error fetching weather data"))

        y = x["main"]  # getting the "main" key from the JSON object

        # getting the "temp" key of y
        temp = y["temp"]
        temp -= 273.15  # converting temperature from Kelvin to Celsius

        # storing the value of the "pressure" key of y
        pres = y["pressure"]

        # getting the value of the "humidity" key of y
        hum = y["humidity"]

        # storing the value of "weather" key in variable z
        z = x["weather"]

        # getting the corresponding "description"
        weather_desc = z[0]["description"]

        # combining the above values as a string
        info = (
            f"Here is the weather description of {cityName}:\n"
            f"Temperature = {temp:.2f}°C\n"
            f"Atmospheric pressure = {pres} hPa\n"
            f"Humidity = {hum}%\n"
            f"Description of the weather = {weather_desc}"
        )

        # showing the notification
        notification.notify(
            title="YOUR WEATHER REPORT",
            message=info,
            timeout=2,
        )
    except Exception as e:
        mb.showerror('Error', f"Unable to fetch weather data: {e}")  # show pop-up message if any error occurred
#creating the window
wn = Tk()
wn.title("PythonGeeks Weather Alert")
wn.geometry('700x200')
wn.config(bg='azure')

# Heading label
Label(wn, text="PythonGeeks Weather Desktop Notifier", font=('Courier', 15), fg='grey19',bg='azure').place(x=100,y=15)

#Getting the city name 
Label(wn, text='Enter the Location:', font=("Courier", 13),bg='azure').place(relx=0.05, rely=0.3)

place = StringVar(wn)
place_entry = Entry(wn, width=50, textvariable=place)
place_entry.place(relx=0.5, rely=0.3)

#Button to get notification
btn = Button(wn, text='Get Notification', font=7, fg='grey19',command=getNotification)
btn.place(relx=0.4, rely=0.75)
#run the window till the closed by user
wn.mainloop()
#Function to get notification of weather report