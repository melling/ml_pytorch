#!/usr/bin/env python3

import torch
x = torch.cuda.is_available()
print(f"Cuda is installed={x}")