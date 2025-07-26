#!/bin/bash

echo "🚀 Installing AmanAI..."
sudo apt update && sudo apt install -y git python3 python3-pip

git clone https://github.com/amankumar/aiRepoWork.git ~/amanai
cd ~/amanai

echo "✅ AmanAI is ready. To begin: python3 main.py"
