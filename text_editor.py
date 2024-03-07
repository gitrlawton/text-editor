import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file(window, text_edit):
    filepath = askopenfilename(filetype = [("Text Files", "*.txt")])
    
    if not filepath:
        return
    else:
        # Delete everything currently in the text editor, from the
        # first character of the first line (1.0) to the end (tk.END).
        text_edit.delete(1.0, tk.END)
        with open(filepath, "r") as input_file:
            content = input_file.read()
            # tk.END is now the beginning of the file, since it is where
            # the above deleting left off.  So, at tk.END, insert
            # the content from the file we're opening.
            text_edit.insert(tk.END, content)
        
        window.title(f"Open File: {filepath}")

def save_file(window, text_edit):
    filepath = asksaveasfilename(filetype = [("Text Files", "*.txt")])
    
    if not filepath:
        return
    else:
        with open(filepath, "w") as output_file:
            # Get everything currently in the text editor, from the
            # first character of the first line (1.0) to the end (tk.END).
            content = text_edit.get(1.0, tk.END)
            output_file.write(content)
        
        window.title(f"Open File: {filepath}")
            

def main():
    window = tk.Tk()
    window.title("Text Editor")
    
    # Set minimum size of first row and second column.
    window.rowconfigure(0, minsize = 400)
    window.columnconfigure(1, minsize = 500)
    
    # Creates a text editing widget inside the window using the font.
    text_edit = tk.Text(window, font = "Helvetica 12")
    # Places the widget in the first row, second column.
    text_edit.grid(row = 0, column = 1)
    
    # Frame goes in the window.  Give it a raised look.
    frame = tk.Frame(window, relief = tk.RAISED, bd = 2)
    
    # Create buttons.  Buttons go in the frame.
    save_button = tk.Button(frame, text = "Save", command = lambda: save_file(window, text_edit))
    open_button = tk.Button(frame, text = "Open", command = lambda: open_file(window, text_edit))
    
    # Place buttons in the first column, in rows 1 and 2.  'ew' is "East/West"
    save_button.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "ew")
    open_button.grid(row = 1, column = 0, padx = 5, sticky = "ew")
    
    # Note: Below, 'ns' stands for "North/South"
    frame.grid(row = 0, column = 0, sticky = "ns")
    
    # Bind save_file and open_file to keyboard shortcuts.
    window.bind("<Control-s>", lambda x: save_file(window, text_edit))
    window.bind("<Control-o>", lambda x: open_file(window, text_edit))
    
    # Continually run the window and keep it alive
    # until the user force quits or clicks X.
    window.mainloop()

main()