Objects and Session Modes
1.	
Which setting controls Teradata versus ANSI mode?
The ANSI Flagger
✓  The Session Transaction setting
The Transaction Protocol setting
The .LOGON command

2.	
The default for comparisons in ANSI mode is casespecific.
✓  True
False

3.	
We have just been handed an ad-hoc request for information which will require us to run a bunch of queries against a summary of last year's sales figures. What is the best choice for this situation?
Global Temporary table
✓  Volatile table
Derived table

4.	
We need to agree with the marketing people on a single table layout so that our numbers can be compared with theirs at the end of the week. What is the best choice for this situation?
X  Derived table
Volatile table ?
Global Temporary table

5.	
When end-of-month queries are run this weekend, make sure that the scripts are set up to populate the necessary temporary tables without having to create them. What is the best choice for this situation?
✓  Global Temporary table
Volatile table
Derived table

6.	
Suppose the system default is to have NO PRIMARY INDEX. Given the below SQL, what will the primary index be?
CREATE TABLE table1
( col1 INTEGER NOT NULL,
col2 INTEGER UNIQUE,
col3 INTEGER PRIMARY KEY,
col4 INTEGER,
CONSTRAINT unique_1 UNIQUE (col1,col4));
col2
col1, col4
No Primary Index ?
X  col1
col3

7.	
Which commands will not work in ANSI mode?
Commands in upper case
✓  BEGIN TRANSACTION and END TRANSACTION
All Teradata extension commands
DML commands

Complex Queries
8.	
What is the maximum number of levels of nesting permitted in a query?
X  32
64 this
128

9.	
If a query depth is not specified in a recursive query, the query is unprotected from infinite looping.
✓  True
False

10.	
Suppose you execute this MERGE INTO query.
MERGE INTO policy
USING VALUES (12345, 'Avril Mondragon', 100000.00) AS NewPolicy (policynum, holdername, policyamt)
ON NewPolicy.policynum = policy_number
WHEN MATCHED THEN UPDATE
SET policy_amount = NewPolicy.policyamt
WHEN NOT MATCHED THEN INSERT
VALUES (NewPolicy.policynum, NewPolicy.holdername, NewPolicy.policyamt, NULL);
What is the result of this query?
SELECT policy_amount
FROM policy
WHERE policy_number = 12345;
We do not know because we do not know if the row was originally in the policy table
12345
✓  100000.00

11.	
When you use a PIVOT followed by an UNPIVOT, you are guaranteed to reproduce the original data.
True
✓  False

Complex Aggregations
12.	
Which of the following functions would you need to represent sales figures for March incremented daily with a final total?
Remaining Sum
X  Moving Sum
Cumulative Sum this
RANK

13.	
Which of the following functions would you need to solve this question: what are the three highest moving averages during February?
Moving AVG, QUANTILE
Moving AVG, SAMPLE
Moving AVG, Cumulative SUM
✓  Moving AVG, RANK

14.	
Which of the following functions would you need to solve this question: what percentage of stores took in less than $25 million last year?
✓  QUANTILE
Cumulative SUM
Moving AVG, RANK
MDIFF

15.	
Which of the following functions is identified by the use of the keywords UNBOUNDED PRECEDING and absence of keywords UNBOUNDED FOLLOWING?
✓  SUM Window Cumulative Function
SUM Window Remaining Function
SUM Window Group Function
SUM Window Moving Function

16.	
Which of the following choices represents the ability to generate different sized samples from different groupings of the data?
Replacement sampling
Randomized sampling
Partitioned sampling
✓  Stratified sampling

17.	
If you want a sample of data to not include duplicate data, which clause should you avoid?
X  SAMPLE PROPORTIONAL ALLOCATION
SAMPLE WITH REPLACEMENT
SAMPLE RANDOMIZED ALLOCATION
SAMPLE STRATIFICATION this

18.	
With the GROUP BY CUBE function, order does not matter. GROUP BY CUBE (col1, col2) is logically the same as GROUP BY CUBE (col2, col1).
✓  True
False

Date, Time, and Formatting
19.	
Choose one of the following SDF Numeric Formatting Options which would be used to represent the number of characters needed to display the INTEGER portion of numeric data.
I
F this
D
X  Z

