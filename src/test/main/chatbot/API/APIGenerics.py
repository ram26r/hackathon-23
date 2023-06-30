from lib2to3.pytree import convert
import requests
from APIEnumsAndConstants import *

class APIGenerics:
    '''This method is a generic template to send GET request and return the response'''
    def invoke_git_GetAPIs(self,baseUrl,token,methodEnum,*args):
        try:
            match methodEnum:
                case APIUrlEnum.GetBranchesInProject:
                    url = APIGenerics.construct_url(baseUrl,GitVariables.branches,*args)

                case APIUrlEnum.GetBranchById:
                     url = APIGenerics.construct_url(baseUrl,GitVariables.branch,*args)

                case APIUrlEnum.GetRepositoryCommits:
                    url = APIGenerics.construct_url(baseUrl,GitVariables.commits,*args)

                case APIUrlEnum.GetCommitById:
                    url = APIGenerics.construct_url(baseUrl,GitVariables.commit,*args)

                case APIUrlEnum.GetCommitReferences:
                    url = APIGenerics.construct_url(baseUrl,GitVariables.references,*args)

                case APIUrlEnum.GetJobs:
                    url = APIGenerics.construct_url(baseUrl,GitVariables.projectJobs,*args)

                case APIUrlEnum.GetPipelineJobs:
                    url = APIGenerics.construct_url(baseUrl,GitVariables.pipelineJobs,*args)

                case APIUrlEnum.GetPipelineTriggerJobs:
                    url = APIGenerics.construct_url(baseUrl,GitVariables.pipeTriggerJobs,*args)

                case APIUrlEnum.GetJobById:
                    url = APIGenerics.construct_url(baseUrl,GitVariables.job,*args)

                case APIUrlEnum.GetJobFileById:
                    url = APIGenerics.construct_url(baseUrl,GitVariables.jobLogFile,*args)

                case APIUrlEnum.GetJobArtifacts:
                    url = APIGenerics.construct_url(baseUrl,GitVariables.jobArtifacts,*args)

                case APIUrlEnum.GetMergeRequests:
                    url = APIGenerics.construct_url(baseUrl,GitVariables.projectMergeRequests,*args)

                case APIUrlEnum.GetMergeRequestsWithFilter:
                    url = APIGenerics.construct_url(baseUrl,GitVariables.projectMergeRequests,*args)

                case APIUrlEnum.GetPipelines:
                    url = APIGenerics.construct_url(baseUrl,GitVariables.pipelines,*args)

                case APIUrlEnum.GetPipelineById:
                    url = APIGenerics.construct_url(baseUrl,GitVariables.pipeline,*args)

                case APIUrlEnum.GetPipelineReport:
                    url = APIGenerics.construct_url(baseUrl,GitVariables.pipelineTestReport,*args)

                case APIUrlEnum.GetPipelineReportSummary:
                    url = APIGenerics.construct_url(baseUrl,GitVariables.pipeTestReportSummary,*args)

                case APIUrlEnum.GetLatestPipeline:
                    url = APIGenerics.construct_url(baseUrl,GitVariables.pipelineLatest,*args)

                case APIUrlEnum.GetGroupMembers:
                    url = APIGenerics.construct_url(baseUrl,GitVariables.groupMembers,*args)

                case APIUrlEnum.GetProjectMembers:
                    url = APIGenerics.construct_url(baseUrl,GitVariables.projectMembers,*args)

                case APIUrlEnum.GetDownloadArtifacts:
                    url = APIGenerics.construct_url(baseUrl,GitVariables.downloadArtifactsArchive,*args)

                case APIUrlEnum.GetDownloadArtifactByJobId:
                    url = APIGenerics.construct_url(baseUrl,GitVariables.downloadArtifactByJobId,*args)

                case APIUrlEnum.GetDownloadArtifactByBranchId:
                    url = APIGenerics.construct_url(baseUrl,GitVariables.downloadArtifactByBranchId,*args)

            return APIGenerics.genericTemplate_InvokingGETAPI(url,token)
        except:
            return GitVariables.err_msg_git_codeError

            
        

    '''This method is a generic template to send GET request and return the response'''
    def genericTemplate_InvokingGETAPI(url,token,toJson=True):
        try:
            headers = APIGenerics.construct_headers(token)
            resp = APIGenerics.invoke_GETAPIs(url,headers)
            if(resp.status_code==StatusCodeEnum.SUCCESS_OK.value):
                return APIGenerics.convert_to_json(resp) if toJson else resp
            else:
                return APIGenerics.return_generic_error_msg(resp.status_code)
        except:
            return GitVariables.err_msg_git_codeError

    '''This method is to send GET request and return the response'''
    def invoke_GETAPIs(url,headers):
        resp = requests.get(url=url,headers=headers)
        return resp

    '''This method is to construct url with the parameters to be added in url Ex:id -- /values/2'''
    def construct_url(url,endpoint,*arr):
        temp = url + endpoint
        if(len(arr)>0):
            temp = temp.format(*arr)
            return temp

    '''This method is to send POST request and return the response'''
    def invoke_POSTAPIs(url,headers,reqBody):
        resp = requests.post(url=url,headers=headers,data=reqBody)
        return resp

    '''This method is to add token as key-value pair'''
    def construct_headers(token):
        return {'Authorization':'Bearer '+token+''}

    '''This method is to return generic template of error message based on the status code'''
    def return_generic_error_msg(statusCode):
        if(statusCode == StatusCodeEnum.UNAUTHORIZED.value):
            return GitVariables.err_msg_git_unauthorized
        elif(statusCode == StatusCodeEnum.BAD_REQUEST.value):
            return GitVariables.err_msg_git_badRequest
        elif(statusCode == StatusCodeEnum.SERVER_ERROR.value):
            return GitVariables.err_msg_git_backend
        elif(statusCode == StatusCodeEnum.NOT_FOUND.value):
            return GitVariables.err_msg_git_notFound
        else:
            return GitVariables.err_msg_git_generic

    '''This method is to convert the response to json format'''
    def convert_to_json(resp):
        try:
            return resp.json()
        except:
            return None

    '''This method is to extract the count from response , it will return the count of parent list'''
    def get_count(resp):
        return len(resp)

    '''This method is to extract the branches name from response'''
    def get_branches_name(resp):
       return APIGenerics.get_values_from_response(resp,GitVariables.name)

    '''This method is to extract the value of the fieldname in each index from response.'''
    def get_values_from_response(resp,fieldName):
        list1=list()
        try:
            for x in resp:
                list1.append(resp.get(fieldName))
        except:
            list1 if list1.count>0 else None

    '''This method is to extract the value of the fieldname in first index from response'''
    def get_value_from_response(resp,fieldName):
        value=APIGenerics.get_values_from_response(resp,fieldName)
        return value[0] if value!=None else None

    '''This method is to extract the value of the fieldname in first index from response'''
    def get_id_from_commits(resp):
        return APIGenerics.get_values_from_response(resp,GitVariables.id)

    '''This method is to extract the value of the fieldname in first index from response'''
    def get_web_url_from_commits(resp):
        return APIGenerics.get_values_from_response(resp,GitVariables.web_url)

    '''This method is to extract the value of the fieldname in first index from response'''
    def get_committed_date_from_commits(resp):
        return APIGenerics.get_values_from_response(resp,GitVariables.committed_date)

    '''This method is to extract the value of the fieldname in first index from response'''
    def get_committer_email_from_commits(resp):
        return APIGenerics.get_values_from_response(resp,GitVariables.committer_email)

    '''This method is to extract the value of the fieldname in first index from response'''
    def get_committer_name_from_commits(resp):
        return APIGenerics.get_values_from_response(resp,GitVariables.committer_name)

    '''This method is to extract the value of the fieldname in first index from response'''
    def get_authored_date_from_commits(resp):
        return APIGenerics.get_values_from_response(resp,GitVariables.authored_date)

    '''This method is to extract the value of the fieldname in first index from response'''
    def get_author_email_from_commits(resp):
        return APIGenerics.get_values_from_response(resp,GitVariables.author_email)

    '''This method is to extract the value of the fieldname in first index from response'''
    def get_author_name_from_commits(resp):
        return APIGenerics.get_values_from_response(resp,GitVariables.author_name)

    '''This method is to extract the value of the fieldname in first index from response'''
    def get_title_from_commits(resp):
        return APIGenerics.get_values_from_response(resp,GitVariables.title)

    '''This method is to extract the value of the fieldname in first index from response'''
    def get_created_at_from_commits(resp):
        return APIGenerics.get_values_from_response(resp,GitVariables.created_at)



    


      




