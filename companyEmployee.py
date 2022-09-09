class Company_employees():
    """creating a welcoming entry for mohawk employees"""

    def __init__(self, name, gender):
        """Initializing name and ages of employees"""
        self.name = name
        self.gender = gender


    def greetings(self):
        """starting greeting function for applicant"""
        print("Hello " + self.name + " so nice to meet you! Welcome to Mohawk")
        if self.gender == "female":
            print("Mohawk has some of the most world renowned female scholars! " +
                  "We are so happy for you to be apart of this team!")


new_hire = Company_employees('maria', 'female')
new_hire.greetings()


