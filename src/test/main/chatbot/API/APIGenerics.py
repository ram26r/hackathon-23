import requests
import APIEnumsAndConstants

def invoke_GETApis(url):
    response= requests.get(url)
    statuscode=response.status_code
    return statuscode


def construct_url(url,endpoint,*arr):
    temp=url+endpoint
    
    if(len(arr)>0):
        temp=temp.format(*arr)
              
        
    return temp

url=construct_url("https://gitlab.dx1.lseg.com/api/v4",APIEnumsAndConstants.projectUrl)
# print(invoke_GETApis(url))