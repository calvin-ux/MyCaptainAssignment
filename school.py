# -*- coding: utf-8 -*-
"""
School Administration Progeam
@author: Calvin
"""
import csv

#function to write into csv
def write_into_csv(info_list):
    with open('student_info.csv', 'a', newline='') as csv_file:
        #writer object
        writer = csv.writer(csv_file)
       
        #header check and header 
        if csv_file.tell() == 0:
            writer.writerow(["Name","Age","Contact Number","E-mail ID"]) 
        #observation
        writer.writerow(info_list)
        
        

#enclosed function(everything into a main)        
if __name__ == '__main__':
    #entry point line by line 1st
    condition  = True
    
    student_num = 1
    
    #while loop to keep enter student info till cond. changes
    while(condition):
        student_into =  input("Enter student infomation for student #{} in the following format (Name Age Contact_Number E-mail_ID): ".format(student_num))
        print("Entered information: " + student_into)
        
        # split large string into small strings
        student_into_list =  student_into.split(' ')
        #single ( ) space split
        print("Entered split up information is:: " + str(student_into_list))
        
        
        print("\nThe entered information is -\nName: {}\nAge :{}\nContact_Number: {}\nE-mail ID: {}"
              .format(student_into_list[0], student_into_list[1], 
                      student_into_list[2], student_into_list[3]))
         
        #ask user
        choice_check = input("Is the entered information correct? (y/n): ")
        #writes into loop again
        if choice_check == "y":
            write_into_csv(student_into_list)
            
            #another set of input
            condition_check = input("Enter (y/n) if you want to enter information for another student: ")
            if condition_check == "y":     # y jumps to start of loop and enter info
                condition = True
                student_num = student_num + 1 #only place user is happy and they cont 
            elif condition_check == "n":   # n programs ended
                condition = False   
        #breaks out of the loop        
        elif choice_check == "n":
            print("\nPlease re-enter the values: ")
        
            
            
    
            
