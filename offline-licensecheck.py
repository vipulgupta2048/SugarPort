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

# Running tests --> verify build & create .xo
def initialise():
    subprocess.call(['python', 'setup.py', "dist_xo"])
    subprocess.call(['python', 'setup.py', "build"])
    print("------------------------------------\n")


# Extract zip files in READ mode 
def extractzip():
    # Specify the zip filename in the commandline
    x = raw_input("Enter file name = ")
    file_name = activity + "/dist/"+ x +".xo"
    with ZipFile(file_name, 'r') as zip:
        os.chdir(activity + '/dist/')
        print('Extracting all the files now...')
        zip.extractall()
        print('Done!')
        os.chdir(activity)
        print("------------------------------------\n")


# Checking Licenses and copyrights in source code 
def licensechecks():
    z = activity + '/dist/'
    subprocess.call(['licensecheck','--recursive',z])
    print("------------------------------------\n")


# Analyzing activity.info
def analyse_activityinfo():
    if os.path.exists(activityFile):
        cp = configparser.ConfigParser()
        cp.read(activityFile, encoding='utf-8')
        print("Analyzing metadata ...")
        try:
            for option in OPTIONS:
                print('{}.{:<20}  : {}'.format(ACTIVITY_SECTION, option, cp.has_option(ACTIVITY_SECTION, option)))
                time.sleep(.3)
                if (option=='exec'):
                    print("--------------------------------------------")
                if (option=='repository'):
                    if not cp.has_option(ACTIVITY_SECTION, 'repository'):
                        r = open(activityFile,"a")
                        r.write("\nrepository = https://github.com/sugarlabs/" + x )
                        r.close()
                        print("Repository Replaced")
                if (option=='website'):
                    if cp.has_option(ACTIVITY_SECTION,'website'):
                        print("PROBLEM in URL")
                if (option=='url'):
                    if not cp.has_option(ACTIVITY_SECTION,'url'):
                        url2 = "https://help.sugarlabs.org"
                        webbrowser.open_new_tab(url2)
        except configparser.NoSectionError as err:
            print(err)

        # Opening activity.info for edits in mousepad application
        subprocess.call(["mousepad", "activity.info"], stdout=subprocess.PIPE, stdin=subprocess.PIPE,  stderr=subprocess.PIPE)
        print("------------------------------------\n")


# Finding COPYING file 
def findLicense():
    try:
        print([w for w in os.listdir("./") if "COPYING" in w])
        print("COPYING file found in the repo.\n")
    except Exception as e:
        print(e)
        print("COPYING file not found in the repo.\n")


# Making a .gitignore if not found
def giti():
    giti = Path(activity + "/.gitignore")
    wines = ["*.pyc\n","locale/\n","dist/\n","*.patch\n","*.bak\n","*.swp\n","*~\n"]
    with open(".gitignore","w") as g:
        f = g.readlines()

        if not giti.exists():
            print(".gitignore not present in the repository hence replacing")
            g.writelines(wines)
        else:
            with open(".gitignore","r") as f:
                z = f.readlines()
                if not "locale/" in z:
                    print("Entities not found, replacing")
                    g.writelines(wines)


# Finding if screenshots exist; If not, new file made to add names of activities to click new screenshots 
def screenshot():
    shot = Path(activity + "/screenshots")
    if shot.exists():
        print("\n Screenshots directory found in the repo \n")
    else:
        print("Screenshots directory NOT found in the repo")
        with open('some_name.txt', "a") as u:
            u.write(x)
            u.close()
            print("Noting it down")
        print("------------------------------------\n")


# Making a PR - Opening the fork when changes pushed
def openurl():
    print('Opening {} '.format(url))
    webbrowser.open_new_tab(url)


# Repository Caller - Enter names of forked repositories under your_account in GitHub
set = []

# Control panel - Script needs to run in the home directory otherwise change path variable
for x in set:
    url = https://www.github.com/your_account/ + x
    subprocess.call(['git','clone','--recursive', url])
    activity = os.getcwd() + "/" + x
    os.chdir(activity)
    subprocess.call(['git','checkout','-b','develop'])
    print ("Just to be sure, we are in {}".format(activity))

    activityFile = activity + '/activity/activity.info'
    ACTIVITY_SECTION = 'Activity'
    OPTIONS = [
    'name', 'activity_version', 'bundle_id', 'license', 'icon', 'exec',
    'mime_types', 'update_url', 'max_participants',  'show_launcher',
    'categories', 'category' ,'single_instance', 'website', 'url',
    'tags','summary','repository',]

    initialise()
    extractzip()
    licensechecks()
    analyse_activityinfo()
    findLicense()
    screenshot()
    giti()
    
    y='r'
    while(y=='r')
        y = raw_input("Ready to PR (y) Check again (r) = ")
        if (y=='y'):
            openurl()
        elif (y=='r'):
            licensechecks()
            analyse_activityinfo()
            findLicense()
            
      
 # To-DO
 # Finalise giti() function add it to control panel 
 # Pull request automation 
 # Forking through GitHub API automation
 # Scrubbing
