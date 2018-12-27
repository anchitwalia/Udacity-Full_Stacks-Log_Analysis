#! /usr/bin/env python
# Import the psycopg2 module to connect to database
import psycopg2


# Making a connection to database.
database = psycopg2.connect(database='news')
cur = database.cursor()


def articles():
    # It returns 3 most popular articles of all time
    print("       3 Most Popular Articles Of All Time Are:\n\n")
    # Query to execute 1
    cur.execute('''SELECT articles.title , count(*) AS frequency
                    FROM articles, log
                    WHERE log.status = '200 OK'
                    AND articles.slug = substring(log.path , 10)
                    GROUP BY articles.title
                    ORDER BY frequency DESC
                    LIMIT 3''')
    # fetchall() function will return the tuple of the data from the query
    result1 = cur.fetchall()
    for i in result1:
        print(str(i[0].title()) + " - " + str(i[1]) + " views")
    print("\n")


def authors():
        # It returns 4 most popular authors
    print("        Most Popular Authors Of All Time Are:\n\n")
    # Query to execute 2
    cur.execute('''SELECT authors.name, count(*) as frequency
                    FROM authors, articles, log
                    WHERE log.status = '200 OK'
                    AND authors.id = articles.author
                    AND articles.slug = substr(log.path, 10)
                    GROUP BY authors.name
                    ORDER BY frequency DESC''')
    result2 = cur.fetchall()
    # fetchall() function will return the tuple of the data from the query
    for i in result2:
        print(str(i[0].title()) + " - " + str(i[1]) + " views")
    print("\n")


def error():
    # Days in which error is more than 1%
    print("        Days in which error is more than 1%:\n\n")
    # Query to execute 3
    cur.execute('''SELECT f.date, round((f.fail*100/(f.fail + s.success)))
                    AS percentage FROM (SELECT DATE(time), count(*) AS fail
                    FROM log WHERE log.status = '404 NOT FOUND'
                    GROUP BY DATE(time)) AS f,
                    (SELECT DATE(time), count(*) AS success
                    FROM log WHERE log.status = '200 OK'
                    GROUP BY DATE(time)) AS s
                    WHERE f.date = s.date
                    AND f.fail*100 > (f.fail + s.success);''')
    result3 = cur.fetchall()
    # fetchall() function will return the tuple of the data from the query
    for i in result3:
        print(str(i[0]) + ": " + str(i[1]) + "% rate of failure")
    print("\n")

# Calling all the functions to execute queries


articles()
authors()
error()

# Disconnect the database
database.close()
