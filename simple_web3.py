from web3 import Web3
from web3 import EthereumTesterProvider

provider = EthereumTesterProvider()
w3 = Web3(provider)

latest_block = w3.eth.get_block('latest')
print(latest_block, '\n')

accounts = w3.eth.accounts
first_account = accounts[0]
print(accounts, '\n')

wei_balance_first_account = w3.eth.get_balance(first_account)
print(wei_balance_first_account, '\n')

ether_amt = w3.fromWei(wei_balance_first_account, 'ether')
print(ether_amt, '\n')