import os
import subprocess
from pathlib import Path

def get_env_size(env_name: str) -> float:
    conda_base = subprocess.check_output(['conda', 'info', '--base']).decode().strip()
    env_path = os.path.join(conda_base, "envs", env_name)
    
    if not os.path.exists(env_path):
        return 0.0
        
    total_size = 0
    for dirpath, _, filenames in os.walk(env_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    
    return total_size / (1024 ** 2)  # Convert to MB

for env_name in [
    "dspy",
    "langgraph",
    "pydanticai",
    "smolagents",
    "browser-use",
]:
    size_mb = get_env_size(env_name)
    print(f"Environment '{env_name}' size: {size_mb:.2f} MB")
