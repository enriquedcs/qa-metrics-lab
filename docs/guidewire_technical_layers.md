# Guidewire Technical Architecture - QA Study Guide

## Overview
Guidewire applications are built on three main layers. Knowing which file type is involved helps identify the root cause of defects and estimate the impact of changes.

---

## 1. UI Layer: PCF (Page Configuration Files)
*   **File Extension:** `.pcf`
*   **Purpose:** Defines the User Interface (Screens, Buttons, Fields, Wizards).
*   **Key Components:** 
    *   **Locations:** Where the user is (e.g., `PolicyFile`).
    *   **Widgets:** Visual elements like `TextInput` or `DetailView`.
*   **QA Focus:** Look here if a button is missing, a field is not visible, or the screen flow is incorrect.

## 2. Logic Layer: Gosu (Programming Language)
*   **File Extension:** `.gs` (Classes) or `.gsx` (Enhancements).
*   **Purpose:** The business logic. It handles calculations, validations, and integrations.
*   **Key Concepts:**
    *   **Classes:** Object-oriented code.
    *   **Enhancements:** Adding functionality to existing OOTB (Out-of-the-Box) classes without modifying the core.
*   **QA Focus:** Look here if a premium calculation is wrong, a validation rule isn't firing, or an API integration fails.

## 3. Data Layer: Data Model
*   **File Extensions:** 
    *   `.eti` (Entity Integration): Defines a new table/entity.
    *   `.etx` (Entity Extension): Adds new fields to an existing OOTB table.
*   **Purpose:** Defines how data is stored in the database.
*   **QA Focus:** Look here if data is not persisting (saving) correctly or if a new required field is causing "Null Pointer" errors.

---

## 🔍 QA "Traceability" Cheat Sheet

| Symptom | Probable File Layer | Language/Tool |
| :--- | :--- | :--- |
| Field is missing from a screen | **PCF** | XML-based / Studio |
| Premium calculation is incorrect | **Gosu** | Gosu |
| New 'Vehicle Plate' field is not saving | **Data Model** | Metadata (XML) |
| Validation error message is not showing | **PCF / Gosu** | Rules / UI Widgets |


**Scenario:** A new field is visible on the UI, but the value is not persisted (it disappears after clicking 'Update').

**Why it's usually a Data Model issue (C) and not Gosu (B):**
*   **The Metadata Constraint:** Guidewire is metadata-driven. If a field exists in a PCF (UI) but is not explicitly defined in an `.etx` or `.eti` file (Data Model), the application has no database column to map that value to.
*   **The Result:** The UI might temporarily hold the value in memory, but when the "Commit" happens, the database ignores the "unknown" field. Upon page refresh, the field appears empty.
*   **Gosu's Role:** Gosu only handles the *transfer* of data. If the "container" (the database column) doesn't exist in the Data Model, Gosu cannot fulfill the save operation.

**Key Exam Takeaway:** Always check the **Data Model** extensions (`.etx`/`.eti`) if data is not persisting but no business logic errors (Gosu) are being triggered.