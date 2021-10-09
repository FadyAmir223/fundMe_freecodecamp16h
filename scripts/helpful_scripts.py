from brownie import network, accounts, config, MockV3Aggregator


DECIMALS = 8
START_PRICE = 2000e8
LOCAL_BLOCKCHIAN_ENVIROMENT = ["development", "ganache-local-dev"]
FORKED_LOCAL_ENVIROMENTS = ["mainnet-fork"]


def get_account():
    if network.show_active() in (
        LOCAL_BLOCKCHIAN_ENVIROMENT or FORKED_LOCAL_ENVIROMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mock():
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, START_PRICE, {"from": get_account()})
