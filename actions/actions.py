from typing import Text, Dict, List, Any

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from get import *

class GetBranchesAction(Action):
    def name(self) -> Text:
        return "action_get_branches"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Call your Python method here
        result = branches()
        for item in result:
            dispatcher.utter_message(text=item)

        # Use the dispatcher to send a message to the user
        # dispatcher.utter_message(text=result)

        return []

class Get_Branch_Action(Action):
    def name(self) -> Text:
        return "get_single_branch"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Call your Python method here
        result = get_branch()
        print(result)
        # for item in result:
        #     dispatcher.utter_message(text=item)

        # Use the dispatcher to send a message to the user
        dispatcher.utter_message(text=str(result))

        return []


class Get_Pipelines(Action):
    def name(self) -> Text:
        return "get_pipelines"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Call your Python method here
        result = get_pipelines()
        print(result)
        for item in result:
            for x in item:
                dispatcher.utter_message(text=str(x))
            dispatcher.utter_message(text="\n")
        # Use the dispatcher to send a message to the user

        return []

class Get_PipelineReport(Action):
    def name(self) -> Text:
        return "get_pipeline_report"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Call your Python method here
        result = get_pipeline_report()
        print(result)
        for item in result:
        #     for x in item:
        #         dispatcher.utter_message(text=str(x))
            dispatcher.utter_message(text=item)
        # Use the dispatcher to send a message to the user

        return []
    
    
class Get_PipelineJobs(Action):
    def name(self) -> Text:
        return "get_pipeline_jobs"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Call your Python method here
        result = get_pipeline_jobs()
        print(result)
        for item in result:
            for x in item:
                dispatcher.utter_message(text=str(x))
            dispatcher.utter_message(text="\n")
        # Use the dispatcher to send a message to the user

        return []
    
class Get_Commits(Action):
    def name(self) -> Text:
        return "get_commits"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Call your Python method here
        result = get_commits()
        print(result)
        for item in result:
            for x in item:
                dispatcher.utter_message(text=str(x))
            dispatcher.utter_message(text="\n")
        # Use the dispatcher to send a message to the user

        return []

