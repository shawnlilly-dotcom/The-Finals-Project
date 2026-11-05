# GameVault — Coding Conventions

**Team:** The Finals  
**Project:** GameVault — Video Game Collection Manager  
**Sprint:** 1  
**Task:** TEAM-01.2 — Document Coding Conventions

## 1. Purpose

The purpose of these coding conventions is to maintain consistency, readability, and organization throughout the GameVault development process. All team members should follow these standards when creating or modifying application code.

## 2. Python Coding Standards

- Follow Python's PEP 8 style guidelines.
- Use four spaces for indentation instead of tabs.
- Use descriptive variable and function names.
- Use `snake_case` for variables and functions.
- Use uppercase names for constants, such as `DATABASE`.
- Include comments when code requires additional explanation.
- Avoid unnecessary or duplicate code.

## 3. File Organization

GameVault will separate application functionality into different Python files.

- **main.py:** Contains the Tkinter graphical user interface and application interactions.
- **database.py:** Contains SQLite database operations, including initialization, inserting records, and retrieving records.
- **gamevault.db:** Stores game collection information locally.
- **README.md:** Provides project information and setup instructions.

## 4. Database Conventions

- Use SQLite for persistent storage.
- Use descriptive table and column names.
- Use parameterized SQL queries when inserting or modifying records.
- Close database connections after completing operations.
- Validate required information before saving records.
- Preserve existing records when restarting the application.

## 5. User Interface Standards

- Maintain consistent fonts, colors, and spacing throughout the Tkinter interface.
- Use clear labels for input fields and buttons.
- Provide confirmation messages when operations succeed.
- Display understandable error messages when operations fail.
- Keep the interface simple and easy to navigate.

## 6. GitHub Version Control

- Commit code after completing and testing a feature.
- Use meaningful commit messages describing changes.
- Avoid committing temporary Python files or local database files.
- Update the GitHub Sprint board when tasks change status.
- Review changes before merging or uploading code.

## 7. Testing Standards

- Test each feature after implementation.
- Verify that required fields are validated.
- Confirm database records save and display correctly.
- Restart the application to test data persistence.
- Document test results and any identified defects.
- Retest features after fixing defects.

## 8. Team Responsibilities

All members of The Finals are expected to follow these conventions. Team members should communicate proposed changes and review code for consistency before considering a task complete.
