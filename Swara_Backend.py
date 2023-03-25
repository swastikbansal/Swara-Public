# Extractes raw data from .wav audio files
import wave

# Plots graph of audio files
import matplotlib.pyplot as plt

# Converts raw data into numerical arrays for plotting
import numpy as np

from tkinter import messagebox
from tkinter import *

# Super Imposes graph in tkineter GUI
from matplotlib.figure import Figure

class Backend :

    #Function For plotting Audio Graphs 
    def plotAudioFiles(self,win,orgFileEntry,userFileEntry,recUser):
        self.orgFile = ""
        self.userFile = ""
        self.orgFile  = orgFileEntry.get()
        self.userFile = userFileEntry.get()
        if self.userFile == "":
            self.userFile = recUser
        
        print(self.userFile,self.orgFile,sep = "\n")

        #Checks for No File Inputs
        if self.userFile == "" or self.orgFile == "":
            messagebox.showerror("Missing Inputs","Please provide both the files.")
            win.destroy()

        else:
            # Loads audio files
            with wave.open(self.userFile, "rb") as self.wavUserFile:
                self.userSr = self.wavUserFile.getframerate()
                self.userX = self.wavUserFile.readframes(self.wavUserFile.getnframes())
                

            with wave.open(self.orgFile, "rb") as self.wav_orgFile:
                self.orgSr = self.wav_orgFile.getframerate()
                self.orgX = self.wav_orgFile.readframes(self.wav_orgFile.getnframes())
                
            # Convert audio files to numpy arrays
            self.userX = np.frombuffer(self.userX, dtype=np.int16)
            self.orgX = np.frombuffer(self.orgX, dtype=np.int16)
            
            #Time = Frame Data/No. of Frames
            self.userTime = np.arange(self.userX.size) / self.userSr
            self.orgTime = np.arange(self.orgX.size) / self.orgSr

            # Plot waveform graph
            self.fig = Figure(figsize=(5,4), dpi=100)
            self.ax = self.fig.add_subplot(111)

            self.ax.plot(self.userTime, self.userX, label=self.userFile, color="red", alpha=0.7) #Transparency
            self.ax.plot(self.orgTime, self.orgX, label=self.orgFile, color="green", zorder=0.6) #Improves Representation

            plt.xlim(0, len(self.userX))

            self.ax.set_xlabel("Time (s)")
            self.ax.set_ylabel("Amplitude")
            self.ax.set_title("Waveform of audio files")
            self.ax.legend()

            return self.fig

    # Function for comparing Audio Files   
    def comparison(self ,text):

        # Compare pitches
        if np.mean(self.userX) > np.mean(self.orgX):
            self.pitchComparison = 'File 1 has  higher pitch.'
        elif np.mean(self.userX) < np.mean(self.orgX):
            self.pitchComparison = 'File 2 has higher pitch.'
        else:
            self.pitchComparison = 'Both the files have the same pitch.'

        # Calculate similarity percentage
        self.similarity = np.corrcoef(self.userX, self.orgX)[0, 1] * 100
        self.similarity = round(self.similarity, 2)

        # Displays result in tkinter GUI
        text.config(text=f"Pitch Comparison: {self.pitchComparison}")
        #text.config(text=f"Pitch Comparison: {self.pitchComparison}\nSimilarity: {self.similarity}%")
        # print(pitchComparison,similarity)