20.	
Which command will establish the default date format of a session as YY/MM/DD?
SET SESSION DATEFORM=INTEGERDATE this
X  SET SESSION DATEFORM=TERADATADATE
SET SESSION DATEFORM=ANSIDATE
SET SESSION DATEFORM=TMODE

21.	
What is the result of the below SQL?
SELECT OADD_MONTHS (DATE '2020-02-29', 1);
2020-03-31
X  2020-03-29
2020-03-28 this
2021-02-28

22.	
What is the result of the below SQL?
SELECT EXTRACT (TIMEZONE_HOUR FROM TIMESTAMP '2016-04-15 10:30:00+06:00');
6 this
X  10
16:30
30

23.	
What is the result of the below SQL?
SELECT EXTRACT (MINUTE FROM (TIME '08:30:20' + INTERVAL '20:45' MINUTE TO SECOND));
20
30
50
✓  51

1.	
Which setting controls Teradata versus ANSI mode?
The Transaction Protocol setting
The ANSI Flagger
The .LOGON command
✓  The Session Transaction setting

2.	
The ANSI Flagger is just a warning device and does not affect command execution.
True
X  False

3.	
Primary Key constraints can always be dropped if they are no longer needed.
X  True
False

4.	
We need to agree with the marketing people on a single table layout so that our numbers can be compared with theirs at the end of the week. What is the best choice for this situation?
Derived table
X  Volatile table
Global Temporary table

5.	
Will the following SQL statement succeed or fail?
CREATE TABLE dept_new(a,b,c) AS
(SELECT department_number
, department_name
FROM dept) WITH DATA;
Succeed
✓  Fail

6.	
Match the Referential Integrity type with its description:
A. Does not actually maintain RI, but helps with join elimination
C. No subtable; Teradata database joins the tables together each time there is a relevant INSERT, UPDATE or DELETE
B. Maintains a subtable to enforce the RI relationship
     	
A. Soft RI
B. Standard RI
C. Batch RI

7.	
If you are using ANSI mode instead of Teradata mode, which two (2) operations might produce different results?
✓  Data conversions
✓  Case sensitivities
OUTER JOIN
INNER JOIN

Complex Queries
8.	
Derived tables may replace the use of temporary tables by using:
Four separate statements
✓  A single statement
Three separate statements
Two separate statements

9.	
Whether using the MERGE or UPDATE syntax for Upsert processing, both must use the Primary Index value of the row to perform their respective operations.
✓  True
False

10.	
Suppose you execute this MERGE INTO query.
MERGE INTO policy
USING VALUES (12345, 'Avril Mondragon', 100000.00) AS NewPolicy (policynum, holdername, policyamt)
ON NewPolicy.policynum = policy_number
WHEN MATCHED THEN UPDATE
SET policy_amount = NewPolicy.policyamt
WHEN NOT MATCHED THEN INSERT
VALUES (NewPolicy.policynum, NewPolicy.holdername, NewPolicy.policyamt, NULL);
What is the result of this query?
SELECT policy_amount
FROM policy
WHERE policy_number = 12345;
12345
We do not know because we do not know if the row was originally in the policy table
✓  100000.00

11.	
If you want to make use an exclusion operation in a query, what is the better choice from a performance standpoint?
NOT IN with a derived query
✓  NOT EXISTS with a correlated subquery

Complex Aggregations
12.	
The COALESCE function always produces integer results.
True
✓  False

13.	
Which of the following functions would you need to solve this question: what are the three highest moving averages during February?
Moving AVG, SAMPLE
Moving AVG, QUANTILE
✓  Moving AVG, RANK
Moving AVG, Cumulative SUM

14.	
A COUNT Window cannot be done in a SELECT involving MIN or MAX functions.
✓  True
False

15.	
COUNT Window and SUM Window are ANSI standard functions.
True
X  False

16.	
Which of the following choices represents the ability to generate different sized samples from different groupings of the data?
✓  Stratified sampling
Randomized sampling
Partitioned sampling
Replacement sampling

