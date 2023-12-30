# Event Ticket Analysis Dashboard

# Data Analysis Dashboard for Event Tickets

This dashboard is designed to provide insights into event tickets, leveraging data analysis techniques. Built using Python and Streamlit, the dashboard aims to answer critical questions related to incident management.

## Significance

Understanding patterns in ticket data is vital for identifying vulnerabilities and continuously improving service management. This dashboard facilitates the analysis of key metrics, helping stakeholders make informed decisions and enhance overall service delivery.

## Dashboard Features

- Interactive visualisation of incident data.
- Quick insights into the most affected configuration items.
- Identification of ticket trends, including reopen and reassignment patterns.
- Analysis of SLA breaches and affected locations.

## Dashboard Screenshots

Explore visual representations of key insights and interactive features offered by the data analysis dashboard. The following screenshots provide a glimpse into the user interface and showcase how the presented data is transformed into actionable information.

![Screenshot 2023-12-30 at 11.26.59 AM.png](Event%20Ticket%20Analysis%20Dashboard%20f37102bd13ef445e8a8b2d088284cb4c/Screenshot_2023-12-30_at_11.26.59_AM.png)

![Screenshot 2023-12-30 at 11.28.14 AM.png](Event%20Ticket%20Analysis%20Dashboard%20f37102bd13ef445e8a8b2d088284cb4c/Screenshot_2023-12-30_at_11.28.14_AM.png)

## Dataset Overview

Dataset link: https://archive.ics.uci.edu/ml/datasets/Incident+management+process+enriched+event+log

The dataset utilized in this analysis is obtained from the UCI Machine Learning repository, offering valuable insights into incident management processes. Each record in the dataset represents a distinct incident, and the information encapsulated in various columns serves as the foundation for the analytical exploration provided by this dashboard.

Here is a breakdown of the essential columns employed in this analysis:

- **number:** An incident identifier, serving as a unique reference for each reported incident.
- **incident state:** Indicates the current state of the incident within the management process. This column encompasses eight levels, representing transitions from the opening to the closing of the case.
- **active:** A boolean attribute signaling whether the incident record is currently active or has been closed or canceled.
- **reassignment_count:** Represents the number of times the incident has undergone reassignment to different groups or support analysts.
- **reopen_count:** Captures the count of incidents where the resolution was rejected by the caller, leading to a reopening of the incident.
- **sys_mod_count:** Quantifies the number of updates made to the incident until the present moment.
- **made_sla:** A boolean attribute indicating whether the incident adhered to the target Service Level Agreement (SLA).
- **caller_id:** Identifies the user affected by the incident.
- **opened_by:** Identifies the user who reported the incident.
- **opened_at:** Records the date and time when the incident was initially reported by the user.
- **sys_created_by:** Identifies the user responsible for registering the incident.
- **sys_created_at:** Captures the date and time of the system's creation of the incident record.
- **sys_updated_by:** Identifies the user responsible for updating the incident, generating the current log record.
- **sys_updated_at:** Records the date and time when the incident system was last updated.
- **contact_type:** A categorical attribute indicating the means by which the incident was reported.
- **location:** Identifies the location of the place affected by the incident.
- **category:** Provides a first-level description of the affected service.
- **subcategory:** Offers a second-level description of the affected service, related to the first-level description (category).
- **u_symptom:** Describes the user's perception of service availability.
- **cmdb_ci:** (Configuration Item) An identifier used to report the affected item, though not mandatory.
- **impact:** Describes the impact caused by the incident, categorized as 1 (High), 2 (Medium), or 3 (Low).
- **urgency:** Describes the urgency informed by the user for incident resolution, with values of 1 (High), 2 (Medium), or 3 (Low).
- **priority:** Calculated by the system based on 'impact' and 'urgency.'
- **assignment_group:** Identifies the support group responsible for managing the incident.
- **assigned_to:** Identifies the user in charge of handling the incident.
- **knowledge:** A boolean attribute indicating whether a knowledge base document was used to resolve the incident.
- **u_priority_confirmation:** A boolean attribute indicating whether the priority field has been double-checked.
- **notify:** A categorical attribute indicating whether notifications were generated for the incident.
- **problem_id:** Identifies the problem associated with the incident.
- **rfc:** (Request for Change) An identifier of the change request associated with the incident.
- **vendor:** Identifies the vendor in charge of handling the incident.
- **caused_by:** Identifies the Request for Change (RFC) responsible for the incident.
- **close_code:** Identifies the resolution code of the incident.
- **resolved_by:** Identifies the user who resolved the incident.
- **resolved_at:** Records the date and time when the incident was resolved by the user (dependent variable).
- **closed_at:** Records the date and time when the incident was closed by the user (dependent variable).

This comprehensive set of columns provides a rich source of data for meaningful analysis and visualisation within the dashboard.

## Getting Started

To run the dashboard locally, follow these steps:

1. Install the required libraries: `pip install -r requirements.txt`.
2. Run the Streamlit app: `streamlit run app.py`.
3. Access the dashboard in your browser at [http://localhost:8501](http://localhost:8501).


## Acknowledgments

- The dataset used in this analysis is from the UCI ML repository.
- Special thanks to the Streamlit and Python communities for their valuable contributions.