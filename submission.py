import onnxruntime as ort
import numpy as np
import requests
import os


SEED = "98991645"      
TOKEN = "10926635"     
ONNX_PATH = "C:\\Users\\Prasad Patil\\Desktop\\Real\\Model_01.onnx"
# ONNX_PATH = "C:\\Users\\Prasad Patil\\Desktop\\Real\\Model_02.onnx"
# ONNX_PATH = "C:\\Users\\Prasad Patil\\Desktop\\Real\\stolen_encoder.pth"


print("🔍 Testing ONNX format...")
with open(ONNX_PATH, "rb") as f:
    model_data = f.read()
    try:
        session = ort.InferenceSession(model_data)
        dummy_input = np.random.randn(1, 3, 32, 32).astype(np.float32)
        output = session.run(None, {"x": dummy_input})[0]
        print("✅ ONNX model valid | Output shape:", output.shape)
        assert output.shape == (1, 1024), "Output shape must be (1, 1024)"
    except Exception as e:
        raise RuntimeError("Failed ONNX check:", e)

# === Submit to Leaderboard ===
print("Submitting to leaderboard...")
url = "http://34.122.51.94:9090/stealing"
headers = {"token": TOKEN, "seed": SEED}

with open(ONNX_PATH, "rb") as f:
    response = requests.post(url, files={"file": f}, headers=headers)

if response.status_code == 200:
    print("Server Response:", response.json())
else:
    print(f"Submission failed: {response.status_code}\n{response.text}")
