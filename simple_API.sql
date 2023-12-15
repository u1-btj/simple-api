create database simple_api

create table users (
	user_id serial PRIMARY KEY,
	email VARCHAR (50) NOT NULL,
	firstname VARCHAR (50) NOT NULL,
	lastname VARCHAR (50) NOT NULL,
	avatar text,
	token_user varchar(50)
);

create table resource (
	resource_id serial PRIMARY KEY,
	name VARCHAR (50) NOT NULL,
	year int NOT NULL,
	color VARCHAR (50),
	pantone_value VARCHAR (50)
);

INSERT INTO simple_api.public.users (email,firstname,lastname,avatar,token_user)
VALUES ('george.bluth@reqres.in', 'George', 'Bluth', 'https://reqres.in/img/faces/1-image.jpg', 'aVoaRVbeEsbJ4GZ'),
('janet.weaver@reqres.in', 'Janet', 'Weaver', 'https://reqres.in/img/faces/2-image.jpg', 'FPDZBVG5eMQQvyX'),
('emma.wong@reqres.in', 'Emma', 'Wong', 'https://reqres.in/img/faces/3-image.jpg', 'yq1ALDafiScP9t5'),
('eve.holt@reqres.in', 'Eve', 'Holt', 'https://reqres.in/img/faces/4-image.jpg', 'CVGIBuH47DEtHA8'),
('charles.morris@reqres.in', 'Charles', 'Morris', 'https://reqres.in/img/faces/5-image.jpg', 'QBQf3ZKr9jw5OpX'),
('tracey.ramos@reqres.in', 'Tracey', 'Ramos', 'https://reqres.in/img/faces/6-image.jpg', 'EyVm6UIH7u8aIMV'),
('michael.lawson@reqres.in', 'Michael', 'Lawson', 'https://reqres.in/img/faces/7-image.jpg', '7jMrCxektsD1tLL'),
('lindsay.ferguson@reqres.in', 'Lindsay', 'Ferguson', 'https://reqres.in/img/faces/8-image.jpg', 'u3SzKKKKBFtVqrg'),
('tobias.funke@reqres.in', 'Tobias', 'Funke', 'https://reqres.in/img/faces/9-image.jpg', 'VUQ8KZ9e4XkGmYu'),
('byron.fields@reqres.in', 'Byron', 'Fields', 'https://reqres.in/img/faces/10-image.jpg', '7sDT6kyX0boJMFb'),
('george.edwards@reqres.in', 'George', 'Edwards', 'https://reqres.in/img/faces/11-image.jpg', 'moYz93FgUHavfPU'),
('rachel.howell@reqres.in', 'Rachel', 'Howell', 'https://reqres.in/img/faces/12-image.jpg', '0yk95ILbL5CJoJy');

INSERT INTO simple_api.public.resource  (name, year, color, pantone_value)
VALUES ('cerulean', 2000, '#98B2D1', '15-4020'),
('fuchsia rose', 2001, '#C74375', '17-2031'),
('true red', 2002, '#BF1932', '19-1664'),
('aqua sky', 2003, '#7BC4C4', '14-4811'),
('tigerlily', 2004, '#E2583E', '17-1456'),
('blue turquoise', 2005, '#53B0AE', '15-5217'),
('sand dollar', 2006, '#DECDBE', '13-1106'),
('chili pepper', 2007, '#9B1B30', '19-1557'),
('blue iris', 2008, '#5A5B9F', '18-3943'),
('mimosa', 2009, '#F0C05A', '14-0848'),
('turquoise', 2010, '#45B5AA', '15-5519'),
('honeysuckle', 2011, '#D94F70', '18-2120');

--select * from simple_api.public.resource

--truncate users 
--truncate resource 