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

## Setup Instructions  

### 1- Prerequisites  
- Install **Elasticsearch**, **Kibana**, and **Filebeat**  
- Python 3.x  

### 2️- Run the Log Generator  
```bash
python logs_generator/security_log_generator.py
