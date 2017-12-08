-- 1. What query would you run to get the total revenue for March of 2012?
select SUM(billing.amount), month(charged_datetime)
from billing
where charged_datetime LIKE '2012-03%';

-- 2. What query would you run to get total revenue collected from the client with an id of 2?
select SUM(billing.amount), billing.charged_datetime, clients.first_name, clients.client_id
from billing
    join clients on clients.client_id = billing.client_id
where clients.client_id = 2;

-- 3. What query would you run to get all the sites that client=10 owns?
select sites.domain_name, clients.first_name, clients.client_id
from clients
    left join sites ON sites.client_id = clients.client_id
where clients.client_id = 10;

-- 4. What query would you run to get total # of sites created per month per year for the client with an id of 1? 
-- What about for client=20?
select count(sites.client_id) as '#', sites.domain_name, clients.first_name, monthname(sites.created_datetime) as 'Month', extract(year from sites.created_datetime) as 'Year', clients.client_id
from sites
    left join clients ON clients.client_id  = sites.client_id
where clients.client_id = 1
group by monthname(sites.created_datetime), extract(year from sites.created_datetime)
order by extract(year from sites.created_datetime),monthname(sites.created_datetime);

select count(sites.client_id) as '#', sites.domain_name, clients.first_name, monthname(sites.created_datetime) as 'Month', extract(year from sites.created_datetime) as 'Year', clients.client_id
from sites
    left join clients ON clients.client_id  = sites.client_id
where clients.client_id = 20
group by monthname(sites.created_datetime), extract(year from sites.created_datetime)
order by extract(year from sites.created_datetime),monthname(sites.created_datetime);

-- 5. What query would you run to get the total # of leads generated for each of the sites between January 1, 2011 to February 15, 2011?
select count(leads.first_name), sites.domain_name, DATE_FORMAT(leads.registered_datetime, '%M %e, %Y')
from leads
    left join sites on sites.site_id = leads.site_id
WHERE leads.registered_datetime BETWEEN '2011-01-01 00:00:01' AND '2011-02-15 23:59:59'
GROUP BY sites.domain_name, DATE_FORMAT(leads.registered_datetime, '%M %e, %Y');

-- 6. What query would you run to get a list of client names and the total # 
-- of leads we've generated for each of our clients between January 1, 2011 to December 31, 2011?
select count(leads.leads_id) as number_leads, clients.first_name, clients.last_name
from leads
    left join sites on sites.site_id = leads.site_id
    left join clients on sites.client_id = clients.client_id
where leads.registered_datetime between '2011-01-01 00:00:01' AND '2011-12-31%'
group by clients.first_name
order by number_leads desc;

-- 7. What query would you run to get a list of client names and the total # 
-- of leads we've generated for each client each month between months 1 - 6 of Year 2011?
select count(leads.leads_id) as number_leads, clients.first_name, clients.last_name, monthname(registered_datetime)
from leads
    left join sites on sites.site_id = leads.site_id
    left join clients on sites.client_id = clients.client_id
where year(leads.registered_datetime) = 2011 and month(leads.registered_datetime) between 1 and 6
group by clients.first_name, month(registered_datetime)
order by month(registered_datetime) asc;

-- 8. What query would you run to get a list of client names and the total # of leads we've generated for each of our clients' sites between January 1, 2011 to December 31, 2011? 
-- Order this query by client id.  Come up with a second query that shows all the clients, the site name(s), and the total number of leads generated from each site for all time.



