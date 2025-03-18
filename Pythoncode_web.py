from web3 import Web3

# Connect to Anvil (local blockchain)
anvil_url = "http://127.0.0.1:8545"
web3 = Web3(Web3.HTTPProvider(anvil_url))

# Check if connected
if web3.is_connected():
    print("✅ Connected to Anvil!")
else:
    print("❌ Connection failed.")
