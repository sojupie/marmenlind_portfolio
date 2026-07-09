# Olle Marmenlind

Computer Engineering undergraduate. Builds backend infrastructure (PostgreSQL, distributed ingestion, ETL), embedded systems (RISC-V/FreeRTOS firmware), and runs product ownership end-to-end at Sevan AB since 2022.

[![CV](https://img.shields.io/badge/CV-Download-blue)](https://marmenlind.com/assets/docs/CV_OLLE_MARMENLIND_RESUME.pdf)
[![GitHub](https://img.shields.io/badge/GitHub-Profile-181717?logo=github&logoColor=white)](https://github.com/sojupie)

---

## Experience

### Sevan AB (March 2022 – Present)
**Technical Product Owner — Stockholm, Sweden (Remote)**

* Promoted to Product Owner; scaled B2C content platform from 4.5K to 200K users and migrated 300+ B2B accounts to a digital e-commerce channel.
* Directed product roadmap and authored 400+ Jira tickets including API schemas and data models.
* Collaborated cross-functionally to translate business requirements into technical solutions and development priorities, coordinated development across external partner teams and vendors.

### Motillo AB (March 2026 – June 2026)
**Software Engineering (Client Project, KTH Industry Course) — Sweden (Remote)**

* Built the React/TypeScript SPA (Entra ID auth) as a two-way control plane for UptimeRobot, managing tenant monitors, and for Litium order ingestion, built specifically to run continuously on legacy Chrome 76 lobby kiosks.
* Implemented a simulated Lambda Architecture using PostgreSQL Materialized Views for historical rollups, merging them with live data to drop query times from 330ms to ~20ms over 4 million rows.
* Set up an asynchronous ingestion buffer using Hangfire and Polly to handle upstream API rate limits and prevent frontend load delays.
* Wrote a C#/ASP.NET Core Web API extension for the Litium platform to extract, transform, and serve flattened Elasticsearch order data.

### Proximion AB (October 2025 – January 2026)
**R&D SWE Member (University-Industry Project) — Stockholm, Sweden**

* Developed FreeRTOS/RISC-V firmware in C for a Fiber Bragg Grating (FBG) Interrogator prototype.
* Used binary semaphores to synchronize high-priority ISRs with background data processing queues (preemptive multithreading, single core SOC). 
* Created a C#/.NET host application with a custom USB protocol for sub-ms sensor readout and visualization.
* Configured a self-hosted Linux CI/CD pipeline using Docker to enforce reproducible RISC-V builds, automated format patching, and release generation.

---

## Other Projects

### B2B Scan-to-Order
**Android / Kotlin** — *Personal Project*

Architected a fault-tolerant Android application using Kotlin Coroutines for structured concurrency. Engineered a distributed data synchronization engine with automatic failover strategies (Firestore/REST). Integrated Google ML Kit for on-device barcode inference to enable scanning in low-connectivity environments.

[View on GitHub](https://github.com/thewayla/Scan2Go_PoC)

---

## Case studies & Previous Academic Work

### Technical Report: Silent Protocol Downgrading and HSTS Mitigation
An analysis of the vulnerability of the HTTP-to-HTTPS transition mechanism to Man-in-the-Middle (MITM) attacks and the effectiveness of HTTP Strict Transport Security (HSTS) as a countermeasure.

[View report](https://marmenlind.com/MITM-attacks-and-HSTS-Mitigation/)

### Technical Report: Principles of Reliable A/B Testing
A technical framework covering the design and execution of statistically valid A/B tests, from hypothesis formulation to the interpretation of results.

[View report](https://marmenlind.com/assets/docs/ab_testing_principles.pdf)

### Case Study: Increasing Average Order Value
A strategy for applying behavioral science to increase Average Order Value (AOV) via data-driven recommendations.

[View case study](https://marmenlind.com/highlight-discount-case/)

---

## About me
* Based in Stockholm, Sweden.
* Technical Product Owner at Sevan AB while pursuing B.Sc. studies.

### Technical Stack
* **Languages:** Java, C#, C, Kotlin, TypeScript, Assembly
* **Systems & Infrastructure:** Linux, Docker, CI/CD, Azure, GCP, AWS, Microservices, Distributed Systems, FreeRTOS, RISC-V, Real-Time Systems
* **Frameworks:** ASP.NET Core, Spring Boot, React, Vite, TanStack Router/Query
* **Data & Networking:** PostgreSQL, MySQL, Elasticsearch, MongoDB, REST, TCP/UDP, ETL/Data Pipelines
* **Tools:** Git, Bash, PowerShell, CMake, Jira, Agile

### Education
**Royal Institute of Technology (KTH)**
B.Sc. in Computer Engineering (Expected June 2027)

* *Relevant Coursework:* Data Structures, Algorithms, Operating Systems, Microcontrollers (graduate level), Computer Networks, Databases, Information Security.
* *Certifications:* CCNA, CCNP

---

## Contact me
Contact me via [email](mailto:ollemarmenlind02@gmail.com).

<small>© 2026 Olle Marmenlind. All rights reserved.</small>