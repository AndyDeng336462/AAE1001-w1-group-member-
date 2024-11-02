![image](https://github.com/user-attachments/assets/ab25a322-81d8-46cd-bbec-c5ec0f304d0a)![image](https://github.com/user-attachments/assets/9dee43b5-355f-4493-8a37-fb6ed7bec108)# AAE1001-w1-group-member-

DENG Jiabao 
(Group Leader)

WANG Qiushi

CHEN Yulin

WONG Siu Him Derick

SO Chak Man

LI Wai Fung

MAN Chor Fung

HO Lok Hang


# Project Report
Introduction:

In this project, we simulate a path planning procedure in aviation engineering, with the assistance from python codes and github.

We rewrite sample codes to compute obstacles and 2 cost-intensive areas in our map,

where it requires more time for aircrafts to travel in these cost-intensive areas.

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
Our program can generate this output automatically just after running the code
![image](https://github.com/user-attachments/assets/3704854a-d925-4d00-a1ff-aad9339a8610)


# Solutions for Task 1:

Since the total cost for A321 is lowest in scenario 1, therefore A321 is the solution for scenario 1.

Since the total cost for A350 is lowest in scenario 2, therefore A350 is the solution for scenario 2.

Since the total cost for A321 is lowest in scenario 3, therefore A321 is the solution for scenario 3.



# Task 2:

In task 2, we try to design a new cost reducing area (jet stream area) to reduce the cost of the flight
![WhatsApp Image 2024-10-29 at 14 55 21](https://github.com/user-attachments/assets/29e216d5-3ea0-4963-8d6e-34b7114ca25c)


We decided to laterally set a minus-cost-area with a width of 5 units at range where y = 45 to 50

It is because the time required for the flight path is the shortest with the assistance of this area at this location.

The time required for this flight path with the presence of jetstream is 101.4896103067892 minutes.



# Task 3:

Step1: Noticing that "tatal time cost" has 16 significant figures, we decide to set up a function to address this complicated problem.

Step2: We notice that when the number of passengers per flight goes greater than 300, the aircraft need to use 4 engines, so we first roughly divide this function into 2 parts:x≤300 and x≥300

Step3: To meet the basic requirement of scenario1, our new need at least 250 capacity to carry all 3000 passengers, and in this design, we need 12 flghts.

Step3: Then we try to increase the capacity of our plane, and we find that if we increase the capacity to 272, the number of flght we need is still 12, only when x goes to 273 will the fight number decrease to 11. So we get our first domain:250≤x≤272. And the tatal cost can be denoted by one function:
![image](https://github.com/user-attachments/assets/8647319a-367d-41ec-ad86-e470cba458dc)

Step4: By the same token, we find the rest domains and set up the functions respectively.
![image](https://github.com/user-attachments/assets/5dcb5cd5-c952-495d-bceb-98d55752e207)

Step5: We use GEOGEBRA to generate its graph. Meanwhile we think the minimum unit of x is 1, so the graph is:
![image](https://github.com/user-attachments/assets/c1d9de35-4a67-4359-9a26-e876915440ea)
![image](https://github.com/user-attachments/assets/4ef25be5-f24f-445a-8889-ca81454cc131)

Step6: Comparing these two values, we decide to make our aircraft have the capacity of 273

