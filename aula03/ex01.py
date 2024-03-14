from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class Employee(ABC):
    name: str
    id: int
    commission: float = 100
    contracts_landed: float = 0

    @abstractmethod
    def compute_pay(self) -> float:
        """Compute how much the employee should be paid."""
        return (self.commission * self.contracts_landed)

@dataclass
class EmployeeTaxa(Employee):

    pay_rate: float = 0
    hours_worked: int = 0

    @abstractmethod
    def compute_pay(self):
        """Calculo a taxa do pagamento do empregado"""
        return super().compute_pay() + self.pay_rate * self.hours_worked

@dataclass
class HourlyEmployee(EmployeeTaxa):
    """Employee that's paid based on number of worked hours."""

    employer_cost: float = 1000
    def compute_pay(self):
        """Calculo do pagamento do empregado por hora"""
        return super().compute_pay() + self.employer_cost


@dataclass
class SalariedEmployee(Employee):
    """Employee that's paid based on a fixed monthly salary."""

    monthly_salary: float = 0
    percentage: float = 1

    def compute_pay(self) -> float:
        """Compute how much the employee should be paid."""
        return (super().compute_pay() + self.monthly_salary * self.percentage)


@dataclass
class Freelancer(EmployeeTaxa):
    """Freelancer that's paid based on number of worked hours."""

    vat_number: str = ""
    def compute_pay(self):
        """Calculo do pagamento do freelancer por hora"""
        return super().compute_pay()


def main() -> None:
    """Main function."""

    henry = HourlyEmployee(name="Henry", id=12346, pay_rate=50, hours_worked=100)
    print(
        f"{henry.name} worked for {henry.hours_worked} hours and earned ${henry.compute_pay()}."
    )

    sarah = SalariedEmployee(
        name="Sarah", id=47832, monthly_salary=5000, contracts_landed=10
    )
    print(f"{sarah.name} landed {sarah.contracts_landed} contracts and earned ${sarah.compute_pay()}.")

    edu = Freelancer(
        name="Edu", id=47822, pay_rate=50, hours_worked=100
    )
    print(f"{edu.name} landed {edu.contracts_landed} contracts and earned ${edu.compute_pay()}.")


if __name__ == "__main__":
    main()