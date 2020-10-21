use GodBlessDS
INSERT INTO flight_merged(csv_f_id,flight_code,depart_date,depart_time,dest_) 
SELECT DISTINCT id,FlightNumber,FlightDate,FlightTime,Destination
FROM csv_flight




UPDATE flight_merged 
SET xlsx_f_id = xlf.id, from_abr = xlf.FromAbr, from_ = xlf.From_, dest_abr = xlf.DestinationAbr/*, from_abr = xlf.FromAbr, from_ = xlf.From_ ,dest_abr = xlf.DestinatiomAbr*/
FROM flight_merged fm JOIN xlsx_flight xlf
	ON xlf.Destination=fm.dest_ AND xlf.FlightNumber=fm.flight_code 
	AND xlf.FlightDate=fm.depart_date AND xlf.FlightTime=fm.depart_time
	/*WHERE fm.xlsx_f_id IS NULL*/
/*checked!*/
SELECT * FROM flight_merged

INSERT INTO flight_merged(xlsx_f_id,flight_code,depart_date,depart_time,dest_,from_,dest_abr,from_abr)
SELECT DISTINCT id,FlightNumber,FlightDate,FlightTime,Destination,From_,DestinationAbr,FromAbr
FROM xlsx_flight
WHERE xlsx_flight.id not in (SELECT xlsx_f_id FROM flight_merged)


UPDATE flight_merged
SET json_f_id = xlf.id, from_abr = xlf.departure, dest_abr = xlf.arrival
FROM flight_merged fm JOIN json_flight xlf
	ON xlf.flight_code=fm.flight_code
	AND xlf.fl_date=fm.depart_date;


INSERT INTO flight_merged(xlsx_f_id,flight_code,depart_date,dest_abr,from_abr)
SELECT DISTINCT id,flight_code,fl_date,arrival,departure
FROM json_flight
WHERE json_flight.id not in (SELECT json_f_id FROM flight_merged);


UPDATE flight_merged
SET xml_f_id = xlf.flight_id, from_abr = xlf.Departure, dest_abr = xlf.Arrival
FROM flight_merged fm JOIN xml_flight xlf
	ON xlf.flightCode=fm.flight_code
	AND xlf.Date=fm.depart_date;

INSERT INTO flight_merged(xml_f_id,flight_code,depart_date,dest_abr,from_abr)
SELECT DISTINCT flight_id,flightCode,Date,Arrival,Departure
FROM xml_flight
WHERE xml_flight.flight_id not in (SELECT xml_f_id FROM flight_merged);

UPDATE flight_merged
SET tab_f_id = xlf.flight_id, from_abr = xlf.[From], dest_abr = xlf.Dest, arrival_date=xlf.ArrivalDate, depart_time=xlf.DepartTime, arrival_time=xlf.ArrivalTime
FROM flight_merged fm JOIN tab_flight xlf
	ON xlf.Flight=fm.flight_code
	AND xlf.DepartDate=fm.depart_date;

INSERT INTO flight_merged(xml_f_id,flight_code,depart_date,arrival_date,dest_abr,from_abr, arrival_time, depart_time)
SELECT DISTINCT flight_id,Flight,DepartDate,ArrivalDate, Dest, [From], ArrivalTime, DepartTime
FROM tab_flight
WHERE tab_flight.flight_id not in (SELECT tab_f_id FROM flight_merged);











