from django import views
from jira import JIRA 
import os
import gc
import shutil

l=[]
def getIssue(a):
    
    try:


        res = None
        options = {
        'server': 'https://athenajira.athenahealth.com/',
        'verify': False
        }
        JQL = 'project = "NOC" '
        authJira = JIRA(token_auth='MzEyODI3NjM1MTExOq0Nl1mveZKT20+z+ZQB+jnkQKqg',options=options)
        #res = authJira.search_issues(JQL,maxResults=100,json_result=True)
        #issues = res['NOC-31885']
        issue_num = a
        issue = authJira.issue(issue_num)

        '''comments =  issue.fields.comment.comments

        for comment in comments:
            print("Comment text : ",comment.body)
            print("Comment author : ",comment.author.displayName)
            print("Comment time : ",comment.created)'''
        Description = issue.fields.description
        Description = Description + " "
        issue.update(description=Description)
        #print(Description)
        #del a
        #gc.collect(a)
        a=''
        return Description
    except:
        return ''

def ssuploader(a):
    try:
        res = None
        options = {
            'server': 'https://athenajira.athenahealth.com/',
            'verify': False
            }
        JQL = 'project = "NOC" '
        authJira = JIRA(token_auth='Mzc2MzU3MjM3OTAzOl3YKbjYFdH7r6ofAGEOBHAh7VBi',options=options)
            
        issue_num = a
        issue = authJira.issue(issue_num)
        s="C:\\Users\\gvarshini\\Desktop\\screenshot"
        for filename in os.listdir(s):
            s1=s+"\\"+filename
                #with open(s1) as f:
            authJira.add_attachment(issue=issue, attachment=s1)
        
    except:
        return ''