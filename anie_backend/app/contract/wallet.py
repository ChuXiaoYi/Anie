from eth_account import Account
from web3 import Web3

from app.config import config
from app.contract.abi import abi


def create_wallet_address():
    """
    Create wallet address
    :return:
    """
    address = Account.create()
    return address.address, address.key.hex()


def mint_nft(to, token_uri):
    """
    Mint NFT
    :param to: mint to address
    :param token_uri: nft token uri
    :return:
    """
    w3 = Web3(Web3.HTTPProvider(config.PROVIDER_URL))
    w3.eth.defaultAccount = Account.from_key(config.PRIVATE_KEY)

    contract = w3.eth.contract(abi=abi, address=config.CONTRACT_ADDRESS)
    increment_tx = contract.functions.safeMint(to, token_uri).build_transaction(
        {
            "from": w3.eth.defaultAccount.address,
            "nonce": w3.eth.get_transaction_count(w3.eth.defaultAccount.address)
        }
    )
    tx_create = w3.eth.account.sign_transaction(increment_tx, w3.eth.defaultAccount._private_key)

    tx_hash = w3.eth.send_raw_transaction(tx_create.rawTransaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    print(f'Tx successful with hash: {tx_receipt.transactionHash.hex()}')
    return tx_receipt.transactionHash.hex()

