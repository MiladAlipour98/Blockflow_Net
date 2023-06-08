# Project Name: Alephium Blockchain Analysis

## Project Description
This project focuses on analyzing the Alephium cryptocurrency, which operates on the BlockFlow blockchain. In this blockchain network, users initiate transactions that need to be confirmed by miners for successful completion. This README file provides an overview of the project and its objectives.

## Objective
The main objectives of this project are:
1. Determine the maximum distance between two miners in the blockchain network.
2. Find the path between two arbitrary miners (a and b) based on a prioritized selection of the next miner using a depth-first search algorithm.

## Dataset
The project utilizes a file called `blockflow.txt`, which represents the edges between miners in a specific time snapshot of the blockchain network. This dataset provides the necessary information to analyze the network structure and perform the required computations.

## Assumptions
1. Each transaction in the network requires confirmation from miners, with a required confirmation rate of one-tenth of a percent.
2. Confirmations must occur consecutively, meaning that the first miner starts the confirmation process, and the result is passed on to subsequent miners until the process is complete.
3. The cryptocurrency in this time snapshot has the capability to confirm multiple transactions simultaneously.

## Tasks
The project involves the following tasks:

### Task A: Determining the Maximum Distance
The first task is to calculate the maximum distance between two miners in the blockchain network. This will provide insights into the overall network topology and the potential reach of transactions.

### Task B: Finding the Path between Miners
To determine the path between two arbitrary miners (a and b), a depth-first search algorithm is employed. At each step of the path, the selection of the next miner is based on the miner with the most common neighbors with the previous miner. This prioritized approach ensures efficient transaction confirmation within the network.

## Getting Started
To run the project and perform the required analysis, follow these steps:

1. Ensure you have the necessary dependencies installed (Python, relevant libraries, etc.).
2. Download the `blockflow.txt` file and place it in the designated directory.
3. Execute the provided Python scripts for each task to obtain the desired results.

## Results
Upon running the project, the following information will be generated:

1. Task A: The maximum distance between two miners in the blockchain network.
2. Task B: The path between two arbitrary miners (a and b) based on the prioritized selection of the next miner using a depth-first search algorithm.

## Conclusion
This project provides insights into the Alephium cryptocurrency operating on the BlockFlow blockchain. By analyzing the network structure and determining the maximum distance and transaction paths between miners, we gain a deeper understanding of the system's efficiency and connectivity.

# Blockflow_Net
Cryptocurrency Network Analysis on BlockFlow Blockchain
Analyzing Alephium cryptocurrency network dynamics using graph theory and complex network analysis for insights into transaction confirmation, network metrics, structure, and visualization.

Network Visualization in python:

![G](https://github.com/MiladAlipour98/Blockflow_Net/assets/105122009/b4a35cc7-f26d-4558-93a0-99a8f9f50809)

Network various layouts in Ucinet:

![w graph](https://github.com/MiladAlipour98/Blockflow_Net/assets/105122009/0fbf6aee-11aa-4e93-b6a7-2e151e8ebd5f)

Circle:

![circlee](https://github.com/MiladAlipour98/Blockflow_Net/assets/105122009/cfe8ec47-ac0b-472f-b842-13d8f2b53ebc)

Disimilarity:

![disimilarity](https://github.com/MiladAlipour98/Blockflow_Net/assets/105122009/e31a22e7-6162-45c2-b5f9-490e1eedd852)

Ego layouts:

![ego file](https://github.com/MiladAlipour98/Blockflow_Net/assets/105122009/67eaf349-6b4f-4e7e-8e43-7912b343dbc1)
![ego](https://github.com/MiladAlipour98/Blockflow_Net/assets/105122009/fdca29ba-9c68-446d-b59b-431b6952356e)
![egosimple](https://github.com/MiladAlipour98/Blockflow_Net/assets/105122009/dcb519e1-b28d-49de-8b63-aac042e32a5e)

Emily:

![emily](https://github.com/MiladAlipour98/Blockflow_Net/assets/105122009/1c2776c4-a610-4865-a987-e3b5f35f418e)

Non-metric:

![non metric](https://github.com/MiladAlipour98/Blockflow_Net/assets/105122009/6d990e1f-e915-4d86-b163-0c361f2b6bfd)

Random:

![random](https://github.com/MiladAlipour98/Blockflow_Net/assets/105122009/ca3e1400-72f3-4679-864b-d5ac7ff30b5b)

Simillarity:

![simillarity](https://github.com/MiladAlipour98/Blockflow_Net/assets/105122009/c7f236d7-64ed-4bde-ad3a-de209b72015c)
