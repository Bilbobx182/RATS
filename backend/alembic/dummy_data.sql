INSERT INTO WORD values ('Python','{1}', 4);
INSERT INTO WORD values ('JavaScript','{1}', 2);
INSERT INTO LOCATION (country,state,city) values ('Ireland','Dublin','City Center');
INSERT INTO COMPANY (name,location_id,jobs_fk) values ('Google',1,'1');
INSERT INTO JOB  (title,company_id,pay,date_posted,has_pension,has_healthcare,has_stock,locations_id) values ('Fullstack Engineer', 1,'40000$', '29-August-2020', true,true,true,1);