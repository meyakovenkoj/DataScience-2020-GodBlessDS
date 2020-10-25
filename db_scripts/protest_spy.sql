create view json_fl(json_id, fl_date, flight, depart, destination) as select jf.id, jf.fl_date, jf.flight_code, a2.city as depart, a.city as dest from json_flight jf join airport a on a.code = jf.arrival join airport a2 on a2.code = jf.departure
where exists(
              select null from date_city_to_check where fl_date between dateadd(day, -3, dates) and dates
          );


create view xml_fl(xml_id, fl_date, flight, depart, destination) as select xf.flight_id, xf.Date, xf.flightCode, a2.city as depart, a.city as dest from  xml_flight xf join airport a on a.code = xf.Arrival join airport a2 on a2.code = xf.Departure
where exists(
              select null from date_city_to_check where xf.Date between dateadd(day, -3, dates) and dates
          );


create view csv_fl(csv_id, fl_date, flight, depart, destination) as select cf.id, cf.FlightDate, cf.FlightNumber, null as depart, a.city as dest from csv_flight cf join airport a on a.code = cf.Destination
where exists(
              select null from date_city_to_check where FlightDate between dateadd(day, -3, dates) and dates
          );


create view tab_fl(tab_id, fl_date, flight, depart, destination) as select tf.flight_id, tf.DepartDate, tf.Flight, a2.city as depart, a.city as dest from tab_flight tf join airport a on a.code = tf.Dest join airport a2 on a2.code = tf.[From]
where exists(
              select null from date_city_to_check where DepartDate between dateadd(day, -3, dates) and dates
          );


create view xlsx_fl(xlsx_id, fl_date, flight, depart, destination) as select xx.id, xx.FlightDate, xx.FlightNumber, a2.city as depart, a.city as dest from xlsx_flight xx join airport a on a.code = xx.DestinationAbr join airport a2 on a2.code = xx.FromAbr
where exists(
              select null from date_city_to_check where FlightDate between dateadd(day, -3, dates) and dates
          );


create table json_fl_t (
    json_id int primary key,
    fl_date date,
    flight varchar(max),
    depart varchar(max),
    destination varchar(max)
);

insert into json_fl_t select * from json_fl;

delete from json_fl_t
where not exists(
    select null from date_city_to_check
    where (fl_date between dateadd(day,-3,dates) and dates) and (depart=cities or destination=cities)
);

create table xml_fl_t (
    xml_id int primary key,
    fl_date date,
    flight varchar(max),
    depart varchar(max),
    destination varchar(max)
);

insert into xml_fl_t select * from xml_fl;

delete from xml_fl_t
where not exists(
    select null from date_city_to_check
    where (fl_date between dateadd(day,-3,dates) and dates) and (depart=cities or destination=cities)
);

create table tab_fl_t (
    tab_id int primary key,
    fl_date date,
    flight varchar(max),
    depart varchar(max),
    destination varchar(max)
);

insert into tab_fl_t select * from tab_fl;

delete from tab_fl_t
where not exists(
    select null from date_city_to_check
    where (fl_date between dateadd(day,-3,dates) and dates) and (depart=cities or destination=cities)
);

create table csv_fl_t (
    csv_id int primary key,
    fl_date date,
    flight varchar(max),
    depart varchar(max),
    destination varchar(max)
);

insert into csv_fl_t select * from csv_fl;

delete from csv_fl_t
where not exists(
    select null from date_city_to_check
    where (fl_date between dateadd(day,-3,dates) and dates) and (depart=cities or destination=cities)
);

create table xlsx_fl_t (
    xlsx_id int primary key,
    fl_date date,
    flight varchar(max),
    depart varchar(max),
    destination varchar(max)
);

insert into xlsx_fl_t select * from xlsx_fl;

delete from xlsx_fl_t
where not exists(
    select null from date_city_to_check
    where (fl_date between dateadd(day,-3,dates) and dates) and (depart=cities or destination=cities)
);


create table fl_to_check (
    id int not null primary key identity,
    json_id int null,
    xml_id int null,
    csv_id int null,
    tab_id int null,
    xlsx_id int null,
    fl_date date,
    flight varchar(max),
    depart varchar(max),
    destination varchar(max)
);

create view fl_merged_views as select json_id, xml_id, csv_id, tab_id, xlsx_id,
                                      coalesce(jf.fl_date, xf.fl_date, cf.fl_date, tf.fl_date, x.fl_date) as fl_date,
                                      coalesce(jf.flight, xf.flight, cf.flight, tf.flight, x.flight) as flight,
                                      coalesce(jf.depart, xf.depart, tf.depart, x.depart) as depart,
                                      coalesce(jf.destination, xf.destination, cf.destination, tf.destination, x.destination) as destination
from json_fl_t jf
    full join xml_fl_t xf
        on jf.fl_date=xf.fl_date and jf.flight=xf.flight and jf.destination=xf.destination
    full join csv_fl_t cf
        on cf.fl_date=xf.fl_date and cf.flight=xf.flight and cf.destination=xf.destination
               or jf.fl_date=cf.fl_date and jf.flight=cf.flight and jf.destination=cf.destination
    full join tab_fl_t tf
        on tf.fl_date=xf.fl_date and tf.flight=xf.flight and tf.destination=xf.destination
               or jf.fl_date=tf.fl_date and jf.flight=tf.flight and jf.destination=tf.destination
               or tf.fl_date=cf.fl_date and tf.flight=cf.flight and tf.destination=cf.destination
    full join xlsx_fl_t x
        on x.fl_date=cf.fl_date and x.flight=cf.flight and x.destination=cf.destination
               or jf.fl_date=x.fl_date and jf.flight=x.flight and jf.destination=x.destination
               or tf.fl_date=x.fl_date and tf.flight=x.flight and tf.destination=x.destination
               or x.fl_date=xf.fl_date and x.flight=xf.flight and x.destination=xf.destination;

insert into fl_to_check select * from fl_merged_views;


select * from fl_to_check where tab_id is not null or csv_id is not null; /*empty -> drop columns */

alter table fl_to_check
drop column csv_id, tab_id;



select distinct count(distinct f.id) as counted, coalesce(ju.first_name, xu.firstname, xxu.PassengerFirstName) as firstname, xxu.PassengerSecondName as secondname, coalesce(ju.last_name, xu.lastname, xxu.PassengerLastName) as lastname, ju.nickname
from fl_to_check f left join json_ticket jt on json_id=jt.fl_id left join json_user ju on jt.usr_id = ju.id
                            left join xml_ticket xt on xml_id=xt.flight_id left join xml_card xc on xt.cardnumber = xc.cardnumber left join xml_user xu on xu.userid = xc.userid
                            left join xlsx_ticket xxt on xlsx_id=xxt.fl_id left join xlsx_user xxu on xxt.usr_id = xxu.id
group by coalesce(ju.first_name, xu.firstname, xxu.PassengerFirstName), xxu.PassengerSecondName, coalesce(ju.last_name, xu.lastname, xxu.PassengerLastName), ju.nickname
having coalesce(ju.first_name, xu.firstname, xxu.PassengerFirstName) is not null or xxu.PassengerSecondName is not null or coalesce(ju.last_name, xu.lastname, xxu.PassengerLastName) is not null or ju.nickname  is not null
order by count(distinct f.id) desc;
