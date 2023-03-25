# Libraries for creating GUI
from tkinter import *
from tkinter import filedialog
from tkcalendar import *

# Canvas For imposing matplotlib graph and toolbar with tkinter gui.
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg , NavigationToolbar2Tk 

# Libraries for recording voice and processing
import pyaudio
import wave
import os

# Importing Custom Files
import Swara_Backend
import Swara_Database

#Functionality Class

class Functionality: 
    #Function for clearing Win

    def clearWin(self,window):
        for widgets in window.winfo_children():
            widgets.destroy()

    #Function for taking File Input 
    def fileInput(self,win,evar,b_x,b_y):
            self.file = filedialog.askopenfile(mode='r', filetypes=[('Music Files', '*.wav')])
            
            if self.file:
                    self.filePath = os.path.abspath(self.file.name)
                    self.path = self.filePath
                    self.fileLocationEntry = Entry(win ,textvar = evar,font = "raleway 10 bold", bg="#1b191a",bd = 0,width = 200)
                    self.fileLocationEntry.delete(first = 0,last = 500)
                    self.fileLocationEntry.insert(0,f"{self.filePath}")
                    self.fileLocationEntry.config(state = "disabled")
                    self.fileLocationEntry.place(x = b_x, y = (b_y + 30))                        
                    return self.path

    #Function for recording Audio
    def recording(self,win,invervalSecEntry):
        self.sec = invervalSecEntry.get()
        self.FRAMES_PER_BUFFER = 3200
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1   
        self.RATE = 16000

        # Calling Python library to record audio
        self.audio = pyaudio.PyAudio()

        self.record = self.audio.open(
                format=self.FORMAT,
                channels=self.CHANNELS,
                rate=self.RATE,
                input=True,
                frames_per_buffer=self.FRAMES_PER_BUFFER
        )
        
        # Creates a label when recording completes.
        self.ch2 = Label(win , text= "Your voice is Recorded!" ,bg = "#141a1a" , fg="#f3b32d" ,font= ("Posterama  16 bold"))
        self.ch2.place(x= 140 , y = 220)

        # Defines recording interval by taking input from user.
        self.seconds = float(self.sec)
        self.frames = []
        self.second_tracking = 0
        self.second_count = 0
        for i in range(0, int(self.RATE/self.FRAMES_PER_BUFFER*self.seconds)):
                self.ch3 = Label(win, textvariable = f'Time Left: {self.seconds - self.second_count} seconds' , bg="#1b191a")
                self.ch3.place(x= 30 , y = 130)
                self.data = self.record.read(self.FRAMES_PER_BUFFER)
                self.frames.append(self.data)
                self.second_tracking += 1
                self.second_count += 1


        self.record.stop_stream()
        self.record.close()
        self.audio.terminate()

        # Stores recorded audio file.

        specimen = wave.open('Audio/user.wav', 'wb')
        specimen.setnchannels(self.CHANNELS)
        specimen.setsampwidth(self.audio.get_sample_size(self.FORMAT))
        specimen.setframerate(self.RATE)
        specimen.writeframes(b''.join(self.frames))
        specimen.close()

# Button bg - #141a1a (Lighter Black)
# Button Text - deeppink 
# bg - #1b191a (Black)
# fontcolour - #f3b32d (Golden Colour)

#-------------------- Login Win -------------------- #

