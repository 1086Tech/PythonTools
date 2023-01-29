import paramiko
import scp
import pathlib
import os
import requests
import time

# 如需重复使用，可在此保存数据，永久有效
IP = None
USERNAME = None
PASSWORD = None
PORT = 22

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
        del PASSWORD, USERNAME, IP
        SCP = scp.SCPClient(ssh.get_transport())
        SCP.get("/etc/hosts", PATH)
        with open(PATH/"hosts", "rt") as f:
            Hosts = f.readlines()
            for ignore in ["github", "Github", "#", "vscode"]:
                Hosts = [each for each in Hosts if ignore not in each]
        with open(PATH/"hosts", "wt+") as f:
            f.write(requests.get("https://gh.api-go.asia/https://raw.githubusercontent.com/521xueweihan/GitHub520/main/hosts").text)
        with open(PATH/"hosts", "rt") as f:
            _Hosts = f.readlines()
            for ignore in ["#"]:
                _Hosts = [each for each in _Hosts if ignore not in each and each != "\n"]
            Hosts.extend(_Hosts)
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
    if len([bool(each) for each in (IP, USERNAME, PASSWORD) if not bool(each)]) > 0:
        IP = input("IP address to be upgrade: ")
        USERNAME = input("The Username: ")
        PASSWORD = input("The Password: ")
        os.system("cls" if os.name == "nt" else "clear")
    Update(IP, USERNAME, PASSWORD)