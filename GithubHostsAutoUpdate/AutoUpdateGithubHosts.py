import paramiko
import scp
import pathlib
import os
import requests
import time

def Update(IP:str, USERNAME:str, PASSWORD:str, PORT:int=22) -> None:
    Nones = len([bool(each) for each in [IP, USERNAME, PASSWORD, PORT] if not bool(each)])
    if Nones > 0:
        print("{} There are {} null values in the entered values, please re-enter them".format(time.strftime("%H:%M:%S"), Nones))
        return
    PATH = pathlib.Path(__file__).parent
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(IP, PORT, USERNAME, PASSWORD)
        SCP = scp.SCPClient(ssh.get_transport())
        SCP.get("/etc/hosts", PATH)
        with open(PATH/"hosts", "rt") as f:
            Hosts = [each for each in f.readlines() if "github" not in each and "Github" not in each and "#" not in each and "vscode" not in each]
        with open(PATH/"hosts", "wt+") as f:
            f.write(requests.get("https://gh.api-go.asia/https://raw.githubusercontent.com/521xueweihan/GitHub520/main/hosts").text)
        with open(PATH/"hosts", "rt") as f:
            Hosts.extend([each for each in f.readlines() if each != "\n" and "#" not in each])
        with open(PATH/"hosts", "w+", encoding="utf-8") as f:
            f.writelines(Hosts)
        SCP.put((PATH/"hosts"), "/etc")
        os.remove(PATH/"hosts")

        print("{} Your Github Hosts update successfully".format(time.strftime("%H:%M:%S")))
    except BaseException as e:
        print("{} Your Github Hosts encountered an error while updating".format(time.strftime("%H:%M:%S")))
        print("{} Cause of the error: {}".format(time.strftime("%H:%M:%S"), e))
    finally:
        return

if __name__ == "__main__":
    IP = input("IP address to be upgrade: ")
    PORT = 22
    USERNAME = input("The Username: ")
    PASSWORD = input("The Password: ")
    os.system("cls" if os.name == "nt" else "clear")
    Update(IP, USERNAME, PASSWORD)