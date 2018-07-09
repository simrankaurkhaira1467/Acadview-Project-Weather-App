#Packages used:
import tkinter as tk
import requests
from tkinter import *
import datetime
from tkinter import font as tkFont
import json
import socket

# checks if we are connected to the internet or not
def connection():
    try:
        # it returns only a single IPv4 address
        gethost = socket.gethostbyname("www.google.com")
        # it creates a connection with the host if available
        skt = socket.create_connection((gethost, 80), 2)
        return True
    except:
        print("Could not connect")
    return False


class WeatherApp():
    # master specifies the frame of the tkinter window.
    def __init__(self, master, city):
        if city != "":
            # the name of the city should not be empty.
            if connection():
                # if internet is available, then we try to retrieve the data
              weather_frame = Frame(master)
              weather_frame.grid(row=0)
              self.custom_font = tkFont.Font(family="Helvetica", size=12, weight="bold")
              self.custom_heading_font = tkFont.Font(family="Helvetica", size=14, weight="bold")
                # initialization of all member variables to None
              self.city_name = StringVar()
              self.temperature = StringVar()
              self.temp1 = StringVar()
              self.date = StringVar()
              self.longitude = StringVar()
              self.latitude = StringVar()
              self.current_weather_url = None
              self.des = StringVar()
              self.description = StringVar()
              self.minimum = StringVar()
              self.maximum = StringVar()
              self.temp2 = StringVar()
              self.sunrise = StringVar()
              self.temp3 = StringVar()
              self.sunset = StringVar()
              self.pressure = StringVar()
              self.humidity = StringVar()
              self.wind_speed = StringVar()
              self.wind_direction = StringVar()
              self.cloudiness = StringVar()
              self.rain = StringVar()

              self.display_information(weather_frame, city)
    #displaying all the information on screen.
    def display_information(self, master, city):
        self.url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=212ef52e80c5bbd6542d046854d27cc3'.format(city)
        self.city_list = requests.get(self.url)
        self.data = self.city_list.json()
        #getting data from json using slicing
        self.city_name = self.data['name']
        self.temperature = self.data['main']['temp']
        self.temp1 = self.data['dt']
        self.date = datetime.datetime.fromtimestamp(int(self.temp1)).strftime('%d-%m-%Y %H:%M:%S')
        self.latitude = self.data['coord']['lat']
        self.longitude = self.data['coord']['lon']
        self.des = self.data['weather'][0]['main']
        self.description = self.data['weather'][0]['description']
        self.minimum = self.data['main']['temp_min']
        self.maximum = self.data['main']['temp_max']
        self.sunrise = self.data['sys']['sunrise']
        self.sumset = self.data['sys']['sunset']
        self.pressure = self.data['main']['pressure']
        self.humidity = self.data['main']['humidity']
        self.wind_speed = self.data['wind']['speed']
        self.wind_direction = self.data['wind']['deg']
        self.cloudiness = self.data['clouds']['all']
        if 'rain' in self.city_list:
            self.rain.set("%0.2f mm" % self.city_list['rain'])
        else:
            self.rain.set("No rain today.")

        label_city = Label(master, text=self.city_name, font=self.custom_heading_font)
        label_city.grid(row=0,column=0, columnspan=3, padx=2, pady=2)

        label_time = Label(master, text=self.date, font=self.custom_heading_font)
        label_time.grid(row=1,column=0, columnspan=3, padx=2, pady=2)

        label_time = Label(master, text='Temperature', font=self.custom_font)
        label_time.grid(row=2, column=0, padx=2, pady=2)
        label_temp = Label(master, text=self.temperature, font=self.custom_font)
        label_temp.grid(row=2,column=1, columnspan=2, padx=2, pady=2)

        label_des = Label(master, text=self.des, font=self.custom_font)
        label_des.grid(row=3, column=0, padx=2, pady=2)
        label_desc = Label(master, text=self.description, font=self.custom_font)
        label_desc.grid(row=3, column=1, padx=2, pady=2)

        label_time = Label(master, text='Minimum Temperature')
        label_time.grid(row=4, column=0, padx=2, pady=2)
        label_min = Label(master, text=self.minimum)
        label_min.grid(row=4,column=1, columnspan=2, padx=2, pady=2)

        label_time = Label(master, text='Maximum Temperature')
        label_time.grid(row=5, column=0, padx=2, pady=2)
        label_max = Label(master, text=self.maximum)
        label_max.grid(row=5, column=1,columnspan=2, padx=2, pady=2)

        label_time = Label(master, text='Pressure')
        label_time.grid(row=6, column=0, padx=2, pady=2)
        label_time = Label(master, text=self.pressure)
        label_time.grid(row=6,column=1, columnspan=5, padx=2, pady=2)

        label_time = Label(master, text='Humidity')
        label_time.grid(row=7, column=0, padx=4, pady=4)
        label_time = Label(master, text=self.humidity)
        label_time.grid(row=7,column=1, columnspan=5, padx=4, pady=4)

        label_time = Label(master, text='Wind Speed')
        label_time.grid(row=8, column=0, padx=4, pady=4)
        label_time = Label(master, text=self.wind_speed)
        label_time.grid(row=8,column=1, columnspan=5, padx=4, pady=4)

        label_time = Label(master, text='Wind Direction')
        label_time.grid(row=9, column=0, padx=4, pady=4)
        label_time = Label(master, text=self.wind_direction)
        label_time.grid(row=9,column=1, columnspan=5, padx=4, pady=4)

        label_time = Label(master, text='Cloudiness')
        label_time.grid(row=10, column=0, padx=4, pady=4)
        label_time = Label(master, text=self.cloudiness)
        label_time.grid(row=10, column=1,columnspan=5, padx=4, pady=4)

        label_time = Label(master, text='Rain')
        label_time.grid(row=11, column=0, padx=4, pady=4)
        Label(master, textvariable=self.rain).grid(row=11, column=1, padx=2, pady=2)

        self.scale(master)

        # scale the widgets with the master window
        def scale(master):
            master.columnconfigure(0, weight=1)
            master.columnconfigure(1, weight=1)
            master.rowconfigure(0, weight=1)
            master.rowconfigure(1, weight=1)
            master.rowconfigure(2, weight=1)
            master.rowconfigure(3, weight=1)
            master.rowconfigure(4, weight=1)
            master.rowconfigure(5, weight=1)
            master.rowconfigure(6, weight=1)
            master.rowconfigure(7, weight=1)
            master.rowconfigure(8, weight=1)
            master.rowconfigure(9, weight=1)
            master.rowconfigure(10, weight=1)
            master.rowconfigure(11, weight=1)
            master.rowconfigure(12, weight=1)



def show_data():
    city = entry_city.get()
    print(city)
    for child in content_frame.winfo_children():
        child.destroy()
    WeatherApp(content_frame, city)


root = Tk()
root.wm_title("Sunshine")
root.wm_iconbitmap('sun-icon.ico')
"""
RWidth = root.winfo_screenwidth()
RHeight = root.winfo_screenheight()
root.geometry(("%dx%d") % (RWidth/5, RHeight/5))
root.resizable(width=False, height=False)
"""
font = tkFont.Font(family="Helvetica", size=10)
top_frame = Frame(root)
top_frame.grid(row=0, columnspan=2, padx=4, pady=4)
Label(top_frame, text="City", font=font).grid(row=0, column=0, sticky="W", padx=4, pady=4)
entry_city = Entry(top_frame, font=font)
entry_city.grid(row=0, column=1, padx=4, pady=4)
entry_city.focus_set()
content_frame = Frame(root)
content_frame.grid(row=1, columnspan=2)
button_city = Button(top_frame, text="Show Weather", command=show_data, font=font, relief=GROOVE)
button_city.grid(row=1, columnspan=2, padx=4, pady=4)
root.update()
root.minsize(200, root.winfo_height())
root.bind("<Return>", lambda x: show_data())

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

root.mainloop()
