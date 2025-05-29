This script takes in a github repo release page URL along with the user's current verison number and figures out if they have the latest version.
It only looks at major releases, not release candidates (rc) or pre-releases.

Example:
PS C:\Users\ADMIN> Python.exe "z:/Scripts/Python/Get Latest Github Release/Get_Latest_Github_Release_V1.1.py"
Enter your current version number (1.0.2): 1.2.3
Enter the GitHub repository release URL (Ex: https://github.com/tensorflow/tensorflow/releases): https://github.com/tensorflow/tensorflow/releases
There is a new version available, version v2.19.0
Get it here: https://github.com/tensorflow/tensorflow/releases/v2.19.0
