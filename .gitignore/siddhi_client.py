import socket
import webbrowser as wb
#from texttospeech import *
chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

client=socket.socket()
client.connect(("172.20.10.2",1233))


while True:
    data=(client.recv(1000)).decode()
    if data=='detected':
        wb.get(chrome_path).open('''https://maker.ifttt.com/trigger/intruder/with/key/cCfpbVMJZa63HcFSJJGSBW''')
