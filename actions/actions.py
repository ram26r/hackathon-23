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

        # Debugging: Print user message and extracted entities
        print("User message:", tracker.latest_message['text'])
        # print("Extracted entities:", tracker.latest_message['entities'])
        branch_name_entity = tracker.get_slot('get_provided_branch')

        # Extract the branch name entity from the user message
        # branch_name_entity = next(tracker.get_latest_entity_values("branch_name"), None)
        # print(branch_name_entity)

        if branch_name_entity:
            # Call your Python method here with the extracted branch_name_entity
            result = get_branch(branch_name_entity)
            print(result)
            dispatcher.utter_message(text=str(result))
        else:
            dispatcher.utter_message(text="Please provide a branch name.")

        return []

        # # Call your Python method here
        # result = get_branch()
        # print(result)
        # # for item in result:
        # #     dispatcher.utter_message(text=item)
        #
        # # Use the dispatcher to send a message to the user
        # dispatcher.utter_message(text=str(result))
        #
        # return []


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

class Get_Job_Report(Action):
    def name(self) -> Text:
        return "get_job_report"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Call your Python method here
        result = get_jobs_artifact_file()
        print(result)
        dispatcher.utter_message(image=result)

        return []

