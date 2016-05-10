# Created by :          John Mezzanotte
#                       jmezzanotte@air.org
#                       650-843-8125(office)
# Date-last-Modified:   7-29-15
# Purpose:              Create fake student names and id for use
#                       with the early warning system. This program generates
#                       fake date customized exclusively for the EWS tool. It
#                       will generate demographic data and contact information
#                       specific to database attributes in the EWS System.
#
# Use:                  Create and instance of the CreateData class and provide
#                       it one argument, which is the number of records to include
#                       in your fake data file.
#
#                       After the data has been created you have to write that
#                       data to file. That can be done through two methods
#
#                       To write Demographic variables make a call to
#                       write_personal_vars(). This will generate a CSV file
#                       in your current working directory
#
#                       To write contact infornmation for students make a call
#                       to write_contacts(). This will generate a CSV file
#                       in your current working directory
#
#                       For each instance of the the CreateData class, a student
#                       id that is unique is generated and maintained between
#                       demographic and contacts files. You can import these
#                       files into the EWS separately, or you can merge them
#                       together in excel.
#



import os
import platform
import random
from datetime import datetime

# https://github.com/joke2k/faker
# faker is a python package that generates fake data for you
from faker import Factory

class CreateData( object ):
    """ Creates fake data for import into the EWS tool. Enter the number of cases you want in the data. Returns fake data

    Constructor arguments:
    data_size -- the number of records in teh data set

    
    """

    def __init__(self, data_size):
        self.f_name = ['FirstName']
        self.l_name = ['LastName']
        self.grade = ['Grade']
        self.dob = ['DateOfBirth']
        self.ethnicity = ['RaceEthnicity']
        self.disability = ['Disability']
        self.disadvantaged = ['Disadvantaged']
        self.ell = ['ELL']
        self.grouping = ['GroupingVar']
        self.parent1_f_name = ['Parent1FirstName']
        self.parent1_l_name = ['Parent1LastName']
        self.parent2_f_name = ['Parent2FirstName']
        self.parent2_l_name = ['Parent2LastName']
        self.sid = ['StudentId']
        self.gender = ['Gender']
        self.email1 = ['Email1']
        self.email2 = ['Email2']
        self.parent_email1 = ['Parent1Email']
        self.parent_email2 = ['Parent2Email']
        self.city = ['City']
        self.state = ['State']
        self.street = ['Address1']
        self.zip = ['Zipcode']
        self.phone1 = ['Phone1']
        self.phone2 = ['Phone2']
        self.parent_phone1 = ['Parent1Phone']
        self.parent_phone2 = ['Parent2Phone']
        
        self.data_size = data_size
    

    def set_birth_date(self, start_year, end_year, start_month=1, end_month=12, start_day=1, end_day=28):   
    
        for i in range( 1, self.data_size + 1 ):
            year = random.randint( start_year, end_year )
            month = random.randint( start_month, end_month )
            day = random.randint( start_day, end_day )
            birth_date =  str(month) + "/"  + str(day) + "/" + str(year)  

            self.dob.append(birth_date)

    def set_first_name(self):

        fake = Factory.create()
        for i in range( 1, self.data_size + 1 ):
            # hold first name in a temp var
            temp = fake.first_name()
            # encode the name from unicode to ascii 
            self.f_name.append( temp.encode( 'ascii' ) )

    def set_last_name(self):

        fake = Factory.create()
        for i in range(1, self.data_size + 1):

            #hold last name in a temp var
            l_temp = fake.last_name()

            self.l_name.append( l_temp.encode( 'ascii' ) )

    def set_grade(self, low_grade_level=1, high_grade_level=12):
        for i in range( 1, self.data_size + 1 ) :
            self.grade.append(random.randint(low_grade_level, high_grade_level))

    def set_parent_one_first_name(self):
        fake = Factory.create()
        for i in range( 1, self.data_size + 1 ):
            p1_temp = fake.first_name()

            self.parent1_f_name.append( p1_temp.encode( 'ascii' ) )
                
    def set_parent_two_first_name(self):

        fake = Factory.create()
        for i in range( 1, self.data_size + 1 ):
            # hold first name in a temp var
            p2_temp = fake.first_name()

            self.parent2_f_name.append( p2_temp.encode( 'ascii' ) )


    def set_parent_one_last_name(self):
        for i in range( 1, self.data_size + 1 ):
            self.parent1_l_name.append( self.l_name[i] )

    def set_parent_two_last_name(self):
        for i in range( 1, self.data_size + 1):
            self.parent2_l_name.append( self.l_name[i] )

    def set_studentId(self, default=True):

        if default:
            for i in range(1,len(self.f_name)):
                self.sid.append(self.f_name[i][0] + self.l_name[i][0] + "_" + str(i))
        else:
            for i in range(1, self.data_size + 1):
                self.sid.append(i)

    def set_gender(self):    
        gender_temp = [ 'M', 'F' ]
        for i in range( 1, len( self.f_name) ):
            self.gender.append( gender_temp[ random.randint(0, 1) ] )

    def set_email(self):
        for i in range( 1, len( self.f_name ) ):
            self.email1.append( self.f_name[i] + self.l_name[i] + "@testdata.com")

    def set_student_email(self):
         # create a student email
        for i in range( 1, len( self.f_name ) ):
            self.email2.append( self.l_name[i] +  "_altemail@testdata.com" )

    def set_parent_email_1(self):
        # create a parent's email
        for i in range( 1, len( self.f_name ) ):
            self.parent_email1.append( self.parent1_f_name[i] + self.parent1_l_name[i]  + "@testdata.com" )

    def set_parent_email_2(self):  
        # create a parent's email
        for i in range( 1, len( self.f_name ) ):
            self.parent_email2.append( self.parent1_f_name[i] + self.parent1_l_name[i]  + "@testdata.com" )

    def set_city(self):

        fake = Factory.create()
        # Create city data
        for i in range( 1, len( self.f_name ) ):
            temp_city = fake.city()

            self.city.append( temp_city.encode( 'ascii' ) )

    def set_state(self):  
        # Create state data
        for i in range( 1, len( self.f_name ) ):
            self.state.append( "CA" )

    def set_street(self):
        fake = Factory.create()
        # Create data for street name in address
        for i in range( 1, len( self.f_name ) ):
            street_temp = fake.street_address()
             
            self.street.append( street_temp.encode( 'ascii' ) )

    def set_zip(self):
        fake = Factory.create()
        # Create data for zip code in address
        for i in range( 1, len( self.f_name ) ):
            zip_temp = fake.zipcode()
             
            self.zip.append( zip_temp.encode( 'ascii' ) )


    def set_phone1(self):
        fake=Factory.create()
        # Create data for phone
        for i in range( 1, len( self.f_name ) ):
            phone_temp = fake.phone_number()
             
            self.phone1.append( phone_temp.encode( 'ascii' ) )

    def set_phone2(self):
        fake=Factory.create()
        # Create data for phone2
        for i in range( 1, len( self.f_name ) ):
            phone2_temp = fake.phone_number()
             
            self.phone2.append( phone2_temp.encode( 'ascii' ) )
            
    def set_parent1phone(self):
        fake=Factory.create()
        for i in range( 1, len( self.f_name ) ):
            p1phone_temp = fake.phone_number()
             
            self.parent_phone1.append( p1phone_temp.encode( 'ascii' ) )

    def set_parent2phone(self):
        fake=Factory.create()
        for i in range( 1, len( self.f_name ) ):
            p2phone_temp = fake.phone_number()
             
            self.parent_phone2.append( p2phone_temp.encode( 'ascii' ) )

    def set_ethnicity(self, *args):

        # handle variable number of arguments
        ethnicities = args
        
        for i in range(1, self.data_size + 1 ):
            self.ethnicity.append( ethnicities[random.randint(0,len(ethnicities)-1)])

    def set_disability(self, *args):
        disabilities = args

        for i in range(1, self.data_size + 1):
            self.disability.append(disabilities[random.randint(0, len(disabilities)-1)])
            
    def set_ell(self, *args):
        ell_status = args

        for i in range(1, self.data_size + 1):
            self.ell.append(ell_status[random.randint(0, len(ell_status)-1)])

    def set_disadvantaged(self, *args):
        disadv_status = args

        for i in range(1, self.data_size + 1):
            self.disadvantaged.append(disadv_status[random.randint(0, len(disadv_status)-1)])


    def set_grouping_variable(self, *args):
        grouping_var = args

        for i in range(1, self.data_size + 1):
            self.grouping.append(grouping_var[random.randint(0, len(grouping_var)-1)])
    

    # write a set method for each instance variable
    def set_all(self):

        self.set_birth_date(1992, 1993)
        self.set_first_name()
        self.set_grade(9, 12)
        self.set_parent_one_first_name()
        self.set_parent_two_first_name()
        self.set_last_name()
        self.set_parent_one_last_name()
        self.set_parent_two_last_name()
        self.set_studentId()
        self.set_gender()
        self.set_email()
        self.set_student_email()
        self.set_parent_email_1()
        self.set_parent_email_2()
        self.set_city()
        self.set_state()
        self.set_street()
        self.set_zip()
        self.set_phone1()
        self.set_phone2()
        self.set_parent1phone()
        self.set_parent2phone()
        self.set_ethnicity('Native American', 'Hispanic/Latino', 'Asian', 'Hawaiian Pacific Islander', 'African American', 'White')
        self.set_disability('Yes', 'No')
        self.set_ell('Yes', 'No')
        self.set_disadvantaged('Yes', 'No')
        self.set_grouping_variable('Homeroom1', 'Homeroom2', 'Homeroom3', 'Homeroom4', 'Homeroom5', 'Homeroom6')


    def write_personal_vars(self):
        # ask the user for a file name

        self.set_all()
       
        self.file_name = raw_input( 'please enter a file name for the personal data file: ' )

                
        try:
            f = open( os.getcwd() + "\\" + self.file_name, 'w' )

            for i in range( 0, len( self.f_name) ):
                # you could also use a join command here
                f.write( self.sid[i] + "," + self.f_name[i] + "," + self.l_name[i] + "," +
                         str(self.grade[i]) + "," +  self.dob[i] + "," + self.gender[i] + "," +
                         self.ethnicity[i] + "," + self.disability[i] +  "," + self.disadvantaged[i] + "," +
                         self.ell[i] + "," + self.grouping[i] + "\n" )

            f.close()
            
        except :
            print "file could not be found or read."
            f.close()
        else:
           print "file created successfully and stored here: " + os.getcwd()


    def write_contacts( self ):
        """ Returns a comma separated file that can be imported as a CSV into excel """
        
        # ask the user for a file name
        self.file_name = raw_input( 'please enter a file name for the contancts: ' )

        
        try:
            f = open( os.getcwd() + "\\" + self.file_name, 'w' )

            for i in range( 0, len( self.f_name) ):
                f.write( self.sid[i] + "," + self.street[i] + "," + self.city[i] +
                     "," + self.state[i]+ "," + self.zip[i] + "," + self.phone1[i] +
                     "," +  self.phone2[i] + "," + self.email1[i] +  "," + self.email2[i] +
                     "," + self.parent1_f_name[i] + "," + self.parent1_l_name[i] + "," +
                     self.parent_phone1[i] + "," + self.parent_email1[i] + "," +
                     self.parent2_f_name[i] + "," + self.parent2_l_name[i] + "," +
                     self.parent_phone2[i] + "," + self.parent_email2[i] + "\n" )


            f.close()
            
        except:
            print "file could not be found or read"
            f.close()
        else:
            print "file created successfully and stored here: " + os.getcwd()

    def write(self):
        # ask the user for a file name

        self.set_all()
       
        self.file_name = raw_input( 'please enter a file name for the data: ' )
      
        try:
            f = open( os.getcwd() + "\\" + self.file_name, 'w' )

            for i in range( 0, len( self.f_name) ):
                # you could also use a join command here
                f.write( self.sid[i] + "," + self.f_name[i] + "," + self.l_name[i] + "," +
                         str(self.grade[i]) + "," +  self.dob[i] + "," + self.gender[i] + "," +
                         self.ethnicity[i] + "," + self.disability[i] +  "," + self.disadvantaged[i] + "," +
                         self.ell[i] + "," + self.grouping[i] + self.street[i] + "," + self.city[i] +
                         "," + self.state[i]+ "," + self.zip[i] + "," + self.phone1[i] +
                         "," +  self.phone2[i] + "," + self.email1[i] +  "," + self.email2[i] +
                         "," + self.parent1_f_name[i] + "," + self.parent1_l_name[i] + "," +
                         self.parent_phone1[i] + "," + self.parent_email1[i] + "," +
                         self.parent2_f_name[i] + "," + self.parent2_l_name[i] + "," +
                         self.parent_phone2[i] + "," + self.parent_email2[i] + "\n" )

            f.close()
            
        except :
            print "file could not be found or read."
            f.close()
        else:
           print "file created successfully and stored here: " + os.getcwd()
            

if __name__ == "__main__":

    # Create an instance of CreateData class
    test1 = CreateData( 700 )

    test1.write_personal_vars()
    test1.write_contacts()
    # test1.write_contacts()



    
    
    


    
        
            
        
        
         
        
        
        
