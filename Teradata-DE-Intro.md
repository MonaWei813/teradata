<p align="center">
  <img width="400"  alt="TERA-LOGO"src="pngfind.com-artificial-intelligence-png-1049836.png" />
</p>
<br>

# **Teradata Data Engineering Introduction(TDVAN4)**
## *Defining Data Engineering Terms*
### Introduction
* **Data engineering** is a **set of tasks and techniques** that provide governed data to the users in an organization. 
* **Data engineers** use applications to answer **analytical questions** which allow their organization to **realize business value**.
* **Data engineers** should have a solid business understanding and the ability to talk to business representatives in business terms. This is important when clarifying requirements, modeling data, or discussing improvement potentials. 
### Business Value
* Realizing business value is the last part of the data engineering definition. It describes the final goal and purpose of data engineering.
* Chances for C-level acceptance and support are highest when an idea directly relates to, or can be tied to, targeted data.
* DE can help an organization **guide budget allocations** and **determine implementations of specific projects** to aid in business value.
### Data
* indicates that special traits must be factored in when following an engineering approach with the goal of extracting value from data.
* An important insight is that **not all data is of equal value**.
* Some of the differentiating dimensions
  * **Velocity of Change**: frequency and tracking
  * **Freshness**: maximum acceptable latency when multiple systems exchange data.
  * **Semantics**: Descriptors of people, places, things, events, and other pertinent information.
  * **Data Format**: native technical representation, ability to convert
  * **Ownership**: responsibility of business processes and systems for generating or using data
  * **Data Quality**: accuracy, errors, missing data
  * **Data Volume**: number of entities to be stored and processed, storage size, historical record, growth expectation
  * **Data Security and Privacy**: authorization, integrity, affect of inappropriate disclosure, legal requirement

#### Types of Data
* **Master Data**
  * low data volume
  * changing slowly
  * keep history of changes
  * very high security and privacy requirements
* **Transactional Data**
  * high data volume
  * very high security
  * have freshness requirements
* **Time Series**
  * sensor data in certain time intervals
  * very high volume
  * can suffer from data quality issues
* **Metadata**
  * system that emitted the data
  * time that data have been moved
  * the meaning of it
* **Data in Teradata Vantage**
  * high volume
  * structured, semi-structured and unstructured
  * support both batch and streaming data loading methods
### Engineering
Emphasizes an established, transparent, and repeatable process that is followed to get to a desired result.
### Purposeful Set of Activities and Techniques
* means that data engineering endeavors do not start at zero.
* At an **operational level**, several established methodologies are available for **organizing workflows** to complete the logical activities.
* certain organizational structures, rules, roles, responsibilities, and technical systems are needed.
  
![alt text](bv.PNG "Business Values"")

* **Business and Technical Analysis** 
  * Data requirement
  * Mock-ups
  * Conceptual data model
  * Semantic model
*  **Data Loading**
   *  Data in a sandbox
   *  Foreign table
   *  Data in staging
*  **Data Profiling**
   *  Data sources
   *  Data profile
   *  Data quality issues
   *  Relationships
*  **Data Preparation**
   *  proper data types
   *  data cleansed
   *  values normalized
* **Model Development Support**
  * Features
  * Analytical Data Set(ADS) created
  * Statistical model trained and tested
* **Data Modelling**
  * Physical data model
  * Mapping
  * Transformations
* **Data Integration**
  * Data in core layer
  * Data in semantic layer
  * ADS creation automated
* **Testing**
  * Test code
  * QA code
  * Deployment code
  * Issues
* **Deployment**
  * New and changed
  * Artifacts available for business use
* **Production**
  * Business value realized
  * Change requests
  * Issues
It is a key requirement that the tools and techniques **integrate well**and support a **high degree of automation**. This helps data engineers keep development and deployment **cycles short**. Reducing the cycles ensures that business value can be realized early and for a long duration.
### Governed Data
* extension to Data
* Master Data Management
* Data Architecture
* Metadata Management
* Data Security and Privacy
* Data Integration
* Data Quality Management
Data governance sets the **boundaries** to work but only to the **limit required** from a business perspective.
### Applications
* user interface providing data access to end users.
* reporting tools, operational business applications, database tools like Teradata Studio, statistical software suites
* An application development is not often considered to be a data engineering task
* **Interpret Data Properly**
  * Metadata
  * Interface definition and documentation
  * Coaching
  * Testing 
  * Change communication
*  **Use the Data Platform Efficiently**
   * Access layer data model 
   * Physical data modeling 
   * Query optimization 
   * Statistics 
   * Locking
* **Do Not Open Security Holes**
  * Database user and privilege management
  * Authentication
  * Data encryption
  * Code injection
**The final goal is to realize business value.** Sub-optimal data interfaces can severely hamper application development. A mutual understanding between data engineers and application developers will help to avoid such an issue.
### Analytic Questions
To answer these analytical questions, use the **Gartner's Maturity Model**.
* **Descriptive**
  * what happened
  * reports are created
* **Diagnostic**
  * why did it happen
  * analysis and understanding of what the data reveals
* **Predictive**
  * What will happen
  * Prediction models to aid in understanding what might happen next
* **Prescriptive**
  * What should we do
  * Machine Learning and decision automation will be used to determine next steps

#### Method to Answer
Different methods can be applied to answer analytical questions, such as **reporting, visualizing, statistical modeling, optimizing, etc**.  A growing set of analytical techniques are available as building blocks:
* SQL queries
* Regression
* Decision trees
* Neural networks

### Keys
* **Data** at its center, as are methods to describe, represent, store, move, and transform data
* **Processes** are another focal point for business processes, because they need data as an input and produce data as an output. Processes for structuring data engineering work determine the time needed from idea to production, process to split work into parallel work streams, and impact of artifacts fit together, constituting a congruent body
* **Techniques, tools, and best practices** exist and if they have been chosen wisely and work well together, which can help data engineers complete their operational tasks efficiently
* **Collaboration** done with business representatives, data scientists, analysts, and others is vital
* **Applications and analytical techniques** must be considered because they often require specific ways to represent data
* **Data governance** makes sure that data engineering work is aligned with business needs and provides the necessary organizational framework
* **Legal requirements** influence what can be done and how things have to be done
***
<p align="center">
  <img width="100"  alt="END-LOGO"src="the-end.png" />
</p>
