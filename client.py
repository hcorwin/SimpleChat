import socket
import emoji

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 8000
s.connect((host, port))

def main():
    while True:
        inp = input()
        s.send(inp.encode())
        data = s.recv(1024).decode()
        if ":)" in data:
            data = data[0: -2]
            data = data + emoji.emojize(':smile:', use_aliases= True)
        if ";)" in data:
            data = data[0: -2]
            data = data + emoji.emojize(':wink:', use_aliases= True)
        if ":P" in data:
            data = data[0: -2]
            data = data + emoji.emojize(':stuck_out_tongue:', use_aliases= True)
        if inp == "Bye" or inp == "bye":
            break
        print("John:", data)
    s.close()

if __name__ == '__main__':
    main()
