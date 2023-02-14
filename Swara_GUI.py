#Libraries for GUI
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

# Canvas For imposing matplotlib graph with tkinter gui.
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  
import pyaudio
import wave
import os

#Importing Custom Files
import Swara_Backend
import Swara_Database

#Function for clearing Win
def clearWin(window):
      for widgets in window.winfo_children():
          widgets.destroy()

#Function for taking File Input 
def fileInput(b_x,b_y):
        file = filedialog.askopenfile(mode='r', filetypes=[('Music Files', '*.wav')])
        
        if file:
                filePath = os.path.abspath(file.name)
                path = filePath
                file_loc_l = Label(win_root, text=str(filePath),font = "raleway 10 bold", bg="paleturquoise")
                file_loc_l.place(x = b_x, y = (b_y + 30))                        
                return path
        
#Function for Recording Audio
def recording(sec_e):
        sec = sec_e.get()
        FRAMES_PER_BUFFER = 3200
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 16000

        audio = pyaudio.PyAudio()

        record = audio.open(
                format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=FRAMES_PER_BUFFER
        )
          
        # Creates a label when recording completes.
        ch2 = Label(win_root , text= "Your voice is Recorded!" , bg="paleturquoise" ,font= ("Posterama  16 bold"))
        ch2.place(x= 140 , y = 220)

        seconds = float(sec)
        frames = []
        second_tracking = 0
        second_count = 0
        for i in range(0, int(RATE/FRAMES_PER_BUFFER*seconds)):
                ch3 = Label(win_root , textvariable = f'Time Left: {seconds - second_count} seconds' , bg="paleturquoise")
                ch3.place(x= 30 , y = 130)
                data = record.read(FRAMES_PER_BUFFER)
                frames.append(data)
                second_tracking += 1
                second_count += 1


        record.stop_stream()
        record.close()
        audio.terminate()

        specimen = wave.open('Audio/user.wav', 'wb')
        specimen.setnchannels(CHANNELS)
        specimen.setsampwidth(audio.get_sample_size(FORMAT))
        specimen.setframerate(RATE)
        specimen.writeframes(b''.join(frames))
        specimen.close()


#-------------------- Login Win -------------------- #
def loginWin():
        clearWin(win_root)

        win_root.geometry("260x200")

        #Login Win Header Frame
        login_h_fr=Frame(win_root, bg="paleturquoise" )
        login_h_fr.pack(side=TOP, fill = X)

        #Login Label
        login_text=Label(login_h_fr, text="LOGIN" ,bg="paleturquoise", fg = "red", font= ("Posterama  20 bold"), padx = 200 , pady = 10)
        login_text.pack()

        #User
        user = Label(win_root , text= "Username ID  :   ", bg="paleturquoise")
        user.place(x= 30 , y = 58)

        userEntry = Entry(win_root , textvariable =uservalue )
        userEntry.place(x=120, y = 58)

        #Password
        password = Label(win_root , text= "Password : ", bg="paleturquoise")  
        password.place(x = 30,y=80)

        passEntry = Entry(win_root , textvariable = passvalue, show = "*")
        passEntry.place(x=120 ,y = 80)
        
        #Login Button
        log_b = Button(win_root, fg="red", text = "Login"  ,font = "raleway 12 bold", command = lambda: Swara_Database.database(userEntry,passEntry,chooseWin)) #Checks and verify the login details
        log_b.place(x = 160, y = 130)

        #Create User Button
        c_user_b = Button(win_root, fg = "red", text = "Sign - Up", font = " raleway 12 bold" ,command= createUserWin)
        c_user_b.place(x = 30, y = 130)
        
def createUserWin():
        messagebox.showinfo("Work In Progress","This Section Of Program is Work in Progress")
        
