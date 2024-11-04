
#                                  КЛАСС COMPANY
#######################################################################################
# print("\nCOMPANY CLASS")


class Company():
    company_id = 0

    def __init__(self, comp_name, position, requirements, salary):
        self._comp_name = comp_name
        self._position = position
        self._requirments = requirements
        self._salary = salary

    @property
    def comp_name(self):
        return self._comp_name

    @property
    def position(self):
        return self._position

    @property
    def requirements(self):
        return self._requirments

    @property
    def salary(self):
        return self._salary


    def __str__(self):
        return f"'{self._comp_name}': position is {self._position}, salary is {self._salary}"

    def __repr__(self):
        return f"Company({self._comp_name}, {self._position}, {self._requirments}, {self._salary})"

    def __lt__(self, other):
        return self._comp_name < other._comp_name

    def __eq__(self, other):
        if isinstance(other, Company):
            return self._comp_name == other._comp_name
        return False

    def __hash__(self):
        return hash(self._comp_name)