def loginWin():
        functionality.clearWin(winRoot)

        winRoot.geometry("260x200")
        winRoot.config(bg = "#1b191a")

        #Login Win Header Frame
        loginHeaderFrame = Frame(winRoot, bg="#1b191a",bd = 2)
        loginHeaderFrame.pack(side=TOP, fill = X)

        #Login Label
        loginLabel = Label(loginHeaderFrame, text="LOGIN" ,bg="#1b191a", fg = "#f3b32d", font= ("Posterama  20 bold"), padx = 200 , pady = 10)
        loginLabel.pack()

        #User
        user = Label(winRoot , text= "Username ID  :   ", bg="#1b191a" , fg="#f3b32d")
        user.place(x= 30 , y = 58)

        userEntry = Entry(winRoot , textvariable =userValue )
        userEntry.place(x=120, y = 58)

        #Password
        password = Label(winRoot , text= "Password : ", bg="#1b191a" , fg="#f3b32d")  
        password.place(x = 30,y=80)

        passEntry = Entry(winRoot , textvariable = passValue, show = "*")
        passEntry.place(x=120 ,y = 80)
        
        #Login Button
        login = lambda:database.login(userEntry,passEntry,chooseWin)  
        closeButton = Button(winRoot, fg="deeppink", bg = "#141a1a", text = "Login"  ,font = "raleway 12 bold", command = login) #Checks and verify the login details
        closeButton.place(x = 160, y = 130)

        #Create User Button
        createUserButton = Button(winRoot,fg = "deeppink",bg = "#141a1a", text = "Sign - Up", font = "raleway 12 bold" ,command= createUserWin)
        createUserButton.place(x = 30, y = 130)


#----------------------------Sign Up window----------------------#

