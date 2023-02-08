<p align="center">
  <img width="400"  alt="TERA-LOGO"src="pngfind.com-artificial-intelligence-png-1049836.png" />
</p>
<br>

# **Teradata Advanced SQL Engine 17.10**
## Module 1 *Database Concept*
* database provides an organized mechanism for storing, managing and retrieving data.
* not all database can perform the same actions:
  * retrieve
  * update
  * cross-reference
  * perform complex aggregate calculations

### Common types of Databases
* relational: is structured to recognize connections between stored items of information. SQL
* No-SQL: only to retrieve information
***
## Module 2 *Relational Database*
* it can cross-reference records in different tables
* relational concept: entity(information), cardinality(number of rows), degree(number of columns)
* based on mathematical set theory
* mathematical concept: relation(table), tuple(row), attribute(column)
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

### Data Modelling
* 3NF: third normal form: rules and guidelines about how the data model should look, which means which columns should belong to which table.
* three types of data models:
  * relational: most common type and reflect business rules
  * dimensional: emphasize usability
    * Normalization
      * is the process of reducing a complex database schema into a simple and stable one. 
      * removing redundant attributes, keys and relationships from the conceptual data model
      * is optimized for entity level transactions
    * Denormalization
      * supports dimensional modelling: speed and simplicity
      * is optimized for answering business questions and driving decision making
    * Fact table: M to M relationship, contains one or more numerical measures that occur for the combination of keys that define each tuple in the table
  * logical: not implemented on hardware, is technology independent
  * physical: technical solution, it is specific to a given database software and hardware
  * logical and physical can be either relational or dimensional
***

## Module 3 *RDBMS*
* relational database management system
* creating and managing databases
* create, retrieve update and manage data
* create reports, enforce database rules/constraints and maintain schema
  
### SQL
* structured query language
* used to create, manage, manipulate and query database objects
***

## Module 4 *Data Warehouse*
* specially constructed data repository where data is organized so that it can be easily accessed by end users for various applications
* common in corporations
* carry many years' worth of detailed data so historical trends can be analyzed
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

### Analytic Processing
* data warehouse is original defined as a decision support system(DSS)
* OLAP: Online Analytic Processing
  * comprise the complex analysis that are performed on a data set
  * data mining, querying, pivoting, slicing, dicing, drilling, reporting and other decision-support applications
  * a data warehouse can be used without OLAP
* OLTP: Online Transaction Processing
  * manages business applications and collects day to day data
  * different than a data warehouse
  * access small number of records or a few tables

### Data Warehouse Architecture
 ![alt text](DWarch.PNG "Data Warehouse Architecture")
* Acquisition: entry into data warehouse, raw data is acquired
* Integration: responsible for integrating data from multiple systems with common metrics and summaries
* Access: provide easy access to the data using various analytic methods
* Tiers:
 ![alt text](tiers.PNG "Tiers")
Not all data tiers are used for every feed coming in from a data source.

### Data Flow
1. Data Warehouse: data is collected and moved to a dedicated server contains a data warehouse
2. Analysis: data can be formatted, validated, recognized, summarized and supplemented
3. data is merged with data from many other sources
4. resulting data warehouse becomes the main source of information for data mining, OLAP, market research, report generation and analysis

### Types of Implementation
* Centralized
  *  useful for small and mid-size data warehouses
  *  a single physical repository
  *  serves separate department within an organization at the same time using a single data model
* Federated
  * share information among a number of different systems
  * master file will be shared and other system can use it
  * can reduce response time
* Data Mart
  * within a single organizational data warehouse repository
  * condensed an focused version of data warehouse dedicated to a specific business need
  * commonly multiple data marts to be used in order to server the needs of each department

### Deployment Options
* no right or wrong answers when choosing if to deploy a data warehouse on-prem or over the cloud
* On-prem
  * buying software and hardware from a data warehousing company
  * gives organization total control
  * most secure
  
* Cloud
  * in public or private cloud
  * trust issue is hard to overcome
  * require high bandwidth
  * private cloud can provide more security
***
## Module 5 *Teradata Advanced SQL Engine Introduction*
* stores current and historical data in one location
* enables effective data analysis and reporting
* a central repository of integrated data
* supports high performance, diverse queries and in-database analytics
* built-in parallelism enables faster processing
  
### Connect to Teradata
* client submit a SQL request to the Teradata Advanced SQL Engine
* the engine also receives response for the user 
* business-led, technology enabled

### Features and Benefits
* single version of business
* high availability
* high scalability
* teradata everywhere
* unlimited parallelism

### Objects with the Engine
* Partitioning: larger tables within a database is divided into smaller tables, can run faster
* tables, views, macros, triggers, stored procedures, and user-defined functions
* partitioned table: set of columns
* set table: no duplicate rows in a table
* secondary index: allows optional ways for the system to access the rows of a table
* stored procedure: a combination of pre defined procedural statements
* join index: enable join queries to be resolved without accessing or joining the actual tables
* user: as a collection of tables, views, macros, triggers, stored procedures, join indices and access right
* data types: specify the type of each values
* view: virtual table, not storing any information
* fallback: protecting the data against AMP failure
* macro: bundles multiple functions together
* trigger: defines a catalyst action and subsequent activities

#### Metadata
* Means of creation of the data
* Purpose of the data
* Time and date of creation along with the creator and author of the data
* Location on a computer network where the data was created
* Standards used and file size

#### Data Dictionary
* owned by the system user DBC
* composed of tables and views
* views provide access to the information in the tables
<p>
  <img width="250"  alt="Tables Store"src="tablestore.PNG" />
  <img width="250"  alt="Views Store"src="viewstore.PNG" />
</p>
<br>

### Components within the Teradata Advanced SQL Engine
* Virtual storage: TVS using SSD. Automatically store data on faster devices if that data get accessed frequently. Less visited stored on HDD.
* BYNET: handles internal communication of the engine.(From Parsing Engine to AMP)
* Node: general purpose processing unit under the control of a single os as hardware platform.
* Hot Standby Node: improve availability and maintain performance in case of node failure. Does not normally participate in operations but can be brought into compensate for the loss of a node
* Additional Options: other options to ensure data integrity
* Archive/Recovery(Teradata ARC): archiving data to tape and disk and restoring data to the Engine
* Teradata Data-Steam Architecture(DSA): similar functionality to ARC, but provides improved performance
* Clique: set of nodes share a common set of disk arrays. Cabling nodes to the same disk arrays creates a clique

### Virtual Components
* Parsing Engine: PE performs session control, query parsing, security validation, query optimization and query dispatch.Interprets sequel requests, receives input records and passes data.Send messages through message passing layer to AMP.
* Access Module Processor: AMP is responsible for managing a portion of the database. Do all the physical work and generating an answer set.
* Virtual Disk Space: is associated with an AMP.Tables and rows are stored in this space. Usually assigned to two or more disk drives in a disk array.
* Message Passing Layer: is the communication layer which is responsible for carrying messages between virtual processors(AMP and PE)
* <p>
  <img width="250"  alt="MPL"src="mpl.PNG" />
</p>

***
<p align="center">
  <img width="100"  alt="END-LOGO"src="the-end.png" />
</p>