17.	
If you want a sample of data to not include duplicate data, which clause should you avoid?
X  SAMPLE STRATIFICATION
SAMPLE PROPORTIONAL ALLOCATION
SAMPLE WITH REPLACEMENT
SAMPLE RANDOMIZED ALLOCATION

18.	
Match the GROUP BY clause with its purpose.
B. You want to show aggregates for all permutations
C. You want to show aggregates for specific permutations
A. You want to show aggregates for a hierarchy
     	
A. ROLLUP
B. CUBE
C. GROUPING SETS

Date, Time, and Formatting
19.	
Choose one of the following SDF Numeric Formatting Options which would be used to separate a whole number from its fractional component.
L
G
X  F
D

20.	
Given the below query, what will the results look like?
X  Time values will be relative to the local time zone, with no time zone displayed.
Time values will be shown as the user originally entered it, and that original time zone will be displayed.
SELECT timecolumn AT LOCAL
Time values will be relative to the local time zone, and the local time zone will be displayed.
FROM table1;

21.	
What is the result of the below SQL?
SELECT ADD_MONTHS (DATE '2020-02-29', 1);
2020-03-29
2020-03-31
X  2020-03-28
2021-02-28

22.	
What is the result of the below SQL?
SELECT (DATE '2018-03-01' - DATE '2016-01-01') DAY;
2-02
X  790
Failure - Interval field overflow
26-00

23.	
What is the result of the below SQL?
SELECT EXTRACT (MINUTE FROM (TIME '08:30:20' + INTERVAL '20:45' MINUTE TO SECOND));
20
30
X  50
51

1.	
Which setting controls Teradata versus ANSI mode?
✓  The Session Transaction setting
The Transaction Protocol setting
The ANSI Flagger
The .LOGON command

2.	
Logging off during an explicit transaction without either a COMMIT or ET will result in a ROLLBACK of any changes.
✓  True
False

3.	
We have just been handed an ad-hoc request for information which will require us to run a bunch of queries against a summary of last year's sales figures. What is the best choice for this situation?
Global Temporary table
✓  Volatile table
Derived table

4.	
This query requires me to denormalize information in three different tables and then join the results. Fortunately, I only need to do it one time. What is the best choice for this situation?
✓  Derived table
Volatile table
Global Temporary table

5.	
When end-of-month queries are run this weekend, make sure that the scripts are set up to populate the necessary temporary tables without having to create them. What is the best choice for this situation?
✓  Global Temporary table
Derived table
Volatile table

6.	
Suppose the system default is to have NO PRIMARY INDEX. Given the below SQL, what will the primary index be?
CREATE TABLE table1
( col1 INTEGER NOT NULL,
col2 INTEGER UNIQUE,
col3 INTEGER PRIMARY KEY,
col4 INTEGER,
CONSTRAINT unique_1 UNIQUE (col1,col4));
col1, col4
col2
col1
X  No Primary Index
col3

7.	
If you are using ANSI mode instead of Teradata mode, which two (2) operations might produce different results?
✓  Case sensitivities
✓  Data conversions
OUTER JOIN
INNER JOIN

Complex Queries
8.	
Correlated subqueries or derived tables may be used to answer the same question in some cases.
✓  True
False

9.	
Whether using the MERGE or UPDATE syntax for Upsert processing, both must use the Primary Index value of the row to perform their respective operations.
✓  True
False

10.	
Suppose you execute this MERGE INTO query.
MERGE INTO policy
USING VALUES (12345, 'Avril Mondragon', 100000.00) AS NewPolicy (policynum, holdername, policyamt)
ON NewPolicy.policynum = policy_number
WHEN MATCHED THEN UPDATE
SET policy_amount = NewPolicy.policyamt
WHEN NOT MATCHED THEN INSERT
VALUES (NewPolicy.policynum, NewPolicy.holdername, NewPolicy.policyamt, NULL);
What is the result of this query?
SELECT policy_amount
FROM policy
WHERE policy_number = 12345;
✓  100000.00
We do not know because we do not know if the row was originally in the policy table
12345

11.	
A WITH table may be defined once and referenced multiple times throughout the query.
✓  True
False

Complex Aggregations
12.	
Which of the following functions would you need to represent sales figures for March incremented daily with a final total?
✓  Cumulative Sum
Moving Sum
RANK
Remaining Sum

