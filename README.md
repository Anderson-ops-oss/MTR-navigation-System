# MTR-navigation-System

This project implements two algorithms for navigating the Hong Kong MTR (Mass Transit Railway) system:Uniform Cost Search (UCS) and Breadth-First Search (BFS). The algorithms help find the optimal path and cost between two stations in the MTR system.

Table of Contents
* Introduction
* Features
* Requirements
* Usage
* File Structure
* Algorithms
  * Uniform Cost Search (UCS)
  * Breadth-First Search (BFS)

_Introduction_  
This project provides a way to navigate the MTR system using two different search algorithms. Users can input the start and goal stations, choose the algorithm, and get the optimal path and cost or the number of stations in the path.

_Features_  
* Uniform Cost Search (UCS): Finds the least-cost path between two stations.
* Breadth-First Search (BFS): Finds the shortest path (in terms of the number of stations) between two stations.
* User-friendly input prompts for start and goal stations and algorithm choice.
* Reads station information from a file.

_Requirements_  
* Python 3
* heapq module (standard library)
* collections module (standard library)

_Usage_  
* Ensure you have Python 3 installed on your system.
* Prepare a file named station_information.txt with the MTR station data.
* Run the main() function to start the program.

_File Structure_  
* mtr_navigation.py: Main script containing the UCS and BFS algorithms and user input handling.
* station_information.txt: Text file containing the MTR station information.

_Algorithms_  
* Uniform Cost Search (UCS)
UCS is used to find the least-cost path between two stations. It uses a priority queue to explore the stations with the lowest cumulative cost first.
* Breadth-First Search (BFS)
BFS is used to find the shortest path (in terms of the number of stations) between two stations. It uses a queue to explore all neighboring stations level by level.
