------------------Creates tables for resource locator app------------------------------------------

----Table related to users-------------------------
--Creates table for app users. General user table.
CREATE TABLE appuser (uid serial primary key, firstname varchar(50), lastname varchar(50),
email varchar(50), password varchar(50), cid references cart(cid))
--Table for user phone numbers
CREATE TABLE phone(phone_id serial primary key, uid integer references user(uid), phone char(10))

----Specialized user tables. They reference the user table.
--Admin table
CREATE TABLE appadmin (aid serial primary key, uid int references user(uid))
--Supplier table
CREATE TABLE supplier (sid serial primary key, saddress varchar(50), slocation varchar(50), sbusiness_type varchar(50) )
--Person in need table
CREATE TABLE person_in_need (nid serial primary key, naddress varchar(50), nlocation varchar(50) )

----Table related to resources------------------------
--Resource table. General resource table.
CREATE TABLE resource(rid serial primary key, rname varchar(50), rquantity int, rdate_added date)

----Specialized resource tables. They reference the resource table.
--Water table
CREATE TABLE water(rid integer references resource(rid), wtype varchar(50), wbrand varchar(50))
--Ice table
CREATE TABLE ice(rid integer references resource(rid), isize varchar(50))
--Food table
CREATE TABLE food(rid integer references resource(rid), ftype varchar(50), fbrand varchar(50), famount integer, 
fexp_date varchar(50))
--Medication table
CREATE TABLE medication(rid integer references resource(rid), mtype varchar(50), mamount integer,
mdose float, mbrand varchar(50))
--Medical devices table
CREATE TABLE medical_devices(rid integer references resource(rid), mdtype varchar(50), mdbrand varchar(50),
mdpower_type varchar(50), mdprecision float)
--Fuel clothes
CREATE TABLE clothes(rid integer references resource(rid), ctype varchar(50), cbrand varchar(50), cgender varchar(10),
cmaterial varchar(50))
--Power Generators table
CREATE TABLE power_generators(rid integer references resource(rid), pgbrand varchar(50), pgwatts float, pggas varchar(10))
--Batteries table
CREATE TABLE batteries(rid integer references resource(rid), btype varchar(50), bsize integer, bbrand varchar(50))
--Tools table
CREATE TABLE tools(rid integer references resource(rid), ttype varchar(50), tbrand varchar(50))
--Heavy Equipment table
CREATE TABLE heavy_equipment(rid integer references resource(rid), hetype varchar(50), hebrand varchar(50), hesize varchar(50),
heweight float, hemodel varchar(50))

--Donations table
CREATE TABLE donates(rid references resource(rid), sid references supplier(sid), primary key (rid,sid))
--Supplies table
CREATE TABLE supplies(rid references resource(rid), sid references supplier(sid), sprice float, primary key (rid,sid))
--Donations table
CREATE TABLE requests(rid references resource(rid), nid references person_in_need(nid), primary key (rid,nid))

----Tables related to transactions and carts-----------------------
--Transaction table.
CREATE TABLE transactions(tid serial primary key, tpayment_method varchar(50), ttotal_cost float, tquantity integer,
ttime time, tdate date, nid references person_in_need(nid))
--Cart table
CREATE TABLE cart(cid serial primary key )
--Cart item table
CREATE TABLE cart_item(ciid serial primary key, ciamount integer, ciprice float)
--has Cart Item table
CREATE TABLE has_cart_item(cid references cart(cid), ciid references cart_item(ciid), primary key(cid, ciid))
--Pays table
CREATE TABLE pays(cid references cart(cid), tid references transactions(tid), primary key (cid,tid) )
