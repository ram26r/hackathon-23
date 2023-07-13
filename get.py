from typing import Text, Dict, List, Any

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

from APIGenerics import APIGenerics
from APIEnumsAndConstants import *
from GitAPIMethods import GitAPIMethods

def branches():
    # Get the necessary inputs from the tracker
    token = "sdp-3yqMtjss-sC61L1fT8RB"
    baseUrl = "https://gitlab.dx1.lseg.com/api/v4"
    projectId = "3544"

    # Create an instance of the GitAPIMethods class
    git_api = APIGenerics()

    # Call the getBranchesInProject method to retrieve the branches
    response = git_api.invoke_git_GetAPIs(baseUrl, token, APIUrlEnum.GetBranchesInProject, projectId)
    branch_response = git_api.get_values_from_branches(response, BranchResponseEnum.Name)
    print("response:", branch_response)
    return branch_response


def get_branch():
    # Get the necessary inputs from the tracker
    token = "sdp-3yqMtjss-sC61L1fT8RB"
    baseUrl = "https://gitlab.dx1.lseg.com/api/v4"
    projectId = "3544"

    # Create an instance of the GitAPIMethods class
    git_api = APIGenerics()

    # Call the getBranchesInProject method to retrieve the branches
    response = git_api.invoke_git_GetAPIs(baseUrl, token, APIUrlEnum.GetBranchById, projectId, "qa_automation_anjali")
    branch_response = git_api.get_value_from_branch(response, BranchResponseEnum.Merged)
    print("response:", branch_response)
    return branch_response


def get_pipelines():
    # Get the necessary inputs from the tracker
    token = "sdp-3yqMtjss-sC61L1fT8RB"
    baseUrl = "https://gitlab.dx1.lseg.com/api/v4"
    projectId = "3544"

    # Create an instance of the GitAPIMethods class
    git_api = APIGenerics()

    # Call the getBranchesInProject method to retrieve the branches
    response = git_api.invoke_git_GetAPIs(baseUrl, token, APIUrlEnum.GetPipelines, projectId)

    pipeline_response = git_api.get_multiple_values_from_response(response, GitVariables.ref, GitVariables.id, GitVariables.status)
    # print("response:", pipeline_response)
    # for item in pipeline_response:
    #
    #     for x in item:
    #         print(str(x))
    #     print("\n")
    return pipeline_response

def get_pipeline_report():
    # Get the necessary inputs from the tracker
    token = "sdp-3yqMtjss-sC61L1fT8RB"
    baseUrl = "https://gitlab.dx1.lseg.com/api/v4"
    projectId = "3544"
    pipelineId = ""

    # Create an instance of the GitAPIMethods class
    git_api = APIGenerics()
    # Call the getBranchesInProject method to retrieve the branches
    response = git_api.invoke_git_GetAPIs(baseUrl, token, APIUrlEnum.GetPipelineReport, projectId, pipelineId)
    pipeline_response = git_api.get_multiple_values_from_response(response, GitVariables.total_time,
                                                                  GitVariables.total_count, GitVariables.success_count,
                                                                  GitVariables.failed_count, GitVariables.error_count,
                                                                  GitVariables.skipped_count)
    # print("response:", pipeline_response)
    return pipeline_response


def get_pipeline_jobs():
    # Get the necessary inputs from the tracker
    token = "sdp-3yqMtjss-sC61L1fT8RB"
    baseUrl = "https://gitlab.dx1.lseg.com/api/v4"
    projectId = "3544"
    pipelineId = ""

    # Create an instance of the GitAPIMethods class
    git_api = APIGenerics()
    # Call the getBranchesInProject method to retrieve the branches
    response = git_api.invoke_git_GetAPIs(baseUrl, token, APIUrlEnum.GetPipelineJobs, projectId, pipelineId)
    pipeline_response = git_api.get_multiple_values_from_response(response, GitVariables.id, GitVariables.name,
                                                                  GitVariables.ref, GitVariables.status)
    # print("response:", pipeline_response)
    return pipeline_response


def get_commits():
    # Get the necessary inputs from the tracker
    token = "sdp-3yqMtjss-sC61L1fT8RB"
    baseUrl = "https://gitlab.dx1.lseg.com/api/v4"
    projectId = "3544"

    # Create an instance of the GitAPIMethods class
    git_api = APIGenerics()
    # Call the getBranchesInProject method to retrieve the branches
    response = git_api.invoke_git_GetAPIs(baseUrl, token, APIUrlEnum.GetRepositoryCommits, projectId)
    pipeline_response = git_api.get_multiple_values_from_response(response, GitVariables.id, GitVariables.title,
                                                                  GitVariables.committer_name, GitVariables.committer_email)

    # print("response:", pipeline_response)
    return pipeline_response

# branches()
# get_branch()
# get_pipelines()


































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
