# Extractes raw data from .wav audio files
import wave

# Plots graph of audio files
import matplotlib.pyplot as plt

# Converts raw data into numerical arrays for plotting
import numpy as np

# Imposes graph in tkineter gui
from matplotlib.figure import Figure

#Function For plotting Audio Graphs 
def plot_audio_files(user_file, org_file):

    # Loads audio files
    with wave.open(user_file, "rb") as wav_user_file:
        user_sr = wav_user_file.getframerate()
        user_X = wav_user_file.readframes(wav_user_file.getnframes())
        

    with wave.open(org_file, "rb") as wav_org_file:
        org_sr = wav_org_file.getframerate()
        org_X = wav_org_file.readframes(wav_org_file.getnframes())
        
    # Convert audio files to numpy arrays
    user_X = np.frombuffer(user_X, dtype=np.int16)
    org_X = np.frombuffer(org_X, dtype=np.int16)

    # Plotting Graph
    fig =  Figure(figsize=(30, 30))
    ax = fig.add_subplot() 
    ax.plot(user_X, label=user_file, color= "red" ,alpha =  0.7) #purple  red 
    ax.plot(org_X, label=org_file , color = "green",zorder=0.6 ) #orange green
    plt.xlim(0, len(user_X))
    ax.set_xlabel('Samples')
    ax.set_ylabel('Amplitude')
    ax.set_title('Waveform of audio files')
    ax.legend()
    return fig

# Function for comparing Audio Files   
def similarity_and_pitch(text, user_file, org_file):

    # Loads audio files
    with wave.open(user_file, "rb") as wav_user_file:
        user_sr = wav_user_file.getframerate()
        user_X = wav_user_file.readframes(wav_user_file.getnframes())
      

    with wave.open(org_file, "rb") as wav_org_file:
        org_sr = wav_org_file.getframerate()
        org_X = wav_org_file.readframes(wav_org_file.getnframes())
        
    
    # Convert audio files to numpy arrays
    user_X = np.frombuffer(user_X, dtype=np.int16)
    org_X = np.frombuffer(org_X, dtype=np.int16)
    

    # Compare pitches
    if np.mean(user_X) > np.mean(org_X):
        pitch_comparison = 'File 1 has  higher pitch.'
    elif np.mean(user_X) < np.mean(org_X):
        pitch_comparison = 'File 2 has higher pitch.'
    else:
        pitch_comparison = 'Both the files have the same pitch.'

    # Calculate similarity percentage
    similarity = np.corrcoef(user_X, org_X)[0, 1] * 100
    similarity = round(similarity, 2)

    # Displays result in tkinter GUI
    # text.config(text=f"Pitch Comparison: {pitch_comparison}\nSimilarity: {similarity}%")
    text.config(text=f"Pitch Comparison: {pitch_comparison}")
    

