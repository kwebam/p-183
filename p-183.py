from tkinter import *
import requests
import json

root = Tk()
root.geometry("1000x700")
root.configure(bg = "#00cc99")

city_name_label = Label(root, text = "Capital City Name", font = ("Gloucester MT Extra Condensed",30, "bold"), bg = "#00cc99", fg = "#55ff00")
city_name_label.place(relx = 0.13, rely = 0.01, anchor = N)

city_entry = Entry(root)
city_entry.place(relx = 0.09, rely = 0.09, anchor = N)

Country_Name = Label(root, text = "Country : ", font = ("Gloucester MT Extra Condensed", 15, "bold"), bg = "#00cc99", fg = "#55ff00")
Country_Name.place(relx = 0.09, rely = 0.17, anchor = N)

region = Label(text = "Region : ")
region.place(relx = 0.09, rely = 0.25, anchor = N)

languages = Label(text = "Language : ")
languages.place(relx = 0.09, rely = 0.33, anchor = N)

population = Label(text = "Population : ")
population.place(relx = 0.09, rely = 0.41, anchor = N)

area = Label(text = "Area : ")
area.place(relx = 0.09, rely = 49, anchor = N)

def city_details():
    global Country_Name
    global city_name_label
    global city_entry
    global region
    global languages
    global population
    global area
    api_request = requests.get("https://restcountries.com/v2/capital/" + city_entry.get())
    api_output_json = json.loads(api_request.content)
    
    country = api_output_json[0]['name']
    reg = api_output_json[0]['region']
    lang = api_output_json[0]['languages']
    popn = api_output_json[0]['population']
    country_area = api_output_json[0]['area']
    
    Country_Name['text'] = 'Country :' + str(country)
    region['text'] = 'Region :' + str(reg)
    languages['text'] = 'Language :' + str(lang)
    population['text'] = 'Population :' + str(popn)
    area['text'] = 'Area :' + str(country_area)

button = Button(root, text = "City Details", command = city_details, relief = FLAT, bg = '#00cc99')
button.place(relx = 0.09,rely = 0.57, anchor = N)

root.mainloop()