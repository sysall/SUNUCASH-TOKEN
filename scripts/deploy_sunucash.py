from brownie import SunucashToken
from scripts.helpful_scripts import get_account
from web3 import Web3

initial_supply = Web3.toWei(14000000, "ether")

def main():
    account = get_account()
    sunucash_token = SunucashToken.deploy(initial_supply, {"from": account})
    print(sunucash_token.name())
    print(sunucash_token.symbol())
