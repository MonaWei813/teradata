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
    FirstName VARCHAR(20) CHARACTER SET LATIN NOT CASESPECIFIC,
    Gender CHARACTER NOT NULL CHARACTER SET LATIN NOT CASESPECIFIC
    SalaryAmount DECIMAL(10,2),
    Employee_Feedback CLOB(2M)
}
UNIQUE PRIMARY INDEX (EmpNo);