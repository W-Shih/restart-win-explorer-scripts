# Restart File Explorer
# This script will kill the explorer.exe process and restart it after 5 seconds.
# `/f` is used to forcefully terminate the process. 
# `/im` is used to specify the image name of the process. 
taskkill /f /im explorer.exe
timeout /t 5 /nobreak  
start explorer.exe
