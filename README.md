## Data and scripts for Project 3 Group 7: Q.L. & M.Z.

We used the flights data from May 1st 2017 to perform database construction and queries. The final python scripts are in **PS3.py**.

We succeeded to get the average departure-delayed time of all airports for each state on that day, and the average departure-delayed time for each airport in Florida, using raw SQL.


### Average delay for each state on May 1st 2017

SELECT State, ROUND(AVG(Dep_Delay_New),2) FROM Flights JOIN Airports ON Origin = Code GROUP BY State;

### Average delay for each airport in Florida on May 1st 2017

SELECT Code,ROUND(AVG(Dep_Delay_New),2) FROM Airports JOIN Flights ON Code = Origin GROUP BY Code HAVING State = 'FL';
