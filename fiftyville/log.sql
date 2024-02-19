-- Keep a log of any SQL queries you execute as you solve the mystery.
--theft July 28 on Humphrey Street
select * from crime_scene_reports where street ='Humphrey Street' and day = 28 and month = 7;
--Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery. Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery.
select * from interviews where day = 28 and month = 7 and transcript like '%bakery%';

-- 'Ruth','Eugene','Raymond'
--1 Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away. If you have security footage from the bakery parking lot,
--1 you might want to look for cars that left the parking lot in that time frame.
select * from bakery_security_logs where day = 28 and month = 7 and hour between 10 and 11;
--plate numbers ('94KL13X','6P58WS2','4328GD8','G412CB7','L93JTIZ','322W7JE','0NTHK55','1106N58','5P2BI95')
select * from people where license_plate in ('94KL13X','6P58WS2','4328GD8','G412CB7','L93JTIZ','322W7JE','0NTHK55','1106N58','5P2BI95');

--2 I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.
select a.*,c.id,c.name,c.phone_number,c.passport_number
from atm_transactions a
left join bank_accounts b on a.account_number = b.account_number
left join people c on b.person_id = c.id
where day = 28 and month = 7 and atm_location = 'Leggett Street' and transaction_type ='withdraw';
--suspects Iman,Taylor,Luca,Diana,Bruce

--3 As the thief was leaving the bakery, they called someone who talked to them for less than a minute. In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow.
--3 The thief then asked the person on the other end of the phone to purchase the flight ticket.
select * from phone_calls where day = 28 and month = 7 and caller in('(829) 555-5269','(286) 555-6063','(389) 555-5198','(770) 555-1861','(367) 555-5533') and duration < 60;
--suspects Taylor,Diana,Bruce
select * from airports where city ='Fiftyville';
--ID = 8 ,abbreviation = CSV
SELECT * from flights a
left join passengers b on a.id = b.flight_id
 where day = 29 and month = 7 and origin_airport_id = 8
 and passport_number in('1988161715','3592750733','5773159633');
 --ver llamadas
 select * from people where phone_number in ('(676) 555-6554','(375) 555-8161');
 --flight id 36
 select city from flights a
 left join airports b on a.destination_airport_id = b.id
 where a.id =36;
