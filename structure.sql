create database SistAgenda char set utf8;
use SistAgenda;
create table PERSONA (
	CODPER int primary key auto_increment,
    NOMPER varchar(100),
    APEPER varchar(100),
    DNIPER varchar(8)    
);
describe persona;

insert INTO PERSONA (NOMPER, APEPER, DNIPER)
	VALUES 
		('Martín Alexis','Samán Arata','72720455');

select * from persona;

