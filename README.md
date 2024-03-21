# IST303TeamProject_RFx

# Raster Function Tracker for ArcGIS Pro

## Introduction

This application serves as a comprehensive tool designed to track and manage the evolution of raster functions within ArcGIS Pro. Our objective is to harness the vast potential of raster imagery data, which is essential for spatial analysis and geospatial data management. The tool will function as a dynamic repository for documenting changes in raster function parameters and maintaining a clear record of ownership and contact information for each function across different releases.

## Table of Contents

- [Introduction](#introduction)
- [Application Concept Overview](#application-concept-overview)
- [Stakeholder Identification](#stakeholder-identification)
- [Project Requirements and User Journeys](#project-requirements-and-user-journeys)
- [Tasks Breakdown](#tasks-breakdown)
- [Development Milestones](#development-milestones)
- [Task Allocation](#task-allocation)
- [Monitoring Progress with a Burn-Down Chart](#monitoring-progress-with-a-burn-down-chart)
- [Documentation of Stand-Up Meetings](#documentation-of-stand-up-meetings)
- [Development and Testing Environment Setup](#development-and-testing-environment-setup)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Application Concept Overview

At the heart of our application lies the objective to harness the power of raster imagery data within ArcGIS Pro. These capabilities are encapsulated in a suite of raster functions, categorized by their use cases, each with unique parameters and required data types. Given the iterative nature of ArcGIS Pro's development, these raster functions are subject to modifications across releases, necessitating a tool that meticulously tracks these changes. Our web database application aims to fulfill this need, serving as a dynamic repository and reference for raster function evolution, ownership, and contact details.

## Stakeholder Identification

Central to this endeavor are the Imagery/Raster team at Esri and various internal teams reliant on raster functions. Their insights and needs inform the core of our development, ensuring our tool remains relevant and valuable.

## Project Requirements and User Journeys

Our journey to revolutionize raster functionality tracking in ArcGIS Pro begins with defining clear, time-estimated user stories:

- **Week 1:** Develop a comprehensive database encompassing all raster functions and parameters from previous ArcGIS Pro releases.
- **Week 2:** Introduce a Tool Owner page, enabling the assignment of raster functions to specific owners.
- **Week 3:** Enhance the Tool Owner page with capabilities to search, filter, and update owner details.
- **Week 4-5:** Implement a comparison feature to discern differences between two software releases regarding raster functions and parameters.

## Tasks Breakdown

Here's how we break down our tasks according to the user stories:

- **Week 1 Tasks:** 
  - Design database schema.
  - Parse XML data for raster functions.
  - Convert XML data to JSON format.
  - Implement RFX info retrieval and display logic.

- **Week 2 Tasks:**
- Shift efforts towards creating a SQL database for tracking raster function ownership, alongside developing the user interface for the RFX owner page.

- **Week 3 Tasks:**
- Implement functionality for editing owner details and introduce a filtering feature to streamline searches on the Tool Owner page.

- **Week 4-5 Tasks:**
- Design and develop a comparison route page that facilitates the analysis of raster function changes between different ArcGIS Pro versions.

## Development Milestones

We've established robust test plans and integrated testing throughout the development process to ensure functionality and reliability. We're also monitoring progress through a burn-down chart, adjusting tasks and timelines as needed to maintain momentum and achieve project milestones efficiently. By focusing on these structured tasks and adhering to our estimated timelines, we position ourselves to create a tool that not only tracks the evolution of raster functions within ArcGIS Pro but also enhances collaboration and transparency among stakeholders.

## Decomposing User Stories Into Tasks:
User Story A (Week 1): Create a database of all raster functions and their parameters in all previous ArcGIS Pro releases.

Task A1: Design database schema.
Task A2: Parse XML data for raster functions.
Task A3: Convert XML data to JSON format.
Task A4: Implement RFX info retrieval and display logic.
User Story B (Week 2): Develop a Tool Owner page for raster function assignment.

Task B1: Create SQL database schema for owner information.
Task B2: Develop the UI for the RFX owner page.
Task B3: Implement logic for assigning raster functions to owners.
User Story C (Week 3): Enhance the Tool Owner page with search, filter, and update capabilities.

Task C1: Implement search and filter functionality.
Task C2: Develop UI elements for editing owner details.
Task C3: Test search, filter, and update features for functionality and usability.
User Story D (Week 4-5): Enable comparison of raster function changes between releases.

Task D1: Design comparison logic.
Task D2: Develop UI for comparison results.
Task D3: Test comparison feature for accuracy and effectiveness.
2. Milestone 1.0 Features:
Milestone 1.0 will focus on establishing the foundational components of the application:

A database containing information on raster functions and parameters.
The initial version of the Tool Owner page with basic functionality.
Basic search and filter capabilities on the Tool Owner page.
3. Building Iterations for Milestone 1.0:
Iteration 1 (Weeks 1-2):

Complete tasks for User Story A and start User Story B.
Total days of work: 10 days (accounting for an 80% velocity due to initial ramp-up and coordination).
Iteration 2 (Weeks 3-5):

Complete tasks for User Stories B (remaining), C, and D.
Total days of work: 15 days (adjusting for continued learning and increased efficiency).

## Task Allocation

- **Aote:** Focus on database schema design and implementation (Tasks A1, B1).
- **Mohammed:** Lead the development of the UI for the Tool Owner page and comparison feature (Tasks B2, D2).
- **Aote:** Handle data parsing, conversion, and logic implementation (Tasks A2, A3, D1).
- **Akilesh:** Work on search, filter, and update functionalities (Tasks C1, C2).
- **Mohammed:** Presentation design and overall concept delivery.

## Monitoring Progress with a Burn-Down Chart

<img width="542" alt="image" src="https://github.com/axin-geo/IST303TeamProject_RFx/assets/157668023/75c09302-1e58-49b6-9156-0c4516dbdb59">

_The burn-down chart above illustrates our team's current progress against the planned work, offering a clear visual of the remaining tasks over the project timeline._

## Documentation of Stand-Up Meetings

We have documented the agendas, decisions, and action items from our bi-weekly stand-up meetings. These documents are a testament to our team's ongoing communication and problem-solving process.

## Development and Testing Environment Setup

Our development environment is fully configured, complete with the necessary software installations, access permissions, and initial database setups. We have included basic functional and test code in our repository to validate the setup's effectiveness.

## Contributing

If you would like to contribute to the Raster Function Tracker project, please review our contributing guidelines and submit your pull requests for review.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgments
- Thanks to the Imagery/Raster team at Esri for their insights and support.
- Gratitude to all team members for their dedication and hard work.
- Grateful for Professor Kallemeyn for his kind patience and walkthrough.
   
