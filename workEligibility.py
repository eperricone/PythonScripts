class WorkEligibility:
    """Creating program to instruct potential applicants of said company, over eligibility of application"""
    def __init__(self, first_name, company_name, position_name):
        """Initializing attribiutes"""
        self.first_name = first_name
        self.company_name = company_name
        self.position_name = position_name

    note = "Applicant are required to have a 4 year degree or 3 years of experience to apply for position."
    print(note)

    def questionnaire(self):
        """Input function created to interact with user. Program will procede to tell user about eligibility of application"""
        prompt_1 = "Do you have a 4 year degree?"
        prompt_1 += "\n(Enter 'Yes' or 'No' to question)"
        prompt_2 = "Do you have 3 years of work experience?"
        prompt_2 += "\n(Enter 'Yes' or 'No' to question)"
        output = input(prompt_1) and input(prompt_2)
        if output == 'Yes':
            print("Congratulations " + self.first_name.title()+ " you are eligible to apply at " +
                  self.company_name.title() + " for the position of " + self.position_name.title() + "!")
        else:
            print("I'm sorry " + self.first_name.title() +  " you are currently ineligible to apply for " +
                  self.company_name.title() + " for the position of " + self.position_name.title() + " at this time.")

potential_hire = WorkEligibility('jim', 'mohawk', 'chemical engineer')
potential_hire.questionnaire()





