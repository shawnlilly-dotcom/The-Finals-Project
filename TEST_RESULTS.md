# GameVault — Sprint 1 Test Results and Defect Log

**Team:** The Finals  
**Project:** GameVault — Video Game Collection Manager  
**Sprint:** 1  
**Task:** TEAM-01.5 — Document Test Results and Defects  
**Testing Environment:** Python, Tkinter, SQLite, Windows, VS Code

## 1. Testing Overview

The purpose of Sprint 1 testing was to verify that the initial GameVault application functions correctly and that game information is saved persistently using SQLite.

Testing focused on application startup, required-field validation, adding games, displaying saved records, database initialization, and data persistence after restarting the application.

## 2. Test Execution Results

| Test ID | Test Description | Expected Result | Actual Result | Status |
|---|---|---|---|---|
| TC-01 | Application Startup | GameVault opens successfully | Application launched and displayed the main interface | Passed |
| TC-02 | Required Field Validation | Warning appears when title is empty | Missing Title warning displayed | Passed |
| TC-03 | Add Game Functionality | Game saves successfully | World of Warcraft was added successfully | Passed |
| TC-04 | Display Saved Games | Saved game appears in collection | World of Warcraft appeared in the collection table | Passed |
| TC-05 | Database Persistence | Game remains after restart | World of Warcraft remained visible after restarting | Passed |
| TC-06 | Database Initialization | SQLite initializes successfully | Database initialized and supported saving and retrieving records | Passed |

## 3. Test Data

The following information was used to test the Add Game functionality.

| Field | Value |
|---|---|
| Title | World of Warcraft |
| Genre | MMORPG |
| Platform | PC |
| Completion Status | In Progress |

The application successfully saved the game and displayed the information in the collection table.

## 4. Database Persistence Testing

The database persistence test was performed using the following procedure:

1. Launched GameVault through VS Code.
2. Entered the World of Warcraft test information.
3. Clicked Add Game.
4. Verified that the game appeared in My Game Collection.
5. Closed the application.
6. Restarted GameVault.
7. Confirmed that the previously saved game remained visible.

**Result:** Passed.

The SQLite database retained the saved game information between application sessions.

## 5. Required-Field Validation Testing

The Title field was intentionally left blank before selecting Add Game.

**Expected Result:** The application should prevent the record from being saved and display a warning.

**Actual Result:** GameVault displayed the message "Please enter a game title."

**Result:** Passed.

## 6. Defect Log

| Defect ID | Description | Severity | Status |
|---|---|---|---|
| None | No defects identified during the six executed Sprint 1 test cases | N/A | N/A |

No defects were observed during the documented test execution. Additional testing may identify issues as new features are developed.

## 7. Testing Summary

**Total Test Cases:** 6  
**Passed:** 6  
**Failed:** 0  
**Known Defects Identified:** 0  
**Pass Rate:** 100%

All six initial test cases passed.

## 8. Sprint 1 Conclusion

Sprint 1 successfully established the foundation of the GameVault application. The team implemented a Tkinter graphical interface, SQLite database initialization, game entry functionality, and persistent data storage.

Testing confirmed that users can add games, view saved records, and retrieve their collection after restarting the application.

The completed functionality provides a foundation for future development, including editing, deleting, searching, and organizing games.

The Sprint 1 functionality covered by these tests is ready for review.
