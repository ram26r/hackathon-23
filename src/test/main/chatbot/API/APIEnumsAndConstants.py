from enum import Enum

##region to add enums and constants used in Git APIs##
branches="/projects/{}/repository/branches"
branch="/projects/{}/repository/branches/{}"
commits="/projects/{}/repository/commits"
commit="/projects/{}/repository/commits/{}"
references="/projects/{}/repository/commits/{}/refs"
projectJobs="/projects/{}/jobs"
pipelineJobs="/projects/{}/pipelines/{}/jobs"
pipeTriggerJobs="/projects/{}/pipelines/{}/bridges"
groupMembers="/groups/{}/members"
projectMembers="/projects/{}/members"
jobArtifacts="/projects/{}/jobs/{}/artifacts"
projectMergeRequests="/projects/{}/merge_requests"
projectMergeRequests="/projects/{}/merge_requests?state={}"
pipelines="/projects/{}/pipelines"
pipeline="/projects/{}/pipelines/{}"
pipelineTestReport="/projects/{}/pipelines/{}/test_report"
pipeTestReportSummary="/projects/{}/pipelines/{}/test_report_summary"
pipelineLatest="/projects/{}/pipelines/latest"
projectStatistics="/projects/{}/statistics"
projects="/projects"
repositories="/projects/{}/repository/tree"

##region error message##
err_msg_git_generic="Request cannot be processed"
err_msg_git_tryAgain = "Error Occured , Please Try again.."
err_msg_git_unauthorized = "You are unauthorized for this request. Please get necessary access and try again.."
err_msg_git_badRequest = "Please provide valid input"
err_msg_git_backend = "Unable to process request. Please try after sometime.."
err_msg_git_codeError = "An exception occured"

##region status codes##
class StatusCodeEnum(Enum):
    UNAUTHORIZED = 401,
    BAD_REQUEST = 400,
    SERVER_ERROR = 500
    SUCCESS_OK = 200
