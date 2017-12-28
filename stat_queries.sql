--Daily available count
with supplied as (select sid, rid, coalesce(sprice, 0) as sprice 
from donates natural full join supplies)
select sum(rquantity) as available, sum(case when sprice = 0 then rquantity end) as donations, sum(case when sprice != 0 then rquantity end) as supply
from resources natural inner join supplied 
where rdate_added = '28-12-2017'

--Daily request count
select sum(rquantity) as requests from resources natural inner join requests where rdate_added = '28-12-2017'

--Quantity for each category
with supplied as (select sid, rid, coalesce(sprice, 0) as sprice 
from donates natural full join supplies)
select rcategory, coalesce(sum(case when sprice is null then rquantity end),0) as request, coalesce(sum(case when sprice >=0 then rquantity end), 0) as available
from resources natural inner join (supplied  natural full join requests)
where rdate_added = '28-12-2017'
group by rcategory
order by rcategory
--Check the resources to confirm 
select * from resources where rdate_added='28-12-2017'

--Weekly available count
with supplied as (select sid, rid, coalesce(sprice, 0) as sprice 
from donates natural full join supplies)
select sum(rquantity) as available, sum(case when sprice = 0 then rquantity end) as donations, sum(case when sprice != 0 then rquantity end) as supply
from resources natural inner join supplied 
where rdate_added >= '24-12-2017' and rdate_added <= '30-12-2017'

--Weekly request count
select sum(rquantity) as requests from resources natural inner join requests where rdate_added >= '24-12-2017' and rdate_added <= '30-12-2017'

--Quantity for each category in week
with supplied as (select sid, rid, coalesce(sprice, 0) as sprice 
from donates natural full join supplies)
select rcategory, coalesce(sum(case when sprice is null then rquantity end),0) as request, coalesce(sum(case when sprice >=0 then rquantity end), 0) as available
from resources natural inner join (supplied  natural full join requests)
where rdate_added >= '24-12-2017' and rdate_added <= '30-12-2017'
group by rcategory
order by rcategory