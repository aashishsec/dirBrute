import requests

import colorama

import random

import argparse

import concurrent.futures

from datetime import datetime

from colorama import Fore, Back, Style

colorama.init(autoreset=True)

green = Fore.GREEN

magenta = Fore.MAGENTA

cyan = Fore.CYAN

mixed = Fore.RED + Fore.BLUE

red = Fore.RED

blue = Fore.BLUE

yellow = Fore.YELLOW

white = Fore.WHITE

reset = Style.RESET_ALL

colors = [magenta,cyan,mixed,red,blue,yellow, white]

random_color = random.choice(colors)

bold = Style.BRIGHT

USER_AGENT  = [
        
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",

    "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36",

    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9",

    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",

    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36",

    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36 Edg/99.0.1150.36",

    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",

    "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36",

    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0",

     ]
     

random_user_agent = random.choice(USER_AGENT)

parser=argparse.ArgumentParser(description=f"{bold}{random_color} DirBrute is a tool designed to efficiently probe for alive endpoints from a provided wordlist list.")

parser.add_argument('-d','--Domain',metavar='list',type=str,required=True,help=f"[{bold}{random_color}INFO]: {bold}{random_color}domain.")

parser.add_argument('-w','--wordlist',metavar='list',type=str,required=True,help=f"[{bold}{random_color}INFO]: {bold}{random_color}List of wordlist.")

parser.add_argument('-o','--output',metavar='output',type=str,default="DirBrute_output.txt",required=False,help=f"[{bold}{random_color}INFO]: {bold}{random_color}File to save our output.")

parser.add_argument("-t", "--threads", help=f"[{bold}INFO{random_color}]: {random_color}{random_color}Threading level to make fast process", type=int, default=10)

args=parser.parse_args()

Domain=args.Domain

output=args.output

threads=args.threads

wordlist=args.wordlist

global_output=[]

path=[]

def banner():

    print(f'''{bold}{random_color}

██████╗░██╗██████╗░░░░██████╗░██████╗░██╗░░░██╗████████╗███████╗
██╔══██╗██║██╔══██╗░░░██╔══██╗██╔══██╗██║░░░██║╚══██╔══╝██╔════╝
██║░░██║██║██████╔╝░░░██████╦╝██████╔╝██║░░░██║░░░██║░░░█████╗░░
██║░░██║██║██╔══██╗░░░██╔══██╗██╔══██╗██║░░░██║░░░██║░░░██╔══╝░░
██████╔╝██║██║░░██║██╗██████╦╝██║░░██║╚██████╔╝░░░██║░░░███████╗
╚═════╝░╚═╝╚═╝░░╚═╝╚═╝╚═════╝░╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░╚══════╝
      
        Author   : Aashish💕💕  
                                              
        Github   : https://github.com/aashishsec
          
        DirBrute is a tool designed to efficiently probe for alive endpoints from a provided wordlist list.
          
      ''')
    print("-" * 80)

    checking_vesion()

    print(f"{bold}{random_color}pyDirBrute starting at {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")

    print("-" * 80)

    print(f"{bold}{random_color}[*] URL".ljust(20, " "), ":", Domain)

    print(f"{bold}{random_color}[*] Wordlist".ljust(20, " "), ":",wordlist)

    print(f"{bold}{random_color}[*] Threads".ljust(20, " "), ":", threads)

def checking_vesion():

    version = "v1.0.2"
    
    url = f"https://api.github.com/repos/aashishsec/dirBrute/releases/latest"
    
    try:
            
         response =  requests.get(url, timeout=10)
          
         if response.status_code == 200:
            
            data = response.json()
                
            latest = data.get('name')
            
            if latest == version:
                
                    message = "latest"
                
                    print(f"[{blue}Version{reset}]: {bold}{white}dirBrute current version {version} ({green}{message}{reset})")
                
                    t.sleep(1)
                
            else:
                
                    message ="outdated"
                
                    print(f"[{blue}Version{reset}]: {bold}{white}dirBrute current version {version} ({red}{message}{reset})")

            
    except KeyboardInterrupt as e:
        
            print(f"[{blue}INFO{random_color}]: dirBrute says BYE!")
        
            exit()
                
    except Exception as e:

           pass


def DirBrute(domain,path):

    global global_output

    try:

            if domain[0:5]=="https" or domain[0:7]=="http://":
                  
                  if path[0]=="/":
                        
                       url=f"{domain}{path}"

                  else:
                        
                        url=f"{domain}/{path}"

            else:
                    if path[0]=="/":
                       
                       url="https://{}{}".format(domain,path)

                    else:

                        url="https://{}/{}".format(domain,path)

            request=requests.get(url,timeout=30,headers={"User-Agent": random_user_agent},allow_redirects=True)

            statusCode=request.status_code

            content_length = request.headers.get('Content-Length')

            if statusCode== 200:

               if content_length is not None:
                   
                   print(f"{green}(Status: {statusCode}) --[Size: {content_length}]---> {url}")

                   global_output.append(f"(Status: {statusCode}) --[Size: {content_length}]---> {url}\n")

               else:
                   
                   print(f"{green}(Status: {statusCode}) --[Size: {len(request.content)}]---> {url}")

                   global_output.append(f"(Status: {statusCode}) --[Size: {len(request.content)}]---> {url}\n")

            elif statusCode==404 or statusCode==429:
                 
                 pass
            
            else:
               
                print(f"{random_color}(Status: {statusCode}) --[Size: {len(request.content)}]---> {url}")

                global_output.append(f"(Status: {statusCode}) --[Size: {len(request.content)}]---> {[path]}\n")
                
    except KeyboardInterrupt as e:
        
            print(f"[{blue}INFO{random_color}]: httpAlive says BYE!")
        
            exit()
                
    except Exception as e:
        
           pass

def saveOutput(output):

    with open(output, 'w') as file:
        
        file.writelines(global_output)


def threading(Domain,paths):
    
    try:

        with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
            
           futures = [executor.submit(DirBrute, Domain,path) for path in paths]
           
        concurrent.futures.wait(futures)
           
    except KeyboardInterrupt as e:
        
        print(f"[{bold}INFO{random_color}]: dirBrute says exit!")
        
        exit()

    except Exception as e:
        
        pass 


def main():
        
    banner()

    global path
    
    try:
        with open(wordlist,"r") as p:
       
           paths=p.read().splitlines()
        
           for p in paths:
          
               path.append(p)
        
        print(f"{bold}{random_color}[*] No.of Words".ljust(20, " "), ":", len(path))

        print("-" * 80)

        threading(Domain,path)

        saveOutput(output) 
           
    except KeyboardInterrupt as e:
        
        print(f"[{blue}INFO{random_color}]: dirbrute says exit!")
        
        exit()

    except Exception as e:
        
        pass 

if __name__ == "__main__":

    main()

