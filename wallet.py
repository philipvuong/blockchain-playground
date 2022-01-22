from web3 import Account
from web3.auto import w3
import os
from dotenv import load_dotenv
load_dotenv()
from mnemonic import Mnemonic
from bip44 import Wallet
from eth_account.messages import encode_defunct


# Load the value of the MNEMONIC variable from the .env file
mnemonic = os.getenv("MNEMONIC")

# Evaluate the contents of the mnemonic variable
# Create a new mnemonic seed phrase if the value of mnemonic equals None
if mnemonic is None:
  mnemo = Mnemonic("english")
  mnemonic = mnemo.generate(strength=128)

# generate wallet instance
wallet = Wallet(mnemonic)

# Create the public and private keys associated with a new Ethereum account
private, public = wallet.derive_account("eth")

# Create an Ethereum account by passing the private key via the Account object
account = Account.privateKeyToAccount(private)

# create message & byte encode
msg = "Zach owes David $20"
encoded_message = encode_defunct(text=msg)

# sign message with private key
signed_message = w3.eth.account.sign_message(encoded_message, private_key=private)
signed_message

# recover message.
w3.eth.account.recover_message(encoded_message, signature=signed_message.signature)
