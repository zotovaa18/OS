import requests

SERVER_URL = "http://server:8000/create"


def create_file(filename):
    payload = {"filename": filename}
    try:
        response = requests.post(SERVER_URL, json=payload)
        if response.status_code == 200:
            print(response.json())
        else:
            print(f"Error: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"Failed to connect to server: {e}")


if __name__ == "__main__":
    filename = "example.txt"
    print(f"Requesting file creation: {filename}")
    create_file(filename)
