CREATE TABLE user_merged (
	u_id int Primary key identity NOT NULL,
	csv_u_id int NULL,
	json_u_id int NULL,
	tab_u_id int NULL,
	xlsx_u_id int NULL,
	xml_u_id int NULL,
	first_name nvarchar(50) NULL,
	second_name nvarchar(50) NULL,
	last_name nvarchar(50) NULL,
	sex nvarchar(10) NULL,
	birth_date date NULL,
	document_s int NULL,
	document_n int NULL
)
CREATE TABLE flight_merged (
	f_id int Primary key identity NOT NULL,
	csv_f_id int NULL,
	json_f_id int NULL,
	tab_f_id int NULL,
	xlsx_f_id int NULL,
	xml_f_id int NULL,

	flight_code varchar(max) NULL,
	depart_date date NULL,
	arrival_date date NULL,
	depart_time time NULL,
	arrival_time time NULL,
	dest_ nvarchar(50) NULL,
	from_ nvarchar(50) NULL
)

CREATE TABLE ticket_merged (
	t_id int Primary key identity NOT NULL,
	u_id int NULL,
	f_id int NULL,
	csv_u_id int NULL,
	json_u_id int NULL,
	tab_u_id int NULL,
	xlsx_u_id int NULL,
	xml_u_id int NULL,
	csv_f_id int NULL,
	json_f_id int NULL,
	tab_f_id int NULL,
	xlsx_f_id int NULL,
	xml_f_id int NULL,
    TicketNumber nvarchar(50) NULL,
    Seq nvarchar(50) NULL,
    Class nvarchar(1) NULL,
    Meal nvarchar(50) NULL,
    Baggage nvarchar(50) NULL,
    Cardnumber nvarchar(50) NULL,
)
 