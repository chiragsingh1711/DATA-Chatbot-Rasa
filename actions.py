# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
#from rasa_sdk import Action, Tracker
#from rasa_sdk.executor import CollectingDispatcher
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

class Question1(Action):

    def name(self) -> Text:
        return "q1ans"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("Inside actions")
        import csv

        f = open("Sample.csv", 'r')
        csv_reader = csv.reader(f)
        user_message = str((tracker.latest_message)['text'])
        month = None
        year = None
        content_text=None
        a = user_message.lower()
        sp = a.split()
        for i in sp:
            if "jan" in i or "january" in i:
                month = "Jan"
            elif "feb" in i or "february" in i:
                month = "Feb"
            elif "mar" in i or "march" in i:
                month = "Mar"
            elif "apr" in i or "april" in i:
                month = "Apr"
            elif "may" in i:
                month = "May"
            elif "june" in i:
                month = "Jun"
            elif "july" in i:
                month = "Jul"
            elif "aug" in i or "august" in i:
                month = "Aug"
            elif "sept" in i or "september" in i:
                month = "Sep"
            elif "oct" in i or "october" in i:
                month = "Oct"
            elif "nov" in i or "november" in i:
                month = "Nov"
            elif "dec" in i or "december" in i:
                month = "Dec"
        for i in sp:
            if "20" in i:
                if len(i)==4:
                    year = i
                else:
                    year=i[:4]
        if month!=None and year!=None:
	        csv_reader = [i for i in csv_reader]
	        csv_reader = csv_reader[1:]
	        content_text = None
	        for i in csv_reader:
		        j = i[1]
		        j = j.split('-')
		        if month in j and year in j:
		            content_text = i[3] + " is the Quality for "+month+" "+year
		            break
        if content_text == None:
        	content_text="Sorry, Please give valid information.        For Eg- What is the quality for (month) (year) ?"
        f.close()
        dispatcher.utter_message(text=content_text)
        return []

class Question2(Action):

    def name(self) -> Text:
        return "q2ans"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("Inside actions")
        import csv

        f = open("Sample.csv", 'r')
        csv_reader = csv.reader(f)
        user_message = str((tracker.latest_message)['text'])
        month1 = None
        year1 = None
        month2 = None
        year2 = None
        a = user_message.lower()
        sp = a.split()
        for i in sp[:sp.index("and")]:
            if "jan" in i or "january" in i:
                month1 = "Jan"
            elif "feb" in i or "february" in i:
                month1 = "Feb"
            elif "mar" in i or "march" in i:
                month1 = "Mar"
            elif "apr" in i or "april" in i:
                month1 = "Apr"
            elif "may" in i:
                month1 = "May"
            elif "june" in i:
                month1 = "Jun"
            elif "july" in i:
                month1 = "Jul"
            elif "aug" in i or "august" in i:
                month1 = "Aug"
            elif "sept" in i or "september" in i:
                month1 = "Sep"
            elif "oct" in i or "october" in i:
                month1 = "Oct"
            elif "nov" in i or "november" in i:
                month1 = "Nov"
            elif "dec" in i or "december" in i:
                month1 = "Dec"
        for i in sp[:sp.index("and")]:
            if "20" in i:
                if len(i)==4:
                    year1 = i
                else:
                    year1=i[:4]

        for i in sp[sp.index("and"):]:
            if "jan" in i or "january" in i:
                month2 = "Jan"
            elif "feb" in i or "february" in i:
                month2 = "Feb"
            elif "mar" in i or "march" in i:
                month2 = "Mar"
            elif "apr" in i or "april" in i:
                month2 = "Apr"
            elif i == "may" in i:
                month2 = "May"
            elif i == "june" in i:
                month2 = "Jun"
            elif i == "july" in i:
                month2 = "Jul"
            elif i == "aug" or i == "august":
                month2 = "Aug"
            elif i == "sept" or i == "september":
                month2 = "Sep"
            elif  "oct" in i or "october" in i:
                month2 = "Oct"
            elif  "nov" in i or "november" in i:
                month2 = "Nov"
            elif  "dec" in i in i or  "december" in i:
                month2 = "Dec"
        for i in sp[sp.index("and"):]:
            if "20" in i:
                if len(i)==4:
                    year2 = i
                else:
                    year2=i[:4]


        csv_reader = [i for i in csv_reader]
        csv_reader = csv_reader[1:]
        content_text = None
        x,y=None,None
        if month1!=None and year1!=None and month2!=None and year2!=None :
            for i in csv_reader:
                j = i[1]
                j = j.split('-')
                if month1 in j and year1 in j:
                    x = float(i[3])
                if month2 in j and year2 in j:
                    y = float(i[3])
		    
            content_text=str(abs(x-y))
            content_text+=" is the Quality Difference between "+month1+" "+year1+" and "+month2+" "+year2
        if content_text==None:
            content_text="Sorry, Please give valid information.        For Eg- Quality Difference between (month1) (year1) and (month2) (year2) ?"

        dispatcher.utter_message(text=content_text)
        return []

