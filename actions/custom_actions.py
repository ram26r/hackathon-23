import subprocess
from typing import Text, Dict, List, Any

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from urllib3.util import url

from APIGenerics import APIGenerics
from APIEnumsAndConstants import *
from GitAPIMethods import GitAPIMethods

class GetBranchesAction(Action):
    # def name(self) -> Text:
    #     return "action_get_branches"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> str | list[Any]:
        # Get the necessary inputs from the tracker
        token = tracker.get_slot("git_token")
        baseUrl = tracker.get_slot("git_base_url")
        projectId = tracker.get_slot("git_project_id")

        curl_command = ['curl', baseUrl]

        if token:
            curl_command.extend(['-H', f'Authorization: Bearer {token}'])

        result = subprocess.run(curl_command, capture_output=True, text=True)

        # return result.stdout
        # Process the response and send the necessary messages to the user using the dispatcher
        # Example response processing:
        if result:
             message = "The branches in the project are: " + f"Response: {result.stdout}"
            # branches = result["branches"]  # Assuming the response contains a "branches" field
            # if branches:
            #     message = "The branches in the project are: " + ", ".join(branches)
            # else:
            #     message = "No branches found in the project."
        else:
            message = "Error occurred while retrieving branches."

        dispatcher.utter_message(text=message)

        return []
