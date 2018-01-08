--CARTS, ITEMS AND ITEM LISTS FOR:

--PERSON IN NEED 1:
--create cart
INSERT INTO cart(nid) VALUES(1);
--create cart items
INSERT INTO cart_item(ciamount, ciprice, rid, sid) VALUES(5, 4.99, 21, 1); --agua
INSERT INTO cart_item(ciamount, ciprice, rid, sid) VALUES(2, 1.99, 25, 2); --baterias
--connect cart items to cart
INSERT INTO item_list(cid, ciid) VALUES (1,1);
INSERT INTO item_list(cid, ciid) VALUES (1,2);


--PERSON IN NEED 2:
--cart 1
INSERT INTO cart(nid) VALUES(2);
INSERT INTO cart_item(ciamount, ciprice, rid, sid) VALUES(5, 2.99, 27, 1); --hielo
INSERT INTO cart_item(ciamount, ciprice, rid, sid) VALUES(1, 3, 32, 6); --cocoa pebbles
INSERT INTO cart_item(ciamount, ciprice, rid, sid) VALUES(10, 1.5, 31, 6); --ravioli
INSERT INTO item_list(cid, ciid) VALUES (2,3);
INSERT INTO item_list(cid, ciid) VALUES (2,4);
INSERT INTO item_list(cid, ciid) VALUES (2,5);
--cart 2
INSERT INTO cart(nid) VALUES(2);
--cart items
INSERT INTO cart_item(ciamount, ciprice, rid, sid) VALUES(1, 2400, 41, 3); --planta
INSERT INTO item_list(cid, ciid) VALUES (3,6);


--PERSON IN NEED 3:
INSERT INTO cart(nid) VALUES(3);
INSERT INTO cart_item(ciamount, ciprice, rid, sid) VALUES(1, 2400, 41, 3); --planta
INSERT INTO item_list(cid, ciid) VALUES (4,7);


--PERSON IN NEED 4:
INSERT INTO cart(nid) VALUES(4);
INSERT INTO cart_item(ciamount, ciprice, rid, sid) VALUES(45, 0.78, 43, 5); --gasolina
INSERT INTO cart_item(ciamount, ciprice, rid, sid) VALUES(1, 4.99, 28, 4); --aspirina
INSERT INTO item_list(cid, ciid) VALUES (5,8);
INSERT INTO item_list(cid, ciid) VALUES (5,9);


--PERSON IN NEED 5:
INSERT INTO cart(nid) VALUES(5);
INSERT INTO cart_item(ciamount, ciprice, rid, sid) VALUES(1, 4500, 42, 3); --planta
INSERT INTO item_list(cid, ciid) VALUES (6,10);


--PERSON IN NEED 6:
INSERT INTO cart(nid) VALUES(6);
INSERT INTO cart_item(ciamount, ciprice, rid, sid) VALUES(50, 0.8, 23, 5); --gasolina
INSERT INTO item_list(cid, ciid) VALUES (7,11);


--PERSON IN NEED 7:
INSERT INTO cart(nid) VALUES(7);
INSERT INTO cart_item(ciamount, ciprice, rid, sid) VALUES(1, 3.99, 37, 7); --panadol
INSERT INTO cart_item(ciamount, ciprice, rid, sid) VALUES(2, 5.6, 39, 6); --hielo
INSERT INTO cart_item(ciamount, ciprice, rid, sid) VALUES(10, 1.5, 31, 6); --ravioli
INSERT INTO item_list(cid, ciid) VALUES (8,12);
INSERT INTO item_list(cid, ciid) VALUES (8,13);
INSERT INTO item_list(cid, ciid) VALUES (8,14);


--PERSON IN NEED 8:
INSERT INTO cart(nid) VALUES(8);
INSERT INTO cart_item(ciamount, ciprice, rid, sid) VALUES(1, 6.99, 33, 2); --baterias AAA
INSERT INTO cart_item(ciamount, ciprice, rid, sid) VALUES(4, 10, 26, 2); --camisas
INSERT INTO item_list(cid, ciid) VALUES (9,15);
INSERT INTO item_list(cid, ciid) VALUES (9,16);


--PERSON IN NEED 9:
INSERT INTO cart(nid) VALUES(9);
INSERT INTO cart_item(ciamount, ciprice, rid, sid) VALUES(10, 4.99, 21, 1); --agua
INSERT INTO cart_item(ciamount, ciprice, rid, sid) VALUES(30, 0.78, 43, 5); --gasolina
INSERT INTO item_list(cid, ciid) VALUES (10,17);
INSERT INTO item_list(cid, ciid) VALUES (10,18);


--PERSON IN NEED 10:
INSERT INTO cart(nid) VALUES(10);
INSERT INTO cart_item(ciamount, ciprice, rid, sid) VALUES(125, 0.78, 43, 5); --gasolina
INSERT INTO cart_item(ciamount, ciprice, rid, sid) VALUES(1, 120000, 36, 3); --digger
INSERT INTO item_list(cid, ciid) VALUES (11,19);
INSERT INTO item_list(cid, ciid) VALUES (11,20);