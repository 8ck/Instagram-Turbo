

import asyncio, aiohttp, requests, json, json, random, os
from colorama import Fore, Back, Style

INSTAGRAM_LOGIN_CSRF = "https://www.instagram.com/data/shared_data/"
INSTAGRAM_EDIT_PROFILE = "https://www.instagram.com/accounts/edit/"

SESSION = requests.session()
Tries = 0

with open('/Users/imsemihk/Desktop/Instagram-Turbo/config.json', 'r') as f:
    config = json.load(f)

def GetCSRF():
    try:
        return json.loads(SESSION.get(INSTAGRAM_LOGIN_CSRF, headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}).text)['config']['csrf_token']
    except Exception:
        print("Failed to get CSRF TOKEN.")

D = {"first_name":"sim#1337","email":config["EMAIL"],"username":config["USERNAME"],"phone_number":config["PHONE_NUMBER"],"biography":"Sim's Instagram Turbo! sim#1337","external_url":""}
H = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-type': 'application/x-www-form-urlencoded','origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/accounts/edit/','Cookie':f'sessionid={config["SESSION"]}',"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0","X-CSRFToken":GetCSRF(),'x-instagram-ajax': '1','x-requested-with': 'XMLHttpRequest'}

async def ClaimUsername(session):
    try:
        async with session.post(INSTAGRAM_EDIT_PROFILE, headers=H, data=D) as response:
            if response.status == 400:
                print(f"{Fore.PURPLE} ATTEMPTING TO CLAIM {Fore.WHITE}| {Fore.CYAN}TRIES: [{Tries}] {Fore.WHITE}| {Fore.BLUE}ERROR: [{response.status}]")
            elif response.status == 200:
                print(f"{Fore.YELLOW}CLAIMED USERNAME: [{config['username']}] {Fore.WHITE}| {Fore.CYAN}TRIES: [{Tries}] {Fore.WHITE}| {Fore.GREEN}ERROR: [{response.status}]")
                input("")
                exit()
            else:
                print(f"{Fore.RED}RATELIMITED {Fore.WHITE}| {Fore.CYAN}TRIES: [{Tries}] {Fore.WHITE}| {Fore.RED}ERROR: [{response.status}]")
    except Exception:
        print(f"{Fore.RED}Network Related Error {Fore.WHITE}| {Fore.RED}TRIES: [{Tries}]")

async def ClaimUsernameProxies(session):
    try:
        async with session.post(INSTAGRAM_EDIT_PROFILE, headers=H, data=D, proxy=f"{random.choice(open('proxies.txt').readlines()).strip()}") as response:
            if response.status == 400:
                print(f"{Fore.PURPLE} ATTEMPTING TO CLAIM {Fore.WHITE}| {Fore.CYAN}TRIES: [{Tries}] {Fore.WHITE}| {Fore.BLUE}ERROR: [{response.status}]")
            elif response.status == 200:
                print(f"{Fore.YELLOW}CLAIMED USERNAME: [{config['username']}] {Fore.WHITE}| {Fore.CYAN}TRIES: [{Tries}] {Fore.WHITE}| {Fore.GREEN}ERROR: [{response.status}]")
                input("")
                exit()
            else:
                print(f"{Fore.RED}RATELIMITED {Fore.WHITE}| {Fore.CYAN}TRIES: [{Tries}] {Fore.WHITE}| {Fore.RED}ERROR: [{response.status}]")
    except Exception:
        print(f"{Fore.RED}Network Related Error {Fore.WHITE}| {Fore.RED}TRIES: [{Tries}]")

async def StartTurbo(THREADS):
    async with aiohttp.ClientSession() as session:
        tasks = []
        global Tries
        for _ in range(THREADS):
            Tries = Tries + 1
            task = asyncio.ensure_future(ClaimUsername(session))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)

async def StartTurboProxies(THREADS):
    async with aiohttp.ClientSession() as session:
        tasks = []
        global Tries
        for _ in range(THREADS):
            Tries = Tries + 1
            task = asyncio.ensure_future(ClaimUsernameProxies(session))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)

if __name__ == "__main__":
    os.system("cls")
    print(f"""{Fore.BLUE}
███████╗██╗███╗   ███╗███████╗    ██╗███╗   ██╗███████╗████████╗ █████╗  ██████╗ ██████╗  █████╗ ███╗   ███╗    ████████╗██╗   ██╗██████╗ ██████╗  ██████╗ 
██╔════╝██║████╗ ████║██╔════╝    ██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝ ██╔══██╗██╔══██╗████╗ ████║    ╚══██╔══╝██║   ██║██╔══██╗██╔══██╗██╔═══██╗
███████╗██║██╔████╔██║███████╗    ██║██╔██╗ ██║███████╗   ██║   ███████║██║  ███╗██████╔╝███████║██╔████╔██║       ██║   ██║   ██║██████╔╝██████╔╝██║   ██║
╚════██║██║██║╚██╔╝██║╚════██║    ██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║   ██║██╔══██╗██╔══██║██║╚██╔╝██║       ██║   ██║   ██║██╔══██╗██╔══██╗██║   ██║
███████║██║██║ ╚═╝ ██║███████║    ██║██║ ╚████║███████║   ██║   ██║  ██║╚██████╔╝██║  ██║██║  ██║██║ ╚═╝ ██║       ██║   ╚██████╔╝██║  ██║██████╔╝╚██████╔╝
╚══════╝╚═╝╚═╝     ╚═╝╚══════╝    ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝       ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═════╝  ╚═════╝ 
""")
    CHOICE = input(f"                                                       {Fore.MAGENTA}[1 = NO PROXIES | 2 = PROXIES] :: ")
    THREADS = input(f"                                                       {Fore.MAGENTA}[Amount of THREADS] :: ")
    if int(CHOICE) == 1:
        while True:
            asyncio.get_event_loop().run_until_complete(StartTurbo(int(THREADS)))
    elif int(CHOICE) == 2:
        while True:
            asyncio.get_event_loop().run_until_complete(StartTurboProxies(int(THREADS)))   



