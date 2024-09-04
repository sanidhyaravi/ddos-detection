from flask import Flask, request, jsonify
import math
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

PACKETS = []
THRESHOLD = 1.5  # Example threshold for entropy

def calculate_entropy(data):
    # Calculate entropy based on packet data
    packet_count = len(data)
    if packet_count == 0:
        return 0
    return math.log2(packet_count)  # Simplified example

@app.route('/data', methods=['POST'])
def receive_data():
    packet = request.json
    PACKETS.append(packet)
    
    if len(PACKETS) % 50 == 0:
        entropy = calculate_entropy(PACKETS)
        ddos_detected = entropy > THRESHOLD
        accuracy = 0.85  # Example accuracy value
        
        # Log the results
        logger.info(f"Entropy: {entropy:.2f}, DDoS Detected: {ddos_detected}, Accuracy: {accuracy:.2f}")
        
        # Clear the packets list for the next set of data
        PACKETS.clear()
        
        return jsonify({
            'entropy': entropy,
            'ddos_detected': ddos_detected,
            'accuracy': accuracy
        })
    
    return 'OK', 200

if __name__ == '__main__':
    app.run(debug=True)
