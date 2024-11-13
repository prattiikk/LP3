// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract BankAccount {

    // Mapping to store the balance of each user
    mapping(address => uint256) private balances;

    // Events to log deposit, withdrawal, and balance checks
    event Deposited(address indexed account, uint256 amount);
    event Withdrawn(address indexed account, uint256 amount);
    event BalanceChecked(address indexed account, uint256 balance);

    // Deposit money to the bank account
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than 0");
        
        balances[msg.sender] += msg.value;
        emit Deposited(msg.sender, msg.value);
    }

    // Withdraw money from the bank account
    function withdraw(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(balances[msg.sender] >= amount, "Insufficient funds");

        balances[msg.sender] -= amount;
        payable(msg.sender).transfer(amount);
        emit Withdrawn(msg.sender, amount);
    }

    // Check balance of the user
    function checkBalance() external returns (uint256) {
        uint256 balance = balances[msg.sender];
        emit BalanceChecked(msg.sender, balance);
        return balance;
    }
}