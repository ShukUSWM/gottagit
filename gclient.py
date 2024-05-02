import socket


host = "192.168.1.7"
port = 7777

while True:
    s = socket.socket()
    try:
        s.connect((host, port))

        data = s.recv(1024) # received the banner
        print(data.decode().strip())  # print banner

        while True:
            user_input = input("").strip()  # let get our input from the user

            s.sendall(user_input.encode())
            reply = s.recv(1024).decode().strip()

            if not reply:
                print("Server closed the connection")
                break

            if "correct" in reply:
                print(reply)
                break

            print(reply)

            # Ask the user if they want to play again or quit
            print("\n")
            print("Do you want to:")
            print("1. Play Again?")
            print("2. Quit the game?")
            choice = input("Enter corresponding number: ")
            if choice != "1":
                print("Thanks For Playing :DDD")
                break

    except ConnectionAbortedError:
        print("Connection was aborted by the software in you host. Please try again.")
    except ConnectionResetError:
        print("Connection was reset by the server. Please try again")
    finally:
        s.close()


