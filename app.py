import subprocess

def get_wifi_password(ssid):
    try:
        result = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', f'name={ssid}', 'key=clear'], text=True)
        for line in result.split('\n'):
            if 'Key Content' in line:
                return line.split(':')[1].strip()
        return "Password not found"
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"

# Replace 'LCAT' with your actual Wi-Fi name
print(get_wifi_password('LCAT'))
