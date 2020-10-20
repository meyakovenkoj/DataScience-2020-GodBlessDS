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











