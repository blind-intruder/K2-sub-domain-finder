import requests,sys,os


def banner():
    print("""

 _   __ _____    _____         _       ______  _             _             
| | / // __  \  /  ___|       | |      |  ___|(_)           | |            
| |/ / `' / /'  \ `--.  _   _ | |__    | |_    _  _ __    __| |  ___  _ __ 
|    \   / /     `--. \| | | || '_ \   |  _|  | || '_ \  / _` | / _ \| '__|
| |\  \./ /___  /\__/ /| |_| || |_) |  | |    | || | | || (_| ||  __/| |   
\_| \_/\_____/  \____/  \__,_||_.__/   \_|    |_||_| |_| \__,_| \___||_|          
                                                                       
                       By: Blind Intruder

             A comprehensive multi level sub domain finder
============================================================================
	""")
thirdlevelsubs=[]
def checkarg():
	if((len(sys.argv)-1)==1):
		os.system("clear")
		banner()
	else:
		print('\033[31m' +"\nMissing or invalid arguments.\nUsage: python3 k2_sub_finder.py target.com\nEnter domain without www.\nExample:hackme.com"+ '\033[0m')
		exit(0)

def checkhost():
	host =sys.argv[1]
	if(os.system("ping -c 1 " + host)==0):
		checkarg()
		print("\nExtracting 2nd level sub domains\n")
		secondlevel()
	else:
		print("Unable to connect to the target domain")

def secondlevel():
	words=open("assets/subs.txt")
	l=words.read()
	subs=l.splitlines()
	host =sys.argv[1]
	for sub in subs:
		subd=f"http://{sub}.{host}"
		subdo=sub+"."+host
		try:
			requests.get(subd)
			res=requests.get(subd)
			code=str(res.status_code)
		except:
			pass
		else:
			thirdlevelsubs.append(subdo)
			print('\033[32m' +"--> Sub domain found:  "+subd+" -->"+code+ '\033[0m')
			getcname(subdo)
	thirdlevel()

def thirdlevel():
	words=open("assets/subs.txt")
	l=words.read()
	subs=l.splitlines()
	for i in thirdlevelsubs:
		host =str(i)
		for sub in subs:
			subd=f"http://{sub}.{host}"
			try:
				requests.get(subd)
				res=requests.get(subd)
				code=str(res.status_code)
			except:
				pass
			else:
				print('\033[32m' +"--> Sub domain found:  "+subd+" -->"+code+ '\033[0m')

def getcname(sdomain):
	os.system("host "+sdomain)
checkhost()
