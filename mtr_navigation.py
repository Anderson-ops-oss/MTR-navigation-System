from heapq import heappush, heappop
from collections import deque

def ucs_mtr_navigation(mtrSystemMap, startState, goalState):
    # Initialize the priority queue with the start state
    stationList = []
    heappush(stationList, (0, startState, startState))
    exploredStation = set()
    
    while stationList:
        # Pop the station with the lowest cost
        cost, station, path = heappop(stationList)
        
        # Check if the goal state is reached
        if station == goalState:
            return path, cost
        
        # If the station has not been explored, add it to the explored set
        if station not in exploredStation:
            exploredStation.add(station)
            
            # Push all neighboring stations to the priority queue
            for child in mtrSystemMap[station]:
                heappush(stationList, (cost + child[0], child[1], path + " -> " + child[1]))

def extract_station(node):
    # Extract the station name from the path string
    return node.split(" -> ")[-1]

def bfs_mtr_navigation(mtrSystemMap, startState, goalState):
    # Initialize the queue with the start state
    queue = deque([(startState, [startState])])
    exploredStation = set()
    
    while queue:
        # Pop the first station in the queue
        station, path = queue.popleft()
        
        # Check if the goal state is reached
        if station == goalState:
            return " -> ".join(path), len(path) - 1
        
        # If the station has not been explored, add it to the explored set
        if station not in exploredStation:
            exploredStation.add(station)
            
            # Append all neighboring stations to the queue
            for _, neighbor in mtrSystemMap[station]:
                if neighbor not in exploredStation:
                    queue.append((neighbor, path + [neighbor]))
    
    return None, 0  

def get_user_input(mtr_station_information):
    # Get user input for start and goal stations and the algorithm choice
    startState = input("Enter the start station: ")
    goalState = input("Enter the goal station: ")
    algorithm = input("Choose the algorithm (UCS/BFS): ").strip().upper()
    
    # Execute the chosen algorithm and print the results
    if algorithm == "UCS":
        path, cost = ucs_mtr_navigation(mtr_station_information, startState, goalState)
        print("Solution path: ", path)
        print("Solution cost: ", cost)
    elif algorithm == "BFS":
        path, num_stations = bfs_mtr_navigation(mtr_station_information, startState, goalState)
        print("Solution path: ", path)
        print("Number of stations: ", num_stations)
    else:
        print("Invalid algorithm choice. Please choose either UCS or BFS.")
        
def read_station_information(file_path):
    # Read station information from a file and return a dictionary
    mtr_station_information = {}
    with open(file_path, 'r') as file:
        for line in file:
            station, connections = line.strip().split(': ')
            connections = connections.split('; ')
            mtr_station_information[station] = [(int(cost), neighbor) for cost, neighbor in (conn.split(',') for conn in connections)]
    return mtr_station_information

def main():
    # Define the file path and read the station information
    file_path = 'station_information.txt'
    mtr_station_information = read_station_information(file_path)
    
    # Get user input and execute the chosen algorithm
    get_user_input(mtr_station_information)
    
main()
