from web3 import Web3
from web3 import EthereumTesterProvider

provider = EthereumTesterProvider()
w3 = Web3(provider)

# access all accounts:
# [0x##, 0x##, 0x##...]
accounts = w3.eth.accounts

sender = accounts[0]
receiver = accounts[1]
print('Sender: ', sender, '\n', 'Receiver: ', receiver, '\n')

# minimum gas value:
gas = 21000

# value to send:
value = w3.toWei(333, 'ether')

# send transaction to blockchain:
transaction = w3.eth.send_transaction({
  'to': receiver,
  'from': sender,
  'gas': gas,
  'value': value
})
print('Transaction: ', transaction)

receipt = w3.eth.getTransactionReceipt(transaction)
print('Receipt: ', receipt, '\n\n')

latest_block = w3.eth.get_block('latest')
print('BLOCK: ', latest_block)
