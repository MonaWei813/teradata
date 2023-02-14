<p align="center">
  <img width="400"  alt="TERA-LOGO"src="pngfind.com-artificial-intelligence-png-1049836.png" />
</p>
<br>

# Teradata Vantage Data Engineering: SQL Part 1 (TDVAN4)
## Module 1 *Character Data Type*

### Create a set table in db named pd
CREATE SET TABLE pd.employee
{
    EmpNo INTEGER NOT NULL,
    DeptNo INTEGER,
   CASESPECIFIC,
    FirstName VARCHAR(20) CHARACTER SET LATIN NOT CASESPECIFIC,
    Gender CHARACTER NOT NULL CHARACTER SET LATIN NOT CASESPECIFIC
    SalaryAmount DECIMAL(10,2),
    Employee_Feedback CLOB(2M)
}
UNIQUE PRIMARY INDEX (EmpNo);

***

* CHAR type **enforce fixed length**
* CHAR(20) means lastname is **always 20 characters** and use **20 bytes** of storage
* VARCHAR is used for columns where we don’t want to enforce fixed length
* A Character Large OBject (CLOB) column can store large character data such as simple text or HTML (Kilobytes; Megabytes; Gigabytes). 
* It has a fixed length up to 2GB in size.

**CHAR** uses a fixed length and hence there could be storage wastage if there is a great variance in the value length. On the other hand, if the variance in value length is minimum, CHAR can be preferred as they don’t take extra 2 bytes overhead unlike VARCHAR. 

Although VARCHAR uses only required storage depending on the value length, they take 2 bytes overhead to store the actual length of the data. They are preferred types over CHAR as we save space. However, they are good for values where there is a great variance in their length, so we get the benefit of space saving. For VARCHAR leading and trailing spaces are also counted.

- A table can have a maximum of 32 LOB columns 
- Queue tables cannot have CLOB columns 
- A LOB column cannot be a component of an index;.because of this restriction, a table must define at least one non-LOB column
- The CHARACTER SET clause can specify the following server character sets for a CLOB column: LATIN and UNICODE .
"""

# DATE and TIME
***
## Module 2 *Date and Time Type*
***
## Module 3 *Column Level Type*
***
## Module 4 *Period Data Type*
***
## Module 5 *JSON Data Type*
***
## Quiz
<p>
<img width="350" src="sql1q1.PNG", alt-text="Q1")>
<img width="350" src="sql1q2.PNG", alt-text="Q2")>
<img width="350" src="sql1q3.PNG", alt-text="Q3")>
<img width="350" src="sql1q4.PNG", alt-text="Q4")>
<img width="350" src="sql1q5.PNG", alt-text="Q5")>
<img width="350" src="sql1q6.PNG", alt-text="Q6")>
<img width="350" src="sql1q7.PNG", alt-text="Q7")>
<img width="350" src="sql1q8.PNG", alt-text="Q8")>
<img width="350" src="sql1q9.PNG", alt-text="Q9")>
<img width="350" src="sql1q10.PNG", alt-text="Q10")>
<img width="350" src="sql1q11.PNG", alt-text="Q11")>
<img width="350" src="sql1q12.PNG", alt-text="Q12")>
<img width="350" src="sql1q13.PNG", alt-text="Q13")>
<img width="350" src="sql1q14.PNG", alt-text="Q14")>
<img width="350" src="sql1q15.PNG", alt-text="Q15")>

<p>
<p align="center">
  <img width="100"  alt="END-LOGO"src="the-end.png" />
</p>
