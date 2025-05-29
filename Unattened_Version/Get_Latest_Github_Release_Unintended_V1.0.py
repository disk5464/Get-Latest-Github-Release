#This script takes in a github repo release page along with the user's current verison number and figures out if they have the latest version.
#It only looks at major releases, not release candidates (rc) or pre-releases.
#Last Modified: 5/29/2025
#Verion 1.0: Initial release. This builds off of the Get_latest_github_release_V1.1 script and added the settings.json file to store the current version and repo URL.
####################################################################################
import requests, json, os
from bs4 import BeautifulSoup
from types import SimpleNamespace

####################################################################################
#Import the settings josn file, open it, read it, then conver it to an object.
filePath = os.path.dirname(os.path.abspath(__file__)) + '/Settings.json'
data = json.loads(open(filePath).read(), object_hook=lambda d: SimpleNamespace(**d))

#Scrape the HTML then use beautifulsoup to parse it
response = requests.get(data.Repo)
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
if data.Current_Version >= latestVersion:
    print("You are up to date!")
else:
    print("There is a new version available, version " + latestVersion + ". You have version: v" + data.Current_Version)
    print("Get it here: " + data.Repo + "/" + latestVersion)
