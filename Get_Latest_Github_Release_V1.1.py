#This script takes in a github repo release page along with the user's current verison number and figures out if they have the latest version.
#It only looks at major releases, not release candidates (rc) or pre-releases.
#Last Modified: 5/29/2025
#Verion 1.0: Initial release
#Version 1.1: Added input prompts for current version and repo URL, adjusted the soup.find section so it targets the github suplied version tag not the version's title. This allows it to work with any github repo.
####################################################################################
import requests
from bs4 import BeautifulSoup

####################################################################################
#Get the current verison and repo URL from the user.
#currentVerson = "v0.19.3"
#repo = 'https://github.com/tensorflow/tensorflow/releases'
currentVerson = "v" + input("Enter your current version number (1.0.2): ")
repo = input("Enter the GitHub repository release URL (Ex: https://github.com/tensorflow/tensorflow/releases)")

#Scrape the HTML then use beautifulsoup to parse it
response = requests.get(repo)
soup = BeautifulSoup(response.content, 'html.parser')

####################################################################################
#Get the content of all the header class that has the github generated version tag  in it. (ex: Mar 11, @tensorflow-jenkins, v2.19.0) Then grab just the version numbers (ex: v2.19.0) 
s = soup.find_all(class_='mr-3 mr-md-0 d-flex pt-1 pt-sm-0')
content = soup.find_all("span",class_='ml-1 wb-break-all')

####################################################################################
#Create an empty list to store the version numbers.
allversions = []

#Foreach h2 element in the HTML, if it has v0 in it add it to the list. 
for i in content:
    if ("v" in i.text) and ("rc" not in i.text):
        allversions.append( (i.text).strip() )

#Sort the list of verison numbers newest to oldest. Save the newest verison to a variable
allversions.sort(reverse=True)
latestVersion = allversions[0]      

####################################################################################
#Compare the current verison and print if there is an update or not.
if currentVerson >= latestVersion:
    print("You are up to date!")
else:
    print("There is a new version available, version " + latestVersion)
    print("Get it here: " + repo + "/" + latestVersion)