13.	
Which of the following functions would you need to solve this question: what are the three highest moving averages during February?
Moving AVG, SAMPLE
Moving AVG, QUANTILE
Moving AVG, Cumulative SUM
✓  Moving AVG, RANK

14.	
Which of the following functions would you need to solve this question: what percentage of stores took in less than $25 million last year?
Moving AVG, RANK
MDIFF
✓  QUANTILE
Cumulative SUM

15.	
Which of the following functions is identified by the total absence of the keyword UNBOUNDED?
SUM Window Cumulative Function
✓  SUM Window Moving Function
SUM Window Remaining Function
SUM Window Group Function

16.	
Which of the following functions is identified by use of keywords UNBOUNDED FOLLOWING and absence of keywords UNBOUNDED PRECEDING?
SUM Window Moving Function
SUM Window Group Function
SUM Window Remaining Function
X  SUM Window Cumulative Function

17.	
By default, the SAMPLE clause takes a proportional allocation, meaning that a sample will be proportional to the number of qualified rows on each AMP. To override this default, you would use:
SAMPLE ACROSS AMPS
SAMPLE WITH RANDOM
SAMPLE RANDOMIZED ALLOCATION
X  SAMPLE RANDOM AMPS

18.	
Which function should you use if you want rows to be given a unique number, even in the event of a tie?
RANK() OVER (ORDER BY column1)
DENSE_RANK() OVER (ORDER BY column1)
ROW_NUMBER() OVER (ORDER BY column1)
X  RANK() OVER (ORDER BY column1 WITH TIES LOW)

Date, Time, and Formatting
19.	
Choose one of the following SDF Numeric Formatting Options which would be used to separate a whole number from its fractional component.
G
F
L
✓  D

20.	
Given the below query, what will the results look like?
X  Time values will be shown as the user originally entered it, and that original time zone will be displayed.
FROM table1;
SELECT timecolumn AT LOCAL
Time values will be relative to the local time zone, and the local time zone will be displayed.
Time values will be relative to the local time zone, with no time zone displayed.

21.	
What is the result of the below SQL?
SELECT DATE '2017-07-15' + INTERVAL '2-04' YEAR TO MONTH;
2017-11-17
2017-09-19
✓  2019-11-15
2019-11-17

22.	
What is the result of the below SQL?
SELECT (DATE '2018-03-01' - DATE '2016-01-01') DAY;
X  2-02
Failure - Interval field overflow
26-00
790

23.	
What is the result of the below SQL?
SELECT 'overlapping'
WHERE (TIME '01:00:00', TIME '10:00:00') OVERLAPS (TIME '01:01:00', TIME '03:00:00');
✓  'overlapping'
no rows returned
(TIME '01:01:00', TIME '03:00:00')

Objects and Session Modes
1.	
To set the session mode in BTEQ, use this command:
SET SESSION MODE (ANSI) OR (BTET)
✓  SET SESSION TRANSACTION (ANSI) OR (BTET)
SET SESSION TYPE (ANSI) OR (BTET)

2.	
The default for comparisons in ANSI mode is casespecific.
✓  True
False

3.	
We have just been handed an ad-hoc request for information which will require us to run a bunch of queries against a summary of last year's sales figures. What is the best choice for this situation?
✓  Volatile table
Derived table
Global Temporary table

4.	
Get me the top ten products by revenue and the top ten by profitability and do an outer join on them. What is the best choice for this situation?
✓  Derived table
Global Temporary table
Volatile table

5.	
Will the following SQL statement succeed or fail?
CREATE TABLE dept_new(a,b,c) AS
(SELECT department_number
, department_name
FROM dept) WITH DATA;
✓  Fail
Succeed

6.	
Which of the following attributes are copied to the new table when you use CREATE TABLE AS? (Choose 3)
✓  CHECK constraints
X  FOREIGN KEY constraints
Triggers
✓  PRIMARY KEY constraints
➤  Data types

7.	
Which commands will not work in ANSI mode?
Commands in upper case
✓  BEGIN TRANSACTION and END TRANSACTION
DML commands
All Teradata extension commands

