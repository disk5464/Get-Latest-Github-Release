#This script takes in a github repo release page along with the user's current verison number and figures out if they have the latest version.
#It only looks at major releases, not release candidates (rc) or pre-releases.
#Last Modified: 5/29/2025
#Verion 1.0: Initial release
####################################################################################
import requests
from bs4 import BeautifulSoup

####################################################################################
#Set the current verison and repo URL, then get the HTML page for the github releases page, then use beautifulsoup to parse it
currentVerson = "v0.19.2"
repo = 'https://github.com/chrisbenincasa/tunarr/releases'

response = requests.get(repo)
soup = BeautifulSoup(response.content, 'html.parser')

####################################################################################
#Get the content of all the div sections with a class called col-md-9. This is the section of each release where the version numbers are located.
s = soup.find('div', class_='col-md-9')
content = soup.find_all('h2')

####################################################################################
#Create an empty list to store the version numbers.
allversions = []

#Foreach h2 element in the HTML, if it has v0 in it add it to the list. 
for i in content:
    if "v0." in i.text:
        allversions.append(i.text)

#Sort the list of verison numbers newest to oldest. Save the newest verison to a variable
allversions.sort(reverse=True)
latestVersion = allversions[0]      

####################################################################################
#Compare the current verison and print if there is an update or not.
if currentVerson >= latestVersion:
    print("You are up to date!")
else:
    print("There is a new version available, version " + latestVersion)
    print("Get it here: " + repo)
