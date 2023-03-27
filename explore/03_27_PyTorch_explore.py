#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 14:26:54 2023

@author: dantan
"""

import torch
x = torch.rand(5, 3)
print(x)

print(torch.backends.mps.is_available())
print(torch.backends.mps.is_built())

# In[]



# In[]

