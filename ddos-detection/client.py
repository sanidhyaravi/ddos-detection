import requests
import random
import time

def send_data_packets(url, total_packets, attack_probability=0.1):
    for _ in range(total_packets):
        data = {
            "user_id": random.randint(1, 1000),
            "timestamp": time.time()
        }
        if random.random() < attack_probability:
            data["attack"] = True
        else:
            data["attack"] = False
        
        response = requests.post(url, json=data)
        print(f"Sent packet: {data}, Response: {response.status_code}")
        time.sleep(random.uniform(0.1, 0.5))

if __name__ == "__main__":
    server_url = "http://localhost:5000/data"
    total_packets = 100
    attack_probability = 0.3  # 30% of the packets are attack packets
    send_data_packets(server_url, total_packets, attack_probability)
