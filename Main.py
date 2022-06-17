import psutil, subprocess, os, sys
import Language, UI

client_process = "LeagueClient.exe"
base_path = "C:\\Riot Games\\League of Legends\\"

def is_process_running(name):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if name.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

def resource_path(relative):
  """ Get absolute path to resource, works for dev and for PyInstaller """
  loc = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
  return os.path.join(loc, relative)

def open_client(language: Language.Language):
  # Check if client is running, if so kill it
  if is_process_running(client_process):
    os.system("taskkill /f /im " + client_process)
  # Start League of Legends with correct language
  subprocess.run([base_path + client_process, "--locale="+ language.value] )
  
if __name__ == "__main__":
  UI.App()



