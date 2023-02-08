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
* Message Passing Layer: is the communication layer which is responsible for carrying messages between virtual processors(AMP and PE) and making parallelism possible. It merges answer sets back to PE. It is a combination of PDE, BYNET software and BYNET hardware for MPP system.
  
<p>
  <img width="250"  alt="MPL"src="mpl.PNG" />
</p>

* Parallel Database Extensions(PDE): software interface layer that lies between the operating system and Teradata Advanced SQL Engine. Supports the parallelism which give the Engine its speed and linear scalability. The ability include:
  * Run in a parallel environment.
  * Execute Vprocs.
  * Manage and prioritize Teradata Advanced SQL Engine workloads.
  * Consistently manage memory, I/O, and messaging system interface across multiple OS platforms.

### Space Management
* before defining application users and databases, the database administrator creates a special administrative user and commonly assigns most of the space in the system to that user.
* space assigned to those objects is virtually separated from the administrative user's space
*  As these users and databases create their own objects, the administrator's space is added to these new users and databases.
*  Once space is allocated to a table, it cannot be reverted without the database administrator's permission.
*  The administrator re-organizes and re- allocates the space and partitions the data. 
*  Teradata’s approach to space management is flexible, dynamic and requires minimal involvement of the database administrator.
<p>
  <img width="600"  alt="Database Administrator"src="dba.PNG" />
</p>

#### Type of spaces
* Permanent Space
  * Perm space is used for storing the data rows of tables and is the maximum storage assigned to a user and/or database.
  *  Not pre-allocated or reserved, it is available on demand. Space is deducted from the owner's allocation as it is used.
* Spool Space
  * unused Perm space that holds intermediate query results or formatted answer sets for queries. 
  * Once the query is completed, the space is released.  
  * All databases have an upper limit of Spool Space. Theoretically, a user could use all the unallocated space in the system for their query.
* Temporary Space
  * sometimes referred to as Temp Space and is used for global temporary tables. 
  * Tables created in Temp Space will survive a restart and remain available to the user until their session is terminated.
* Database Space is the 
  * total amount of space available in the database to create and store objects that need permanent space.
  *  All space assigned to the User/Database is equally divided among all the of AMPs in the system.
***

## Module 6 *Data Distribution and Access Introduction*
* A distributed database represents multiple interconnected databases spread out across several sites connected by a network.
* uses hashing to dynamically distribute data across all AMPs.
* Hashing is the transformation of a string of characters into a usually shorter fixed-length value or key that represents the original string.
* provides optimized performance with minimal tuning and no manual reorganizations, resulting in lower administration costs and reduced development time.
* generates a row hash by hashing the values of the PI columns. The row hash and a sequence number, which is assigned to distinguish between rows with the same row hash within a table, are collectively called a row identifier and uniquely identify each row in a table.
* Teradata **QueryGrid** provides seamless, high-performing data access, processing, and movement across one or more systems in heterogeneous analytical environments.
  
### Metadata
* stored in tables that belong to user DBC and is reserved for use by the system.
* information is stored in the Data Dictionary. 
* The Data Dictionary contains metadata about the objects in the system like privileges, system events, and system usage. Views provide access to the information in the tables.

### Indexes
* Primary Index
  * a unique identifier that uniquely identifies each row.
  * The PI is defined when the table is created and is there for two major reasons:
    * To determine data distribution
    * Enhance performance
    * Indexes can provide an easier and faster way of accessing and locating data and thus reducing unwanted inputs and outputs.
  * Accessing data with equality on Primary Index result in a one AMP operation, which is extremely fast and efficient. Similar improvements can be seen with the use of other indexes.
  * A good choice of Primary Index will ensure even data distribution.
* No Primary Index
  *  simply a table without a primary index.
  *  NOPI tables are typically used as staging tables for the initial data load.
* Secondary Index
  * can be used to enforce uniqueness on a column. 
  * The SI also provides an alternate path to access data.
* Join Index
  * an indexing structure containing columns from multiple tables, specifically the resulting columns from one or more tables. 
  * The join Index (JI) is an optional index which may be created by the user to improve performance of complex queries.

#### Relationship between PI and PK
* PI  
  * A primary key is a logical database concept. 
  * Relational modeling convention which ensures each row to be uniquely identified
  * Consists of one or more columns
  * Must not be null and must be unique
  * Logical concept of data modeling
* PK
  * Teradata convention which determines how the row will be stored and accessed
  * Consists of more or more columns
  * May be unique or non-unique
  * Provides a physical access path and is also a mechanism for determining where the data is stored
* Unique Primary Index(UPI)
* Non Unique Primary Index
* Unique Secondary Index
* Non Unique Secondary Index: One or more columns, may have duplicate values and is used to improve access.
* Partition Primary Index
  * Can quickly improve the performance of complex range-based queries.
  * Partitioned Primary Index (PPI) is an indexing mechanism that is useful in improving the performance of certain queries. 
  * When rows are inserted into a table, they are stored in an AMP and arranged by their row hash order. 
  * When a table is defined with PPI, the rows are sorted by their partition number. Within each partition, they are arranged by their row hash. Rows are assigned to a partition based on the partition expression defined.
* No Primary Index(): Supports faster loads and inserts into tables with no primary index defined.
***
<p align="center">
  <img width="100"  alt="END-LOGO"src="the-end.png" />
</p>
