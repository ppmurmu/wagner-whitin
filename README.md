# wagner-whitin
Solving factory problem with Wagner-Whitin procedure using dynammic programming

Consider the problem from Section 2.3.3 of the Factory Physics book (data given below).
Develop a python code to solve this problem using the Wagner-Whitin procedure. Disregard
the number of working days in each week for this problem, and use the set up and inventory
carrying costs from the book (assume constant set up and inventory carrying costs).
The python code should have the following functionalities: take in demand up to 12 periods
(i.e., the user should be able to input 6 months, 3 months, 10 months, or 6 weeks, 3 weeks, 10
weeks), take in constant set up and carrying costs, and output both production quantity and
schedule (e.g., produce 100 units at 𝑡 = 1, 120 at 𝑡 = 2, 0 in 𝑡 = 3, and so on). Therefore,
your python code should be able to detect the number of periods (max 12) of demand entered
and modify its calculations accordingly. Your python code should replicate the results from
the book.
Week Demand in Units
1     20
2     50
3     10
4     50
5     50
6     10
7     20
8     40
9     20
10    30
