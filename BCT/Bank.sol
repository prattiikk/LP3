// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Bank {

    // Mapping to track the balance of each user
    mapping(address => uint256) private balances;

    // Deposit money into the bank account
    function DepositMoney(uint256 amount) public {
        require(amount > 0, "Amount should be greater than zero");
        
        // Increase the balance of the sender by the deposit amount
        balances[msg.sender] += amount;
    }

    // Withdraw money from the bank account
    function WithdrawMoney(uint256 amount) public {
        require(amount <= balances[msg.sender], "Insufficient balance");
        
        // Decrease the balance of the sender by the withdrawal amount
        balances[msg.sender] -= amount;
    }

    // Show the balance of the caller
    function ShowBalance() public view returns (uint256) {
        return balances[msg.sender];
    }
}