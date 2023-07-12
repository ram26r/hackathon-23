from enum import Enum


class GitVariables:
    # region to add enums and constants used in Git APIs#
    def __init__(self):
        pass

    branches = "/projects/{}/repository/branches"
    branch = "/projects/{}/repository/branches/{}"
    commits = "/projects/{}/repository/commits"
    commit = "/projects/{}/repository/commits/{}"
    references = "/projects/{}/repository/commits/{}/refs"
    projectJobs = "/projects/{}/jobs"
    pipelineJobs = "/projects/{}/pipelines/{}/jobs"
    pipeTriggerJobs = "/projects/{}/pipelines/{}/bridges"
    job = "/projects/{}/jobs/{}"
    jobLogFile = "/projects/{}/jobs/{}/trace"
    groupMembers = "/groups/{}/members"
    projectMembers = "/projects/{}/members"
    jobArtifacts = "/projects/{}/jobs/{}/artifacts"
    projectMergeRequests = "/projects/{}/merge_requests"
    projectMergeRequestsWithFilter = "/projects/{}/merge_requests?state={}"
    pipelines = "/projects/{}/pipelines"
    pipeline = "/projects/{}/pipelines/{}"
    pipelineTestReport = "/projects/{}/pipelines/{}/test_report"
    pipeTestReportSummary = "/projects/{}/pipelines/{}/test_report_summary"
    pipelineLatest = "/projects/{}/pipelines/latest"
    projectStatistics = "/projects/{}/statistics"
    projects = "/projects"
    repositories = "/projects/{}/repository/tree"
    downloadArtifactsArchive = "/projects/{}/jobs/artifacts/{}/download?job={}"
    downloadArtifactByJobId = "/projects/{}/jobs/{}/artifacts/{}"
    downloadArtifactByBranchId = "/projects/{}/jobs/artifacts/{}/raw/{}?job={}"
    oAuthToken = "/oauth/token"
    oAuthReqBody = "grant_type=password&username={}&password={}"

    # region error message#
    err_msg_git_generic = "Request cannot be processed"
    err_msg_git_tryAgain = "Error Occurred , Please Try again.."
    err_msg_git_unauthorized = "You are unauthorized for this request. Please get necessary access and try again.."
    err_msg_git_badRequest = "Please provide valid input"
    err_msg_git_backend = "Unable to process request. Please try after sometime.."
    err_msg_git_notFound = "Requested resource not found."
    err_msg_git_codeError = "An exception occurred"

    # region values that are used in git
    name = "name"
    web_url = "web_url"
    committed_date = "committed_date"
    committer_email = "committer_email"
    committer_name = "committer_name"
    authored_date = "authored_date"
    author_email = "author_email"
    author_name = "author_name"
    title = "title"
    created_at = "created_at"
    id = "id"
    merged = "merged"
    protected = "protected"
    default = "default"
    can_push = "can_push"
    iid = "iid"
    project_id = "project_id"
    status = "status"
    source = "source"
    ref = "ref"
    sha = "sha"
    updated_at = "updated_at"
    total_time = "total_time"
    total_count = "total_count"
    success_count = "success_count"
    failed_count = "failed_count"
    skipped_count = "skipped_count"
    error_count = "error_count"
    time = "time"
    count = "count"
    success = "success"
    failed = "failed"
    skipped = "skipped"
    error = "error"
    suite_error = "suite_error"
    total = "total"


# region status codes#
class StatusCodeEnum(Enum):
    UNAUTHORIZED = 401,
    BAD_REQUEST = 400,
    SERVER_ERROR = 500
    SUCCESS_OK = 200
    NOT_FOUND = 404


class APIUrlEnum(Enum):
    GetBranchesInProject = 0,
    GetBranchById = 1,
    GetRepositoryCommits = 2,
    GetCommitById = 3,
    GetCommitReferences = 4,
    GetJobs = 5,
    GetPipelineJobs = 6,
    GetPipelineTriggerJobs = 7,
    GetJobById = 8,
    GetJobFileById = 9,
    GetJobArtifacts = 10,
    GetMergeRequests = 11,
    GetMergeRequestsWithFilter = 12,
    GetPipelines = 13,
    GetPipelineById = 14,
    GetPipelineReport = 15,
    GetPipelineReportSummary = 16,
    GetLatestPipeline = 17,
    GetGroupMembers = 18,
    GetProjectMembers = 19,
    GetDownloadArtifacts = 20,
    GetDownloadArtifactByJobId = 21,
    GetDownloadArtifactByBranchId = 22


class CommitResponseEnum(Enum):
    Id = 0,
    WebUrl = 1,
    CommittedDate = 2,
    CommitterEmail = 3,
    CommitterName = 4,
    AuthoredDate = 5,
    AuthorEmail = 6,
    AuthorName = 7,
    Title = 8
    CreatedAt = 9


class BranchResponseEnum(Enum):
    Name = 0,
    Merged = 1,
    Protected = 2,
    Default = 3,
    Can_Push = 4,
    WebUrl = 5


class PipelineResponseEnum(Enum):
    Id = 0,
    Iid = 1,
    ProjectId = 2,
    Status = 3,
    Source = 4,
    Ref = 5,
    Sha = 6,
    Name = 7,
    WebUrl = 8,
    CreatedAt = 9
    UpdatedAt = 10


class PipeTestReportSumEnum(Enum):
    Time = 0,
    Count = 1,
    Success = 2,
    Failed = 3,
    Skipped = 4,
    Error = 5,
    SuiteError = 6


class PipeTestReportEnum(Enum):
    TotalTime = 0,
    TotalCount = 1,
    SuccessCount = 2,
    FailedCount = 3,
    SkippedCount = 4,
    ErrorCount = 5
