// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StudentData {

    // Define the structure for a student
    struct Student {
        string name;
        uint256 rollno;
        string class;
    }

    // Create a private array to store the student data
    Student[] private students;

    // Function to add a new student to the array
    function addStudent(string memory name, uint256 rollno, string memory class) public {
        // Push a new student to the array
        students.push(Student(name, rollno, class));
    }

    // Function to get a student's details by their index
    function getStudentById(uint256 id) public view returns (string memory, uint256, string memory) {
        // Ensure the id is valid and within bounds of the students array
        require(id < students.length, "Student does not exist in database");
        
        // Return the student's details based on their index
        return (students[id].name, students[id].rollno, students[id].class);
    }

    // Function to get the total number of students in the database
    function getTotalNumberOfStudents() public view returns (uint256) {
        return students.length;
    }
}