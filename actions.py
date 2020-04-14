# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import pandas as pd
import json

class Actiontuvan(Action):

     def name(self) -> Text:
         return "action_tochat"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         nganh_new = tracker.get_slot("nganh_intent")

         with open('data_train.json', encoding="utf8") as f:
             data = json.load(f)

         columns = ["nganh", "tochat", "cohoivieclam", "luong", "hocphi", "hocodau", "lagi", "tudongnghia"];
         df = pd.DataFrame(data, columns=columns)
         ng = ""
         for i in df.nganh :
             if ( nganh_new == i):
                    ng = i
                    dispatcher.utter_message("Để học tốt ngành {}".format(ng))
             else : dispatcher.utter_message("không kéét noi dc")
         return []
         # read file json
         """with open('data_train.json', encoding="utf8") as f:
             data = json.load(f)

         columns = ["nganh", "tochat", "cohoivieclam", "luong", "hocphi", "hocodau", "lagi", "tudongnghia"];
         df = pd.DataFrame(data, columns=columns)
         ##
         #x = "Sư phạm tiếng anh"
         y = "tochat"
         # lấy index của x
         z = df.nganh.tolist()
         # print(z.index(x))
         tc = df.tochat.tolist()
         # print(type(a))
         for i in df.nganh:
             if (nganh_new == i):
                 for j in df:
                     if (y == j):
                         ng = i
                         tc_new = tc[z.index(nganh_new)]

         dispatcher.utter_message("Để học tốt ngành {} , {}".format(ng,tc_new))
         return [SlotSet("tc_new", tc_new)] """
