#Importing required libraries
import requests
import json
from win10toast import ToastNotifier
import time
 
def covid_update(): 
    '''
    this function takes no parameter, will get a response from the given api and access the values in Bangladesh row from the response data.
    Then return the text with proper values and display itt as notification.
    '''
    response = requests.get('https://coronavirus-19-api.herokuapp.com/countries')
    data = response.json()
    confirmed_cases = data[26]['cases']
    deaths = data[26]['deaths']
    today_cases = data[26]['todayCases']
    today_deaths = data[26]['todayDeaths']
    recovered = data[26]['recovered']
    text = f'Confirmed_cases: {confirmed_cases}\nDeaths: {deaths}\nToday_cases: {today_cases}\nToday_deaths: {today_deaths}\nRecovered: {recovered}'

    while True: 
        toast = ToastNotifier()
        toast.show_toast('Covid-19 Updates Bangladesh', text, duration = 15)
        time.sleep(10)
        
covid_update()
