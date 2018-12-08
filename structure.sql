create database SistAgenda char set utf8;
use SistAgenda;
create table PERSONA (
	CODPER int primary key auto_increment,
    NOMPER varchar(100),
    APEPER varchar(100),
    DNIPER varchar(8),
    EMAILPER VARCHAR(50)
);
describe persona;

insert INTO PERSONA (NOMPER, APEPER, DNIPER, EMAILPER)
	VALUES 
		('Martín Alexis','Samán Arata','72720455','martin.saman@vallegrande.edu.pe');

select * from persona;

