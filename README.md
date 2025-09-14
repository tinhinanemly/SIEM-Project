# SIEM-Project
Custom SIEM lab using ELK stack, Filebeat, and Python log generator
# SIEM Project with ELK Stack  

## Project Overview  
This project demonstrates how to build a **basic SIEM (Security Information and Event Management)** system using the **ELK Stack (Elasticsearch, Filebeat, Kibana)**.  

- A **Python log generator** creates simulated security events.  
- Logs are shipped to **Elasticsearch** using **Filebeat**.  
- In **Kibana**, I created **detection rules** and **dashboards** to visualize alerts and security trends.  

---

## Features  
- Custom **Python Security Log Generator**  
- Logs shipped with **Filebeat**  
- Indexed and stored in **Elasticsearch**  
- Detection rules for suspicious activities  
- **Dashboards** in Kibana for log visualization and alerts  
- Alerts triggered when rules are matched  

---

## 📊 Kibana Dashboards & Visualizations

The project includes pre-built Kibana dashboards for real-time security monitoring:

- **Security Overview Dashboard**: High-level view of security events
- **Threat Analysis Dashboard**: Detailed attack pattern analysis  
- **Incident Investigation Dashboard**: Deep dive into specific security events

### Key Visualizations:
- **Events Over Time**: Area chart showing event volume trends
- **Top Attack Types**: Pie chart of most frequent attack categories
- **Geographical Threat Map**: Source IP locations (if GeoIP enabled)
- **Port Scan Analysis**: Bar chart showing scan activity by source IP
- **Service Targeting**: Horizontal bar chart of most attacked services

## 🚨 Detection Rules

Custom detection rules created in Kibana for:

- **Brute Force Attacks**: Multiple failed authentication attempts
- **Port Scanning**: Abnormal port scanning activity
- **Web Application Attacks**: SQL injection and XSS detection
- **High Severity Events**: Critical severity level triggers
- **Malware Detection**: Known malware pattern matching

## 🏗️ Architecture

```mermaid
graph LR
    A[Python Log Generator] --> B[JSON Log Files]
    B --> C[Filebeat]
    C --> D[Elasticsearch]
    D --> E[Kibana]
    E --> F[Dashboards]
    E --> G[Detection Rules]
    E --> H[Alerts]