def createUserWin():

    global signUpWin

    #Window Properties
    signUpWin = Toplevel(winRoot)
    signUpWin.geometry("410x500")
    signUpWin.resizable(False,False)
    signUpWin.title("Sign - Up")    
    signUpWin.configure(bg="#1b191a")  
    signUpWin.grab_set()

    #Heading Frame
    signUpHeaderFrame = Frame(signUpWin , bg="#1b191a" ,bd=10)
    signUpHeaderFrame.grid(row=0,column=0)
    createAccountLabel = Label(signUpHeaderFrame ,text="Create Account",font=("Times 20 bold") , bg="#1b191a" , fg="#f3b32d")
    createAccountLabel.grid(padx=100,pady=2)

    #Details Frame
    detailsFrame = Frame(signUpWin , bg="#1b191a")
    detailsFrame.grid(row=1,column=0)

    #Mobile No.
    mobileNumberLabel = Label(detailsFrame,text="Mobile Number : " , bg="#1b191a" , fg="#f3b32d")      
    mobileNumberLabel.grid(row=0,column=0,padx=5,pady=10)
    userCreateMobile.set("")
    
    mobileNumberEntry = Entry(detailsFrame,width=20,justify="center",textvariable=userCreateMobile)
    mobileNumberEntry.config(state="normal")
    mobileNumberEntry.grid(row=0,column=1)

    #E-mail
    emailLabel= Label(detailsFrame,text="Email Address : " , bg="#1b191a", fg="#f3b32d")
    emailLabel.grid(row=1,column=0,padx=5,pady=10,sticky='w')
    userCreateEmail.set("")
    
    emailEntry= Entry(detailsFrame,width=20,justify="center",textvariable=userCreateEmail)
    emailEntry.config(state="normal")
    emailEntry.grid(row=1,column=1)

    #Function for Enabling Rest of the Entry boxes
    def enableEntry():
        firstNameEntry.config(state = "normal")
        lastNameEntry.config(state = "normal")
        usernameEntry.config(state = "normal")
        passwordEntry.config(state = "normal")
        choose.config(state = "normal")
        sumbitButton.config(state = "normal")
        # checkButton.destroy()

    #Check Button
    checkCmd = lambda : database.regCheck(mobileNumberEntry,emailEntry,enableEntry)
    checkButton = Button(detailsFrame,text="Check", command = checkCmd ,bg = "#141a1a",  fg="deeppink" ,  font= ("times  10 bold"))
    checkButton.grid(row=1,column=2,padx=10)
    
    #Username
    usernameLabel = Label(detailsFrame,text="Username : " , bg="#1b191a", fg="#f3b32d")
    usernameLabel.grid(row=2,column=0,padx=5,pady=10,sticky='w')
    userCreateUsername.set("")
    
    usernameEntry = Entry(detailsFrame,width=20,justify="center",textvariable=userCreateUsername)
    usernameEntry.grid(row=2,column=1)
    usernameEntry.config(state="disabled")

    #Password
    passwordLabel = Label(detailsFrame,text="Password : " , bg="#1b191a" , fg="#f3b32d")
    passwordLabel.grid(row=3,column=0,padx=5,pady=10,sticky='w')
    userCreatePassword.set("")
    
    passwordEntry = Entry(detailsFrame,width=20,justify="center",show = "*",textvariable=userCreatePassword)
    passwordEntry.grid(row=3,column=1)
    passwordEntry.config(state="disabled")

    #First Name
    firstNameLabel = Label(detailsFrame,text="First Name : " , bg="#1b191a" , fg="#f3b32d")
    firstNameLabel.grid(row=4,column=0,padx=5,pady=10,sticky='w')
    userCreateFirstName.set("")
    
    firstNameEntry = Entry(detailsFrame,width=20,justify="center",textvariable=userCreateFirstName)
    firstNameEntry.grid(row=4,column=1)
    firstNameEntry.config(state="disabled")

    #Last Name
    lastNameLabel = Label(detailsFrame,text="Last Name : " , bg="#1b191a" , fg="#f3b32d")
    lastNameLabel.grid(row=5,column=0,padx=5,pady=10,sticky='w')
    userCreateLastName.set("")
    
    lastNameEntry = Entry(detailsFrame,width=20,justify="center",textvariable=userCreateLastName)
    lastNameEntry.grid(row=5,column=1)
    lastNameEntry.config(state="disabled")

    #DOB
    dobLabel = Label(detailsFrame,text="Date Of Birth : " , bg="#1b191a" , fg="#f3b32d")
    dobLabel.grid(row=6,column=0,padx=5,pady=10,sticky='w',columnspan=2)
    
    dateLabel = Label(detailsFrame , bg="#1b191a")
    dateLabel.grid(row=6,column=1,padx=5,pady=10)
    userCreateDOB.set("")          

    #Function for Choosing Date
    def choose_date():
        datePicker = Toplevel(signUpWin)
        datePicker.resizable(False,False)
        datePicker.title("Date Picker")
        datePicker.grab_set()
        dobEntry = Calendar(datePicker,selectmode='day',year=2000,month=1,day=1)                
        dobEntry.pack()

        #Function for Saving chosen Date
        def picked():
            dateLabel.config(text=dobEntry.get_date(), fg="#f3b32d")
            userCreateDOB.set(dobEntry.get_date())                    
            datePicker.destroy()
        
        #Ok Button
        ok = Button(datePicker,text="OK",bd=5,command=picked , fg= "deeppink" ,bg = "#141a1a")
        ok.pack(pady=10)           

    #Choose Button
    choose = Button(detailsFrame,text="Choose Date",command=choose_date, bg = "#141a1a", fg="deeppink", font= ("times  10 bold"))
    choose.grid(row=6,column=2)
    choose.config(state="disabled")
    choose.config(state="disabled")

   
    #Sumbit Button
    submit = lambda : database.regSumbit(signUpWin, userCreateEmail, userCreateMobile,userCreateUsername,userCreatePassword,userCreateFirstName,userCreateLastName,userCreateDOB ) 
    sumbitButton = Button( signUpWin , text="SUBMIT",width=10,bd=6,font= ("Posterama  20 bold"), command = submit , fg = "deeppink", bg = "#141a1a")
    sumbitButton.config(state="disabled")
    sumbitButton.place(x=100 , y=360)


    #Function for going back to Login Win
    def back():
        signUpWin.destroy()

    #Back Button
    backCreateUserButton = Button(signUpWin ,text="<--- Go Back to Login",bd=6,command=back , fg = "deeppink" ,bg = "#141a1a")
    backCreateUserButton.place( x= 6 , y= 450 )


