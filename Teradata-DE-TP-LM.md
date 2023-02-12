<p align="center">
  <img width="400"  alt="TERA-LOGO"src="pngfind.com-artificial-intelligence-png-1049836.png" />
</p>
<br>

# **Teradata Data Engineering Transaction Processing and Lock Management(TDVAN4)**

## Module 1 *Session and Transactions in Vantage*
### Session
* A **session** is a **logical connection** between the user and Teradata Vantage that allows users to **submit** one transaction at a time and receive one response at a time. 
* Any current session can have **only one** transaction outstanding at any time.
* A user may communicate through **one or more** active sessions concurrently.
* A session is **explicitly** logged on and off from Teradata Vantage.
  * **Logged On**: A session is established when the Teradata Vantage server accepts the logon string of the user.
  * **Logged Off**: When a session is logged off the system discards the user-session identification and does not accept additional Teradata SQL statements from that Session.
##### The Database Administrator can specify the number of sessions a user or utility can use at a time. The maximum number of sessions per parsing engine (PE) is 120.

##### Utility session rules specify the number of sessions that a utility job can use. 
To create utility session rules in the Workload Designer portlet in Viewpoint, you can access the Utility Sessions tab from the Sessions view. Utility session rules override the minimum and maximum session limits in scripts (the MINSESS and MAXSESS parameters). For **non-conforming** utilities, utility session rules override **only the maximum** session limits.

### Transaction Processing in Teradata Vantage
Processing in Vantage is **transaction-based**. The principal purpose of transaction management is to **optimize concurrency** to ensure that as many sessions as possible can access the information in the database concurrently without compromising the consistency or integrity of the data.
* **Transaction**
  * Consists of one or more **requests**
  * Unit of work (a **set of SQL** operations to be performed)
  * Unit of recovery (a **set of rollback operations** to be performed)
  * Can be **implicit or explicit** ET (Teradata mode) or **COMMIT WORK** (ANSI mode) which commits the currently active EXPLICIT transaction
  * A **DDL** command must be the **last request** in a transaction
  * At the **end of a transaction**, two important activities occur:
    * The **transient journal** (TJ) images are discarded from the WAL log
    * The **locks are released**
* **Requests**
  * Consists of one or more **statements** 
  * A **minimal** unit of work that is transmitted from a client system
    * Request-level API options
    * Zero or more SQL statements
    * Request-related metadata
    * Request-related data
  * Gets **parsed** (syntax checking, resolving, security, optimization)
  * Applies the **most restrictive** locks of all statements in the request (i.e., there is no upgrading of locks within a request)
  * May be committed **implicitly** (i.e., as an implicit transaction)
  * Is all or nothing (i.e., should any statement error or fail, the request will error or fail)
  * **Cannot** mix DML and DDL in the same request
* **Statements**
  * An SQL construct 
  * Requires locks
  * May be sent, by itself, as a request
  * May be one statement in a multi-statement request
  * May be components of a macro
  * May be components of an SQL procedure
###  Differences between Teradata and ANSI modes 
* **Teradata Transaction Mode**
  * Teradata session mode is also referred to as **Begin Transaction End Transaction (BTET) mode**
  * Each request submitted in Teradata session mode is an **implicit transaction** unless it is preceded by a **BEGIN TRANSACTION** statement, in which case, the transaction becomes **explicit**
  * The default is that a transaction is implicit. Explicit transactions are available using the BT and ET commands
CREATE TABLE – Defaults to SET table
Data comparison is NOT case specific
Allows truncation of display data
(Example: Insert ‘Teradata’ in column data type CHAR(6) -> Insert ‘Terada’ and successful)
Error Behavior – Only Warnings, Failures and Successes are notified, but not the Errors. A Failure rolls back the entire transaction and releases the locks
Failure Behavior – Rolls back the transaction whether implicit or explicit and releases all locks
* **ANSI Transaction Mode**
## Module 2 *Lock Management in Teradata Vantage*
## Module 3 *System Default*
***

<p align="center">
  <img width="100"  alt="END-LOGO"src="the-end.png" />
</p>