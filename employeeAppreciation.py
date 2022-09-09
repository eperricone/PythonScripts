class EmployeeAppreciation:
    """Programming appreciation letter for employee"""


    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        """Initialization of attributes"""

    def code_of_appreciation(self):
        """utilizing dictionary and attributes to make letter of appreciation"""
        full_name = self.first_name + " " + self.last_name
        information_about_employee1 = {'company_position': 'tufting operator', 'years_of_service': '5 years'}
        message = full_name.title() + ", you have spent " + information_about_employee1[
            'years_of_service'] + " of service to our company as a " + information_about_employee1[
                      'company_position'] + " and we are incredibly grateful to have had your loyalty and talent throughout the years. Thank you!"

        print(message)

employee_1_letter = EmployeeAppreciation('sarah', 'mendoza')
employee_1_letter.code_of_appreciation()