#-----------------Choose option window---------------#

def chooseWin():

        global commandWin

        #Command Window Properties
        commandWin = Toplevel(winRoot)
        commandWin.grab_set() 
        commandWin.configure(bg="#1b191a")
        commandWin.resizable(False,False)
        commandWin.title("Option Window")
        commandWin.geometry("280x200")

        #Command Win Header Frame
        recordHeaderFrame=Frame(commandWin, bg="#1b191a" )
        recordHeaderFrame.pack(side=TOP, fill = X)

        #Command Label
        recordLabel=Label(recordHeaderFrame, text="COMMAND" ,bg="#1b191a", fg="#f3b32d", font= ("Posterama  20 bold"), padx = 200 , pady= 20)
        recordLabel.pack()
        
        #Upload Button
        uploadCndButton = Button(commandWin, fg="deeppink" , bg = "#141a1a" ,text = "Upload File", font = " raleway 12 bold" , command = fileWin)
        uploadCndButton.place(x = 20, y = 90)

        #Record Button
        recordCndButton = Button(commandWin , fg="deeppink",  bg = "#141a1a", text = "Record Audio"  ,font = "raleway 12 bold", command = recordWin )
        recordCndButton.place(x = 140, y = 90)

        #Function for going back to Login Window

        def back():
                commandWin.destroy()

        #Back Button
        backChooseButton=Button(commandWin, text="<--- Go Back to Login",bd=6,command=back , fg="deeppink",  bg = "#141a1a")
        backChooseButton.place(x=6 , y=160 )  


#-----------------Record audio window---------------#

def recordWin():
    
    global recordingWin
    global orgFileLoc
    global userFileLoc

    userFileLoc = ""

    #Record Win Configurations
    recordingWin = Toplevel(commandWin) 
    recordingWin.grab_set()
    recordingWin.geometry("520x450")
    recordingWin.configure(bg="#1b191a")
    recordingWin.resizable(False,False)
    recordingWin.title("Record Audio")

    # User Recorded file path
    cwd = os.getcwd()
    userFileLoc = cwd + r"\Audio\user.wav"


    #Command Win Header Frame
    recordHeaderFrame=Frame(recordingWin, bg="#1b191a" )
    recordHeaderFrame.pack(side=TOP, fill = X)
        
    #Command Label
    recordLabel=Label(recordHeaderFrame, text="Record Audio" ,bg="#1b191a", fg="#f3b32d", font= ("Posterama  25 bold"), padx = 200 , pady= 10)
    recordLabel.pack()

    # Original File upload label
    orgRecFileLabel = Label(recordingWin , text= "Original File : " , bg="#1b191a",  fg="#f3b32d", font= ("Posterama  12 bold"))
    orgRecFileLabel.place(x= 20 , y= 80)
    orgRecFileLoc = functionality.fileInput(recordingWin,orgFileLocEntry,20,80)
    orgRecFileButton = Button(recordingWin , bg = "#141a1a" , fg= "deeppink",  text= "Browse",command = orgRecFileLoc)#(120,140))
    orgRecFileButton.place(x= 165 , y= 80)
    
    #Interval input label
    invervalLabel = Label(recordingWin , text= "Enter recording interval : \n(in Seconds)  " , fg="#f3b32d", bg="#1b191a",  font= ("Posterama  12 bold"))
    invervalLabel.place(x= 35 , y= 150)

    # Interval input entry box
    invervalSecEntry = Entry(recordingWin,font = "Posterama 15 bold", width = 10)
    invervalSecEntry.place(x= 260 , y= 150)
    

    # Record Audio button
    recordButton = Button(recordingWin, text="Record Audio",bg = "#141a1a" , fg= "deeppink"  , command= lambda : functionality.recording(recordingWin,invervalSecEntry) , font = " arial 15 bold", width = 14, height= 2,
                relief = RAISED) 
    recordButton.place(x=170 , y=260)

    # Plot and compare button
    nextButton = Button(recordingWin, text ="Plot and Compare", command=graphWin ,font = " arial 15 bold", width = 16, height= 2
                , bg = "#141a1a" , fg= "deeppink"  , relief = RAISED )
    nextButton.place(x= 160 , y= 350)
    
    #Function for going back to Command Window
    def back():
        recordingWin.destroy()
        
    #Back Button
    backRecButton=Button(recordingWin ,text="<--- Go Back", bg = "#141a1a" , fg= "deeppink" ,bd=6,command=back )
    backRecButton.place(x= 10 , y=400)
  

