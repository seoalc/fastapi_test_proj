from tronpy import Tron

client = Tron()
new_wallet = client.generate_address()
print(new_wallet)
# print("Private Key:", new_wallet["private_key"])
# print("Public Address:", new_wallet["address"])