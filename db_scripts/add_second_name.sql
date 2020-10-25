update csv_user 
set PassengerSecondName=(SELECT PassengerSecondName from u2) 
from csv_user as u1 
join csv_user as u2 
on (u1.PassengerDocumentS=u2.PassengerDocumentS 
    and u1.PassengerDocumentN=u2.PassengerDocumentN 
    and u1.id!=u2.id 
    and u2.PassengerSecondName not like '_.');

