from github import Github
from github.GithubException import GithubException
import configparser

# Author: vipulgupta2048
# Date: 30/05/18
# Libraries needed - PyGitHub ----> run " pip3 install pygithub --user " before
# execution

'''Data such as missing license mentions, abstract of activities from the wikis, missing links from help activity, missing sections etc. In addition to this, ensuring that activity.info file is consistent and containing all information needed'''

cp = configparser.ConfigParser()
activityFile = 'activity/activity.info'

SECTIONS = 'Activity'
OPTIONS = [
            'name', 'activity_version', 'bundle_id', 'icon', 'exec',
            'mime_types', 'license', 'summary', 'update_url', 'tags',
            'max_participants', 'repository ', 'tags', 'single_instance']


def analyse_activityinfo(repo):
    '''Return True if the repository has a license field in
    activity/acitvity.info, else false'''
    print("Going through activity.info file")
    try:
        repo.get_file_contents(activityFile)
        metadata_string = repo.get_file_contents(activityFile).decoded_content
        cp.read_string(metadata_string.decode())
    except Exception as e:
        print(e)
    try:
        cp.has_section(SECTIONS)
        print("{} section is present".format(SECTIONS))
    except configparser.NoSectionError as err:
        print(err)

    for option in OPTIONS:
        has_option = cp.has_option(SECTIONS, option)
        print('{}.{:<20}  : {}'.format(SECTIONS, option, has_option))


def findLicense(repo):
    try:
        repo.get_file_contents('LICENSE')
        print("License found in the repo")
    except GithubException as error:
        print("License not found in the repo")


def screenshot(repo):
    try:
        repo.get_file_contents('/screenshot')
        print("Screenshot directory found in the repo")
    except GithubException as error:
        print("Screenshot directory not found in the repo")


def readme(repo):
    '''Return True if the repository has a README.md, else false'''
    try:
        repo.get_file_contents('README.md') or repo.get_file_contents('README')
        print("README found in the repo")
        # summary(repo)
    except GithubException as e:
        print("README not found in the repo")

# def summary(repo):
    # try:
        # strin = repo.get_file_contents('README.md')
        # cp.read_string(string.decode())
        # print (string)
    # except Exception as e:
        # print (e)


def activity(repo):
    '''Return True if the repository is an activity, else false'''
    try:
        repo.get_file_contents(activityFile)
        print("Activity found - %s" % repo.html_url)
        findLicense(repo)
        readme(repo)
        screenshot(repo)
        analyse_activityinfo(repo)
    except Exception as e:
        print("Not an activity - %s" % repo.html_url)


if __name__ == '__main__':
    # Enter your access token here
    g = Github("3c3b561923fc2536301ffa37a16d92f3cbadee7f")
    # Replace with organisation name
    sugar_activities = g.get_organization("sugarlabs")
    # file = open('Results.txt', 'w')
    for repo in sugar_activities.get_repos():
        print("---------------------------------------------------------")
        activity(repo)
        # Repository names not containing README.md recorded
        # file.write("\n " + repo.html_url)
