

#########################
# Import create_engine
from sqlalchemy import create_engine
# Create an engine that connects to the XXX.sqlite file
engine = create_engine("sqlite:///XXX.sqlite")

# Print table names
print(engine.table_names())

########################
# Import create_engine, MetaData, and Table
from sqlalchemy import create_engine, Table, MetaData
# Create engine, metadata
# Initialize MetaData: metadata
metadata = MetaData(engine)
# Reflect
# x = Table("tablename", metadata, autoload=True, autoload_with=engine)
# Doing this loads table info into Python as an object.

# # Print the column names
# print(x.columns.keys())
# result_proxy is result fo executing
# then we need to fetch the result proxy

# results = connection.execute("THE SELECT STRING;").fetchall()
# returns a list of "row proxies" (<class 'sqlalchemy.engine.result.RowProxy'>), which look like tuples to me.

# use idiomatic select (sqlalchemy.select()) and limit rows returned:
# results = connection.execute(stmt).fetchmany(size=10)
# the sqlalchemy select takes a list, with the object, not a string.

# ResultSet is technically a list (of lists)
######
# ORM where: statement.where(table.columns.colname.predicate("somerelevantstring"))
# where predicate is something like "startswith()" or "in" or "like"
# .in_(), .like(), .and_(), .or_()
# Then use a for loop to print (or whatever) the result.
# Because connection.execute() (the result proxy -- not necessarily the fetched result) is an iterable.
"""
stmt.where(or_(table.columns.colname == "x",
               table.columns.colname == "y"))
"""
connstring = "postgresql+psycopg2" + \
"://username:password" + \
"@postgresql.whatever.us-east-1.rds.amazonaws.com" + \
":5432/tablename"
engine = create_engine(connstring)

# We can iterate over the resultproxy.


# StatementToExecute = select([func.count(table.columns.colname.distinct())])  # counts distinct values
# ie, gives count of the distinct-transformed column object. apply the .distinct() method within the parentheses.


statementstring = select([table1, table2])

"""
statementstring_join = statementstring.select_from(
    table1.join(table2, table1.columns.joincol == table2.columns.joincol))

# Execute the statement and get the first result: result
resultfetched = connection.execute(statementstring_join).fetchall()

# Loop over the keys in the result object and print the key, value
for key in resultfetched.keys():
    print(key, getattr(resultfetched, key))
statement = select()  # put in some list of things, either whole tables or columns or subsets/aggregates of columns
statement.select_from()
statement.group_by()
"""

# Large resultsets.
"""
# Start a while loop checking for more results
while more_results:
    # Fetch the first 50 results from the ResultProxy: partial_results
    partial_results = results_proxy.fetchmany(50)

    # if empty list, set more_results to False
    if partial_results == []:
        more_results = False

    # Loop over the fetched records and increment the count for the state
    for row in partial_results:
        if row.state in state_count:
            state_count[row.state] += 1
        else:
            state_count[row.state] = 1

# Close the ResultProxy, and thus the connection
results_proxy.close()

# Print the count by state
print(state_count)
"""
#####
# Creating tables
#
# Alembic
# Import Table, Column, String, Integer, Float, Boolean from sqlalchemy
from sqlalchemy import Table, Column, String, Integer, Float, Boolean

# Define a new table with a name, count, amount, and valid column: data
data = Table('data', autoload=True,
             Column("name", String(255)),
             Column('count', Integer()),
             Column("amount", Float()),
             Column("valid", Boolean())
)

# Use the metadata to create the table
metadata.create_all(data)

# Print table details
print(repr(data))
#########################################
# Defaults:
# Import Table, Column, String, Integer, Float, Boolean from sqlalchemy
from sqlalchemy import Table, Column, String, Integer, Float, Boolean

# Define a new table with a name, count, amount, and valid column: data
data = Table('data', metadata,
             Column('name', String(255), unique=True),
             Column('count', Integer(), default=1),
             Column('amount', Float()),
             Column('valid', Boolean(), default=False)
)

# Use the metadata to create the table
metadata.create_all(engine)

# Print the table details
print(repr(metadata.tables['data']))
####
# Insert statement
stmt = insert(tablename)

# from sqlalchemy import insert, select
#
"""
the_insert_statement = sqlalchemy.insert(data).values(var1="text",
                                           intvar2=10,
                                           floatvar3=500.05,
                                           boolvar4=False)
"""

# if a separate list of values (ie, a list of dicts), pass as an argument to the connection.execute()
# command
# Pandas df .to_sql() uses sqlalchemy (i think) to put to a db table. need to specify table name, connection
# exist option (

# covered correlated updates. Use a value (eg, select([column]), then .order_by(desc(samecolumn))
# then .limit(1) to get the max value (call it newcolumnvalue)
# then pass that value to the update(table).values(column=newcolumnvalue)
# result_proxy = connection.execute(stmt)
# print(result_proxy.rowcount)
