from tkinter import *
# Tkinter is used to create a GUI( GRAPHIC USER INTERFACE)
# The "*" symbol is used to use all the tools or resources available in tkinter module or library

from tkinter import messagebox


# The ConfigParser class from the configparser module in Python is used for working with configuration files, including .ini files.
# It provides methods for reading, writing, and manipulating configuration data stored in .ini file format.
# As the api keys should be kept hidden i used a ini file to hide it from other people to see the key.

from configparser import ConfigParser

import requests

# This is the URL that u can copy from a website of the API...this will help us to take the data of a particular city
url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

# These lines load the contents of the specified .ini configuration file into the config object and then retrieve the value of the "api_key" key.
config_file = "config.ini"
config = ConfigParser()
config.read(config_file)
api_key = config["api_key"]["key"]

# This function that is defined here is used to take info from the API and show us in GUI
def get_weather(city):
    result = requests.get(url.format(city, api_key))
    if result:
# The line json = result.json() suggests that you are working with a JSON response obtained from an API request or a JSON-formatted data structure.
        json = result.json()
# Now we want ( City, Country, Temp celcius, temp farenhiet, icon, weather)
        city = json["name"]
        country = json["sys"]["country"]
        temperature = json["main"]["temp"]
        Temp_celcius = temperature - 273.15
        Temp_farenhiet = (temperature - 273.15) * 9/5 + 32
        icon= json["weather"][0]["icon"]
        weather = json[ "weather"][0]["main"]
        final = (city, country, Temp_celcius, Temp_farenhiet, icon, weather)
        return final
    else:
        return None



# This def function will be used later int his program
def search():
    city = city_search.get()
    weather = get_weather(city)
    if weather:
        location["text"] = "{}, {}".format(weather[0], weather[1])
# Here the image wasnt printing if just plainly used image["text] = etc....so i created a new def function below to show the image properly
        update_weather_icon(weather[4])
# Here the .2f will only let 2 digits after the decimal point appear on screen
        temp["text"] = "{:.2f}°C, {:.2f}°F".format(weather[2], weather[3])
        weather_condition["text"] = weather[5]
    else:
        messagebox.showerror("ERROR", "Invalid City Name: {}".format(city))

# define function to update the weather icon

def update_weather_icon(icon_name):
    image_path = "weather icons/{}.png".format(icon_name)
    photo = PhotoImage(file=image_path)
    image.config(image=photo)
    image.image = photo





app = Tk()

# This line above is used to create the window prompt for the imput and output of the interface

# Now after creating the window prompt we add a title

app.title("KNOW THE WEATHER")

# Now we set the ratio or size of the window prompt

app.geometry("350x700")

# I want to change my background colour from plane white to eye pleasing colour
# Be sure to add the bg=#b7c9b1 in every label_space or you will get white spaces in between the background

app.configure(bg="#b7c9b1")

# To show more details in the prompt we can use the following lines

# This line is used for vertical spacing
label_space = Label(app, text="", bg="#b7c9b1")
label_space.pack()
# the .pack is used to end and showcase the object in the window prompt
label = Label(app, text=("Enter the City Name: "))
label.pack()

label_space = Label(app, text="", bg="#b7c9b1")
label_space.pack()

# Now to make the window prompt look better I want to add the search button and the entry bar side by side:
entry_frame = Frame(app, bg="#b7c9b1")
# Here Frame(app) will create an invisible rectangular bar which can hold multiple widgets together...this will help in maintaining the neatness of the prompt
entry_frame.pack()

# Entry here helps you to make the search bar in ur window prompt where u can type and stringvar helps u to input text from the user.
city_search = StringVar()
# Here  we use entry_frame rather than app as we want to group button and entry bar together
city_search = Entry(entry_frame, text="city_search", bg="#ffffff")

# Here in pack paranthesis..if u do not add any direction..the frame wont be holding the widgets side by side
city_search.pack(side = LEFT)

# This will give us a Horizontal spacing in between entry bar and search button
label_space = Label(entry_frame, text=" ", bg="#b7c9b1")
label_space.pack(side = LEFT)

# To search the city's weather from API that will be used later in this program the following search button is added.
# Here we use the "search" that we defined earlier
# Here if you observe in the parenthesis,,,we use entry_frame rather than app...its because now we can group button and entry bar together.
search_button= Button(entry_frame, text="Search Weather", width = 12, command=search)
search_button.pack(side=LEFT)

label_space = Label(entry_frame, text="", bg="#b7c9b1")
label_space.pack()

# Now to add more stuff like location, temp, weather icon, weather type etc we use the following lines
# Calibri is a font name...u can add any other type of font that u like
location=Label(app, text="", font=("Calibri", 20), bg="#b7c9b1")
location.pack()

label_space = Label(app, text="", bg="#b7c9b1")
label_space.pack()

# Now I want to add an icon that will be showing us the weather condition according to the data recieved from the API.
image = Label(app, bitmap="", bg="#b7c9b1")
image.pack()

label_space = Label(app, text="", bg="#b7c9b1")
label_space.pack()

#I also want to show the temperature of the city in celcius and farenhiet
temp = Label(app, text = ": ", bg="#b7c9b1")
temp.pack()

label_space = Label(app, text="", bg="#b7c9b1")
label_space.pack()

# Now to show the weather
weather_condition= Label(app, text= "", bg="#b7c9b1")
weather_condition.pack()

label_space = Label(app, text="", bg="#b7c9b1")
label_space.pack()


# To show the window prompt when we run the program the following line will initialize it.


app.mainloop()






