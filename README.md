# SugarPort

All source code related to the project used and made for Google Summer of Code 2018 under Sugar Labs. 
**Project Details** - [GSoC Official Website](http://tiny.cc/vgsoc) | Blogs - **Mixster** --> [GSoC#2018](https://mixstersite.wordpress.com/gsoc2018/) | **Progress Tracker** and meeting MoM's - [Sugar Tracker](https://docs.google.com/document/d/1VdzjA-DnEBh0ntHY17ktXlp7c2pIofq8458gSCTwiSM/edit?usp=sharing) 

## Introduction
**SugarPort** started out as WikiPort, before I was retasked to work on a similar project with a different aim of setting up the new Activity Server for Sugar Labs called **ASLOv3**. This repository will work as a holdout till the project is ready for all the scripts and code that would be written for its deployment.

**[Sugar Labs](https://sugarlabs.org/)** is a community-run software project whose mission is to produce, distribute, and support the use of **Sugar**, an open source desktop environment and learning platform. Sugar Labs is a member of the **Software Freedom Conservancy**, an umbrella organization for free software (FLOSS) projects. Sugar is widely used by children from under-developed countries, as medium to learn new things from and improve their skills. 

**Sugar Labs** also participates in **Google Code-in**, **Google Summer of Code** which serves as an outlet for young programmers. 

(_Edited from [Wikipedia](https://en.wikipedia.org/wiki/Sugar_Labs)_)

## Aim
To deploy ASLOv3 by the end of Summer 2018 (i.e August according to the timeline)

## Work Done
- For the successful deployment of ASLOv3, the activity metadata is added/updated in the activity repositories for correct information to be displayed on the web portal. (All 161+ of them present at [sugarlabs](www.github.com/sugarlabs) More details about this are present in the Sugar Tracker.

- A script automates analyzing of repositories present on GitHub using PyGitHub and GitHub API. Parse through them with ConfigParser finding parameters that are missing and storing the clean output in a seperate file for future reference. 

- After analyes gets completed, activites are fixed with their metadata updated as necessary. This can be done manually as well as automated (working on that)

### Testing the Analysis Script
1. Fork and clone this repository. 
`git clone [Forked repository URL]` 
2. Install the requirements listed in the `requirements.txt` file
`pip install -r requirements.txt` 
3. Enter your GitHub API access token, refer to this [tutorial](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/) for generating your personal token.
4. Open the repo-statuschecker-draft.py and enter the token where listed. 
5. Run the script using the command. 
`python3 -u repo-statuschecker.py | tee output.txt`
6. It takes time to execute completely, after execution you will find output.txt showing you the results of the analysis. 
  
## License
The source code is under [GPLv3](https://github.com/vipulgupta2048/SugarPort/blob/master/LICENSE)

