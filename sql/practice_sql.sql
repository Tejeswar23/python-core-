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

-- sub query
select e_name from employee
where e_salary > (select avg(e_salary) from employee)

-- non co-realted 
--find the employees whose salary is greater than the avg salary
select e_name,e_salary as salary_greater_than_avg
from employee
where e_salary > (select avg(e_salary) from employee)

-- co-realted 
-- employees earning more than their department average
select e1.e_name, e1.e_salary, e1.dept_id
from Employee e1
where e1.e_salary >
      (select avg(e2.e_salary)
       from Employee e2
       where e2.dept_id = e1.dept_id);

-- using of all operator
-- salary greater than all salaries of hr department
select e_name,e_salary from employee
where e_salary > all 
              (select e_salary 
              from employee
              where dept_id = 1);

--In operator
select e_name from employee
where e_name IN 
             (select e_name
             from employee
             where dept_id = 1);

--NOT IN
select e_name from employee
where e_name NOT IN
               (select e_name
               from employee
               where dept_id = 1);

--ANY
select e_name as employee_salary_greater_than_hr_employees
from employee 
where e_salary > ANY 
                 (select e_salary from employee 
                 where dept_id = 1);

--exist
select d.dept_name
from Department d
where EXISTS (
    select 1 from Employee e
    where e.dept_id = d.dept_id
);

--window functions
--sum
select d.dept_name,
       e.e_name,
       e.e_salary,
       sum(e.e_salary) over (partition by d.dept_name) as dept_total_salary
from employee e
join department d
on d.dept_id = e.dept_id;

--dense_rank vs rank 
select e_salary,
rank() over (order by e_salary desc) as salary_rank,
dense_rank() over (order by e_salary desc) as salary_dense_rank
from employee

--COMMON TABLE EXPRESSION
with hr_employees as (
            select e_name,
                   e_salary
                   from employee
                   where dept_id = 1
)
select * from hr_employees

-- cte with high salary empolyee
with high_salary_empolyees as (
              select e_salary
              from employee
              where e_salary > 50000
)
select * from high_salary_empolyees



