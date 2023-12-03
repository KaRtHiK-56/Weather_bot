# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
import requests
from datetime import datetime


class ActionGreetTime(Action):
    def name(self) ->Text:
        return "action_greet_time"

    def run(self,dispatcher:CollectingDispatcher,tracker:Tracker,domain:Dict[Text,any]) ->List[Dict[Text,any]]:
        now = datetime.now()
        hour = now.hour
        minute = now.minute

        if hour < 11.59:
            greeting = "Good Morning"
        elif hour < 17.59:
            greeting = "Good Afternoon"
        else:
            greeting = "Good Evening"

        dispatcher.utter_message(text=greeting)

        return[]


class ActionWeather(Action):
    def name(self):
        return 'action_weather'

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        city = tracker.get_slot('location')
        api_key = 'd1dcf6f5f9e6f85f1aa51222e18cd4c6'

        complete_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={api_key}"

        # Make the API request
        response = requests.get(complete_url)

        # Check if the API request was successful
        if response.status_code == 200:
            data = response.json()
            temperature = round(data['main']['temp'] - 273.15, 2)
            place = data["name"]
            weather_desc = data['weather'][0]['main']


            weather_message = f"It's {temperature} degree Celsius currently in {place}. The weather can be described as {weather_desc}."


            dispatcher.utter_message(weather_message)

            # Update the location slot
            return [SlotSet("location", city)]
        else:
            dispatcher.utter_message("Sorry, I couldn't fetch the weather information at the moment.")


        return []


