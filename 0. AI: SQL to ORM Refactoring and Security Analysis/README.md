# SQL to ORM Refactoring and Security Analysis

This folder contains the files and documentation for the AI Lab Assignment focused on translating procedural Python database code utilizing raw SQL into a modern, robust, and object-oriented solution using the SQLAlchemy Object-Relational Mapper (ORM).

## Folder Contents

* **`initial_code.py`**: The original procedural Python script utilizing `mysql.connector` with raw SQL execution and parameterized queries for database operations.
* **`refactored_code.py`**: The modern, object-oriented version refactored using SQLAlchemy, featuring declarative models (`User`), session management, and cleaner CRUD workflows.

## Overview of Improvements

1. **Object-Centric Abstraction:** Replaces error-prone raw SQL query strings with Python classes and methods, mapping database tables directly to Python objects.
2. **Enhanced Maintainability:** Centralizes database schemas and operations within model classes, making long-term code updates significantly easier and less prone to syntax errors.
3. **Robust Security & Safety:** Inherently manages connection lifecycles, parameter binding, and transaction rollbacks cleanly via SQLAlchemy sessions.