#------------------ File Input Win -------------------#

def fileWin():

        global fileInputWin

        #File Input Win Configuration        
        fileInputWin = Toplevel(commandWin)
        fileInputWin.grab_set() 
        fileInputWin.configure(bg="#1b191a")
        fileInputWin.resizable(False,False)
        fileInputWin.title("File Input")
        fileInputWin.geometry("600x270")
        
        # Defining file path variables
        global userFileLoc
        global orgFileLoc

        #File Header Frame
        fileHeaderFrame=Frame(fileInputWin, bg ="#1b191a" )
        fileHeaderFrame.pack(side=TOP, fill = X)

        #Header Text
        fileHeaderLabel=Label(fileHeaderFrame, text="File Input" ,bg="#1b191a", fg="#f3b32d",
                          font= ("Posterama  20 bold"), padx = 200 , pady = 10)
        fileHeaderLabel.pack()

        #Instruction Text
        instructionLabel = Label(fileInputWin,text="Input your recorded music file and Original Music File Here.",
                        bg="#1b191a" , fg="#f3b32d", font = ("Posterama  12 bold") )
        instructionLabel.pack()

        #User File
        userFileLabel = Label(fileInputWin , text= "Recorded File :   " , bg="#1b191a" , fg="#f3b32d",  font= ("times  12  bold"))
        userFileLabel.place(x= 30 , y = 85)
        userFileButton = Button(fileInputWin ,bg = "#141a1a", fg="deeppink" , text= "Browse",command=lambda : functionality.fileInput(fileInputWin,userFileLocEntry,30,85))
        userFileLoc = functionality.fileInput(fileInputWin,userFileLocEntry,30,85)
        userFileButton.place(x=140, y = 85)

        #Original File
        orgFileLabel = Label(fileInputWin , text= "Original File : " ,  fg="#f3b32d", bg="#1b191a" , font= ("times  12 bold"))
        orgFileLabel.place(x = 30,y=148)
        orgFileButton = Button(fileInputWin , fg="deeppink"  ,bg = "#141a1a", text= "Browse",command=lambda : functionality.fileInput(fileInputWin,orgFileLocEntry,30,148))
        orgFileLoc = functionality.fileInput(fileInputWin,orgFileLocEntry,30,148)
        orgFileButton.place(x=140, y = 148)

        
        # Plot and Compare button
        plotAndCompareButton = Button(fileInputWin, bg = "#141a1a" , fg= "deeppink" , text="Plot and Compare",command=graphWin)
        plotAndCompareButton.place(x=240, y = 220)
        

        #Function for going back to Command Window
        def back():
            fileInputWin.destroy()

        #Back Button
        backFileButton=Button( fileInputWin ,text="<--- Go Back", bg = "#141a1a" , fg= "deeppink" ,bd=6,command=back )
        backFileButton.place(x=6, y=230)
            

#---------------- Graph Input Win ------------------- #