#-----------------Choose option window---------------#
def chooseWin():
        clearWin(win_root)
        win_root.geometry("280x200")

        #Command Win Header Frame
        ch_h_fr=Frame(win_root, bg="paleturquoise" )
        ch_h_fr.pack(side=TOP, fill = X)

        #Command Label
        ch_text=Label(ch_h_fr, text="COMMAND" ,bg="paleturquoise", fg = "red", font= ("Posterama  20 bold"), padx = 200 , pady= 20)
        ch_text.pack()
        
        #Command Button
        rec_b = Button(win_root, fg="red", text = "Record Audio"  ,font = "raleway 12 bold", command = recordWin )
        rec_b.place(x = 140, y = 130)

        #Create User Button
        up_b = Button(win_root, fg = "red", text = "Upload File", font = " raleway 12 bold" , command = fileWin)
        up_b.place(x = 20, y = 130)

#-----------------Record audio window---------------#
def recordWin():
        global orgMusic_file_loc
        global user_file_loc

        user_file_loc = "Audio/user.wav"

        clearWin(win_root)
        win_root.geometry("520x450")

        #Command Win Header Frame
        ch_h_fr=Frame(win_root, bg="paleturquoise" )
        ch_h_fr.pack(side=TOP, fill = X)
         
        #Command Label
        ch_text=Label(ch_h_fr, text="Record Audio" ,bg="paleturquoise", fg = "red", font= ("Posterama  25 bold"), padx = 200 , pady= 10)
        ch_text.pack()

        # Original File upload label
        org_music_l = Label(win_root , text= "Original File : " , bg="paleturquoise",  font= ("Posterama  12 bold"))
        org_music_l.place(x= 35 , y= 80)
        orgMusic_file_loc = fileInput(20,80)
        org_file_but = Button(win_root , text= "Browse",command=lambda : fileInput(120,140))
        org_file_but.place(x= 165 , y= 80)
        
        #Interval input label
        interval_l = Label(win_root , text= "Enter recording interval : \n(in Seconds)  " , bg="paleturquoise",  font= ("Posterama  12 bold"))
        interval_l.place(x= 35 , y= 150)

        # Interval input entry box
        sec_e = Entry(win_root,font = "Posterama 15 bold", width = 10)
        sec_e.place(x= 260 , y= 150)
        

        # Record Audio button
        record_button = Button(win_root, text="Record Audio", command= lambda : recording(sec_e) , font = " arial 15 bold", width = 14, height= 2,
                  relief = RAISED,fg="red" ) 
        record_button.place(x=170 , y=260)

        # Plot and compare button
        next_button = Button(win_root, text ="Plot and Compare", command=graphWin ,font = " arial 15 bold", width = 16, height= 2
                  ,fg="red" , relief = RAISED )
        next_button.place(x= 160 , y= 350)
        

#---------------- File Input Win -------------------
def fileWin():
        global user_file_loc
        global orgMusic_file_loc
        clearWin(win_root)

        win_root.geometry("500x270")

        #File Header Frame
        file_h_fr=Frame(win_root, bg ="paleturquoise" )
        file_h_fr.pack(side=TOP, fill = X)

        #Header Text
        file_h_text=Label(file_h_fr, text="File Input" ,bg="paleturquoise", fg = "red",
                          font= ("Posterama  20 bold"), padx = 200 , pady = 10)
        file_h_text.pack()

        #Instruction Text
        inst_l = Label(win_root,text="Input your recorded music file and Original Music File Here.",
                        bg="paleturquoise" , fg = "Red", font = ("Posterama  10 bold") )
        inst_l.place(x = 50,y = 50)

        #User File
        user_file_l = Label(win_root , text= "Recorded File :   " , bg="paleturquoise")
        user_file_l.place(x= 30 , y = 85)
        user_file_but = Button(win_root , text= "Browse",command=lambda : fileInput(30,85))
        user_file_loc = fileInput(30,85)
        user_file_but.place(x=140, y = 85)

        #Original File
        org_music_l = Label(win_root , text= "Original File : " , bg="paleturquoise")  
        org_music_l.place(x = 30,y=140)
        org_file_but = Button(win_root , text= "Browse",command=lambda : fileInput(30,140))
        orgMusic_file_loc = fileInput(30,140)
        org_file_but.place(x=140, y = 140)

        
        # Plot and Compare button
        plot_and_compare_button = Button(win_root, text="Plot and Compare",command=graphWin)
        plot_and_compare_button.place(x=120, y = 220)
        

