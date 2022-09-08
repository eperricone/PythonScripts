class Conduct():

    def __init__(self, name, gender, violation):
        """Initialize name, gender, and violation"""
        self.violation = violation
        self.name = name
        self.gender = gender

    def CodeOfConduct(self):
        """Function for suspicion of a code of conduct violation and actions following specific violations"""
        print( self.name + " is a " + self.gender + " that is under suspicion of a " + self.violation)
        if self.violation == 'hate crime':
            print( "If found guilty. Please terminate " + self.name + " immediately!")
        elif self.violation == 'bullying act':
            print("If found guilty. Please terminate " + self.name + "immediately!")



mohawk_employee = Conduct('David', 'male', 'hate crime')
mohawk_employee.CodeOfConduct()
