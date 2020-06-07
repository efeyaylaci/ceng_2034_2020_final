# Name: Efe Yaylacı

import os , requests, uuid, hashlib
from multiprocessing import Pool


#assignment 1

def create_child(): 
	global child
	child = os.fork()
  	if child == 0: 
		print("Child process id is: ", os.getpid()) 
	
create_child()


#assignment 2

urls =["http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg","https://upload.wikimedia.org/wikipedia/tr/9/98/Mu%C4%9Fla_S%C4%B1tk%C4%B1_Ko%C3%A7man_%C3%9Cniversitesi_logo.png","https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024px-Hawai%27i.jpg","http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg","https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024px-Hawai%27i.jpg"]

def download_file(url, file_name=None):
	r = requests.get(url, allow_redirects=True)
	file = file_name if file_name else str(uuid.uuid4())
	open(file, 'wb').write(r.content)

n=0
if child == 0:
	for url in urls:
		n = n + 1
		name = str(n)
		download_file(url, name)


#assignment 3

if child == 0:
	print('Terminated process id is: ', os.getpid())
	os._exit(0)	


#assignment 4 (in this assignment i couldn't use multiprocessing because i didn't understand how i can use it with a function which uses list. Below code is still working for my objective: finding duplicates in a file)

files_list = os.listdir('.')
files_list.sort()
duplicates = []
hash_keys = dict()
t = 0
for filename in files_list:
	t = t + 1
	with open(filename, 'rb') as f:
		filehash = hashlib.md5(f.read()).hexdigest()
	if filehash not in hash_keys: 
		hash_keys[filehash] = t
	else:
		duplicates.append(( t, hash_keys[filehash]))

print(duplicates)
