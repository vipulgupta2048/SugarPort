from github import Github
from github.GithubException import GithubException
import configparser
cp = configparser.ConfigParser()

def check_metadata_license(repo):
    try:
       repo.get_file_contents('activity/activity.info')
    except GithubException as error:
       return False
    metadata_string = repo.get_file_contents('activity/activity.info').decoded_content
    try:
    	cp.read_string(metadata_string.decode())
    except Exception as error:
        return False
    return cp.has_option('Activity','License') or cp.has_option('Activity','license')

def check_root_license(repo):
    try:
       repo.get_file_contents('LICENSE')
    except GithubException as error:
       return False
    return True

file_root_license = open('has_root_license.txt','w')
file_metadata_license = open('has_metadata_license.txt','w')
file_both_license = open('has_both_license.txt','w')
file_no_license = open('has_no_license.txt','w')
file_overall_stats = open('stats.txt','w')

# Replace xxxx string with the User's Oauth token
g = Github("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

sugar_activities  = g.get_organization("sugarlabs")

public_repos = sugar_activities.public_repos

count_license_in_metadata = 0
count_license_in_root_dir = 0
count_both = 0
count_no_license = 0
processed_repos = 0

for repo in sugar_activities.get_repos():
    meta_check = check_metadata_license(repo)
    root_check = check_root_license(repo)
    if meta_check:
       print(repo.clone_url,file=file_metadata_license)
       count_license_in_metadata  = count_license_in_metadata + 1
    if root_check:
       print(repo.clone_url,file=file_root_license)
       count_license_in_root_dir = count_license_in_root_dir + 1
    if meta_check and root_check:
       print(repo.clone_url,file=file_both_license)
       count_both = count_both +1
    if not(meta_check) and not(root_check):
       print(repo.clone_url,file=file_no_license)
       count_no_license = count_no_license +1
    processed_repos = processed_repos + 1
    print(repo.clone_url)
    print(" Processed {}  out of {} repos".format(processed_repos,public_repos))
    print("Repos with MetaData License : {}".format(count_license_in_metadata))
    print("Repos with LICENSE File : {}".format(count_license_in_root_dir))
    print("Repos with License entry in file and metadata : {}".format(count_both))
    print("Repos with No License : {}".format(count_no_license))


print("Total repos check : {} ".format(public_repos),file=file_overall_stats)
print("Repos with MetaData License : {}".format(count_license_in_metadata),file=file_overall_stats)
print("Repos with LICENSE File : {}".format(count_license_in_root_dir),file=file_overall_stats)
print("Repos with License entry in file and metadata : {}".format(count_both),file=file_overall_stats)
print("Repos with No License : {}".format(count_no_license),file=file_overall_stats)

file_metadata_license.close()
file_root_license.close()
file_both_license.close()
file_no_license.close()
file_overall_stats.close()
