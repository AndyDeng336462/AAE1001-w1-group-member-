DENG Jiabao 
(Group Leader)

WANG Qiushi

CHEN Yulin

WONG Siu Him Derick

SO Chak Man

LI Wai Fung

MAN Chor Fung

HO Lok Hang



# Table of content

- Introduction

- Task 1

- Task 2

- Task 3

- Task A1

- Task A2

- Task A3

- Evaluations


# Project Report
Introduction:

In this project, we simulate a path planning procedure in aviation engineering, with the assistance from python codes and github.

We rewrite sample codes to compute obstacles and 2 cost-intensive areas in our map,

where it requires more time for aircrafts to travel in these cost-intensive areas. Also, we added a cost saving area which is a jetstream. Aircraft could speed up and reduce their cost consumption. 

![international-flight-planning-101](https://github.com/user-attachments/assets/b3725ff7-f0d3-4bcd-a8ce-2fbfda2bde82)


# Our codes for obstacles:
![Screenshot 2024-10-29 164847](https://github.com/user-attachments/assets/e5911789-561e-4ae2-9e65-910428dfc5ed)
# Our map layout:
![WhatsApp Image 2024-10-29 at 16 53 19](https://github.com/user-attachments/assets/3dbd2fdc-9627-4f01-b4a7-744b25dc0f24)




# Task 1:

By running our modified codes, we are able to come out with a direct flight path which requires the shortest time
to travel from the starting point to the ending point.

# Our flight path:
![WhatsApp Image 2024-10-29 at 14 55 21 (1)](https://github.com/user-attachments/assets/ba92769f-e837-49e4-874e-9e4119a81ed7)


Total flight time required for shortest path:
102.48813844421308 minutes

Scenario:
 1. 2000 passengers travel from start to destination this week
 2. 10 flights maximum for one week
 3. Time cost = low, Fuel cost = 0.8 $/kg



# Scenario 1:
Our codes to calculate the total cost of different aircrafts for scenario 1:
![Screenshot 2024-10-29 170004](https://github.com/user-attachments/assets/a19fab1a-75d3-4b24-8cbf-11f183b826b7)

Total cost of different types of aircrafts (in $) :

Total cost for A321 = 90521.22334096441

Total cost for A330 = 106950.93665607038

Total cost for A350 = 110496.31566820135


# Scenario 2:
Our codes to calculate the total cost of different aircrafts for scenario 2:
![Screenshot 2024-10-29 170216](https://github.com/user-attachments/assets/4e292580-e969-4043-9d26-830239be1c1f)



Total cost of different types of aircrafts (in $) :

Total cost for A321 = 61039.993754272866

Total cost for A330 = 61715.51465894991

Total cost for A350 = 56406.62908753968


# Scenario 3:
Our codes to calculate the total cost of different aircrafts for scenario 3:
![Screenshot 2024-10-29 170123](https://github.com/user-attachments/assets/07178dec-271f-4023-bd7d-b78d7b272487)


Total cost of different types of aircrafts (in $) :

Total cost for A321 = 105072.7975261934

Total cost for A330 = 105442.8797206026

Total cost for A350 = 106499.98884691585


# Operation Overview:
![2024-11-05 12-42-34 00_00_04-00_00_46 (3)](https://github.com/user-attachments/assets/025c7182-15f3-4f5f-82e9-4da17cb4ca49)




# Solutions for Task 1:

Since the total cost for A321 is lowest in scenario 1, however, as A320
cannot meet the task requirement (transport 3000 passengers with maximum 12 flights in one week)
, therefore A330 is the solution for scenario 1 as A330 has the second lowest cost.

Since the total cost for A350 is lowest in scenario 2, therefore A350 is the solution for scenario 2.

Since the total cost for A321 is lowest in scenario 3, therefore A321 is the solution for scenario 3.



# Task 2:

In task 2, we try to design a new cost reducing area (jet stream area) to reduce the cost of the flight
![image](https://github.com/user-attachments/assets/664e1718-594b-4fd0-9c3c-8fc513abe481)
(This blue area is our cost saving area)


We decided to laterally set a minus-cost-area with a width of 5 units at range where y = 45 to 50

It is because the time required for the flight path is the shortest with the assistance of this area at this location.

The time required for this flight path with the presence of jetstream is 101.4896103067892 minutes.



# Task 3:

# Situation:

We design a new aircraft to best fit Scenario 1 in task 1
, while only considering the cruise time of the flight

We also design the passenger capacity of the aircraft, 
for each 50 passenger (min 100 to max 450) to increase 
time cost by 2 $/min (Base CT = 12 $/min) ,given that each engine consumes fuel at 20kg/min

# Solution:

## SCENARIO 1: Capacity can increase by the unit of 1)

Step1: From the powerpoint we can simply get the equation and the first thing we need to do is to separate the domain.

Step2: We notice that when the number of passengers per flight goes greater than 300, the aircraft need to be equiped with 4 engines, so we first roughly divide this function into 2 parts: x≤300 and x≥300

Step3: To meet the basic requirement of scenario1, We need at least 250 capacity to carry all 3000 passengers, and in this design, we need 12 flghts.

Step4: Then we try to increase the capacity of our plane. We find that when x goes 272, it still requir 12 flights. Only when x goes to 273 will the fight number decrease to 11. So we get our first domain:250. And the tatal cost can be denoted by one function:
![image](https://github.com/user-attachments/assets/fb9f9785-975d-4ae0-bb97-1963e8de20b1)

$${\color{lightgreen}Some \space group \space memebers \space argue \space that \space the \space capacity \space of \space aircraft \space can \space not \space increase \space by \space the \space unit \space of \space 1 \space due \space to \space its \space design, \space so \space we \space separate \space out \space scenario \space 2(the \space capacity \space of \space aircraft \space increase \space by \space the \space unit \space of \space 50)}$$

Step5: By the same token, we find the rest domains and write the equation respectively.
![image](https://github.com/user-attachments/assets/de43a6ca-1856-4b16-87c8-7dfff6cb7aec)


Step6: We use GEOGEBRA to generate its graph. Meanwhile we think the minimum unit of x is 1, so the graph is:
![image](https://github.com/user-attachments/assets/1d763389-07cd-47e3-9d7b-86bb6524b5d4)

![image](https://github.com/user-attachments/assets/8347d03d-787d-4133-b008-f66b51cfc141)


Step7: Comparing these two values, we decide to make our aircraft with two engines and 273 capacity . It is the optimum design.We name this aircraft to be a350-200. 

## SCENARIO 2: Capacity increase by the unit of 50

Step1: In this scenatio, we only have 5 types of aircraft, with capacity of 250,300,350,400,450. And their functions are as followes.
![image](https://github.com/user-attachments/assets/3e66e322-fc71-44e3-95c6-26531193039d)

Step2: So we write a code to automatically calculate five respective costs, then compare them and print the minimum cost
![image](https://github.com/user-attachments/assets/6dd57e33-4271-4b31-8336-f4e9fc637805)

### Overview:
![2024-11-09 13-06-34 00_00_01-00_00_08](https://github.com/user-attachments/assets/5b4c8602-da39-4967-a0b0-cdf2f1771841)

# Verdict:

In scenario1 of task 3, the best capacity is 273
In scenario2 of task 3, the best capacity is 450



# Task A1

In task A1, we add two checkpoints on the basis of task 1, one checkpoint for each cost intensive area. We also let the aircraft reach these two points.

The code for adding these two checkpoints:

<img width="619" alt="截屏2024-11-09 下午9 27 56" src="https://github.com/user-attachments/assets/f678d8ea-817c-4a40-9458-fec2890f49c8">
<img width="468" alt="截屏2024-11-09 下午9 38 01" src="https://github.com/user-attachments/assets/a0b1b956-8deb-4f09-acc5-4a7bb80563d2">


The code for letting the aircraft reach the checkpoints:

<img width="659" alt="截屏2024-11-09 下午9 38 35" src="https://github.com/user-attachments/assets/e3a2b3e3-b5bf-434a-bbef-2f484783f427">

The final path:

<img width="606" alt="截屏2024-11-09 下午8 58 07" src="https://github.com/user-attachments/assets/455ba55d-5c0f-43d3-b323-593dfe434543">



# Task A3
In task A3, we chose Breadth-First Search algorithm:

<img width="666" alt="截屏2024-11-11 下午10 31 54" src="https://github.com/user-attachments/assets/452695e4-b2e1-4ec3-9144-002604e7ea90">

And Dijkstra's Algorithm:

<img width="696" alt="截屏2024-11-12 下午12 48 32" src="https://github.com/user-attachments/assets/f07b9c21-36ef-457d-8898-f55adeb61581">

# Similarity between the two algorithms:

Both algorithms traverse a graph by systematically visiting nodes in a specific order. 

Both algorithms also maintain a list of visited nodes to avoid revisiting the same node multiple times.

# Difference between the two algorithms:

Breadth-First Search Algorithm: 

Commonly used in network analysis, shortest path problems in unweighted graphs, and graph traversal.
In data structures, Breadth-First Search Algorithm uses a simple queue to manage nodes, processing them in the order they are discovered and uses a visited set to track explored nodes.

Dijkstra's Algorithm: 

Frequently applied in routing algorithms, network analysis, and pathfinding in maps or GPS systems.
In data structures, Dijkstra's Algorithm uses a priority queue to manage nodes, ensuring the node with the smallest known distance is processed first, maintains a distances dictionary to track the shortest known distance to each node and uses a visit set to track explored nodes.

# Individual Evaluation

Ho Lok Hang

In this project, I am mostly responsible for the github readme page creation as well as the 
code testing of Task 2. It has allowed me to showcase my ability to comprehensively understand the project's purpose , functionality, and usage. 
I also have a deeper understandings in the creation of a github homepage with readme file.

On the other hand, my involvement in code testing for Task 2 has been both challenging and fulfilling. Conducting repeated testing to validate the functionality of the code has shaped my problem-solving skills. Through the process, I have been ensuring that the code meets the project requirements. This allows me to understand the importance of accuracy in coding procedures.

Overall, my role in README creation and code testing has provided me with valuable insights into the importance of effective documentation, thorough testing practices, and collaborative project management. 