#---------------- Graph Input Win ------------------- #
def graphWin():
        global user_file_loc
        global orgMusic_file_loc              
        
        #Configuring Main Window
        clearWin(win_root)
        win_root.geometry("1400x700") 
        win_root.configure(bg="paleturquoise")
        win_root.title("Graph Input")

        #Graph Window Header Frame
        grp_h_fr=Frame(win_root, bg="paleturquoise" )
        grp_h_fr.pack(side=TOP, fill = X)

        # Label for graph Window
        grp_text=Label(grp_h_fr, text="GRAPH" , bg="paleturquoise" , fg = "red", font= ("Posterama  40"), pady= 10)
        grp_text.pack()
        
        result_text = Label(win_root, text="" , bg="paleturquoise" ,fg = "green",  font= ("Posterama  20"))
        result_text.pack()               


        # Creating the graph holding frame
        grpframe = Frame(win_root , bg ="paleturquoise")
        grpframe.pack(side=LEFT)
        
        #Code execution and selection.
        try:    
                fig = Swara_Backend.plot_audio_files(user_file_loc,orgMusic_file_loc) 
                Swara_Backend.similarity_and_pitch(result_text,user_file_loc,orgMusic_file_loc)

        except:
                fig = Swara_Backend.plot_audio_files(user_file_loc,orgMusic_file_loc) 


        #Placing Graph in Tkinter GUI Window using canvas
        canvas = FigureCanvasTkAgg( fig, master=grpframe)
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=2)
               
        # Creating Close Button    
        log_b = Button(win_root, fg="red", text = "CLOSE"  ,font = "raleway 12 bold", command = ackWin)
        log_b.place(x=680, y=660)

# ---------------------- Acknowledgement Window ----------------------------------
def ackWin():
        clearWin(win_root)
        win_root.geometry("400x300")
        win_root.title("Acknowledgement")

        # Graph Window Header Frame
        ack_h_fr = Frame(win_root, bg="paleturquoise")
        ack_h_fr.pack( fill=X)
        
        
        messagebox.showinfo("Work In progress","This Program is still under development.")

        # Thank You Label for Acknowledgement Window
        thanks_l = Label(ack_h_fr, text="Thank You!!!\n\n\nFor using our software." , 
                         bg="paleturquoise", fg="red", font=("Posterama  20") , pady =60)
        thanks_l.pack()
                
# --------------- Main Window --------------------- #


#Window Properties
win_root = Tk() 
win_root.geometry("450x460")
win_root.configure(bg="paleturquoise")
win_root.resizable(False,False)
win_root.title("Swara")

#Global Variables
user_file_loc = ""
orgMusic_file_loc = ""

uservalue = StringVar()
passvalue = StringVar()

#Welcome Text frame
wel_fr=Frame(win_root, bg="paleturquoise" )
wel_fr.pack(side=TOP, fill = X)

#Welcome Label
wel_text=Label(wel_fr, bg = "paleturquoise" , text="SWARA", fg = "red", font= ("Posterama  40 bold"), padx = 200 , pady=10)
wel_text.pack()

#Import image
sw_photo = PhotoImage(file="Images\logo.png")
sw_image = Label(image=sw_photo,bg = "paleturquoise")
sw_image.place(x = 230,y = 200,anchor="center")


#Start Button
start_b = Button(win_root, text = "START",font = " arial 20 bold", width = 10, height= 2, bd = 5 
                  ,fg="red" , command =  loginWin)
start_b.place(x = 230,y = 380,anchor='center')


win_root.mainloop()
