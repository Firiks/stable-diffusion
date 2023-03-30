"""
Debug information for CUDA devices. Detects if CUDA is available.
"""

import torch

available = torch.cuda.is_available()
device_count = torch.cuda.device_count()
current_device = torch.cuda.current_device()
device_name = torch.cuda.get_device_name(current_device)

print(f"Available: {str(available)}")
print(f"Device count: {str(device_count)}")
print(f"Current device: {str(current_device)}")
print(f"Device name: {str(device_name)}")
