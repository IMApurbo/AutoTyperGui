import customtkinter as ctk
import pyautogui
import time
import threading

# Function to automate typing
def automate_typing(initial_delay, text_to_type, repeat_count, status_label, start_button):
    # Update button text and status label
    start_button.configure(text="Typing.........")
    status_label.configure(text="")

    # Give user time to switch focus to the desired window
    time.sleep(5)

    # Initial typing with delay
    time.sleep(initial_delay)
    pyautogui.write(text_to_type)
    pyautogui.press('enter')

    # Perform typing without delay after the first time
    for _ in range(repeat_count - 1):
        pyautogui.write(text_to_type)
        pyautogui.press('enter')

    # Update button text and status label after completion
    start_button.configure(text="Start Typing")
    status_label.configure(text="Finished")

# Function to start typing in a separate thread
def start_typing(status_label, start_button):
    initial_delay = float(entry_initial_delay.get())
    text_to_type = entry_text_to_type.get()
    repeat_count = int(entry_repeat_count.get())

    # Start typing in a separate thread to prevent GUI freezing
    threading.Thread(target=automate_typing, args=(initial_delay, text_to_type, repeat_count, status_label, start_button)).start()

# Set up the main window
ctk.set_appearance_mode("Dark")  # Set theme
ctk.set_default_color_theme("blue")  # Set color theme
app = ctk.CTk()  # Create the main window
app.title('PyAutoGUI Automator')
app.geometry("800x400")  # Width x Height


# Define the grid layout
app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=1)
app.grid_rowconfigure(2, weight=1)
app.grid_rowconfigure(3, weight=1)
app.grid_rowconfigure(4, weight=1)

# Create and place the initial delay input
label_initial_delay = ctk.CTkLabel(app, text="Initial Delay (s):")
label_initial_delay.grid(row=0, column=0, pady=10, padx=10, sticky="e")
entry_initial_delay = ctk.CTkEntry(app, placeholder_text="Enter initial delay")
entry_initial_delay.grid(row=0, column=1, pady=10, padx=10, sticky="we")

# Create and place the text to type input
label_text_to_type = ctk.CTkLabel(app, text="Text to Type:")
label_text_to_type.grid(row=1, column=0, pady=10, padx=10, sticky="e")
entry_text_to_type = ctk.CTkEntry(app, placeholder_text="Enter text to type")
entry_text_to_type.grid(row=1, column=1, pady=10, padx=10, sticky="we")

# Create and place the repeat count input
label_repeat_count = ctk.CTkLabel(app, text="Repeat Count:")
label_repeat_count.grid(row=2, column=0, pady=10, padx=10, sticky="e")
entry_repeat_count = ctk.CTkEntry(app, placeholder_text="Enter repeat count")
entry_repeat_count.grid(row=2, column=1, pady=10, padx=10, sticky="we")

# Create and place the status label
status_label = ctk.CTkLabel(app, text="")
status_label.grid(row=3, column=0, columnspan=2, pady=10)

# Create and place the start button
start_button = ctk.CTkButton(app, text="Start Typing", command=lambda: start_typing(status_label, start_button))
start_button.grid(row=4, column=0, columnspan=2, pady=20)

# Add neon light effect, hover effect, text color, input text color, button border, etc.
entry_initial_delay.configure(fg_color=("gray75", "gray30"), text_color="white", border_color="blue", border_width=2)
entry_text_to_type.configure(fg_color=("gray75", "gray30"), text_color="white", border_color="blue", border_width=2)
entry_repeat_count.configure(fg_color=("gray75", "gray30"), text_color="white", border_color="blue", border_width=2)
start_button.configure(fg_color=("gray75", "blue"), hover_color="blue", text_color="white", border_color="blue", border_width=2)

# Run the main loop
app.mainloop()
