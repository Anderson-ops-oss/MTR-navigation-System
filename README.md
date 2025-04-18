# MTR-navigation-System

This project implements two algorithms for navigating the Hong Kong MTR (Mass Transit Railway) system:Uniform Cost Search (UCS) and Breadth-First Search (BFS). The algorithms help find the optimal path and cost between two stations in the MTR system.

## Table of Contents ##
* Introduction
* Features
* Requirements
* Limitations
* Usage
* File Structure
* Algorithms
  * Uniform Cost Search (UCS)a
  * Breadth-First Search (BFS)

## Introduction ## 
This project provides a way to navigate the MTR system using two different search algorithms. Users can input the start and goal stations, choose the algorithm, and get the optimal path and cost or the number of stations in the path.

## Features ##  
* Uniform Cost Search (UCS): Finds the least-cost path between two stations.
* Breadth-First Search (BFS): Finds the shortest path (in terms of the number of stations) between two stations.
* User-friendly input prompts for start and goal stations and algorithm choice.
* Reads station information from a file.

## Requirements ## 
* Python 3
* heapq module (standard library)
* collections module (standard library)

## Limitations ##
* Fare Information: Current station costs are based on the MTR 2024 fare table as single journey fares
* Distance-based Pricing: The system currently doesn't account for the MTR's distance-based pricing where longer journeys have proportionally lower costs per station
* Interchange Stations: Special cases like Hong Kong/Central stations and Tsim Sha Tsui/East Tsim Sha Tsui stations are treated as separate stations in the current implementation

## Usage ##  
* Ensure you have Python 3 installed on your system.
* Prepare a file named station_information.txt with the MTR station data.
* Run the main() function to start the program.

## File Structure ## 
* mtr_navigation.py: Main script containing the UCS and BFS algorithms and user input handling.
* station_information.txt: Text file containing the MTR station information.
* HKMTR Fares.pdf: MTR Tickets and Fares

## Algorithms ##
* Uniform Cost Search (UCS)
UCS is used to find the least-cost path between two stations. It uses a priority queue to explore the stations with the lowest cumulative cost first.
* Breadth-First Search (BFS)
BFS is used to find the shortest path (in terms of the number of stations) between two stations. It uses a queue to explore all neighboring stations level by level.