class Question3(Action):

    def name(self) -> Text:
        return "q3ans"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("Inside actions")

        import csv

        f = open("Sample.csv", 'r')
        csv_reader = csv.reader(f)

        user_message = str((tracker.latest_message)['text'])
        year = None
        a = user_message.lower()
        sp = a.split()

        for i in sp:
            if "20" in i:
                if len(i)==4:
                    year = i
                else:
                    year=i[:4]


        content_text=None

        csv_reader = [i for i in csv_reader]
        dict = {}
        csv_reader = csv_reader[1:]
        if year!=None:
            for i in csv_reader:
                j = i[1]
                j = j.split('-')
                if year in j:
                    dict[float(i[3])] = j[1]
            f.close()
            l = [i for i in dict.keys()]
            content_text = dict[max(l)]
            content_text += " month has the Highest Quality in " + year
        if content_text==None:
            content_text="Sorry, Please give valid information.        For Eg - Highest quality month in (year) ?"
        dispatcher.utter_message(text=content_text)
        return []

class Question4(Action):

    def name(self) -> Text:
        return "q4ans"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("Inside actions")
        import csv

        f = open("Sample.csv", 'r')
        csv_reader = csv.reader(f)

        user_message = str((tracker.latest_message)['text'])
        user_message = str((tracker.latest_message)['text'])
        year = None
        a = user_message.lower()
        sp = a.split()

        for i in sp:
            if "20" in i:
                if len(i)==4:
                    year = i
                else:
                    year = i[:4]
        content_text=None
        csv_reader = [i for i in csv_reader]
        dict = {}
        if year!=None:
            csv_reader = csv_reader[1:]
            for i in csv_reader:
                j = i[1]
                j = j.split('-')
                if year in j:
                    dict[float(i[3])] = j[1]
            f.close()
            l = [i for i in dict.keys()]
            content_text = dict[min(l)]
            content_text += " month has the Lowest Quality in " + year
        if content_text==None:
            content_text="Sorry, Please give valid information.        For Eg- Lowest quality month in (year) ?"
        dispatcher.utter_message(text=content_text)
        return []

class Question6(Action):

    def name(self) -> Text:
        return "q6ans"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("Inside actions")
        import csv

        f = open("Sample.csv", 'r')
        csv_reader = csv.reader(f)
        user_message = str((tracker.latest_message)['text'])
        month = None
        year = None
        a = user_message.lower()
        sp = a.split()
        for i in sp:
            if "jan" in i or "january" in i:
                month = "Jan"
            elif "feb" in i or "february" in i:
                month = "Feb"
            elif "mar" in i or "march" in i:
                month = "Mar"
            elif "apr" in i or "april" in i:
                month = "Apr"
            elif "may" in i:
                month = "May"
            elif "june" in i:
                month = "Jun"
            elif "july" in i:
                month = "Jul"
            elif "aug" in i or "august" in i:
                month = "Aug"
            elif "sept" in i or "september" in i:
                month = "Sep"
            elif "oct" in i or "october" in i:
                month = "Oct"
            elif "nov" in i or "november" in i:
                month = "Nov"
            elif "dec" in i or "december" in i:
                month = "Dec"
        for i in sp:
            if "20" in i:
                if len(i)==4:
                    year = i
                else:
                    year=i[:4]

        csv_reader = [i for i in csv_reader]
        dict = {}

        content_text=None
        csv_reader = csv_reader[1:]
        if month!= None and year!=None:
            for i in csv_reader:
                j = i[1]
                j = j.split('-')
                if month in j and year in j:
                    dict[float(i[3])] = i[2]
            l = [i for i in dict.keys()]
            if l[0] > l[1]:
                content_text=dict[l[0]]
            else:
                content_text=dict[l[1]]
            f.close()
            content_text += " Category was better in " + month + " " + year
        if content_text==None:
            content_text="Sorry, Please give valid information.        For Eg- Lowest quality month in (year) ?"
        dispatcher.utter_message(text=content_text)
        return []