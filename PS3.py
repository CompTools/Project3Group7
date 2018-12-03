#!/usr/bin/python
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy import DateTime, Boolean
import csv
import pandas as pd
import datetime

# Create a sqlite database 
engine = create_engine('sqlite:///project3group7.sqlite')

metadata = MetaData(engine)


# Create the Airports Table
try:
    Airports = Table('Airports', metadata, autoload=True)
except:
    Airports = Table ('Airports', metadata,
                Column('ID', Integer, autoincrement=True),
                Column('Code', String, primary_key=True),
                Column('City', String),
                Column('State', String)
               )


# Create the Flights table
try:
    Flights = Table('Flights', metadata, autoload=True)
except:
    Flights = Table ('Flights', metadata,
                 Column('ID', Integer, autoincrement=True),
		 Column('Time', String, primary_key=True),
                 Column('Fl_date', DateTime),
                 Column('Airline_ID', String),				 
                 Column('Origin', String, ForeignKey("Airports.Code")),
                 Column('Destination', String),
                 Column('Dep_Time', String),
                 Column('Dep_Delay_New', Integer),
		 Column('Dep_Del15', Integer),
                 Column('Arr_Time', String),
                 Column('Arr_Delay_New', Integer),
		 Column('Arr_Del15', Integer),
                 Column('Cancelled', Boolean),
                 Column('Cancellation_Code', String),
                 Column('Diverted', Boolean),
                 Column('Air_Time', Integer),
                 Column('Flights', Integer),
                 Column('Distance', Integer),
                 Column('Carrier_Delay', Integer),
                 Column('Weather_Delay', Integer),
                 Column('NAS_Delay', Integer),
                 Column('Security_Delay', Integer),
                 Column('Late_Aircraft_Delay', Integer)
                )
                                  
metadata.create_all(engine)


# Read the csv file
flights = open("flights.20170501.csv")
reader = csv.DictReader(flights)

Airport_dict = {}


# Create a dictionary of unique airport codes
for Line in reader:
    if Line['ORIGIN'] not in Airport_dict:
        Airport_dict[Line['ORIGIN']]=[Line['ORIGIN_CITY_NAME'], Line['ORIGIN_STATE_ABR']]

    if Line['DEST'] not in Airport_dict:
        Airport_dict[Line['DEST']]=[Line['DEST_CITY_NAME'], Line['DEST_STATE_ABR']]
		
conn = engine.connect()


# Add the Airport_dict codes to the Airports table
def insert_airport(code,city,state):
    ins = Airports.insert().values(Code=code,
                                  City=city,
                                  State=state)
    
    result = conn.execute(ins)

for key, value in Airport_dict.items(): 
    insert_airport(key, value[0], value[1])


# Close the file	
flights.close()

flights = open("flights.20170501.csv")

reader = csv.DictReader(flights)

Flight_dict = {}

def to_date(dates, lookup=False, **args):
	if lookup:
		return dates.map({v: pd.to_datetime(v, **args) for v in dates.unique()})
	return pd.to_datetime(dates, **args)

# Create a dictionary of Time using the departure time and arrival time
# Add data to the database
for Line in reader:
	Time = (Line['DEP_TIME'] + Line['ARR_TIME'])
	if (Line['DEP_TIME'] + Line['ARR_TIME']) not in Flight_dict:
		Flight_dict[Time]=[to_date(Line['FL_DATE']), Line['AIRLINE_ID'], Line['ORIGIN'], Line['DEST'],
		Line['DEP_TIME'], Line['DEP_DELAY_NEW'], Line['DEP_DEL15'], 
		Line['ARR_TIME'], Line['ARR_DELAY_NEW'], Line['ARR_DEL15'],
		int(float((Line['CANCELLED']))), Line['CANCELLATION_CODE'], int(float((Line['DIVERTED']))), Line['AIR_TIME'], Line['FLIGHTS'],
		Line['DISTANCE'], Line['CARRIER_DELAY'], Line['WEATHER_DELAY'], Line['NAS_DELAY'], Line['SECURITY_DELAY'], Line['LATE_AIRCRAFT_DELAY']]
	
conn = engine.connect()


def insert_flight(time, fl_date, airline_id, origin, destination, dep_time, dep_delay_new,
                   dep_del15, arr_time, arr_delay_new, arr_del15, cancelled, cancellation_code,
		   diverted, air_time, flights, distance, carrier_delay, weather_delay,
			    nas_delay, security_delay, late_aircraft_delay):
					
    ins = Flights.insert().values(Time = time,
				    Fl_date = fl_date,
				    Airline_ID = airline_id,
				    Origin = origin,
				    Destination = destination,
				    Dep_Time = dep_time,
				    Dep_Delay_New = dep_delay_new,
				    Dep_Del15 = dep_del15,
				    Arr_Time = arr_time,
				    Arr_Delay_New = arr_delay_new,
				    Arr_Del15 = arr_del15,
				    Cancelled = cancelled,
				    Cancellation_Code = cancellation_code,
				    Diverted = diverted,
				    Air_Time = air_time,
				    Flights = flights,
				    Distance = distance,
				    Carrier_Delay = carrier_delay,
				    Weather_Delay = weather_delay,
				    NAS_Delay = nas_delay,
				    Security_Delay = security_delay,
				    Late_Aircraft_Delay = late_aircraft_delay)
    
    result = conn.execute(ins)

for key, value in Flight_dict.items(): 
    insert_flight(key, value[0], value[1], value[2], value[3], value[4], value[5], value[6],
					value[7], value[8], value[9], value[10], value[11], value[12], value[13],
					value[14], value[15], value[16], value[17], value[18], value[19], value[20])