Complex Queries
8.	
Derived tables may replace the use of temporary tables by using:
✓  A single statement
Three separate statements
Two separate statements
Four separate statements

9.	
Whether using the MERGE or UPDATE syntax for Upsert processing, both must use the Primary Index value of the row to perform their respective operations.
✓  True
False

10.	
Which three are features of WITH clause processing?
X  Iterative control statements
✓  Recursive views
➤  Non-recursive derived tables
✓  Recursive INSERT/SELECTs

11.	
When you use a PIVOT followed by an UNPIVOT, you are guaranteed to reproduce the original data.
True
✓  False

Complex Aggregations
12.	
Which of the following functions would you need to represent sales figures for March incremented daily with a final total?
Remaining Sum
RANK
✓  Cumulative Sum
Moving Sum

13.	
Which of the following functions would you need to graph the disparities between sales on Saturdays in Q1?
Moving SUM
➤  Moving Difference
X  QUANTILE
Moving AVG

14.	
Which of the following functions would you need to solve this question: what percentage of stores took in less than $25 million last year?
✓  QUANTILE
MDIFF
Cumulative SUM
Moving AVG, RANK

15.	
Which of the following functions is identified by the total absence of the keyword UNBOUNDED?
SUM Window Group Function
SUM Window Remaining Function
SUM Window Cumulative Function
✓  SUM Window Moving Function

16.	
Which of the following choices represents the ability to generate different sized samples from different groupings of the data?
Partitioned sampling
Randomized sampling
✓  Stratified sampling
Replacement sampling

17.	
By default, the SAMPLE clause takes a proportional allocation, meaning that a sample will be proportional to the number of qualified rows on each AMP. To override this default, you would use:
SAMPLE ACROSS AMPS
X  SAMPLE WITH RANDOM
SAMPLE RANDOM AMPS
➤  SAMPLE RANDOMIZED ALLOCATION

18.	
Which function should you use if you want rows to be given a unique number, even in the event of a tie?
✓  ROW_NUMBER() OVER (ORDER BY column1)
DENSE_RANK() OVER (ORDER BY column1)
RANK() OVER (ORDER BY column1)
RANK() OVER (ORDER BY column1 WITH TIES LOW)

Date, Time, and Formatting
19.	
Choose one of the following SDF Numeric Formatting Options which would be used to separate a whole number from its fractional component.
G
F
✓  D
L

20.	
Which of the following are options for formatting result sets in Teradata Studio Express (15.10)? Choose 3.
➤  Alternating colors of result set rows
✓  Using a 1000 separator
X  Adding a currency symbol
✓  Choosing how you want to display a NULL value

21.	
What is the result of the below SQL?
SELECT DATE '2017-07-15' + INTERVAL '2-04' YEAR TO MONTH;
2017-11-17
2017-09-19
✓  2019-11-15
2019-11-17

22.	
What is the result of the below SQL?
SELECT EXTRACT (TIMEZONE_HOUR FROM TIMESTAMP '2016-04-15 10:30:00+06:00');
✓  6
10
16:30
30

23.	
What is the result of the below SQL?
SELECT EXTRACT (MINUTE FROM (TIME '08:30:20' + INTERVAL '20:45' MINUTE TO SECOND));
20
30
50
✓  51


1.	
To set the session mode in BTEQ, use this command:
SET SESSION MODE (ANSI) OR (BTET)
SET SESSION TYPE (ANSI) OR (BTET)
✓  SET SESSION TRANSACTION (ANSI) OR (BTET)

2.	
The default for comparisons in ANSI mode is casespecific.
✓  True
False

3.	
We have just been handed an ad-hoc request for information which will require us to run a bunch of queries against a summary of last year's sales figures. What is the best choice for this situation?
Global Temporary table
Derived table
✓  Volatile table

4.	
We need to agree with the marketing people on a single table layout so that our numbers can be compared with theirs at the end of the week. What is the best choice for this situation?
Derived table
Volatile table
✓  Global Temporary table

5.	
When end-of-month queries are run this weekend, make sure that the scripts are set up to populate the necessary temporary tables without having to create them. What is the best choice for this situation?
Volatile table
✓  Global Temporary table
Derived table

