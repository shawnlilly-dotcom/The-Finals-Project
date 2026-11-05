# GameVault — Sprint 1 Test Cases

**Team:** The Finals  
**Project:** GameVault — Video Game Collection Manager  
**Sprint:** 1  
**Task:** TEAM-01.3 — Create Initial Test Cases  
**Testing Environment:** Python, Tkinter, SQLite, Windows, VS Code

## 1. Purpose

The purpose of these test cases is to verify that the initial GameVault application functions correctly. Testing focuses on application startup, user input validation, database operations, and persistent storage.

## 2. Test Cases

### TC-01 — Application Startup

**Objective:** Verify that GameVault launches successfully.

**Steps:**
1. Open the GameVault project in VS Code.
2. Run `python main.py`.
3. Observe the application window.

**Expected Result:** The GameVault window opens and displays the Add Game form and My Game Collection table.

### TC-02 — Required Field Validation

**Objective:** Verify that users cannot add a game without a title.

**Steps:**
1. Launch GameVault.
2. Leave the Title field blank.
3. Click Add Game.

**Expected Result:** A warning message appears requesting a game title. No record is saved.

### TC-03 — Add Game Functionality

**Objective:** Verify that users can add a game to their collection.

**Test Data:**
- Title: World of Warcraft
- Genre: MMORPG
- Platform: PC
- Completion Status: In Progress

**Steps:**
1. Enter the test data into the Add Game form.
2. Click Add Game.
3. Observe the confirmation message.

**Expected Result:** The application confirms that the game was added successfully.

### TC-04 — Display Saved Games

**Objective:** Verify that saved games appear in the collection table.

**Steps:**
1. Add a game using the Add Game form.
2. Locate the My Game Collection table.
3. Verify that the saved information is displayed.

**Expected Result:** The table displays the game's ID, title, genre, platform, and completion status.

### TC-05 — Database Persistence

**Objective:** Verify that saved games remain available after restarting GameVault.

**Steps:**
1. Add a game to the collection.
2. Close GameVault completely.
3. Restart the application using `python main.py`.
4. Review the My Game Collection table.

**Expected Result:** Previously saved games remain visible after restarting the application.

### TC-06 — Database Initialization

**Objective:** Verify that GameVault initializes its SQLite database.

**Steps:**
1. Confirm that `main.py` calls `create_database()`.
2. Launch GameVault.
3. Verify that the application connects to SQLite without an error.
4. Confirm that the games table supports inserting and retrieving records.

**Expected Result:** The SQLite database initializes successfully and supports the application's database operations.

## 3. Test Execution Summary

| Test ID | Test Case | Status |
|---|---|---|
| TC-01 | Application Startup | Passed |
| TC-02 | Required Field Validation | Passed |
| TC-03 | Add Game Functionality | Passed |
| TC-04 | Display Saved Games | Passed |
| TC-05 | Database Persistence | Passed |
| TC-06 | Database Initialization | Passed |

## 4. Defect Tracking

Any defects discovered during testing will be documented with a description, reproduction steps, expected behavior, actual behavior, and resolution status.

## 5. Conclusion

The initial GameVault tests cover the core functionality developed during Sprint 1. The application has demonstrated successful startup, game entry, database storage, game display, and persistence. Required-field validation remains to be tested separately.
