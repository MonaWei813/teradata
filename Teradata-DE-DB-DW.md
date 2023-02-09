<p align="center">
  <img width="400"  alt="TERA-LOGO"src="pngfind.com-artificial-intelligence-png-1049836.png" />
</p>
<br>

# **Teradata Data Engineering Database and Data Warehouse(TDVAN4)**
## Module 1 *Database Concepts*
* an organized collection of persistent data, stored electronically in a computer system
* is usually controlled by special software: **database management system**
* different paradigms of how to organize data and the extremely successful paradigm is the relational model
*  relational databases organize data into tables consisting of rows and columns, like spreadsheets, where each table is a concept, each row is an instance, and each column is a property
* A database can be used to retrieve specific records, update records in bulk, cross reference data in different tables, and perform complex aggregate calculations
* not all database can perform the same actions:
  * **retrieve** all records that match certain criteria
  * **update** records in bulk
  * **cross-reference** records in different tables
  * **perform** complex aggregate calculations
***
## Module 2 *Relational Databases*
* it can cross-reference records in different tables
* relational concept: entity(information), cardinality(number of rows), degree(number of columns)
* in a table:
  * each record is called row
  * each column is called fields (plural!)
* schema refers to organizing the data as a blueprint that shows how the database is divided into tables
* **Formal definition of a Schema:** a set of formulas or sentences called integrity constraints imposed on a database
* each column in the **entire database** need not be unique
* only columns within a **single table** must be distinct
* primary key: unique identifier for each record or row
* foreign key: a column or group of columns in a relational database table that defines the relationship between the data in two tables.
* when the same primary key (name can be different, but contains the same information) is included in another table, it becomes a foreign key.
* FK must agrees with PK
### Data Integrity
**Referential integrity** is a relational database concept, which states that the table relationships must be **consistent**. A foreign key can never contain a value which is not a primary key for a row in the parent table.
* **Unique**
  * Enforces a uniqueness on a column (or a set of columns).
  * Any unique column set is also a candidate key. 
  * Uniqueness constraints are sometimes referred to as key constraints. 
* **Check**
  * Enforces the specific conditions on data values of a column. 
  * A check constraint is used to create conditions that a particular column or set of columns must fulfill.
* **Primary Key**
  * Enforces both row uniqueness and together with REFERENCES constraints, referential integrity. 
  * Primary key constraints are a subset of the uniqueness constraints.
* **References**
  * Enforces a referential integrity between the foreign keys in one table and the primary keys of another table. 
  * A table which has a foreign key referencing the primary key of the same table is a special case, but has no exception to the rule.
***
## Module 3 *Relational Database Management Systems*
* Provides multiple users and programmers with a systematic way to create, retrieve, update, and manage data
* Enforces database rules and constraints
* Maintains the database schema

### SQL
* structured query language
* used to create, manage, manipulate and query database objects

### 
* OLAP: Online Analytic Processing
  * comprise the complex analysis that are performed on a data set
  * data mining, querying, pivoting, slicing, dicing, drilling, reporting and other decision-support applications
  * a data warehouse can be used without OLAP
  * processing is characterized by a smaller number of read operations which access and combine a large portion of available data. 
  * the latency is often less critical. 
  * Analytical business applications like reports, dashboards, statistical model training and scoring, or ad-hoc analysis typically emit OLAP workloads.
* OLTP: Online Transaction Processing
  * manages business applications and collects day to day data
  * different than a data warehouse
  * access small number of records or a few tables
  * characterized by a large number of small changes which must be executed with minimal latency and no inconsistencies. 
  * Operational business applications like point of sales, stock management, accounting, or core banking systems typically emit OLTP workloads.
***
## Module 4 *Data Models*
* Data Models are **planning tools**, used by the business analysts, the data modelers, and the data engineers to describe which **elements of the real world**, often called **entities**, are needed to solve particular business needs by the means of a software
* They collect **entities' characteristics or attributes**
* Data Models capture **whether and how entities are related**
* Models can contain **further explanations**, such as which business processes emit or need certain data, which business rules and restrictions are in place, security classification, privacy requirements, known quality issues, or expected data volumes

