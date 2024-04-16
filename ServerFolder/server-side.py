'''
@author: Ashlyn Campbell
VM1
'''
from dotenv import load_dotenv
import socket
from Model import *
import json
import os

print(os.getcwd())
load_dotenv()
def run(type=None):
    # client socket
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (('10.0.0.5', 8888))

    # connect to the server
    c.connect(server_address)

    # request tldr summaries
    if type == 'tldr':
        begin()
        with open('/home/azureuser/ClientFolder/tldr.json', 'r') as json_file:
            data = json.load(json_file)
    # send fetal development data to database
    elif type == 'fetaldevelopment':
        with open('/home/azureuser/ClientFolder/fetaldevelopment.json', 'r') as json_file:
            data = json.load(json_file)
    else:
        print('Invalid Request Type')
        return
    # print('The data looks like: ', data)
    # send data to client and close the connection
    json_data = json.dumps(data['week-by-week']['1-2-3-weeks'])
    bytes_data = json_data.encode('utf-8')
    c.sendall(bytes_data)
    c.close()

    print('Data has been sent to the server...')
    print('------------------------------------------------------')
if __name__ == '__main__':
    run(type='tldr')