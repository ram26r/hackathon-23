import requests
from APIGenerics import APIGenerics
from APIEnumsAndConstants import *


class GitAPIMethods:
    '''This method is to get all branches in a project'''
    def getBranchesInProject(self,token,baseUrl,projectId):
        url = APIGenerics.construct_url(baseUrl,GitVariables.branches,projectId)
        return APIGenerics.genericTemplate_InvokingGETAPI(url,token)
       

    '''This method is to get a branch by id'''
    def getBranchById(self,token,baseUrl,projectId,branchId):
        url = APIGenerics.construct_url(baseUrl,GitVariables.branch,projectId,branchId)
        return APIGenerics.genericTemplate_InvokingGETAPI(url,token)


    '''This method is to get all commits in a project'''
    def getRepositoryCommits(self,token,baseUrl,projectId):
        url = APIGenerics.construct_url(baseUrl,GitVariables.commits,projectId)
        return APIGenerics.genericTemplate_InvokingGETAPI(url,token)


    '''This method is to get a commit details'''
    def getCommitById(self,token,baseUrl,projectId,commitId):
        url = APIGenerics.construct_url(baseUrl,GitVariables.commit,projectId,commitId)
        return APIGenerics.genericTemplate_InvokingGETAPI(url,token)


    '''This method is to get references of a commit'''
    def getCommitReferences(self,token,baseUrl,projectId,commitId):
        url = APIGenerics.construct_url(baseUrl,GitVariables.references,projectId,commitId)
        return APIGenerics.genericTemplate_InvokingGETAPI(url,token)

    '''This method is to get jobs'''
    def getJobs(self,token,baseUrl,projectId):
        url = APIGenerics.construct_url(baseUrl,GitVariables.projectJobs,projectId)
        return APIGenerics.genericTemplate_InvokingGETAPI(url,token)

    '''This method is to get pipeline jobs'''
    def getPipelineJobs(self,token,baseUrl,projectId,pipelineId):
        url = APIGenerics.construct_url(baseUrl,GitVariables.pipelineJobs,projectId,pipelineId)
        return APIGenerics.genericTemplate_InvokingGETAPI(url,token)

    '''This method is to get pipeline trigger jobs'''
    def getPipelineTriggerJobs(self,token,baseUrl,projectId,pipelineId):
        url = APIGenerics.construct_url(baseUrl,GitVariables.pipeTriggerJobs,projectId,pipelineId)
        return APIGenerics.genericTemplate_InvokingGETAPI(url,token)

    '''This method is to get job details by job id'''
    def getJobById(self,token,baseUrl,projectId,jobId):
        url = APIGenerics.construct_url(baseUrl,GitVariables.job,projectId,jobId)
        return APIGenerics.genericTemplate_InvokingGETAPI(url,token)

    '''This method is to get job log file by job id'''
    def getJobFileById(self,token,baseUrl,projectId,jobId):
        url = APIGenerics.construct_url(baseUrl,GitVariables.jobLogFile,projectId,jobId)
        return APIGenerics.genericTemplate_InvokingGETAPI(url,token)

    '''This method is to get job artifacts'''
    def getJobArtifacts(self,token,baseUrl,projectId,jobId):
        url = APIGenerics.construct_url(baseUrl,GitVariables.jobArtifacts,projectId,jobId)
        return APIGenerics.genericTemplate_InvokingGETAPI(url,token)

    '''This method is to get merge requests'''
    def getMergeRequests(self,token,baseUrl,projectId):
        url = APIGenerics.construct_url(baseUrl,GitVariables.projectMergeRequests,projectId)
        return APIGenerics.genericTemplate_InvokingGETAPI(url,token)

    '''This method is to get merge requests with filter Ex:state=open'''
    def getMergeRequestsWithFilter(self,token,baseUrl,projectId,state):
        url = APIGenerics.construct_url(baseUrl,GitVariables.projectMergeRequests,projectId,state)
        return APIGenerics.genericTemplate_InvokingGETAPI(url,token)

    '''This method is to get pipelines in a project'''
    def getPipelines(self,token,baseUrl,projectId):
        url = APIGenerics.construct_url(baseUrl,GitVariables.pipelines,projectId)
        return APIGenerics.genericTemplate_InvokingGETAPI(url,token)

    '''This method is to get pipeline by pipeline id'''
    def getPipelineById(self,token,baseUrl,projectId,pipelineId):
        url = APIGenerics.construct_url(baseUrl,GitVariables.pipeline,projectId,pipelineId)
        return APIGenerics.genericTemplate_InvokingGETAPI(url,token)

    '''This method is to get pipeline test report'''
    def getPipelineReport(self,token,baseUrl,projectId,pipelineId):
        url = APIGenerics.construct_url(baseUrl,GitVariables.pipelineTestReport,projectId,pipelineId)
        return APIGenerics.genericTemplate_InvokingGETAPI(url,token)

    '''This method is to get pipeline test report summary'''
    def getPipelineReportSummary(self,token,baseUrl,projectId,pipelineId):
        url = APIGenerics.construct_url(baseUrl,GitVariables.pipeTestReportSummary,projectId,pipelineId)
        return APIGenerics.genericTemplate_InvokingGETAPI(url,token)

    '''This method is to get latest pipeline'''
    def getLatestPipeline(self,token,baseUrl,projectId):
        url = APIGenerics.construct_url(baseUrl,GitVariables.pipelineLatest,projectId)
        return APIGenerics.genericTemplate_InvokingGETAPI(url,token)

    '''This method is to get members in a group'''
    def getGroupMembers(self,token,baseUrl,groupId):
        url = APIGenerics.construct_url(baseUrl,GitVariables.groupMembers,groupId)
        return APIGenerics.genericTemplate_InvokingGETAPI(url,token)

    '''This method is to get members in a project'''
    def getProjectMembers(self,token,baseUrl,projectId):
        url = APIGenerics.construct_url(baseUrl,GitVariables.projectMembers,projectId)
        return APIGenerics.genericTemplate_InvokingGETAPI(url,token)

    '''This method is to download artifacts archive'''
    def getDownloadArtifacts(self,token,baseUrl,projectId,artifactId,jobName):
        url = APIGenerics.construct_url(baseUrl,GitVariables.downloadArtifactsArchive,projectId,artifactId,jobName)
        return APIGenerics.genericTemplate_InvokingGETAPI(url,token)

    '''This method is to download artifact archive by job id'''
    def getDownloadArtifactByJobId(self,token,baseUrl,projectId,jobId,artifactPath):
        url = APIGenerics.construct_url(baseUrl,GitVariables.downloadArtifactByJobId,projectId,jobId,artifactPath)
        return APIGenerics.genericTemplate_InvokingGETAPI(url,token)

    '''This method is to download artifact archive by branch id'''
    def getDownloadArtifactByBranchId(self,token,baseUrl,projectId,branchName,artifactPath,jobName):
        url = APIGenerics.construct_url(baseUrl,GitVariables.downloadArtifactByBranchId,projectId,branchName,artifactPath,jobName)
        return APIGenerics.genericTemplate_InvokingGETAPI(url,token)





