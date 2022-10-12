import time
import os
from pyrogram import Client
import json
from colorama import Fore,init
init(convert=True)
os.system("title Telegram Username Sniper v1 [Loading Config] [Support : @udpskid] [Discord : Terminal#1465]")
time.sleep(2)
with open('config.json') as f:
    config = json.load(f)
api_id = config['api_id']
api_hash = config['api_hash']
app = Client("randomNameHere", api_id=api_id, api_hash=api_hash)
os.system("title Telegram Username Sniper v1 [Loaded Config] [Support : @udpskid] [Discord : Terminal#1465]")
time.sleep(2)
app.start()
success_count = 0
fail_count = 0
attempt = 0
async def valid(username):
    global success_count
    global fail_count
    global attempt
    try:
        await app.get_users(username)
        fail_count += 1
        attempt += 1
        return False
    except Exception as e:
        await app.set_username(username)
        success_count += 1
        attempt += 1
        return True
    

while True:
    for i in config['username']:
        resp = app.run(valid(i))
        if resp:
            print(f'{Fore.GREEN}[+] Success : {Fore.RESET}{Fore.CYAN} {i} {Fore.RESET} {Fore.LIGHTMAGENTA_EX}| Attempt :{Fore.RESET}{Fore.CYAN}{attempt}{Fore.RESET} ')
            os.system(f"title Telegram Username Sniper v1 [Running] [Success : {success_count}] [Fails : {fail_count}]")
            time.sleep(999999)
        else:
            print(Fore.RED+f"[+] Fail :{Fore.RESET} {Fore.CYAN} {i} {Fore.RESET} {Fore.LIGHTMAGENTA_EX}| Attempt :{Fore.RESET}{Fore.CYAN}{attempt}{Fore.RESET} ")
            os.system(f"title Telegram Username Sniper v1 [Running] [Success : {success_count}]  [Fails : {fail_count}]")