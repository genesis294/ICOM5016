------------------Creates tables for resources locator app------------------------------------------

----Tables related to users-------------------------
--Creates table for app users. General user table.
CREATE TABLE appuser (uid serial primary key, firstname varchar(50), lastname varchar(50),
email varchar(50), upassword varchar(50));
--Table for user phone numbers. Phone attribute for appuser.
CREATE TABLE phone(phone_id serial primary key, uid integer references appuser(uid), phone char(10));
--Table for user location. Location attribute for supplier and person in need.
CREATE TABLE user_location(location_id serial primary key, uid integer references appuser(uid), latitude float, 
longitud float);
--Table for user address. Address attribute for supplier and person in need
CREATE TABLE address(address_id serial primary key, uid integer references appuser(uid), line1 varchar(50),
line2 varchar(50), city varchar(20), state varchar(2), zipcode varchar(10));

----Specialized user tables. They reference the user table.
--Admin table
CREATE TABLE appadmin (aid serial primary key, uid int references appuser(uid));
--Supplier table
CREATE TABLE supplier (sid serial primary key, uid int references appuser(uid), sbusiness_type varchar(50));
--Person in need table
CREATE TABLE person_in_need (nid serial primary key, uid int references appuser(uid));

----Tables related to resources------------------------
--resources table. General resources table.
CREATE TABLE resources(rid serial primary key, rname varchar(50), rquantity int, rdate_added date, rcategory varchar(15));

----Specialized resources tables. They reference the resources table.
--Water table
CREATE TABLE water(wid serial primary key,rid integer references resources(rid), wtype varchar(50), wbrand varchar(50));
--Ice table
CREATE TABLE ice(iid serial primary key,rid integer references resources(rid), isize varchar(50));
--Food table
CREATE TABLE food(fid serial primary key,rid integer references resources(rid), ftype varchar(50), 
fbrand varchar(50), famount integer, fexp_date varchar(50));
--Medication table
CREATE TABLE medication(mid serial primary key,rid integer references resources(rid), mtype varchar(50), mamount integer,
mdose float, mbrand varchar(50));
--Medical devices table
CREATE TABLE medical_devices(mdid serial primary key,rid integer references resources(rid), mdtype varchar(50), 
mdbrand varchar(50),mdpower_type varchar(50), mdprecision float);
--Fuel clothes
CREATE TABLE clothes(clid serial primary key,rid integer references resources(rid), ctype varchar(50), cbrand varchar(50), cgender varchar(10),
cmaterial varchar(50));
--Power Generators table
CREATE TABLE power_generators(pgid serial primary key,rid integer references resources(rid), pgbrand varchar(50), 
pgwatts float, pggas varchar(10));
--Batteries table
CREATE TABLE batteries(bid serial primary key,rid integer references resources(rid), btype varchar(50), 
bsize integer, bbrand varchar(50));
--Tools table
CREATE TABLE tools(tlid serial primary key,rid integer references resources(rid), ttype varchar(50), tbrand varchar(50));
--Heavy Equipment table
CREATE TABLE heavy_equipment(heid serial primary key, rid integer references resources(rid), hetype varchar(50), 
hebrand varchar(50), hesize varchar(50), heweight float, hemodel varchar(50));

--Donations table. Relates a supplier with resources in the case that the resources was free.
CREATE TABLE donates(rid integer references resources(rid), sid integer references supplier(sid), primary key (rid,sid));
--Supplies table. Relates a supplier with resources in the case that the resources was being sold.
CREATE TABLE supplies(rid integer references resources(rid), sid integer references supplier(sid), sprice float, 
primary key (rid,sid));
--Requests table. Relates a person in need with resources when they need a specific resources.
CREATE TABLE requests(rid integer references resources(rid), nid integer references person_in_need(nid), 
primary key (rid,nid));

----Tables related to cart
--Cart table
CREATE TABLE cart(cid serial primary key, nid integer references person_in_need(nid));
--Cart item table
CREATE TABLE cart_item(ciid serial primary key, ciamount integer, ciprice float, rid integer references resources(rid));
--itemList table
CREATE TABLE item_list(list_id serial primary key, cid integer references cart(cid), 
ciid integer references cart_item(ciid));
--has Cart table. Relates the cart and person in need
CREATE TABLE has_cart(cid integer references cart(cid), ciid integer references cart_item(ciid), primary key(cid,ciid));

----Tables related to transactions-----------------------
--Transaction table.
CREATE TABLE transactions(tid serial primary key, ttotal_cost float, tquantity integer,ttime time, 
tdate date, nid integer references person_in_need(nid));
--Pays table. Relates transaction with cart. 
CREATE TABLE pays(cid integer references cart(cid), tid integer references transactions(tid), primary key (cid,tid) );
--Payment Method table
CREATE TABLE credit_card(card_id integer primary key, cardnumber integer, exp_date date, 
nid integer references person_in_need(nid));

