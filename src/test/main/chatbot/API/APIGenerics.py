import requests
from APIEnumsAndConstants import *

class APIGenerics:

    '''This method is a generic template to send GET request and return the response'''
    def genericTemplate_InvokingGETAPI(url,token):
        try:
            headers = APIGenerics.construct_headers(token)
            resp = APIGenerics.invoke_GETAPIs(url,headers)
            if(resp.status_code==StatusCodeEnum.SUCCESS_OK.value):
                return resp
            else:
                return APIGenerics.return_generic_error_msg(resp.status_code)
        except:
            return err_msg_git_codeError

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
            return err_msg_git_unauthorized
        elif(statusCode == StatusCodeEnum.BAD_REQUEST.value):
            return err_msg_git_badRequest
        elif(statusCode == StatusCodeEnum.SERVER_ERROR.value):
            return err_msg_git_backend
        else:
            return err_msg_git_generic

    '''This method is to extract the branch count from response'''
    def get_branches_count(resp):
        return len(resp.json())

    '''This method is to extract the branch count from response'''
    def get_branches_name(resp):
        list1= list()
        for branch in resp.json():
            list1.append(branch.get('name'))
        return list1

      




