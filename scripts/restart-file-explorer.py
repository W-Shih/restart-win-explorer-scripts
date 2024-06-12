import subprocess
import time

def restart_file_explorer():
    # Kill the explorer.exe process
    #   `/f` is used to forcefully terminate the process. 
    #   `/im` is used to specify the image name of the process. 
    subprocess.run(["taskkill", "/f", "/im", "explorer.exe"], check=True)
    
    # Wait for 5 seconds
    time.sleep(5)
    
    # Restart the explorer.exe process
    subprocess.run(["start", "explorer.exe"], shell=True)

if __name__ == "__main__":
    restart_file_explorer()