def graphWin():

    # Defining File path Variables
    global userFileLoc
    global orgFileLoc
    global grpWin

    #Configuring Main Window
    grpWin = Toplevel(commandWin) 
    grpWin.grab_set()
    grpWin.geometry("450x460")
    grpWin.configure(bg="grey94")
    grpWin.resizable(False,False)
    grpWin.geometry("1500x760") 
    grpWin.title("Graph Input")

    #Graph Window Header Frame
    graphHeaderFrame=Frame(grpWin, bg="grey94" )
    graphHeaderFrame.pack(side=TOP, fill = X)

    # Label for graph Window
    graphLabel=Label(graphHeaderFrame, text="GRAPH" , bg="grey94" ,  fg="#f3b32d", font= ("Posterama  40"), pady= 10)
    graphLabel.pack()
    
    #Label to show which file has higher pitch
    resultLabel = Label(grpWin, fg="deeppink", bg= "grey94",  font= ("Posterama  20"))
    resultLabel.pack()               

    #Code execution and selection.
    try:    
            fig = backend.plotAudioFiles(grpWin,orgFileLocEntry,userFileLocEntry,userFileLoc) 
            backend.comparison(resultLabel)

    except:
            fig = backend.plotAudioFiles(grpWin,orgFileLocEntry,userFileLocEntry,userFileLoc) 


    #Placing  Matplotlib Graph in Tkinter GUI Window using canvas

    canvas = FigureCanvasTkAgg(fig, master = grpWin)
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    
    #Placing  Matplotlib Graph Toolbar in Tkinter GUI Window using canvas
    toolbar = NavigationToolbar2Tk(canvas , grpWin)
    toolbar.update()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        
    #Function for going back to Login Win
    def back():
        grpWin.destroy()

    #Back Button
    backButton=Button(grpWin ,text="<--- Go Back", bg = "white" , fg= "deeppink" ,bd=6,command=back )
    backButton.place(x=660, y= 720 )
        

# ---------------------- Acknowledgement Window ------------------------#
    def ackWin():
            
        functionality.clearWin(grpWin)
        grpWin.geometry("400x300")
        grpWin.title("Acknowledgement")

        # Graph Window Header Frame
        ackHeaderFrame = Frame(grpWin, bg="#1b191a")
        ackHeaderFrame.pack(fill=X)

        # Thank You Label for Acknowledgement Window
        thanksLabel = Label(ackHeaderFrame, text="Thank You!!!\n\n\n\nFor using our software." , 
                        bg="#1b191a", fg="#f3b32d", font=("Posterama  20") , pady =60)
        thanksLabel.pack()

        winRoot.destroy()

    # Creating Close Button    
    closeButton = Button(grpWin, bg = "white" , fg= "deeppink" , text = "CLOSE"  ,font = "raleway 12 bold", command = ackWin)
    closeButton.place(x=780, y=720)


# ------------------- Main Window ---------------------- #

#Windows 
winRoot = Tk() 
signUpWin = None
grpWin = None

#Main Window Properties
winRoot.geometry("460x450")
winRoot.resizable(False,False)
winRoot.title("Swara")

# Global Variables
userFileLoc = ""
orgFileLoc = ""

userFileLocEntry = StringVar()
orgFileLocEntry = StringVar()

#Variables for storing Login details 
userValue = StringVar()
passValue = StringVar()

#Variables for storing Signup details
userCreateMobile= StringVar()
userCreateEmail= StringVar()
userCreateUsername= StringVar()
userCreatePassword= StringVar()
userCreateFirstName= StringVar()
userCreateLastName= StringVar()
userCreateDOB= StringVar()

#Objects
database = Swara_Database.Database()
backend = Swara_Backend.Backend()
functionality = Functionality()


#Import image
swaraLogo = PhotoImage(file=r"Images\front.png")
swaraImageLabel = Label(image=swaraLogo)
swaraImageLabel.pack(anchor="center" )

#Start Button
startButtonImg = PhotoImage(file = r"Images\btn.png")
startButton = Button(winRoot,image = startButtonImg   , fg="red" , bg = "#1b191a",  command =  loginWin , relief = "flat") 
startButton.place(x = 82 ,y = 20)

# Creates a loop. To re-execute tkinter gui again and again.
winRoot.mainloop()
