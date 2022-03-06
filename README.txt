How to run?
----------------------------
    1. Download the file and unzip it
    2. locate the file
    3. Find the path of the file
    4. open your terminal
    5. Make sure you have pip and python installed
        a. Heres a guide that can help you figure it out: https://www.geeksforgeeks.org/how-to-install-pip-on-windows/
        b. You can google the one for mac theres lots of guides
    6. once you have everything installed, navigate to the folder
        a. you can use the command "ls" to see what files and directories are in your current working directory
        b. you can use the command "cd" to navigate to a directory in the current working directory
        c. you can see if the python file is in your current working directory and if it is proceed to stwp 7
    7. type "python Auditing-Test.py" and press enter
    8. The program should run!
    9. email or text me if you cant get it to work






How to understand the input?
-----------------------------
Semester: 3 <-- "Semester" (which is just a cycle here) this program assumes semester 1 is
                 when the auditing is done for the first time

Cycle: 1 <-- This represents how many three-semester cycles have been executed

Clubs: <-- This is a list of all of the currently "active" clubs at the beginning of each cycle
1 2 3 4 5 6 7

Clubs Audited Semester 3: <-- These are the clubs that were selected to be audited for the current semester
2 3 4

-- The following lines are the past audits conducted labeled by semester --
Semester 1 audit:
10 9 7
Semester 2 audit:
6 1 5
Semester 3 audit: <-- This should be the same as Clubs Audited for the current semester
2 3 4
-------------

Club Change: -2 <-- Represents the change in the number of active clubs requesting funding

End of Semester 3 eligible clubs <-- A list of clubs that are eligible to be audited in the next semester
10 9 7 6 1 5

End of Semester 3 priority clubs <-- A list of clubs that will be audited in the next semester
                                     (if blank, all clubs audited next semester are being chosen randomly)