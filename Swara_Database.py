import mysql.connector
from tkinter import messagebox

#Main Function for the main File 
def database(userEntry,passEntry,func):
    #Getting Username Ans Password entered
    username = userEntry.get()
    password = passEntry.get()
    
    #Establishing Connection with database
    global cur
    mycon = mysql.connector.connect(
            host = "bdviswxznb9a4x9gntyw-mysql.services.clever-cloud.com",
            user = "umi4t5ojvgegwvre",
            password = "v7eLTxeCKFcIibZv0dFN",
            database = "bdviswxznb9a4x9gntyw"
        )

    cur = mycon.cursor()   # Creating an Object for working in Database

    #If Connection is Succesfull 
    if mycon.is_connected(): 
        messagebox.showinfo("Connection Successfull","Connected to database Successfully.")

        login(username,password,func)

    #If Connection is unsuccessful        
    else:
        messagebox.showerror("Connection Failed","We can't connect to database at this movemnt.\nPlease Try Again Later.")

#Function for logging in user
def login(username,password,func):
        cur.execute("SELECT Username,Password FROM users")
        data_retrieved=cur.fetchall()       #Storing username and password from database
        
        #Condition for empty Entry boxes
        if username=="" or password=="":
            messagebox.showerror("No Data Entered","Please fill all the fields!")
        
        else:
            #Correct Creditionals
            if (username,password) in data_retrieved:
                messagebox.showinfo("Success","You have Logged In Successfully.")
                func()

            #Incorrect Creditionals                         
            else:
                messagebox.showerror("User not found","Username or Password is wrong") 