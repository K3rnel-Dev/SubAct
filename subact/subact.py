# CREATED BY K3RNEL-DEV
# GIT:https://github.com/K3rnel-dev/
import sys
import requests
import concurrent.futures
from os import system

# Colors
GREEN = '\033[1;32m'
RED = '\033[1;31m'
RESET = '\033[0m'


def logo():
    system('clear')
    print(f"{RED}  ██████  █    ██  ▄▄▄▄    ▄▄▄       ▄████▄  ▄▄▄█████▓")
    print(f"▒██    ▒  ██  ▓██▒▓█████▄ ▒████▄    ▒██▀ ▀█  ▓  ██▒ ▓▒")
    print(f"░ ▓██▄   ▓██  ▒██░▒██▒ ▄██▒██  ▀█▄  ▒▓█    ▄ ▒ ▓██░ ▒░")
    print(f"  ▒   ██▒▓▓█  ░██░▒██░█▀  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒░ ▓██▓ ░ ")
    print(f"▒██████▒▒▒▒█████▓ ░▓█  ▀█▓ ▓█   ▓██▒▒ ▓███▀ ░  ▒██▒ ░ ")
    print(f"▒ ▒▓▒ ▒ ░░▒▓▒ ▒ ▒ ░▒▓███▀▒ ▒▒   ▓▒█░░ ░▒ ▒  ░  ▒ ░░   ")
    print(f"░ ░▒  ░ ░░░▒░ ░ ░ ▒░▒   ░   ▒   ▒▒ ░  ░  ▒       ░    ")
    print(f"░  ░  ░   ░░░ ░ ░  ░    ░   ░   ▒   ░          ░      ")
    print(f"      ░     ░      ░            ░  ░░ ░               ")
    print(f"                        ░           ░                  ")
    print('\t\t--=By: K3rnel-Dev=--\t\t')
    print('\t   Git:https://github.com/K3rnel-Dev\t\t')


def check_domain_status(domain):
    try:
        response = requests.get(f"http://{domain}", timeout=5)
        if response.status_code == 200:
            return domain, f"{GREEN}ONLINE{RESET}"
    except requests.exceptions.RequestException:
        pass
    return None


def main():
    logo()
    if len(sys.argv) < 2:
        print("Usage: python3 activesub.py <filename> [output_filename]")
        return

    filename = sys.argv[1]
    output_filename = sys.argv[2] if len(sys.argv) > 2 else None

    with open(filename, "r") as file:
        domains = file.readlines()

    domains = [domain.strip() for domain in domains]  # Удаляем символы новой строки и пробелы в начале и конце

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(check_domain_status, domain) for domain in domains]

        online_domains = []
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result:
                domain, status = result
                online_domains.append((domain, status))
                print(f"{domain}: {status}")

    if output_filename:
        with open(output_filename, "w") as output_file:
            for domain, status in online_domains:
                output_file.write(f"{domain}: {status}\n")


if __name__ == "__main__":
    main()
