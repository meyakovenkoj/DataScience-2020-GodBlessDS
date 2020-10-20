use GodBlessDS
SELECT DISTINCT cu1.id, cu1.PassengerFirstName,cu1.PassengerLastName,cu1.PassengerBirthDate,
cu1.PassengerDocumentS,cu1.PassengerDocumentN,
cu2.id,
cu2.PassengerFirstName,cu2.PassengerLastName,cu2.PassengerBirthDate,
cu2.PassengerDocumentS,cu2.PassengerDocumentN,
cf1.Destination,cf1.FlightDate,cf1.FlightNumber
FROM csv_user cu1 JOIN csv_ticket ct1 ON cu1.id= ct1.usr_id 
JOIN csv_flight cf1 ON ct1.fl_id=cf1.id JOIN csv_user cu2
ON cu2.PassengerDocumentS=cu1.PassengerDocumentS 
AND cu2.id!=cu1.id
AND ABS(cu2.PassengerDocumentN-cu1.PassengerDocumentN)<10
JOIN csv_ticket ct2 
ON ct2.usr_id=cu2.id AND ct2.fl_id=ct1.fl_id

