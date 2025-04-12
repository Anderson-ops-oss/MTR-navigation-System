# MTR Navigation System
from heapq import heappush, heappop
from collections import deque

def ucs_mtr_navigation(mtrSystemMap, startState, goalState):
    # Initialize the priority queue with the start state
    stationList = []
    heappush(stationList, (0, startState, [startState]))
    exploredStation = set()
    
    while stationList:
        # Pop the station with the lowest cost
        cost, station, path = heappop(stationList)
        
        # Check if the goal state is reached
        if station == goalState:
            return " -> ".join(path), cost
        
        # If the station has not been explored, add it to the explored set
        if station not in exploredStation:
            exploredStation.add(station)
            
            # Push all neighboring stations to the priority queue
            for child_cost, child_station in mtrSystemMap[station]:
                new_cost = cost + child_cost
                new_path = path + [child_station]
                heappush(stationList, (new_cost, child_station, new_path))
    
    return None, 0 

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
            for cost, neighbor in mtrSystemMap[station]:
                if neighbor not in exploredStation:
                    queue.append((neighbor, path + [neighbor]))
    
    return None, 0  

def get_user_input(mtr_station_information):
    # Get user input for start and goal stations
    print("Available stations:", ", ".join(mtr_station_information.keys()))
    startState = input("Enter the start station: ").strip()
    goalState = input("Enter the goal station: ").strip()
    
    # Validate the input stations
    if startState not in mtr_station_information or goalState not in mtr_station_information:
        print("Invalid station name. Please check the station names and try again.")
        return
    
    # Get user input for the algorithm choice
    algorithm = input("Choose the algorithm (UCS for lowest price / BFS for fewest stations): ").strip().upper()
    
    # Execute the chosen algorithm and print the results
    if algorithm == "UCS":
        path, cost = ucs_mtr_navigation(mtr_station_information, startState, goalState)
        if path:
            print("\n--- Lowest Price Path (UCS) ---")
            print("Path:", path)
            print("Total cost:", round(cost, 2))
        else:
            print("No path found from", startState, "to", goalState)
    elif algorithm == "BFS":
        path, num_stations = bfs_mtr_navigation(mtr_station_information, startState, goalState)
        if path:
            print("\n--- Fewest Stations Path (BFS) ---")
            print("Path:", path)
            print("Number of stations:", num_stations)
        else:
            print("No path found from", startState, "to", goalState)
    else:
        print("Invalid algorithm choice. Please choose either UCS or BFS.")

def read_station_information(file_path):
    # Read station information from a file and return a dictionary
    mtr_station_information = {}
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line into station name and connections
            station, connections_str = line.strip().split(': ')
            
            # Process each connection string
            connections = []
            for conn_str in connections_str.split('; '):
                cost, neighbor = conn_str.split(',')
                connections.append((float(cost), neighbor))
            
            # Add to the dictionary
            mtr_station_information[station] = connections
            
    return mtr_station_information

def main():
    # Define the file path and read the station information
    file_path = 'station_information.txt'
    mtr_station_information = read_station_information(file_path)
    
    # Get user input and execute the chosen algorithm
    get_user_input(mtr_station_information) 
if __name__ == "__main__":
    main()
