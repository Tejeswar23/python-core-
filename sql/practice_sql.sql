select * from department
select * from employee

-- INNER JOIN
select d.dept_name,e.e_name
from department d
inner join employee e on
d.dept_id = e.dept_id; 

-- LEFT JOIN
select d.dept_name,e.e_name
from department d
left join employee e on
d.dept_id = e.dept_id; 

--RIGHT JOIN
select d.dept_name,e.e_name
from department d
right join employee e on
d.dept_id = e.dept_id;

-- FULL JOIN
select d.dept_name,e.e_name
from department d
full join employee e on
d.dept_id = e.dept_id;

--Aggeregate Functions
--using of sum()
select sum(e_salary) as emp_total_sum
from employee

--using of max()
select max(e_salary) as emp_highest_salary
from employee

--using of min()
select min(e_salary) as emp_lowest_salary
from employee

--using of avg()
select avg(e_salary) as emp_avg_salary
from employee

--using of count()
--count the no of employees department can have
select d.dept_name,count(e_id) as employee_count
from department d 
left join employee e on
d.dept_id = e.dept_id
group by dept_name

--sum the department spending on employees
select d.dept_name,sum(e_salary) as department_spending
from department d 
left join employee e on
d.dept_id = e.dept_id
group by dept_name

