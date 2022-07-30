import os, requests, random, string, threading, time
from colorama import Fore
os.system('title ⚡️ Token Generator ⚡️')

allproxies = open('proxies.txt', 'r').read().splitlines()
#---------------
red = Fore.RED
green = Fore.LIGHTGREEN_EX
wh = Fore.LIGHTWHITE_EX
#---------------
dur = int(input('Длительность: '))
delay = float(input('Задержка: '))
start = input('Для старта нажми Enter: ')

headers = {
"user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.600 Chrome/91.0.4472.106 Electron/13.1.4 Safari/537.36", 
}

def gen():
 nitro = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
 url = f"https://discord.gift/{nitro}"
 check = f'https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true'
 try: 
  r = requests.get(check, headers=headers, proxies ={'https://discordapp.com': random.choice(allproxies)})
  if r.status_code == 429:
   print(red, '[RATE-LIMITED] Error')
  elif r.status_code == 200:
     suc += 1
     print(green, f'[VALID]{wh} {url}')  
     with open('valid.txt', 'a') as f:
       f.write(url + '\n')
  elif r.status_code != 200:
     print(red, f'[INVALID]{wh} {url}')    
  else: 
    print(red, f'[ERROR]{wh} {url}')         
 except Exception as e:
   pass 
sec = time.time()
while time.time()<=sec+dur:
   try:
    time.sleep(delay)  
    threading.Thread(target=gen).start()  
   except:
      pass 
