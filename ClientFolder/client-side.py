'''
@author: Ashlyn Campbell
VM2
'''
from dotenv import load_dotenv
import psycopg2 as p
from psycopg2 import Error
import socket
import json
import os

load_dotenv()
def run():
    # server socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0',8888))
    s.listen(1)

    print('Server is listening...')
    print('------------------------------------------------------')

    # accept incoming connections from client
    c_socket, c_address = s.accept()
    print(f'Connection from {c_address}')
    print('------------------------------------------------------')

    # receive data from the client
    data = c_socket.recv(1024).decode()
    data_dict = json.loads(data)
    print(f'Received from client: {data_dict}')
    print('------------------------------------------------------')
   
    inputData(data_dict)
    
def inputData(data):
    with open('input-tldr-data.sql', 'w') as tldr_sql:
        input_query = f"INSERT INTO tldr (title, summary, link) VALUES ('{data['title']}', '{data['summary']}', '{data['website_url']}');"
        tldr_sql.write(input_query)
        tldr_sql.write('SELECT * FROM week_by_week;')
    print('The SQL file has been updated...')
    print('------------------------------------------------------')

def insertData(data):
    try:
        connection = p.connect(
            dbname=os.getenv('DATABASE_NAME'),
            user=os.getenv('DATABASE_USERNAME'),
            password=os.getenv('DATABASE_PASSWORD'),
            host=os.getenv('VM2_HOST'),
            port=os.getenv('VM2_PORT'),
            sslmode='require'
        )
        cursor = connection.cursor()

        # different queries for different databases
        if data['database'] == 'fetaldevelopment':
            print('fetal development') # add query later
        elif data['database'] == 'tldr':
            print('Placing json data into tldr database') # add query later
        else:
            print('Incorrect database input')
            return

        input_query = f"INSERT INTO tldr (title, summary, link) VALUES ('{data['title']}', '{data['summary']}', '{data['website_url']}')"
        cursor.execute(insert_query)
        connection.commit() # save changes
        print('Data inserted successfully')

    except (Exception, Error) as error:
        if connection:
            connection.rollback()
            print('Error inserting data into PostgreSQL table:', error)

    finally:
        # close the curson and connection
        if connection:
            cursor.close()
            connection.close()
            print('PostgreSQL connection is closed')

def outputData(data):
    # place the data.json file in the home directory
    with open('~/data.json', 'w') as json_file:
        json_file.write(data)
    print('JSON data has been written successfully')

if __name__ == '__main__':
    run()
