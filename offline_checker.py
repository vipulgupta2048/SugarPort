'''Offline Repo-Analyzer for SugarLabs'''

#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Copyright (C) 2018, Vipul Gupta - vipulgupta2048

# This file is part of SugarPort.

# The program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# The program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import configparser
import os
import time
import webbrowser
import subprocess
from zipfile import ZipFile
from pathlib import Path

def initialise():
    """Running tests --> verify build & create .xo."""
    subprocess.call(['python', 'setup.py', "dist_xo"])
    subprocess.call(['python', 'setup.py', "build"])
    print("------------------------------------\n")


def extractzip():
    '''Extract zip files in READ mode.'''
    # Specify .xo filename in commandline when prompted
    c = input("Enter file name = ")
    file_name = activity + "/dist/"+ c +".xo"
    with ZipFile(file_name, 'r') as zips:
        os.chdir(activity + '/dist/')
        print('Extracting all the files now...')
        zips.extractall()
        print('Done!')
        os.chdir(activity)
        print("------------------------------------\n")


def licensechecks():
    '''Check Licenses and copyrights in source code.'''
    checkpath = activity + '/dist/'
    subprocess.call(['licensecheck', '--recursive', checkpath])
    print("------------------------------------\n")


def analyse_activityinfo():
    '''Analyzing activity.info'''
    if os.path.exists(activityFile):
        cp = configparser.ConfigParser()
        cp.read(activityFile, encoding='utf-8')
        print("Analyzing metadata ... \n")
        try:
            for option in OPTIONS:
                print('{}.{:<20}  : {}'.format(SECTION, option, cp.has_option(SECTION, option)))
                time.sleep(.3)
                if option == 'exec':
                    print("--------------------------------------------")
                if option == 'repository':
                    if not cp.has_option(SECTION, 'repository'):
                        r = open(activityFile, "a")
                        r.write("\nrepository = https://github.com/sugarlabs/" + x)
                        r.close()
                        print("Repository Replaced")
                if option == 'website':
                    if cp.has_option(SECTION, 'website'):
                        print("PROBLEM in URL")
                if option == 'url':
                    if not cp.has_option(SECTION, 'url'):
                        url2 = "https://help.sugarlabs.org"
                        webbrowser.open_new_tab(url2)
        except configparser.NoSectionError as err:
            print(err)

        # Opening activity.info for edits in mousepad application
        subprocess.call(["mousepad", activityFile], stderr=subprocess.PIPE)
        print("------------------------------------\n")


def find_license():
    ''' Find COPYING in directory'''
    try:
        print([w for w in os.listdir("./") if "COPYING" in w])
        print("COPYING file found in the repo.\n")
    except FileNotFoundError as err:
        print(err)


def giti():
    '''Create .gitignore if not found'''
    entities = ["*.pyc\n", "locale/\n", "dist/\n", "*.patch\n", "*.bak\n", "*.swp\n", "*~\n"]
    gitipath = Path(activity + "/.gitignore")
    if not gitipath.exists():
        print(".gitignore not present in the repository hence replacing")
        with open(".gitignore", "w") as g:
            g.writelines(entities)
            g.close()
    # Experimental - Alpha
    #~ else:
        #~ with open('.gitignore', "r+") as g:
            #~ print("here")
            #~ lines = g.readlines()
            #~ if not "locale" in lines:
                #~ g.write("locale/\n")
                #~ print("entity added")
            #~ if not "dist" in lines:
                #~ g.write("dist/")
                #~ print("entity added")

    print("*******.gitignore after corrections******")
    with open(str(gitipath), 'r') as gitiread:
        print (gitiread.read())


def screenshot():
    '''Find screenshots; If not found, add activity name to click new screenshots'''
    shot = Path(activity + "/screenshots")
    if shot.exists():
        print("\n Screenshots directory found in the repo \n")
    else:
        print("Screenshots directory NOT found in the repo")
        with open('some_name.txt', "a") as shotfile:
            shotfile.write(x)
            shotfile.close()
            print("Noting it down")
        print("------------------------------------\n")


def openurl():
    '''Make PR - Opens fork when changes pushed'''
    print('Opening {} '.format(url))
    webbrowser.open_new_tab(url)


# Execution starts here - Repository Caller
# Enter names of forked repositories that needs to be analysed under your_account on GitHub

USERNAME = input("Enter your GitHub username : ")
CALLER = []
while 1:
    q = input("Enter forked repository name (Leave blank to stop) = ")
    if q == "":
        print("Thank you for adding !!")
        break
    CALLER.append(q)
print ("Repositories in pipeline for analysis are as follows {} ".format(CALLER))

# Control panel
for x in CALLER:
    url = "https://www.github.com/" + USERNAME + "/" + x
    subprocess.call(['git', 'clone', '--recursive', url])
    activity = os.getcwd() + "/" + x
    os.chdir(activity)
    subprocess.call(['git', 'checkout', '-b', 'develop'])
    print("Just to be sure, we are in {}".format(activity))

    activityFile = activity + '/activity/activity.info'
    SECTION = 'Activity'
    OPTIONS = [
        'name', 'activity_version', 'bundle_id', 'license', 'icon', 'exec',
        'mime_types', 'update_url', 'max_participants', 'show_launcher',
        'categories', 'category', 'single_instance', 'website', 'url',
        'tags', 'summary', 'repository',]

    initialise()
    extractzip()
    licensechecks()
    analyse_activityinfo()
    find_license()
    screenshot()
    giti()

    y = 'r'
    while y == 'r':
        y = input("Ready to PR (y) Check again (r) = ")
        if y == 'y':
            openurl()
        elif y == 'r':
            licensechecks()
            analyse_activityinfo()
            find_license()
