import mysql.connector

# Function to execute the query and print the result
def test_big_countries():
    # Establish a connection to MySQL database
    conn = mysql.connector.connect(
        host="your_mysql_host",
        user="your_mysql_user",
        password="your_mysql_password",
        database="your_database_name"
    )
    cur = conn.cursor()

    # Create the World table
    cur.execute('''
        CREATE TABLE World (
            name varchar(255) PRIMARY KEY,
            continent varchar(255),
            area int,
            population int,
            gdp bigint
        )
    ''')

    # Insert data into the World table
    cur.executemany('''
        INSERT INTO World (name, continent, area, population, gdp)
        VALUES (%s, %s, %s, %s, %s)
    ''', [
        ('Afghanistan', 'Asia', 652230, 25500100, 20343000000),
        ('Albania', 'Europe', 28748, 2831741, 12960000000),
        ('Algeria', 'Africa', 2381741, 37100000, 188681000000),
        ('Andorra', 'Europe', 468, 78115, 3712000000),
        ('Angola', 'Africa', 1246700, 20609294, 100990000000),
    ])

    # Commit the changes
    conn.commit()

    # Query to find big countries
    query = '''
        SELECT name, population, area
        FROM World
        WHERE area >= 3000000 OR population >= 25000000
    '''

    # Execute the query and fetch the result
    cur.execute(query)
    result = cur.fetchall()

    # Print the result
    print(result)

# Run the test function
test_big_countries()
