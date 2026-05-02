# Guidewire SurePath Methodology - QA Study Guide

## Overview
SurePath is Guidewire’s implementation methodology designed to provide a standardized, agile-based approach to software delivery. It focuses on maximizing out-of-the-box (OOTB) features and ensuring high quality through predictable phases.

---

## 1. Inception Phase (The Foundation)
**Goal:** Align stakeholders, define scope, and establish the Product Backlog.
* **Key Deliverables:** Prioritized Product Backlog, Lighthouse Project (Initial Prototype), and confirmed Architecture.
* **QA Manager Focus:** 
    * Review User Stories for "Testability."
    * Define the **Definition of Done (DoD)** and the overall Test Strategy.
    * Ensure Acceptance Criteria are clear before development starts.

## 2. Development Phase (Build & Configure)
**Goal:** Configure the application through iterative Sprints.
* **Activities:** Screen configuration (PCF files), Business Logic (Gosu), and Data Model extensions.
* **QA Manager Focus:** 
    * Execution of Functional, Integration, and Regression tests.
    * Monitor **Defect Density** per User Story to identify "hot spots" in code (e.g., complex Gosu rules).
    * Ensure Automated Test coverage is increasing with each Sprint.

## 3. Stabilization Phase (Quality Gate)
**Goal:** Finalize the system for production-readiness. **No new features are developed here.**
* **Activities:** Performance Testing, Security Testing, and User Acceptance Testing (UAT).
* **QA Manager Focus:** 
    * **Critical Exit Criteria:** Monitoring **Defect Density**. If the density is above the threshold, the **Go-Live** must be postponed.
    * Final Regression cycles to ensure bug fixes didn't break existing features.

## 4. Deployment Phase (Execution & Support)
**Goal:** Transition the system to the production environment.
* **Activities:** Final Data Migration, Cut-over, and Hypercare support.
* **QA Manager Focus:** 
    * Smoke Testing in the Production environment.
    * **Defect Leakage Analysis:** Measuring the ratio of defects found in Production vs. those found during the project to evaluate QA effectiveness.

---

## Key Metrics Summary for QA Management

| Metric | Phase | Purpose |
| :--- | :--- | :--- |
| **Defect Density** | Development / Stabilization | Measure quality per Story Point. Used as a Go/No-Go gate. |
| **Defect Leakage** | Post-Deployment (Hypercare) | Evaluate the effectiveness of the Testing Strategy. |
| **Automation Coverage**| Development | Ensure long-term maintainability and fast regression. |