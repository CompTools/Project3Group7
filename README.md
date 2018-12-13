## Data and scripts for Project 3 Group 7: Q.L. & M.Z.

We used the flights data from May 1st 2017 to perform database construction and queries. The final python scripts are in **PS3.py**.

We succeeded to get the average departure-delayed time of all airports for each state on that day, and the average departure-delayed time for each airport in Florida, using raw SQL.


### Average delay for each state on May 1st 2017

SELECT State, ROUND(AVG(Dep_Delay_New),2) FROM Flights JOIN Airports ON Origin = Code GROUP BY State;

### Average delay for each airport in Florida on May 1st 2017

SELECT Code,ROUND(AVG(Dep_Delay_New),2) FROM Airports JOIN Flights ON Code = Origin GROUP BY Code HAVING State = 'FL';


## Grading
You will receive points for:

Rubric item	|Points	|Your score
--------------|-------|----------|
Group plan submitted	|5 points| **5**	
Defined elements above: <br> * Database:<br> * Tables are normalized <br> * Tables have reasonable structure<br> * Tables have primary and foreign keys defined<br><br>* SQLAlchemy <br>* Add data to database<br>* Query database<br>* Select, where, join|20 points| **20**
Having at least one commit from each member of the team	|2 points|	**2**
Using meaningful commit messages|	2 points|	**2**
Using branches to work collaboratively|	4 points|	**4**
Using comments in code|	1 points	|**1**
Logical flow to code	|3 points	|**3**
Readability of code	|3 points|	**3**

Total points:

**40**/40

## Comments:
Good job. Would have been better to add the queries to your python script, but OK.
