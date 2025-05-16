# Sample code for recommendation accuracy improvement tracking
from sklearn.metrics import accuracy_score
import time

def evaluate_model(predictions, true_labels):
    accuracy = accuracy_score(true_labels, predictions)
    print("Model Accuracy:", accuracy)
    return accuracy

# Sample chatbot response latency measurement (in milliseconds)
def generate_response(user_input):
    # Simulate response logic (you can replace this with real chatbot logic)
    time.sleep(0.1)
    return "Thank you for reaching out!"

def chatbot_response(user_input):
    start = time.time()
    response = generate_response(user_input)
    end = time.time()
    latency = (end - start) * 1000
    print(f"Chatbot Response: {response}")
    print(f"Response Time: {latency:.2f} ms")
    return response

# Sample IoT engagement tracking
class IoTDevice:
    def __init__(self, id):
        self.id = id
        self.connected = False

    def connect(self):
        self.connected = True
        print(f"Device {self.id} connected.")

    def send_data(self, data):
        if self.connected:
            print(f"Data from device {self.id}: {data}")
        else:
            print("Device not connected.")

# ====== Running the code with sample inputs ======
print("\n--- AI Model Performance ---")
evaluate_model([1, 0, 1, 1], [1, 0, 0, 1])

print("\n--- Chatbot Performance ---")
chatbot_response("Hi, I need help with my order.")

print("\n--- IoT Device Engagement ---")
device = IoTDevice("Device_001")
device.connect()
device.send_data("User approached smart display")
