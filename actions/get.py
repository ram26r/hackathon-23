from typing import Text, Dict, List, Any

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

from APIGenerics import APIGenerics
from APIEnumsAndConstants import *
from GitAPIMethods import GitAPIMethods

class GetBranchesAction(Action):
    def name(self) -> Text:
        return "action_get_branches"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Get the necessary inputs from the tracker
        token = tracker.get_slot("sdp-3yqMtjss-sC61L1fT8RB")
        baseUrl = tracker.get_slot("https://gitlab.dx1.lseg.com")
        projectId = tracker.get_slot("3544")

        # Create an instance of the GitAPIMethods class
        git_api = GitAPIMethods()

        # Call the getBranchesInProject method to retrieve the branches
        response = git_api.getBranchesInProject(token, baseUrl, projectId)

        # Process the response and send the necessary messages to the user using the dispatcher
        # Example response processing:
        if response:
            branches = response["branches"]  # Assuming the response contains a "branches" field
            if branches:
                message = "The branches in the project are: " + ", ".join(branches)
            else:
                message = "No branches found in the project."
        else:
            message = "Error occurred while retrieving branches."

        dispatcher.utter_message(text=message)

        return []



























# from typing import Text, Dict, List, Any
#
# import self as self
# from rasa_sdk import Action, Tracker
# from rasa_sdk.events import SlotSet
# from rasa_sdk.executor import CollectingDispatcher
#
# from APIGenerics import APIGenerics
# from APIEnumsAndConstants import *
# from GitAPIMethods import GitAPIMethods
#
#
# def run(token, baseUrl, projectId):
#     # Get the necessary inputs from the tracker
#     # print(token, baseUrl, projectId)
#
#     # Create an instance of the GitAPIMethods class
#     # git_api = GitAPIMethods()
#
#     # Call the getBranchesInProject method to retrieve the branches
#     response = GitAPIMethods.getBranchesInProject(token, baseUrl, projectId)
#     return response
#
#     # Process the response and send the necessary messages to the user using the dispatcher
#     # Example response processing:
#     # if response:
#     #     branches = response["branches"]  # Assuming the response contains a "branches" field
#     #     if branches:
#     #         message = "The branches in the project are: " + ", ".join(branches)
#     #         print(message)
#     #     else:
#     #         print('No branches found in the project.')
#     #         message = "No branches found in the project."
#     # else:
#     #     print("Error occurred while retrieving branches.")
#     #     message = "Error occurred while retrieving branches."
#
#
# token = "sdp-3yqMtjss-sC61L1fT8RB"
# baseUrl = "https://gitlab.dx1.lseg.com"
# projectId = "3544"
#
# response1 = run(token, baseUrl, projectId)
# print(response1)