### Relational Data Model
A **relational data model** is created with the intention to store the data in a relational database, and to follow the **design principle** to **avoid redundancy**. The absence of redundancy has many positive consequences.
* Does not have inconsistencies
* Reduces likelihood of update conflicts
* Reduces storage space
* Reduces implementation effort by reusing existing tables 
* Entity Relationship Diagrams(ERDs)
  * Relational data models are often graphically represented as ERDs.
### Different Data Models
![alt-text](dm.PNG "Data Models")
* **Conceptual**
  * using business terminology and depicting the relevant entities, relationships and potential identifiers
* **Logical**
  * add more details and might replace business terminology
* **Extended Logical**
* analyze the future workload, add more information which then become a critical input for the physical database design(Teradata call this step: activity and transaction modelling)
* **Physical**
  * create the physical data model for the RDBMS
### Dimensional Data Model
* designed for reporting
* models navigation paths (not business rules) and aligns with the work process of the business users
* emphasizes usability because the tables are defined in a way that a business uses the data and is organized in a way that a given user or group of users think about the data
    * Normalization
      * is the process of reducing a complex database schema into a simple and stable one. 
      * removing redundant attributes, keys and relationships from the conceptual data model
      * is optimized for entity level transactions
    * Denormalization
      * supports dimensional modelling: speed and simplicity
      * is optimized for answering business questions and driving decision making
    * Fact table: M to M relationship, contains one or more numerical measures that occur for the combination of keys that define each tuple in the table
## Module 5 *Data Warehouse Concepts*
A **data warehouse**is a specially constructed data repository where data is organized to be easily accessed by end users for various applications.
* common in corporations
* carry many years' worth of detailed data so **historical trends** can be analyzed
* data warehousing is a process **NOT** a product which manage and assemble data from various sources to answer business questions
### Data Mart
* data warehouse is more like an enterpriser-level
* compare to it, information in data mart pertains to a single department
* Independent Data Mart
  * isolated entities entirely separate from the enterprise data warehouse
  * derived from independent sources 
  * be viewed as data pirates
  * have high likelihood of producing data that does not match that of the warehouse
* Dependent Data Mart
  * derived from enterprise data warehouse
  * might(or not) be useful depending on the configuration
  * permits users to have full access to the enterprise data store
* Logical Data Mart
  * a form of dependent data mart
  * constructed virtually from the physical warehouse
  * data is presented using a series of SQL views
### Data Warehouse Architecture
#### Data Integration
* **Tightly**
  * define upfront structure and rules for how the data need to be rationalized, organized, and optimized for performance
  * Ease of use
  * Faster response times
  * Data quality and integrity assurance
  * Consistent results
  * best used for heterogeneous data that is frequently accessed and extensively reused with strong needs for data quality and integrity
* **Loosely**
  * apply the structure and the rules, are deferred as late as possible, often at runtime, to avoid unnecessary data preparation
  * Data is treated as raw materials stored in a close container in its original form
  * the flexibility to shape the data at the user’s discretion and the opportunity to leverage the data that would be out of reach due to the impracticality of utilizing tight coupling methods
  * best used for homogenous data that is less frequently accessed or where the structure of the source data is evolving, which makes the on-going rationalization untenable
* **Non-Integrated**
  * the purest raw form of data with no additional keys defined during acquisition or prior consumption of the data to aid the integration
  * integration of non-integrated data with loosely and tightly integrated data can occur through expertly written end user code that creates the linkages (keys) on the fly
  * the opportunity to leverage the data that would be withheld during the time in which data provisioners are working to define additional structure
  * best used for the datasets with no perceived value from integration with other datasets, or in cases where the understanding of a new dataset is still in process
### Data Layer
![alt-text](dly.PNG "Data Layer")
* Examples of data sources are on the left
* The data platform is next to the data sources
* Analytic methods and interfaces connect users and other data consumers to the data platform
* Examples of users and other data consumers are on the right
* On the bottom there are two fundamental sections:
  * Data management and governance is the organizational framework
  * Deployment represents the technical infrastructure
* data entering on the left side, and flowing through the data platform, interfaces and analytic methods to the users
### Data Platform
![alt-text](dpl.PNG "Data Platform")
## Module 6 *Data Modelling Concepts*

***
<p align="center">
  <img width="100"  alt="END-LOGO"src="the-end.png" />
</p>