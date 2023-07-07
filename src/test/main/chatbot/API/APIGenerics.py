import requests
from APIEnumsAndConstants import *


class APIGenerics:
    '''This method is a generic template to send GET request and return the response'''
    def invoke_git_GetAPIs(self, baseUrl, token, methodEnum, *args):
        try:
            match methodEnum:
                case APIUrlEnum.GetBranchesInProject:
                    url = APIGenerics.construct_url(self, baseUrl, GitVariables.branches, *args)

                case APIUrlEnum.GetBranchById:
                    url = APIGenerics.construct_url(self, baseUrl, GitVariables.branch, *args)

                case APIUrlEnum.GetRepositoryCommits:
                    url = APIGenerics.construct_url(self,baseUrl, GitVariables.commits, *args)

                case APIUrlEnum.GetCommitById:
                    url = APIGenerics.construct_url(self,baseUrl, GitVariables.commit, *args)

                case APIUrlEnum.GetCommitReferences:
                    url = APIGenerics.construct_url(self,baseUrl, GitVariables.references, *args)

                case APIUrlEnum.GetJobs:
                    url = APIGenerics.construct_url(self,baseUrl, GitVariables.projectJobs, *args)

                case APIUrlEnum.GetPipelineJobs:
                    url = APIGenerics.construct_url(self,baseUrl, GitVariables.pipelineJobs, *args)

                case APIUrlEnum.GetPipelineTriggerJobs:
                    url = APIGenerics.construct_url(self,baseUrl, GitVariables.pipeTriggerJobs, *args)

                case APIUrlEnum.GetJobById:
                    url = APIGenerics.construct_url(self,baseUrl, GitVariables.job, *args)

                case APIUrlEnum.GetJobFileById:
                    url = APIGenerics.construct_url(self,baseUrl, GitVariables.jobLogFile, *args)

                case APIUrlEnum.GetJobArtifacts:
                    url = APIGenerics.construct_url(self,baseUrl, GitVariables.jobArtifacts, *args)

                case APIUrlEnum.GetMergeRequests:
                    url = APIGenerics.construct_url(self,baseUrl, GitVariables.projectMergeRequests, *args)

                case APIUrlEnum.GetMergeRequestsWithFilter:
                    url = APIGenerics.construct_url(self,baseUrl, GitVariables.projectMergeRequests, *args)

                case APIUrlEnum.GetPipelines:
                    url = APIGenerics.construct_url(self,baseUrl, GitVariables.pipelines, *args)

                case APIUrlEnum.GetPipelineById:
                    url = APIGenerics.construct_url(self,baseUrl, GitVariables.pipeline, *args)

                case APIUrlEnum.GetPipelineReport:
                    url = APIGenerics.construct_url(self,baseUrl, GitVariables.pipelineTestReport, *args)

                case APIUrlEnum.GetPipelineReportSummary:
                    url = APIGenerics.construct_url(self,baseUrl, GitVariables.pipeTestReportSummary, *args)

                case APIUrlEnum.GetLatestPipeline:
                    url = APIGenerics.construct_url(self,baseUrl, GitVariables.pipelineLatest, *args)

                case APIUrlEnum.GetGroupMembers:
                    url = APIGenerics.construct_url(self,baseUrl, GitVariables.groupMembers, *args)

                case APIUrlEnum.GetProjectMembers:
                    url = APIGenerics.construct_url(self,baseUrl, GitVariables.projectMembers, *args)

                case APIUrlEnum.GetDownloadArtifacts:
                    url = APIGenerics.construct_url(self,baseUrl, GitVariables.downloadArtifactsArchive, *args)

                case APIUrlEnum.GetDownloadArtifactByJobId:
                    url = APIGenerics.construct_url(self,baseUrl, GitVariables.downloadArtifactByJobId, *args)

                case APIUrlEnum.GetDownloadArtifactByBranchId:
                    url = APIGenerics.construct_url(self,baseUrl, GitVariables.downloadArtifactByBranchId, *args)

            return APIGenerics.genericTemplate_InvokingGETAPI(self, url, token)
        except:
            return GitVariables.err_msg_git_codeError

    '''This method is a generic template to send GET request and return the response'''
    def genericTemplate_InvokingGETAPI(self, url, token, to_json=True):
        try:
            headers = APIGenerics.construct_headers(self, token)
            resp = APIGenerics.invoke_GETAPIs(self, url, headers)
            if resp.status_code == StatusCodeEnum.SUCCESS_OK.value:
                return APIGenerics.convert_to_json(self, resp) if to_json else resp
            else:
                return APIGenerics.return_generic_error_msg(self, resp.status_code)
        except:
            return GitVariables.err_msg_git_codeError

    '''This method is to send GET request and return the response'''
    def invoke_GETAPIs(self, url, headers):
        resp = requests.get(url=url, headers=headers)
        return resp

    '''This method is to construct url with the parameters to be added in url Ex:id -- /values/2'''
    def construct_url(self,url, endpoint, *arr):
        temp = url + endpoint
        if len(arr) > 0:
            temp = temp.format(*arr)
            return temp

    '''This method is to send POST request and return the response'''
    def invoke_POSTAPIs(self, url, headers, req_body):
        resp = requests.post(url=url, headers=headers, data=req_body)
        return resp

    '''This method is to add token as key-value pair'''
    def construct_headers(self, token):
        return {'Authorization': 'Bearer ' + token + ''}

    '''This method is to return generic template of error message based on the status code'''
    def return_generic_error_msg(self, statusCode):
        if statusCode == StatusCodeEnum.UNAUTHORIZED.value:
            return GitVariables.err_msg_git_unauthorized
        elif statusCode == StatusCodeEnum.BAD_REQUEST.value:
            return GitVariables.err_msg_git_badRequest
        elif statusCode == StatusCodeEnum.SERVER_ERROR.value:
            return GitVariables.err_msg_git_backend
        elif statusCode == StatusCodeEnum.NOT_FOUND.value:
            return GitVariables.err_msg_git_notFound
        else:
            return GitVariables.err_msg_git_generic

    '''This method is to convert the response to json format'''
    def convert_to_json(self, resp):
        try:
            return resp.json()
        except:
            return None

    '''This method is to extract the count from response , it will return the count of parent list'''
    def get_count(self, resp):
        return len(resp)

    '''This method is to extract the branches name from response'''
    def get_branches_name(self, resp):
        return APIGenerics.get_values_from_response(self, resp, GitVariables.name)

    '''This method is to extract the value of the field name in each index from response.'''
    def get_values_from_response(self, resp, field_name):
        list1 = list()
        try:
            for x in resp:
                list1.append(x.get(field_name))
            return list1
        except:
            return list1 if len(list1) > 0 else None

    '''This method is to extract the value of the field name in first index from response'''
    def get_value_from_response(self, resp, field_name):
        return resp.get(field_name)

    '''This method is to extract the value of the field name from commits response based on the Enum passed'''
    def get_values_from_commits(self, resp, commitsEnum):
        field=""
        try:
            match commitsEnum:
                case CommitResponseEnum.Id:
                    field=GitVariables.id
                case CommitResponseEnum.WebUrl:
                    field = GitVariables.web_url
                case CommitResponseEnum.CommittedDate:
                    field = GitVariables.committed_date
                case CommitResponseEnum.CommitterEmail:
                    field = GitVariables.committer_email
                case CommitResponseEnum.CommitterName:
                    field=GitVariables.committer_name
                case CommitResponseEnum.AuthoredDate:
                    field = GitVariables.authored_date
                case CommitResponseEnum.AuthorEmail:
                    field = GitVariables.author_email
                case CommitResponseEnum.AuthorName:
                    field = GitVariables.author_name
                case CommitResponseEnum.Title:
                    field = GitVariables.title
                case CommitResponseEnum.CreatedAt:
                    field = GitVariables.created_at
            return APIGenerics.get_values_from_response(self, resp, field)
        except:
            return GitVariables.err_msg_git_codeError

    '''This method is to extract the value of the field name from commits response based on the Enum passed'''
    def get_value_from_single_commit(self, resp, commitsEnum):
        field = ""
        try:
            match commitsEnum:
                case CommitResponseEnum.Id:
                    field = GitVariables.id
                case CommitResponseEnum.WebUrl:
                    field = GitVariables.web_url
                case CommitResponseEnum.CommittedDate:
                    field = GitVariables.committed_date
                case CommitResponseEnum.CommitterEmail:
                    field = GitVariables.committer_email
                case CommitResponseEnum.CommitterName:
                    field = GitVariables.committer_name
                case CommitResponseEnum.AuthoredDate:
                    field = GitVariables.authored_date
                case CommitResponseEnum.AuthorEmail:
                    field = GitVariables.author_email
                case CommitResponseEnum.AuthorName:
                    field = GitVariables.author_name
                case CommitResponseEnum.Title:
                    field = GitVariables.title
                case CommitResponseEnum.CreatedAt:
                    field = GitVariables.created_at
            return APIGenerics.get_value_from_response(self, resp, field)
        except:
            return GitVariables.err_msg_git_codeError

    '''This method is to extract the value of the field name from branch response based on the Enum passed'''
    def get_value_from_branch(self, resp, branchEnum):
        field = ""
        try:
            match branchEnum:
                case BranchResponseEnum.Name:
                    field = GitVariables.name
                case BranchResponseEnum.Merged:
                    field = GitVariables.merged
                case BranchResponseEnum.Protected:
                    field = GitVariables.protected
                case BranchResponseEnum.Default:
                    field = GitVariables.default
                case BranchResponseEnum.Can_Push:
                    field = GitVariables.can_push
                case BranchResponseEnum.WebUrl:
                    field = GitVariables.web_url
            return APIGenerics.get_value_from_response(self, resp, field)
        except:
            return GitVariables.err_msg_git_codeError

    '''This method is to extract the values of the field name from branches response based on the Enum passed'''
    def get_values_from_branches(self, resp, branchEnum):
        field = ""
        try:
            match branchEnum:
                case BranchResponseEnum.Name:
                    field = GitVariables.name
                case BranchResponseEnum.Merged:
                    field = GitVariables.merged
                case BranchResponseEnum.Protected:
                    field = GitVariables.protected
                case BranchResponseEnum.Default:
                    field = GitVariables.default
                case BranchResponseEnum.Can_Push:
                    field = GitVariables.can_push
                case BranchResponseEnum.WebUrl:
                    field = GitVariables.web_url
            return APIGenerics.get_values_from_response(self, resp, field)
        except:
            return GitVariables.err_msg_git_codeError

    '''This method is to extract the values of the field name from pipelines response based on the Enum passed'''
    def get_values_from_pipelines(self, resp, pipeEnum):
        field = ""
        try:
            match pipeEnum:
                case PipelineResponseEnum.Id:
                    field = GitVariables.id
                case PipelineResponseEnum.Iid:
                    field = GitVariables.iid
                case PipelineResponseEnum.ProjectId:
                    field = GitVariables.project_id
                case PipelineResponseEnum.Status:
                    field = GitVariables.status
                case PipelineResponseEnum.Source:
                    field = GitVariables.source
                case PipelineResponseEnum.Ref:
                    field = GitVariables.ref
                case PipelineResponseEnum.Sha:
                    field = GitVariables.sha
                case PipelineResponseEnum.Name:
                    field = GitVariables.name
                case PipelineResponseEnum.WebUrl:
                    field = GitVariables.web_url
                case PipelineResponseEnum.CreatedAt:
                    field = GitVariables.created_at
                case PipelineResponseEnum.UpdatedAt:
                    field = GitVariables.updated_at
            return APIGenerics.get_values_from_response(self, resp, field)
        except:
            return GitVariables.err_msg_git_codeError

    '''This method is to extract the values of the field name from pipeline test report  based on the Enum passed'''
    def get_from_pipe_test_report(self, resp, pipeEnum):
        field = ""
        try:
            match pipeEnum:
                case PipeTestReportEnum.TotalTime:
                    field = GitVariables.total_time
                case PipeTestReportEnum.TotalCount:
                    field = GitVariables.total_count
                case PipeTestReportEnum.SuccessCount:
                    field = GitVariables.success_count
                case PipeTestReportEnum.FailedCount:
                    field = GitVariables.failed_count
                case PipeTestReportEnum.SkippedCount:
                    field = GitVariables.skipped_count
                case PipeTestReportEnum.ErrorCount:
                    field = GitVariables.error_count
            return APIGenerics.get_value_from_response(self, resp, field)
        except:
            return GitVariables.err_msg_git_codeError

    '''This method is to extract the values of the field name from pipe test summary based on the Enum passed'''
    def get_from_pipe_test_report_sum(self, resp, pipeEnum):
        field = ""
        try:
            temp_res = resp.get(GitVariables.total)
            match pipeEnum:
                case PipeTestReportSumEnum.Time:
                    field = GitVariables.time
                case PipeTestReportSumEnum.Count:
                    field = GitVariables.count
                case PipeTestReportSumEnum.Success:
                    field = GitVariables.success
                case PipeTestReportSumEnum.Failed:
                    field = GitVariables.failed
                case PipeTestReportSumEnum.Skipped:
                    field = GitVariables.skipped
                case PipeTestReportSumEnum.Error:
                    field = GitVariables.error
                case PipeTestReportSumEnum.SuiteError:
                    field = GitVariables.suite_error
            return APIGenerics.get_value_from_response(self, temp_res, field)
        except:
            return GitVariables.err_msg_git_codeError

