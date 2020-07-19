
# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"


from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import UserUtteranceReverted
import re 

def redirectToSlot(slot, value, dispatcher, tracker, remapping):
    response = {slot: value} # default response

    if (slot == "school"):
        regex = r'^[#.0-9a-zA-Z\s,-]+$'
        if(re.search(regex, value)):
            response = {slot: value}
        else:
            dispatcher.utter_message(template="utter_wrong_school")
            response = {slot: None}
    elif (slot == "mailid"):
        regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        print("red", slot, value)
        if(re.search(regex, value)):
            response = {slot: value}
        else:
            dispatcher.utter_message(template="utter_wrong_emailid")
            response = {slot: None}
    elif (slot == "phone_number"):
        if len(value) == 10:
            if(value.isdigit()):
                response = {slot: value}
            else:
                response = {slot: None}  
                dispatcher.utter_message(template="utter_wrong_phonenumberalpha")                
        else:
            response = {slot: None}  
            dispatcher.utter_message(template="utter_wrong_phonenumber")

    if (type(remapping) == str):
        response[remapping] = None

    return response

class StudentInfoForm(FormAction):
    """Collects student information"""

    def name(self):
        return "info_form"
    @staticmethod
    def required_slots(tracker):
        return [
            "username",
            "mailid",
            "phone_number",
            "school",
            ]
        
    def validate_phone_number(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
     ) -> Dict[Text, Any]:
        """Validate phone."""
        value=tracker.get_slot("phone_number")

        print("validate_phone_number() method  ", value)

        requestedSlot = tracker.get_last_event_for("slot", skip=1)
        if (requestedSlot['name'] == 'requested_slot' and requestedSlot['value']):
            if (requestedSlot['value'] == 'phone_number'): # If requested slot was phone_number and value also corresponds to the phone_number 
                return redirectToSlot(requestedSlot['value'], value, dispatcher, tracker, None)
            else: # If value corresponds to the wrong slot
                return redirectToSlot(requestedSlot['value'], value, dispatcher, tracker, 'phone_number')
        else:
            return redirectToSlot('phone_number', value, dispatcher, tracker, None)

    def validate_mailid(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
     ) -> Dict[Text, Any]:
        """Validate mailid."""
        value=tracker.get_slot("mailid")

        print("validate_mailid() method  ", value)

        requestedSlot = tracker.get_last_event_for("slot", skip=1)
        if (requestedSlot['name'] == 'requested_slot' and requestedSlot['value']):
            if (requestedSlot['value'] == 'mailid'): # If requested slot was mailid and value also corresponds to the mailid 
                return redirectToSlot(requestedSlot['value'], value, dispatcher, tracker, None)
            else: # If value corresponds to the wrong slot
                return redirectToSlot(requestedSlot['value'], value, dispatcher, tracker, 'mailid')
        else:
            return redirectToSlot('mailid', value, dispatcher, tracker, None)

    def validate_username(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
     ) -> Dict[Text, Any]:
        """Validate username."""
        value=tracker.get_slot("username")

        print("validate_username() method", value)

        requestedSlot = tracker.get_last_event_for("slot", skip=1)
        if (requestedSlot['name'] == 'requested_slot' and requestedSlot['value']):
            if (requestedSlot['value'] == 'username'): # If requested slot was username and value also corresponds to the username 
                return redirectToSlot(requestedSlot['value'], value, dispatcher, tracker, None)
            else: # If value corresponds to the wrong slot
                return redirectToSlot(requestedSlot['value'], value, dispatcher, tracker, 'username')
        else:
            return redirectToSlot('username', value, dispatcher, tracker, None)

    def validate_school(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
     ) -> Dict[Text, Any]:
        """Validate school."""
        value=tracker.get_slot("school")

        print("validate_school() method", value)

        requestedSlot = tracker.get_last_event_for("slot", skip=1)
        if (requestedSlot['name'] == 'requested_slot' and requestedSlot['value']):
            if (requestedSlot['value'] == 'school'): # If requested slot was school and value also corresponds to the school 
                return redirectToSlot(requestedSlot['value'], value, dispatcher, tracker, None)
            else: # If value corresponds to the wrong slot
                return redirectToSlot(requestedSlot['value'], value, dispatcher, tracker, 'school')
        else:
            return redirectToSlot('school', value, dispatcher, tracker, None)


    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        username = tracker.get_slot("username")
        mailid = tracker.get_slot("mailid")
        phone_number=tracker.get_slot("phone_number")
        school=tracker.get_slot("school")
        message="REGISTRATION DETAILS:"+"\n\n"+"Name:"+username+"\n"+"Email:"+mailid+"\n"+"Phone Number:"+phone_number+"\n"+"School:"+school+"\nThanks! for sharing the information."
        saveFile = open("some.txt", 'a')
        saveFile.write(message)
        saveFile.close()
        dispatcher.utter_message(message)
        return []
        
class ShowCoursesForm(FormAction):
    def name(self):
        return "show_courses_form"

    @staticmethod
    def required_slots(tracker):
        return [
            "board",
            "standard",
            "subject",
            "portion",
            ]

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        board = tracker.get_slot("board")
        standard = tracker.get_slot("standard")
        subject=tracker.get_slot("subject")
        chapter=tracker.get_slot("portion")
        output="All done! Click on the given link it will direct you to the course page: https://example.com/signup?board={}&class={}&subject={}&chapter={}".format(board,standard,subject,chapter)
        dispatcher.utter_message(output) 
        return []

class ActionPaymentConfirmed(Action):
    def name(self):
        return "action_payment_done"
    def run(self,dispatcher,tracker,domain):
        output="Have a great learning ahead with MissionED.You will be getting the dashboard access within 24 hrs."
        dispatcher.utter_message(output)
        return [UserUtteranceReverted()]
    
class AsktheBot(Action):
    def name(self):
        return "action_ask_bot"
    def run(self,dispatcher,tracker,domain):
        output="1. Registration:\n I can help you to register to MissionEd, so that you get updates about our new courses.(Eg: How can i register on MissionEd?) \n2. Enrollment: \nI can help you to enroll in a course. We have both paid and free courses.(Eg: How to enroll in a course?) \n3. Payment: \nI can help you with payment.(Eg: How to make the payment?) \n4. Pricing: \nI can help you to know the price of different courses.(Eg: Tell me about the prices.) \n5. Course:\n I can help you to find the suitable course for you.(Can I get a course list?)\n6. Doubt sessions: \nI can provide you all the information about the doubt sessions, also provide notes and other study material according to your requirements.(Eg: when will the doubt clearing session be?)"
        dispatcher.utter_message(output)
        return [UserUtteranceReverted()]
