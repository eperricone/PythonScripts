class GeneralMachineryForIndustries:
    """Utilizing general branch of class to institute a general time frame for inspections"""


    def __init__(self, plant):
        """Initializing plant attribute and standard time frame"""
        self.standard_inspection_time_in_days = 7
        self.plant = plant

class AladdinPlantMachinery(GeneralMachineryForIndustries):
    """Creating class specifically for plant name: Aladdin"""


    def __init__(self, plant):
        """Ensuring python attain attributes from general machinery class"""
        super(). __init__(plant)

    def ap_inspection_time(self):
        """Creating parameters for all Aladdin machinery"""

        if self.plant == "machine_x_for_ap":
            ap_time = self.standard_inspection_time_in_days - 2
            print("The inspection time for this 'ap' machine is " + str(ap_time) + " days.")

        if self.plant == "machine_y_for_ap":
            ap_time = self.standard_inspection_time_in_days -3
            print("The inspection time for this 'ap' machine is " + str(ap_time) + " days")

        else:
            ap_time = self.standard_inspection_time_in_days
            print("The inspection time for this 'ap' machine is " + str(ap_time) + " days")

class Antioch(GeneralMachineryForIndustries):
    """Creating class for machinery at plant: Antioch"""


    def __init__(self, plant):
        """Ensuring python attain attributes from general machinery class"""
        super(). __init__(plant)

    def an_inspection_time(self):
        """Creating parameters for all machinery in Antioch"""
        if self.plant == "machine_x_for_an":
            an_time = self.standard_inspection_time_in_days - 3
            print("The inspection time for this 'an' machine is " + str(an_time) + " days")
        else:
            an_time = self.standard_inspection_time_in_days
            print("The Inspection time for this 'an' machine is " + str(an_time) + " days.")


#these are sets of examples for machines in wide variety of plants
inspection_1 = AladdinPlantMachinery("machine_x_for_ap")
print(inspection_1.ap_inspection_time())

inspection_2 = AladdinPlantMachinery("machine_y_for_ap")
print(inspection_2.ap_inspection_time())

inspection_3 = AladdinPlantMachinery("general_machinery_for_ap")
print(inspection_3.ap_inspection_time())

inspection_4 = Antioch("machine_x_for_an")
print(inspection_4.an_inspection_time())

inspection_5 = Antioch("general_machinery_for_an")
print(inspection_5.an_inspection_time())




