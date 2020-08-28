def demographics():
    first_name = input('Enter the first name:')
    last_name = input('Enter the last name:')
    date_of_birth = input('Enter the Date of birth:')
    return first_name,last_name,date_of_birth

class Student:
    student_count = 0

    def __init__(self, first_name,last_name,date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.student_count = self.student_count + 1

    def uc_6_2(self):
        last_name_length = len(self.last_name)
        final_result = "";
        if last_name_length > 6:
            final_result = self.last_name[0:6]
        else:
            final_result = self.last_name
            rem_length = 6 - last_name_length
            final_result = final_result + self.first_name[0:rem_length]
        final_result = final_result + self.first_name[0] + self.first_name[len(self.first_name) - 1]
        return (final_result)

    def student_number(self):
        return self.date_of_birth + " "+ str(self.student_count)

    def student_id(self):
        return self.uc_6_2()