// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StudentData {

    // Define a structure to represent a Student
    struct Student {
        uint id;
        string name;
        uint age;
        string course;
    }

    // Create an array to store multiple students
    Student[] public students;

    // Fallback function to accept ether sent to the contract
    // This function gets triggered when ether is sent to the contract without calling a specific function
    fallback() external payable {
        // Optionally, we could log an event or perform other actions when funds are received
    }

    // Function to add a new student
    function addStudent(uint _id, string memory _name, uint _age, string memory _course) public {
        // Add the student to the array
        students.push(Student(_id, _name, _age, _course));
    }

    // Function to get the total number of students
    function getTotalStudents() public view returns (uint) {
        return students.length;
    }

    // Function to retrieve student data by ID
    function getStudentById(uint _id) public view returns (uint, string memory, uint, string memory) {
        for (uint i = 0; i < students.length; i++) {
            if (students[i].id == _id) {
                return (students[i].id, students[i].name, students[i].age, students[i].course);
            }
        }
        revert("Student not found");
    }

    // Function to retrieve the contract balance
    function getBalance() public view returns (uint) {
        return address(this).balance;
    }
}