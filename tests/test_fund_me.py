from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHIAN_ENVIROMENT
from scripts.deploy import deploy_fund_me
from brownie import network, accounts, exceptions
import pytest


def test_can_fund_withdraw():
    account = get_account()
    crt_add = deploy_fund_me()
    entrance_fee = crt_add.getEntranceFee()  # + 100

    trx1 = crt_add.fund({"from": account, "value": entrance_fee})
    trx1.wait(1)  # search its importance
    assert crt_add.addressToAmountFunded(account.address) == entrance_fee

    trx2 = crt_add.withdraw({"from": account})
    trx2.wait(1)
    assert crt_add.addressToAmountFunded(account.address) == 0


def test_onlyOwner():
    if network.show_active() not in LOCAL_BLOCKCHIAN_ENVIROMENT:
        pytest.skip("only for local testing")
    account = get_account()
    bad_actor = accounts.add()
    crt_add = deploy_fund_me()
    with pytest.raises(exceptions.VirtualMachineError):
        crt_add.withdraw({"from": bad_actor})
