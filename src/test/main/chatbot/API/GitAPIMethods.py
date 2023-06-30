import requests
from APIGenerics import APIGenerics
from APIEnumsAndConstants import *


class GitAPIMethods:
    '''This method is to get all branches in a project'''
    def getBranchesInProject(self,token,baseUrl,projectId):
        url = APIGenerics.construct_url(baseUrl,branches,projectId)
        APIGenerics.genericTemplate_InvokingGETAPI(url,token)
       

    '''This method is to get a branch by id'''
    def getBranchById(self,token,baseUrl,projectId,branchId):
        url = APIGenerics.construct_url(baseUrl,branch,projectId,branchId)
        APIGenerics.genericTemplate_InvokingGETAPI(url,token)


    '''This method is to get all commits in a project'''
    def getRepositoryCommits(self,token,baseUrl,projectId):
        url = APIGenerics.construct_url(baseUrl,commits,projectId)
        APIGenerics.genericTemplate_InvokingGETAPI(url,token)


    '''This method is to get a commit details'''
    def getCommitById(self,token,baseUrl,projectId,commitId):
        url = APIGenerics.construct_url(baseUrl,commit,projectId,commitId)
        APIGenerics.genericTemplate_InvokingGETAPI(url,token)


    '''This method is to get references of a commit'''
    def getCommitReferences(self,token,baseUrl,projectId,commitId):
        url = APIGenerics.construct_url(baseUrl,references,projectId,commitId)
        APIGenerics.genericTemplate_InvokingGETAPI(url,token)

    '''This method is to get jobs'''
    def getJobs(self,token,baseUrl,projectId):
        url = APIGenerics.construct_url(baseUrl,projectJobs,projectId)
        APIGenerics.genericTemplate_InvokingGETAPI(url,token)

    '''This method is to get pipeline jobs'''
    def getPipelineJobs(self,token,baseUrl,projectId,pipelineId):
        url = APIGenerics.construct_url(baseUrl,pipelineJobs,projectId,pipelineId)
        APIGenerics.genericTemplate_InvokingGETAPI(url,token)

    '''This method is to get pipeline trigger jobs'''
    def getPipelineTriggerJobs(self,token,baseUrl,projectId,pipelineId):
        url = APIGenerics.construct_url(baseUrl,pipeTriggerJobs,projectId,pipelineId)
        APIGenerics.genericTemplate_InvokingGETAPI(url,token)

    '''This method is to get job artifacts'''
    def getJobArtifacts(self,token,baseUrl,projectId,jobId):
        url = APIGenerics.construct_url(baseUrl,jobArtifacts,projectId,jobId)
        APIGenerics.genericTemplate_InvokingGETAPI(url,token)

    '''This method is to get merge requests'''
    def getMergeRequests(self,token,baseUrl,projectId):
        url = APIGenerics.construct_url(baseUrl,projectMergeRequests,projectId)
        APIGenerics.genericTemplate_InvokingGETAPI(url,token)

    '''This method is to get merge requests with filter Ex:state=open'''
    def getMergeRequestsWithFilter(self,token,baseUrl,projectId,state):
        url = APIGenerics.construct_url(baseUrl,projectMergeRequests,projectId,state)
        APIGenerics.genericTemplate_InvokingGETAPI(url,token)

    '''This method is to get pipelines in a project'''
    def getMergeRequestsWithFilter(self,token,baseUrl,projectId):
        url = APIGenerics.construct_url(baseUrl,pipelines,projectId)
        APIGenerics.genericTemplate_InvokingGETAPI(url,token)

    '''This method is to get pipeline by pipeline id'''
    def getMergeRequestsWithFilter(self,token,baseUrl,projectId,pipelineId):
        url = APIGenerics.construct_url(baseUrl,pipeline,projectId,pipelineId)
        APIGenerics.genericTemplate_InvokingGETAPI(url,token)

    '''This method is to get pipeline test report'''
    def getMergeRequestsWithFilter(self,token,baseUrl,projectId,pipelineId):
        url = APIGenerics.construct_url(baseUrl,pipelineTestReport,projectId,pipelineId)
        APIGenerics.genericTemplate_InvokingGETAPI(url,token)

    '''This method is to get pipeline test report summary'''
    def getMergeRequestsWithFilter(self,token,baseUrl,projectId,pipelineId):
        url = APIGenerics.construct_url(baseUrl,pipeTestReportSummary,projectId,pipelineId)
        APIGenerics.genericTemplate_InvokingGETAPI(url,token)

    '''This method is to get latest pipeline'''
    def getMergeRequestsWithFilter(self,token,baseUrl,projectId):
        url = APIGenerics.construct_url(baseUrl,pipelineLatest,projectId)
        APIGenerics.genericTemplate_InvokingGETAPI(url,token)

    '''This method is to get members in a group'''
    def getGroupMembers(self,token,baseUrl,groupId):
        url = APIGenerics.construct_url(baseUrl,groupMembers,groupId)
        APIGenerics.genericTemplate_InvokingGETAPI(url,token)

    '''This method is to get members in a project'''
    def getGroupMembers(self,token,baseUrl,projectId):
        url = APIGenerics.construct_url(baseUrl,projectMembers,projectId)
        APIGenerics.genericTemplate_InvokingGETAPI(url,token)

    
    def getProjectStatistics(self, token, baseUrl, projectId):
        #  GET /projects/:projectId/statistics
        url = APIGenerics.construct_url(baseUrl, projectStatistics, projectId)
        APIGenerics.genericTemplate_InvokingGETAPI(url,token)

    def getProjectsList(self, token, baseUrl):
        #  GET /projects
        url = APIGenerics.construct_url(baseUrl, projects)
        APIGenerics.genericTemplate_InvokingGETAPI(url, token)
    
    def getRepositoriesList(self, token, baseUrl, projectId):
        #  GET /projects/:id/repository/tree
        url = APIGenerics.construct_url(baseUrl, repositories, projectId)
        APIGenerics.genericTemplate_InvokingGETAPI(url, token)




