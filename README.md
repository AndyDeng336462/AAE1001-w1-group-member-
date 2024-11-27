# Group member

DENG Jiabao 
(Group Leader)

WANG Qiushi

CHEN Yulin

WONG Siu Him Derick

MAN Chor Fung

HO Lok Hang



# Table of Contents

- [Introduction](#Introduction)

- [Task 1](#Task-1) 

- [Task 2](#Task-2) 

- [Task 3](#Task-3)

- [Task A1](#Task-A1)

- [Task A2](#Task-A2)

- [Task A3](#Task-A3)

- [Individual Evaluation](#Individual-Evaluation)


# Introduction:

In this project, we simulate a path planning procedure in aviation engineering, with the assistance from python codes and github.

We rewrite sample codes to compute obstacles and 2 cost-intensive areas in our map,

where it requires more time for aircrafts to travel in these cost-intensive areas. Also, we added a cost saving area which is a jetstream. Aircraft could speed up and reduce their cost consumption. 

![international-flight-planning-101](https://github.com/user-attachments/assets/b3725ff7-f0d3-4bcd-a8ce-2fbfda2bde82)


## Our codes for obstacles:
![Screenshot 2024-10-29 164847](https://github.com/user-attachments/assets/e5911789-561e-4ae2-9e65-910428dfc5ed)

## Our map layout:
![WhatsApp Image 2024-10-29 at 16 53 19](https://github.com/user-attachments/assets/3dbd2fdc-9627-4f01-b4a7-744b25dc0f24)




# Task 1:

By running our modified codes, we are able to come out with a direct flight path which requires the shortest time
to travel from the starting point to the ending point.

## Our flight path:
![WhatsApp Image 2024-10-29 at 14 55 21 (1)](https://github.com/user-attachments/assets/ba92769f-e837-49e4-874e-9e4119a81ed7)


Total flight time required for shortest path:
102.48813844421308 minutes

Scenario:
 1. 2000 passengers travel from start to destination this week
 2. 10 flights maximum for one week](Scenario-2
 3. Time cost = low, Fuel cost = 0.8 $/kg](Scenario-3



## Scenario 1:
Our codes to calculate the total cost of different aircrafts for scenario 1:
![Screenshot 2024-10-29 170004](https://github.com/user-attachments/assets/a19fab1a-75d3-4b24-8cbf-11f183b826b7)

Total cost of different types of aircrafts (in $) :

Total cost for A321 = 90521.22334096441

Total cost for A330 = 106950.93665607038

Total cost for A350 = 110496.31566820135


## Scenario 2:
Our codes to calculate the total cost of different aircrafts for scenario 2:
![Screenshot 2024-10-29 170216](https://github.com/user-attachments/assets/4e292580-e969-4043-9d26-830239be1c1f)



Total cost of different types of aircrafts (in $) :

Total cost for A321 = 61039.993754272866

Total cost for A330 = 61715.51465894991

Total cost for A350 = 56406.62908753968


## Scenario 3:
Our codes to calculate the total cost of different aircrafts for scenario 3:
![Screenshot 2024-10-29 170123](https://github.com/user-attachments/assets/07178dec-271f-4023-bd7d-b78d7b272487)


Total cost of different types of aircrafts (in $) :

Total cost for A321 = 105072.7975261934

Total cost for A330 = 105442.8797206026

Total cost for A350 = 106499.98884691585


# Operation Overview:
![2024-11-13 11-37-50 00_00_04-00_01_09](https://github.com/user-attachments/assets/764be472-519b-4544-a5ac-7e3695a985f7)





## Solutions for Task 1:

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

## Situation:

We design a new aircraft to best fit Scenario 1 in task 1
, while only considering the cruise time of the flight

We also design the passenger capacity of the aircraft, 
for each 50 passenger (min 100 to max 450) to increase 
time cost by 2 $/min (Base CT = 12 $/min) ,given that each engine consumes fuel at 20kg/min

## Solution:

## SCENARIO 1: Capacity can increase by the unit of 1

Step1: From the powerpoint we can simply get the equation and the first thing we need to do is to separate the domain.

Step2: We notice that when the number of passengers per flight goes greater than 300, the aircraft need to be equiped with 4 engines, so we first roughly divide this function into 2 parts: x≤300 and x≥300

Step3: To meet the basic requirement of scenario1, We need at least 250 capacity to carry all 3000 passengers, and in this design, we need 12 flghts.

Step4: Then we try to increase the capacity of our plane. We find that when x goes 272, it still requir 12 flights. Only when x goes to 273 will the fight number decrease to 11. So we get our first domain:250≤x≤272. And the tatal cost can be denoted by one function:
![image](https://github.com/user-attachments/assets/fb9f9785-975d-4ae0-bb97-1963e8de20b1)

$${\color{lightgreen}Some \space group \space memebers \space argue \space that \space the \space capacity \space of \space aircraft \space can \space not \space increase \space by \space the \space unit \space of \space 1 \space due \space to \space its \space design, \space so \space we \space separate \space out \space scenario \space 2(the \space capacity \space of \space aircraft \space increase \space by \space the \space unit \space of \space 50)}$$

Step5: By the same token, we find the rest domains and write the equation respectively.
![image](https://github.com/user-attachments/assets/de43a6ca-1856-4b16-87c8-7dfff6cb7aec)


Step6: We use GEOGEBRA to generate its graph. Meanwhile we think the minimum unit of x is 1, so the graph is:
![image](https://github.com/user-attachments/assets/1d763389-07cd-47e3-9d7b-86bb6524b5d4)

![image](https://github.com/user-attachments/assets/8347d03d-787d-4133-b008-f66b51cfc141)


Step7: Comparing these two values, we decide to make our aircraft with two engines and 273 capacity . It is the optimum design.

## SCENARIO 2: Capacity increase by the unit of 50

Step1: In this scenatio, we only have 5 types of aircraft, with capacity of 250,300,350,400,450. And their functions are as followes.
![image](https://github.com/user-attachments/assets/3e66e322-fc71-44e3-95c6-26531193039d)

Step2: So we write a code to automatically calculate five respective costs, then compare them and print the minimum cost
![image](https://github.com/user-attachments/assets/6dd57e33-4271-4b31-8336-f4e9fc637805)

### Overview:
![2024-11-09 13-06-34 00_00_01-00_00_08](https://github.com/user-attachments/assets/5b4c8602-da39-4967-a0b0-cdf2f1771841)

## Optimum design:
In scenario 1 of task 3, capacity:273, equipped with 2 engines.
In scenario 2 of task 3, capacity:450, equipped with 4 engines.
And her name is A350-Group 6



# Task A1

We analysed the ground rules of A* algorithm and completely understand how it works. So, other than generating 3 individual paths and combine them together, we define "check points" in the code, and change its movement rule to make the path go through two check points.

We add two checkpoints on the basis of task 1, one checkpoint for each cost intensive area.

The code for adding these two checkpoints:

<img width="619" alt="截屏2024-11-09 下午9 27 56" src="https://github.com/user-attachments/assets/f678d8ea-817c-4a40-9458-fec2890f49c8">
<img width="468" alt="截屏2024-11-09 下午9 38 01" src="https://github.com/user-attachments/assets/a0b1b956-8deb-4f09-acc5-4a7bb80563d2">

Newly added moving rule:

![image](https://github.com/user-attachments/assets/06d9106e-eaca-4748-816e-87e398efdc91)

Print the animation:

<img width="659" alt="截屏2024-11-09 下午9 38 35" src="https://github.com/user-attachments/assets/e3a2b3e3-b5bf-434a-bbef-2f484783f427">

The final path:

<img width="606" alt="截屏2024-11-09 下午8 58 07" src="https://github.com/user-attachments/assets/455ba55d-5c0f-43d3-b323-593dfe434543">


# Task A2

In task A2, the environment keep changing for each operations inside the boundary. There is a ramdomly generated cost intensive area with a fixed area of 40 units * 40 units. Obstacles with moderate density are randomly generated inside the boundary and they cannot surround the starting point and goal and cannot be covered by the cost intensive area. Starting point and finishing point should have a distance of minimun 40 units. 

#### Random path is plotted by the code. These are some of the generated result.
![ban diagonal ](https://github.com/user-attachments/assets/f2900cf9-3ac6-4d65-a086-d3a40956e61f)
![ban diagonal 2](https://github.com/user-attachments/assets/c3825a52-3d2d-40e9-98de-01597dda4647)


#### These codes below ensure both starting point and goal are generated randomly and in the boundaries.
![Start and goal point ](https://github.com/user-attachments/assets/a2606b66-a781-4251-9dc3-eb33cb2ec8b2)

#### These codes below allow obstacles to be generated randomly with moderate density of index below 1000. Obstacle generation is banned within 2 units near starting point and goal to prevent the path being blocked near both points.
![obstacles](https://github.com/user-attachments/assets/8494927c-a2da-4b76-99ba-043b4393687d)

#### Codes below generate a random cost intensive area with a fixed dimension of 20 units *20 units. 
![random cost intensive area](https://github.com/user-attachments/assets/eff31a69-448a-4e82-9dbd-fd403632414c)


#### These codes restrict diagonal movements.
![no diagonal code](https://github.com/user-attachments/assets/1c64d3c8-4284-48ad-8123-e6f851c9aaeb)


# Task A3
In task A3, we use AI to generate two codes, with exactly same boundary and obstacles, but driven by Breadth-First Search(BFS) algorithm and Dijkstra's Algorithm respectively

Breadth-First Search(BFS):
![image](https://github.com/user-attachments/assets/864b8c7f-b7b7-4c52-ad50-b581cba17910)

Dijkstra:
![image](https://github.com/user-attachments/assets/809a5717-e171-4c25-8242-b24149eec3d0)

## Working principle:
### Breadth-First Search (BFS)
1.Determine the starting node.
2.Examine all unvisited neighbors of this node.
3.Mark each neighbor as visited and enqueue them.
4.Repeat the process until the goal node is found or all nodes have been explored.

### Dijkstra's Algorithm
1.Determine the starting node.
2.For each unvisited neighbor of this node, calculate the distance from the start node through the current node. If this new distance is smaller than the previously known distance, update the tentative distance.
3.Once all neighbors of the current node are processed, move to the next node with the smallest tentative distance.
4.Repeat the process until the shortest path to all nodes is determined.

## Comparison
### Breadth-First Search (BFS)
#### Pros:
Completeness: BFS is complete, meaning it will find a solution if one exists.
Optimality: In unweighted graphs, BFS finds the shortest path in terms of the number of edges.
#### Cons:
Memory Usage: BFS can require a lot of memory because it stores all nodes at the current depth level.
Inefficiency in Weighted Graphs: BFS does not account for edge weights, making it unsuitable for finding the shortest path in weighted graphs.

### Dijkstra's Algorithm
#### Pros:
Optimality: Dijkstra's algorithm is guaranteed to find the shortest path in graphs with non-negative weights.
Versatility: It can be used to find the shortest path from a single source to all other nodes.
#### Cons:
Inefficiency with Large Graphs: Dijkstra's algorithm can be slower than A* in large graphs because it does not use heuristics to guide the search.
Memory Usage: Like A*, it can consume a lot of memory, especially in dense graphs.

## Application Scenarios
![image](https://github.com/user-attachments/assets/067ad168-774d-4ee1-bba5-1232a5d1ef88)


# Individual Evaluation

## Ho Lok Hang

In this project, I am mostly responsible for the github readme page creation as well as the 
code testing of Task 2. It has allowed me to showcase my ability to comprehensively understand the project's purpose , functionality, and usage. 
I also have a deeper understandings in the creation of a github homepage with readme file.

On the other hand, my involvement in code testing for Task 2 has been both challenging and fulfilling. Conducting repeated testing to validate the functionality of the code has shaped my problem-solving skills. Through the process, I have been ensuring that the code meets the project requirements. This allows me to understand the importance of accuracy in coding procedures.

Overall, my role in README creation and code testing has provided me with valuable insights into the importance of effective documentation, thorough testing practices, and collaborative project management. 

## Man Chor Fung

In this project, I am responsible for Task 1, additional task A2 and the readme page. During the whole project, I realized the importance of teamwork. By allocating the task properly to groupmates with different talents, it will increase the efficiency of the working process. For example, one of my groupmates has experience in coding so he focused on coding. Those who are not familiar with coding will do the report part. Proper division of labor has speeded up our progress.

At first, when I was trying to do task 1, I found it difficult to edit the sample codes since I don't have any coding experience before. After reading the code and notes, I briefly understand the pattern and the mechanism of the code. When I was editing the code, I encountered a problem. By changing the coordinates of the existing obstacles codes, I successfully placed the obstacle bar to the correct position of (30,50) and (40, 10). However, the slope of the bar is too steep so the obstacles points are too sparse, and the path might pass through the obstacle bar. After asking other people, I realized that I could use an equation in term of x to generate the same obstacle bar with denser obstacle points. From this task, I acquired basic coding skills, and most importantly, critical thinking. I found that by thinking in diverse ways, I can get the same result in a simpler and faster way. I believe this skill would be beneficial in my future study and career development.

Besides, in task A2, I have learnt to use AI to assist my work. In the era of AI, it is important to know how to implement AI into our work. This project provided an opportunity to let me use AI to assist with my work. AI helped me to proofread and explain how does the code works. Additionally, AI provides some sample code for reference. With those samples, I could gradually finish Task A2 such as coding a random cost intensive area and obstacles even without any coding experience. By the task I realized the power of AI and how it would improve our efficiency.

To conclude, this project offered me an insight into how AI assists our work and a taste of coding. I believe this experience would be invaluable for my studies in the future.

## CHEN Yulin

In this group project, I cooperated with my teammates to finish the task 3 and wrote the report of task A1 in the readme page. I've learned a lot coding knowledge from my teammates and realized the importance of cooperation.

When I tried to finish task 3, at the beginning, I overlooked some details. After my teammate's modification, we finally finish this task. When I wrote the report of task A1 in the readme page, I should first learn to understand my teammates' code and then wrote the report, giving me the opportunity to learn the meaning of every steps in code.

In conclusion, this group project give me a valuable opportunity to cooperate with others and learn some coding knowledge. I think this experience will promote my further study.

## Wang Qiushi

In terms of tools, this was my first time using GitHub as well as Visual studio code. I think Github is a great tool for collaboration in terms of writing code, and it greatly improved the efficiency of our collaboration. Also, I learned how to use AI in Visual Studio Code to help us complete and understand the code, which accelerated my understanding of the code base. For example, when I am working with complex code, I can ask the AI about the methods used and what they represent.

In terms of working with aviation, I learned about the calculation of aviation fuel and the importance of cost through the task three. 

Lastly, in terms of code, I tried to solve additional task 2 but I ran into some problems. I could not get the fuel consumption zones to appear accurately and randomly. So, I still need more practice to familiarize myself with the code and using the AI.

## Wong Siu HIm Derick

In this project, I mainly responsible for assisting my groupmates to finish task 2 and 3. I've learned the importance of communication when working with others. Besides, as this is my first time using Github and coding, I've learned a lot of coding skills from my groupmates.

Apart from that, I also understand many terms and calculations about aviaion such as how jet stream areas can reduce the cost of flight or how importance it is for us to calculate the amount of fuel for the flight carefully before the plane took off. 

Moreover, during number of testings, I,ve learned that AI is a very useful tool for us to carry out multiple simulations, doing some prediction and give us some information that we can apply it to our learning. 

In the end, I think this group project provided me an unforgettable experience to access to different knowledges about aviation and eventually increased my interest in coding and AI. 


## DENG Jiabao

We are given some difficult tasks from the ground that we all are not familiar with. We spent time learning using GitHub to cooperate effectively and sharing our own comprehension on coding, which was a rosy experience for all of us.

In the process of coding, I first tried to figure out the meaning of each code, after wasting 4 hours in vain, I decided to use AI for assistance. Then I got to know the power of AI tools. I learned a whole lot of tactics to make AI understand my exact meaning. And I accumulate a large deal of tips and tricks for choosing appropriate AI tools to reach different goals respectively.

In the larger sense, I realized the convenience of AI and its potential as an assistant for improving my academic learning efficiency. Even though this lecture will literally end in the near future, I will still keep my steps in digging out the potential usage of AI and make it a strong partner for me.
