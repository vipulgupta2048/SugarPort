# Author: vipulgupta2048
# Date: 30/03/18
# Script to find repositories that don't contain files like README.md, CONTRIBUTING.md, requirements.txt in an organisation
# Reference: https://gist.github.com/Pro-Panda/0e96e9011fd118e684ff93fd972299de#file-github-sugarlabs-analysis-py-L13
# Libraries needed - PyGitHub ----> run " pip3 install pygithub --user " before execution

from github import Github

def readme(repo):
    '''Return True if the repository has a README.md, else false'''
    find = 'README.md'      #Add path of file that needs to be searched. Searching for README.md here.
    try:
        repo.get_file_contents(find)
        print ("Readme Found- %s" %repo.html_url)
        return True
    except Exception as e:
        print ("README NOT Found")
    return False

def activity(repo):
    '''Return True if the repository is an activity, else false'''
    ACTIVITY_FILE = 'activity/activity.info'
    try:
        repo.get_file_contents(ACTIVITY_FILE)
        print ("Activity found - %s" %repo.html_url)
        if readme(repo):
            return False
        else:
            return True
    except Exception as e:
        print ("Not a activity - %s" %repo.html_url)
    return False


    g = Github("94cb9120ef578a8a6412203da548b37004873485s")  # Enter your access token here
    sugar_activities = g.get_organization("sugarlabs")  # Replace with organisation name
    file = open('Results.txt', 'w')

    for repo in sugar_activities.get_repos():
        if activity(repo):
            print("Writing it down")    # Repository names not containing README.md recorded
            file.write("\n " + repo.html_url)
