
## Exercicio de diagrama

``` mermaid
classDiagram



class FreelancerWithCommission{
    +commission: float
    +contracts_landed: float
    compute_pay(float)
}

class SalariedEmployeeWithCommission{
    +commission: float
    +contracts_landed: float
    compute_pay(float)
}

class HourlyEmployeeWithCommission{
     +commission: float
     +contracts_landed: float
      compute_pay(float)
}


class HourlyEmployee{
    +pay_rate: float
    +hours_worked: int 
    +employer_cost: float 
    compute_pay(float)
}

class SalariedEmployee{
    +monthly_salary: float
    +percentage: float
    compute_pay(float)
}


class Freelancer{
    +pay_rate: float
    +hours_worked: int 
    +vat_number: str 
    compute_pay(float)
}
class Employee {
    +name: str
    +id: int
    compute_pay(float)
}

Employee <|---  HourlyEmployee
Employee <|---  SalariedEmployee
Employee <|---  Freelancer
SalariedEmployee <|--- SalariedEmployeeWithCommission
HourlyEmployeeWithCommission <|---  HourlyEmployee
FreelancerWithCommission <|---  Freelancer



```