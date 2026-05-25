import pytest
from genlayer import *
from contracts.decentrajudge_contract import DecentraJudge

def test_decentrajudge_payout_flow(direct_vm, direct_deploy):
    # 1. Use Direct Mode to mock the LLM non-comparative consensus rule
    # This simulates GenLayer validators agreeing that the work meets requirements
    direct_vm.mock_llm(
        pattern=".*Analyze the text data and determine if it satisfies this goal.*",
        response="YES"
    )

    # 2. Mock the internet lookup behavior
    # This ensures that when the contract queries the web, it gets back a mock webpage
    direct_vm.mock_web(
        pattern=".*example.org.*",
        response={"method": "GET", "status": 200, "body": "Web3 freelance delivery text content is complete."}
    )

    # 3. Deploy our Intelligent Contract directly into memory
    contract = direct_deploy(
        "contracts/decentrajudge_contract.py", 
        "0xClientAddress123", 
        "@MorenWeb3", 
        "Write a professional promotion thread about GenLayer testnet."
    )
    
    # 4. Check the initial setup state is uncompleted (False)
    assert contract.get_status() is False

    # 5. Trigger the smart contract's validation logic
    contract.verify_and_pay()
    
    # 6. Confirm that the state successfully shifted to True
    assert contract.get_status() is True