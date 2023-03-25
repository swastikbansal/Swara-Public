import mysql.connector
from tkinter import messagebox

class Database:
    #Checking Connection with Database
    try:
        mycon = mysql.connector.connect(
                host = "bdviswxznb9a4x9gntyw-mysql.services.clever-cloud.com",
                user = "umi4t5ojvgegwvre",
                password = "v7eLTxeCKFcIibZv0dFN",
                database = "bdviswxznb9a4x9gntyw"
        )

        mycon.autocommit = True

        # Creating an Object for working in Database
        cur = mycon.cursor()
    
        #If Connection is Successfull 
        if mycon.is_connected(): 
                messagebox.showinfo("Connection Successfull","Connected to database Successfully.")


    #If Connection is Unsuccessful        
    except mysql.connector.Error:
            messagebox.showerror("Connection Failed","We can't connect to database at this movemnt.\nPlease Try Again Later.")
            quit()
        
    
    #Function for Logging In User
    def login(self,userEntry,passEntry,func):
            
            #Getting Username And Password entered
            self.password = passEntry.get()
            self.username = userEntry.get()

            self.cur.execute("SELECT Username,Password FROM users")
            self.dataRetrieved=self.cur.fetchall()       #Storing username and password from database

            #Condition for Empty Entry Box
            if self.username == "" or self.password == "":
                    messagebox.showerror("No Data Entered","Please fill all the fields!")

            else:
                    #Correct Creditionals
                    if (self.username,self.password) in self.dataRetrieved:
                            messagebox.showinfo("Success","You have Logged In Successfully.")
                            func()               
                    #Incorrect Creditionals                         
                    else:
                            messagebox.showerror("User not found","Username or Password is Incorrect") 
    
    #Function for Checking New Users Email Id And Password
    def regCheck(self,mobileEntry,emailEnrtry,func):

        self.cond = True

        #Getting Mobile No. and Email Id entered
        self.mobile_no = mobileEntry.get()
        self.email = emailEnrtry.get()

        #Getting data from Table 
        self.cur.execute("SELECT Mobile_no,Email FROM users")
        self.data = self.cur.fetchall()

        #Checking Details
        
        #Empty Fields
        if self.mobile_no == "" or self.email == "" :
             messagebox.showerror("Empty Feilds","Please fill all the feilds")

        #Invalid Input of Mobile No.
        else:
            if self.mobile_no.isdigit() == False:
                messagebox.showerror("Invalid Input","Please Enter Valid Mobile No. \nIn Digits")

            elif len(self.mobile_no) != 10:
                messagebox.showerror("Invalid Input","Please Enter Valid Mobile No. \nIt should be of 10 digits  ")
            
            #If Mobile No. satisfies the above conditons
            else:
                for current in self.data:
                    #Mobile No and Email both exists
                    if (self.mobile_no in current) and (self.email in current):
                        messagebox.showerror("Already Exists","Email and Phone alread exist")
                        self.cond = False

                    #Only Email Exists
                    elif (self.mobile_no not in current) and (self.email in current):
                        messagebox.showerror("Already Exists","Email Already Exists")
                        self.cond = False

                    #Only Mobile No. Exists
                    elif (self.mobile_no in current) and (self.email not in current):
                        messagebox.showerror("Already Exists","Mobile No. Already Exists")
                        self.cond = False
    
                    #Enabling the disaled Entries after verification is complete
                    else:
                        self.cond = True

            #If Cond is returned True            
            if self.cond == True :
                func()
    
    #Function for Uploading/Sumbitting details on Database 
    def regSumbit(self, win, emailEntry, mobileEntry, usernameEntry, passwordEntry, firstNameEntry ,lastNameEntry ,dobEntry):
        #Getting all the detaila from entrybox
        self.newUser = usernameEntry.get()
        self.firstName = firstNameEntry.get()
        self.lastName = lastNameEntry.get()
        self.newMobile = mobileEntry.get()
        self.newEmail = emailEntry.get()
        self.newPass = passwordEntry.get()
        self.dob = dobEntry.get()
        
        #Checking for empty fields
        if (self.newUser == "" or self.firstName == "" or self.lastName == "" or self.newMobile == "" or self.newEmail == "" or self.newPass == "" or self.dob == ""):
             messagebox.showerror("Empty Feilds","Please fill all the Feilds")
        
        else :
            self.newMobile = int(self.newMobile) 
            self.cur.execute("SELECT Username FROM users")
            self.data = self.cur.fetchall()
            
            #Checking Username And Name 
            if self.newUser not in self.data:

                #Checking Password Length
                if len(self.newPass) < 6 :
                    messagebox.showerror("Short Password","Password should have length greater than 6.") 

                else:    
                    #Uploading Data
                    if self.firstName.isalpha() and self.lastName.isalpha() :
                        self.cur.execute(f"INSERT INTO users (Username,F_name,L_name,Mobile_no,Email,Password,DOB) VALUES('{self.newUser}','{self.firstName}','{self.lastName}','{self.newMobile}','{self.newEmail}','{self.newPass}','{self.dob}')")            
                        win.destroy()
                        messagebox.showinfo("Registration Successfull","You Have Registered Successfully ...")
                        

                    else:
                        messagebox.showerror("Invalid Input","Please Input First Name and Last Name in Alphabetical form.")
            
            else:
                messagebox.showerror("Data Conflict","Username Already Exists.")
 