6.	
Suppose the system default is to have NO PRIMARY INDEX. Given the below SQL, what will the primary index be?
CREATE TABLE table1
( col1 INTEGER NOT NULL,
col2 INTEGER UNIQUE,
col3 INTEGER PRIMARY KEY,
col4 INTEGER,
CONSTRAINT unique_1 UNIQUE (col1,col4));
No Primary Index
col1, col4
col1
✓  col3
col2

7.	
If you are using ANSI mode instead of Teradata mode, which two (2) operations might produce different results?
INNER JOIN
✓  Case sensitivities
OUTER JOIN
✓  Data conversions

Complex Queries
8.	
Derived tables may replace the use of temporary tables by using:
✓  A single statement
Two separate statements
Three separate statements
Four separate statements

9.	
If a query depth is not specified in a recursive query, the query is unprotected from infinite looping.
✓  True
False

10.	
Which three are features of WITH clause processing?
✓  Non-recursive derived tables
Iterative control statements
✓  Recursive views
✓  Recursive INSERT/SELECTs

11.	
If you want to make use an exclusion operation in a query, what is the better choice from a performance standpoint?
✓  NOT EXISTS with a correlated subquery
NOT IN with a derived query

Complex Aggregations
12.	
Which of the following functions would you need to represent sales figures for March incremented daily with a final total?
RANK
✓  Cumulative Sum
Remaining Sum
Moving Sum

13.	
Which of the following functions would you need to graph the disparities between sales on Saturdays in Q1?
QUANTILE
Moving SUM
Moving AVG
✓  Moving Difference

14.	
SUM Window results may be used in other calculations.
✓  True
False

15.	
Which of the following functions is identified by the total absence of the keyword UNBOUNDED?
SUM Window Remaining Function
SUM Window Group Function
SUM Window Cumulative Function
✓  SUM Window Moving Function

16.	
Which of the following functions is identified by use of keywords UNBOUNDED FOLLOWING and absence of keywords UNBOUNDED PRECEDING?
X  SUM Window Cumulative Function
SUM Window Remaining Function
SUM Window Moving Function
SUM Window Group Function

17.	
If you want a sample of data to not include duplicate data, which clause should you avoid?
X  SAMPLE RANDOMIZED ALLOCATION
SAMPLE STRATIFICATION
SAMPLE WITH REPLACEMENT
SAMPLE PROPORTIONAL ALLOCATION

18.	
Match the GROUP BY clause with its purpose.
X  You want to show aggregates for all permutations
X  You want to show aggregates for specific permutations
X  You want to show aggregates for a hierarchy
     	
A. ROLLUP
B. CUBE
C. GROUPING SETS

Date, Time, and Formatting
19.	
Choose one of the following SDF Numeric Formatting Options which would be used to separate a whole number from its fractional component.
✓  D
L
G
F

20.	
Given the below query, what will the results look like?
Time values will be relative to the local time zone, with no time zone displayed.
FROM table1;
Time values will be shown as the user originally entered it, and that original time zone will be displayed.
SELECT timecolumn AT LOCAL
X  Time values will be relative to the local time zone, and the local time zone will be displayed.

21.	
What is the result of the below SQL?
SELECT DATE '2017-07-15' + INTERVAL '2-04' YEAR TO MONTH;
2017-11-17
2017-09-19
✓  2019-11-15
2019-11-17

22.	
What is the result of the below SQL?
SELECT (DATE '2018-03-01' - DATE '2016-01-01') DAY;
2-02
X  26-00
790
Failure - Interval field overflow

23.	
What is the result of the below SQL?
SELECT 'overlapping'
WHERE (TIME '01:00:00', TIME '10:00:00') OVERLAPS (TIME '01:01:00', TIME '03:00:00');
(TIME '01:01:00', TIME '03:00:00')
X  no rows returned
'overlapping'

1.	
To set the session mode in BTEQ, use this command:
SET SESSION MODE (ANSI) OR (BTET)
✓  SET SESSION TRANSACTION (ANSI) OR (BTET)
SET SESSION TYPE (ANSI) OR (BTET)

