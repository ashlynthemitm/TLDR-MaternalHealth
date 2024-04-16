# TLDR Maternal Health
![image](https://github.com/ashlynthemitm/TLDR-MaternalHealth/assets/106557299/9fa0855a-1479-4c78-afe6-175e72700b54)

# Table of Contents
1. [Project Overview](#project-overview)
2. [Design](#design)
    - [Azure Virtual Machines](#azure-virtual-machines)
    - [PostgreSQL Database](#postgresql-database)
    - [Docker](#docker)
    - [Python Transformers](#python-transformers)
3. [Implementation Instructions](#implementation-instructions)
    - [Azure Virtual Machines Setup](#azure-virtual-machines-setup)
    - [PostgreSQL Database Setup](#postgresql-database-setup)
    - [Docker Setup](#docker-setup)
4. [Usage](#usage)
    - [Using Azure Virtual Machines](#using-azure-virtual-machines)
    - [Accessing the PostgreSQL Database](#accessing-the-postgresql-database)
    - [Running Docker](#running-docker)
5. [Project Structure](#project-structure)
6. [Key Measurement Results](#key-measurement-results)
7. [Demo](#demo)
8. [License](#license)

# Project Overview

TLDR Maternal Health is a project that utilizes cloud computing, and natural language processing and hopes to integrate an interactive user interface to provide crucial information to pregnant women. 

# Design
This section shows a visual design of the primary components of TLDR Maternal Health, which are Azure Virtual Machines, a PostgreSQL Database, and Python Transformers.

## Azure Virtual Machines

![CCmaps](https://github.com/ashlynthemitm/TLDR-MaternalHealth/assets/106557299/10d1fe9c-ca8b-481e-b5af-ebe1d9abcbf8)

## PostgreSQL Database

![CCmaps (1)](https://github.com/ashlynthemitm/TLDR-MaternalHealth/assets/106557299/18eca218-2d19-4ac7-ab53-97ad70fbb167)

## Docker

![CCmaps (2)](https://github.com/ashlynthemitm/TLDR-MaternalHealth/assets/106557299/79ce2f9d-6dad-4748-b0d9-d3fbcd828172)

## Python Transformers

Originally the proposal suggested using SpaCy for text summarization, but this NLP library didn't have the best precision. The final chosen text summarization technique is a Bart Transformer model that processes slightly slower but generates incredible summaries that take key insights.

![CCmaps (3)](https://github.com/ashlynthemitm/TLDR-MaternalHealth/assets/106557299/90a5e7dc-4c61-41b9-b695-c75e80ee0757)

# Implementation Instructions

This section provides step-by-step instructions for setting up the project environment.

## Azure Virtual Machines Setup

Instructions: https://learn.microsoft.com/en-us/azure/network-watcher/monitor-vm-communication

Here are the steps summarized for your implementation instructions section:

1. Create Virtual Machine 1 or Server VM 
- Size
    - Size: Standard B2s
    - vCPUs: 2
    - RAM: 4 GiB
2. Create Virtual Machine 2 or Client VM
- Size
    - Size: Standard B1ms
    - vCPUs: 1
    - RAM: 2 GiB
3. Set up Azure Network Watcher:
   - Understand the role of Azure Network Watcher in monitoring and troubleshooting network communication.

4. Setting up Network Watcher:
   - Navigate to the Azure portal and locate the Network Watcher service.
   - Enable Network Watcher for your Azure subscription and select the appropriate region.
   - Verify that Network Watcher is enabled for the virtual network where your virtual machines reside.

5. Monitoring VM-to-VM Communication:
   - Access the Network Watcher dashboard and select the "VM to VM" option.
   - Choose the source and destination virtual machines to monitor communication between them.
   - Analyze the network traffic flow and troubleshoot any connectivity issues detected.

6. Utilizing Network Watcher Tools:
   - Explore the various tools available within Network Watcher, such as Connection Monitor and Packet Capture.
   - Use Connection Monitor to track network connectivity between virtual machines and diagnose connectivity problems.
   - Employ Packet Capture to capture and analyze network traffic for troubleshooting purposes.

7. Implementing NSG Flow Logs:
   - Enable NSG flow logs for the network security groups (NSGs) associated with your virtual machines.
   - Configure the storage account where NSG flow logs will be stored for analysis.

8. Configuring NSG and Firewall Rules:
   - Define and implement network security group (NSG) rules to control inbound and outbound traffic for your virtual machines.
   - Configure firewall rules to further restrict network traffic and enhance security within your Azure environment.
     
![CCmaps (4)](https://github.com/ashlynthemitm/TLDR-MaternalHealth/assets/106557299/2d886327-eac9-4617-8d08-dcd59b851135)

## PostgreSQL Database Setup

This subsection explains how to set up the PostgreSQL Database.

## Docker Setup

This subsection outlines the setup process for Docker in the project.

# Usage

This section explains how to use the project after it has been set up.

## Using Azure Virtual Machines

This subsection provides instructions on how to utilize Azure Virtual Machines.

## Accessing the PostgreSQL Database

This subsection explains how to access and interact with the PostgreSQL Database.

## Running Docker

This subsection describes how to run the project using Docker.

# Project Structure

This section provides an overview of the project directory structure.

# Key Measurement Results

This section outlines how to contribute to the project and guidelines for contributors.

# Demo


# License

© Ashlyn Campbell
