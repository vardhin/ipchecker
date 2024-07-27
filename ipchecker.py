import time
import os
import requests

# Define the file to store the IP address
IP_FILE = 'ip.txt'
CHECK_IP_URL = 'http://checkip.amazonaws.com'

def get_current_ip():
    try:
        response = requests.get(CHECK_IP_URL)
        return response.text.strip()
    except requests.RequestException as e:
        print(f"Error retrieving IP: {e}")
        return None

def update_ip_file(ip_address):
    with open(IP_FILE, 'w') as file:
        file.write(ip_address)

def main():
    while True:
        current_ip = get_current_ip()
        if current_ip:
            if os.path.exists(IP_FILE):
                with open(IP_FILE, 'r') as file:
                    previous_ip = file.read().strip()
            else:
                previous_ip = None

            if current_ip != previous_ip:
                print(f"IP changed: {current_ip}")
                update_ip_file(current_ip)
                # Optional: Update DNS or notify about the IP change here
            else:
                print(f"IP unchanged: {current_ip}")

        time.sleep(60)  # Wait for 60 seconds

if __name__ == '__main__':
    main()
