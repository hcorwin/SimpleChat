import socket
import emoji

host = "127.0.0.1"
port = 8000

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host, port))
socket.listen(5)
client, address = socket.accept()


def main():

    while True:
        data = client.recv(1024).decode()
        if ":)" in data:
            data = data[0: -2]
            data = data + emoji.emojize(':smile:', use_aliases= True)
        if ";)" in data:
            data = data[0: -2]
            data = data + emoji.emojize(':wink:', use_aliases= True)
        if ":P" in data:
            data = data[0: -2]
            data = data + emoji.emojize(':stuck_out_tongue:', use_aliases= True)
        print("Becky: ", data)
        inp = input()
        client.send(inp.encode())
        if inp == "Bye" or inp == "bye":
            break
    client.close()

if __name__ == '__main__':
    main()