2.	
Logging off during an explicit transaction without either a COMMIT or ET will result in a ROLLBACK of any changes.
✓  True
False

3.	
Primary Key constraints can always be dropped if they are no longer needed.
True
✓  False

4.	
Get me the top ten products by revenue and the top ten by profitability and do an outer join on them. What is the best choice for this situation?
Global Temporary table
✓  Derived table
Volatile table

5.	
When end-of-month queries are run this weekend, make sure that the scripts are set up to populate the necessary temporary tables without having to create them. What is the best choice for this situation?
Volatile table
✓  Global Temporary table
Derived table

6.	
Suppose the system default is to have NO PRIMARY INDEX. Given the below SQL, what will the primary index be?
CREATE TABLE table1
( col1 INTEGER NOT NULL,
col2 INTEGER UNIQUE,
col3 INTEGER PRIMARY KEY,
col4 INTEGER,
CONSTRAINT unique_1 UNIQUE (col1,col4));
col2
col1
No Primary Index
✓  col3
col1, col4

7.	
If you are using ANSI mode instead of Teradata mode, which two (2) operations might produce different results?
✓  Data conversions
✓  Case sensitivities
OUTER JOIN
INNER JOIN

Complex Queries
8.	
Derived tables may replace the use of temporary tables by using:
Two separate statements
✓  A single statement
Four separate statements
Three separate statements

9.	
If a query depth is not specified in a recursive query, the query is unprotected from infinite looping.
✓  True
False

10.	
Which three are features of WITH clause processing?
✓  Non-recursive derived tables
Iterative control statements
✓  Recursive INSERT/SELECTs
✓  Recursive views

11.	
When you use a PIVOT followed by an UNPIVOT, you are guaranteed to reproduce the original data.
True
✓  False

Complex Aggregations
12.	
Which of the following functions do you need to answer this question: given a random selection of six products, what is the moving average of their product sales for the twelve months of 2005?
QUANTILE, RANK
MDIFF
RANK
✓  Moving AVG, SAMPLE

13.	
Which of the following functions would you need to graph the disparities between sales on Saturdays in Q1?
Moving SUM
➤  Moving Difference
X  QUANTILE
Moving AVG

14.	
A COUNT Window cannot be done in a SELECT involving MIN or MAX functions.
✓  True
False

15.	
Which of the following functions is identified by the total absence of the keyword UNBOUNDED?
SUM Window Cumulative Function
✓  SUM Window Moving Function
SUM Window Group Function
SUM Window Remaining Function

16.	
Which of the following choices represents the ability to generate different sized samples from different groupings of the data?
Partitioned sampling
Randomized sampling
✓  Stratified sampling
Replacement sampling

17.	
If you want a sample of data to not include duplicate data, which clause should you avoid?
SAMPLE STRATIFICATION
SAMPLE RANDOMIZED ALLOCATION
SAMPLE PROPORTIONAL ALLOCATION
✓  SAMPLE WITH REPLACEMENT

18.	
With the GROUP BY CUBE function, order does not matter. GROUP BY CUBE (col1, col2) is logically the same as GROUP BY CUBE (col2, col1).
✓  True
False

Date, Time, and Formatting
19.	
Choose one of the following SDF Numeric Formatting Options which would be used to separate a whole number from its fractional component.
✓  D
F
L
G

20.	
Which command will establish the default date format of a session as YY/MM/DD?
SET SESSION DATEFORM=TERADATADATE
SET SESSION DATEFORM=TMODE
✓  SET SESSION DATEFORM=INTEGERDATE
SET SESSION DATEFORM=ANSIDATE

21.	
What is the result of the below SQL?
SELECT ADD_MONTHS (DATE '2020-02-29', 1);
✓  2020-03-29
2020-03-31
2020-03-28
2021-02-28

22.	
What is the result of the below SQL?
SELECT CAST ((INTERVAL '1 04:45' DAY TO MINUTE) AS INTERVAL HOUR TO MINUTE);
4:45
✓  28:45
29:00
104 h 45 m

23.	
What is the result of the below SQL?
SELECT EXTRACT (MINUTE FROM (TIME '08:30:20' + INTERVAL '20:45' MINUTE TO SECOND));
20
30
50
✓  51
