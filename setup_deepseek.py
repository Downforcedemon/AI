'''
# Libraries
transformers: To load and use Hugging Face models.
accelerate: For optimization in CPU environments.
bitsandbytes: To enable quantized models (if supported).
datasets: If any datasets are needed for testing.
torch: Install a CPU-compatible version.
'''

'''
pip install transformers accelerate bitsandbytes datasets flask 
pip install torch --index-url https://download.pytorch.org/whl/cpu
'''

pip install open-webui

open-webui serve

# ntegrate Your Model
vim ~/.open-webui/config.json

# Add your Flask API endpoint (http://<YOUR_SERVER_IP>:5000/generate) to the configuration
{
    "model": {
        "type": "remote",
        "endpoint": "http://192.168.4.31:5000/generate",
        "tokenizer": "huggingface",
        "name": "DeepSeek-Qwen-14B"
    },
    "ui": {
        "host": "0.0.0.0",
        "port": 8080
    }
}

# start or restart
open-webui serve



