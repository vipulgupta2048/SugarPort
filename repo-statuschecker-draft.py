# -*- coding: utf-8 -*-
# Copyright 2018, Vipul Gupta

# This file is part of SugarPort.

# SugarPort is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# SugarPort is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with SugarPort.  If not, see <http://www.gnu.org/licenses/>.

from github import Github
from github.GithubException import GithubException
import configparser

'''Data such as missing license mentions, missing links from
 help activity, missing sections etc. In addition to this, ensuring that
  activity.info file is consistent and containing all information needed'''

cp = configparser.ConfigParser()

activityFile = 'activity/activity.info'
SECTIONS = 'Activity'
OPTIONS = [
            'name', 'activity_version', 'bundle_id', 'icon', 'exec',
            'mime_types', 'license', 'summary', 'update_url', 'tags',
            'max_participants', 'repository', 'tags', 'show_launcher',
            'categories', 'category' ,'screenshots','single_instance', 'website']


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
        repo.get_file_contents('LICENSE') or repo.get_file_contents('COPYING')
        print("License found in the repo")
    except GithubException as error:
        print("License not found in the repo")


def screenshot(repo):
    try:
        repo.get_dir_contents('screenshot/') or repo.get_dir_contents('screenshots/')
        print("Screenshots directory found in the repo")
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
    # tried various methods to extract summary of an activity but
    # couldn't (Methods used configparser, scraping, raw extract)

def activity(repo):
    '''Return True if the repository is an activity, else false'''
    try:
        repo.get_file_contents(activityFile)
        print("Activity found - %s" % repo.html_url)
    except Exception as e:
        print("Not an activity - %s" % repo.html_url)
        return
    findLicense(repo)
    readme(repo)
    screenshot(repo)
    analyse_activityinfo(repo)


if __name__ == '__main__':
    # Enter your access token here
    g = Github("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    # Replace with organisation name
    sugar_activities = g.get_organization("sugarlabs")
    # Searching all repo of the organiztion
    counter = 0
    for repo in sugar_activities.get_repos():
        counter = counter + 1
        print("---------------------------------------------------------")
        print("No of Repositories searched - {}".format(counter))
        activity(repo)
