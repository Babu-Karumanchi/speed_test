from tkinter import *
import speedtest

def speedCheck():
    st = speedtest.Speedtest()
    st.get_servers()
    download_speed = str(round(st.download() / (10**6), 3)) + " Mbps"
    upload_speed = str(round(st.upload() / (10**6), 3)) + " Mbps"
    lab_down.config(text=download_speed)
    lab_up.config(text=upload_speed)

# Initialize the main window
app = Tk()
app.title("Speed Test")
app.geometry("500x650")
app.config(bg="black")

# Heading
heading_label = Label(app, text="Speed Test", font=("Times New Roman", 30, "bold"), bg="black", fg="red")
heading_label.place(x=60, y=40, height=50, width=380)

# Download speed label
download_label = Label(app, text="Download Speed", font=("Times New Roman", 30, "bold"), bg="black", fg="white")
download_label.place(x=60, y=130, height=50, width=380)

# Download speed result
lab_down = Label(app, text="00", font=("Times New Roman", 30, "bold"), fg="red", bg="black")
lab_down.place(x=60, y=200, height=50, width=380)

# Upload speed label
upload_label = Label(app, text="Upload Speed", font=("Times New Roman", 30, "bold"), bg="black", fg="white")
upload_label.place(x=60, y=290, height=50, width=380)

# Upload speed result
lab_up = Label(app, text="00", font=("Times New Roman", 30, "bold"), fg="red", bg="black")
lab_up.place(x=60, y=360, height=50, width=380)

# Check speed button
check_speed_button = Button(app, text="Check Speed", font=("Times New Roman", 30, "bold"), relief=RAISED, bg="red", command=speedCheck)
check_speed_button.place(x=60, y=460, height=50, width=380)

# Run the application
app.mainloop()
