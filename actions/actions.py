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
from rasa_sdk.executor import CollectingDispatcher

class ActionRecommendDestinations(Action):
    def name(self) -> Text:
        return "action_recommend_destinations"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        preferences = tracker.get_slot("preferences")
        # Perform logic to fetch recommendations based on user preferences
        recommendations = ["Paris", "Bali", "Maldives"]  # Replace with actual recommendations

        # Provide the recommendations to the user
        if recommendations:
            dispatcher.utter_message(f"Here are some recommended destinations: {', '.join(recommendations)}")
        else:
            dispatcher.utter_message("Sorry, I couldn't find any recommendations matching your preferences.")
        return []

class ActionRecommendActivities(Action):
    def name(self) -> Text:
        return "action_recommend_activities"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        destination = tracker.get_slot("destination")
        # Perform logic to fetch activities for the recommended destination
        activities = ["Scuba Diving", "Hiking", "Sightseeing"]  # Replace with actual activities

        # Provide the activities to the user
        if activities:
            dispatcher.utter_message(f"Here are some activities you can enjoy in {destination}: {', '.join(activities)}")
        else:
            dispatcher.utter_message("Sorry, I couldn't find any activities for the recommended destination.")
        return []
