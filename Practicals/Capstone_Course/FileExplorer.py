from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


# Function for opening the file explorer window
def browse_files():
    try:
        filename = filedialog.askopenfilename(initialdir="/",
                                              title="Select a File",
                                              filetypes=[("all files", "*.*")])

        if filename:
            label_file_explorer.configure(text="File Opened: " + filename)
        else:
            messagebox.showinfo("No file selected", "You did not select a file.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


# Function to close the application
def close_app():
    window.quit()


# Create the root window
window = Tk()

# Set window title and icon
window.title('File Explorer')

# Open window in fullscreen
window.attributes('-toolwindow', True)

# Set background color
window.config(background="#f0f0f0")

# Configure grid to prevent resizing of widgets in full screen or minimized
window.grid_rowconfigure(0, weight=1)  # Row 0 does not expand
window.grid_rowconfigure(1, weight=1)  # Row 1 does not expand
window.grid_columnconfigure(0, weight=1)  # Column 0 does not expand
window.grid_columnconfigure(1, weight=1)  # Column 1 does not expand

# Create a File Explorer label
label_file_explorer = Label(window,
                            text="Select a file...",
                            width=50, height=4,
                            fg="blue", font=('Arial', 12))

# Create buttons
button_explore = Button(window,
                        text="Browse Files",
                        width=20,
                        height=2,
                        fg="white", bg="#4CAF50",
                        activebackground="#45a049",
                        command=browse_files)

button_exit = Button(window,
                     text="Exit",
                     width=20,
                     height=2,
                     fg="white", bg="#f44336",
                     activebackground="#e53935",
                     command=close_app)


# Grid layout for widgets (Centered with padding)
label_file_explorer.grid(column=0, row=0, padx=10, pady=20, columnspan=2, sticky="nsew")
button_explore.grid(column=0, row=1, padx=10, pady=10, sticky="nsew")
button_exit.grid(column=1, row=1, padx=10, pady=10, sticky="nsew")

# # Minimize and Close buttons at the top-right-corner
# # Create Minimize and Close buttons
# minimize_button = Button(window, text="Minimize", command=lambda: window.iconify())
# close_button = Button(window, text="Close", command=close_app)
# # Align The buttons
# minimize_button.grid(row=0, column=2, padx=10, pady=5)
# close_button.grid(row=0, column=3, padx=10, pady=5)

# Prevent resizing of the window by the user (optional)
window.resizable(False, False)

# Run the window loop
window.mainloop()
