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

## Common types of Databases
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

## Data Modelling
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
  
## SQL
* structured query language
* used to create, manage, manipulate and query database objects
***

## Module 4 *Data Warehouse*
* specially constructed data repository where data is organized so that it can be easily accessed by end users for various applications
* common in corporations
* carry many years' worth of detailed data so historical trends can be analyzed
* data warehousing is a process **NOT** a product which manage and assemble data from various sources to answer business questions

## Data Mart
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

## Analytic Processing
* data warehouse is original defined as a decision support system(DSS)
* OLAP: Online Analytic P
***
<p align="center">
  <img width="100"  alt="END-LOGO"src="the-end.png" />
</p>
