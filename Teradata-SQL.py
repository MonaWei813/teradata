"""
Teradata Vantage Data Engineering: SQL Part 1 (TDVAN4)
"""
# Character Data Type

# Create a set table in db named pd
CREATE SET TABLE pd.employee
{
    EmpNo INTEGER NOT NULL,
    DeptNo INTEGER,
    # CHAR type enforce fixed length
    # CHAR(20) means lastname is always 20 characters and use 20 bytes of storage
    # LATIN is one of the server_character_set
    LastName CHAR(20) CHARACTER SET LATIN NOT CASESPECIFIC,
    # VARCHAR is used for columns where we don’t want to enforce fixed length
    FirstName VARCHAR(20) CHARACTER SET LATIN NOT CASESPECIFIC,
    Gender CHARACTER NOT NULL CHARACTER SET LATIN NOT CASESPECIFIC
    SalaryAmount DECIMAL(10,2),
    # A Character Large OBject (CLOB) column can store large character data
    # such as simple text or HTML (Kilobytes; Megabytes; Gigabytes). 
    # It has a fixed length up to 2GB in size.
    Employee_Feedback CLOB(2M)
}
UNIQUE PRIMARY INDEX (EmpNo);
"""
CHAR uses a fixed length and hence there could be storage wastage if there is a great variance in the value length. On the other hand, if the variance in value length is minimum, CHAR can be preferred as they don’t take extra 2 bytes overhead unlike VARCHAR. 

Although VARCHAR uses only required storage depending on the value length, they take 2 bytes overhead to store the actual length of the data. They are preferred types over CHAR as we save space. However, they are good for values where there is a great variance in their length, so we get the benefit of space saving. For VARCHAR leading and trailing spaces are also counted.

- A table can have a maximum of 32 LOB columns 
- Queue tables cannot have CLOB columns 
- A LOB column cannot be a component of an index;.because of this restriction, a table must define at least one non-LOB column
- The CHARACTER SET clause can specify the following server character sets for a CLOB column: LATIN and UNICODE .
"""

# DATE and TIME