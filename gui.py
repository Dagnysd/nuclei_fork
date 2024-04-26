import tkinter as tk
from tkinter import filedialog
import os

def select_folder(label):
    folder_path = filedialog.askdirectory()
    label.config(text=folder_path)

def run_function():
    # Implement your function here
    print("Function executed!")

def main():
    root = tk.Tk()
    root.title("Image Processing GUI")

    # Labels to display selected folders
    image_folder_label = tk.Label(root, text="Select Image Folder:")
    image_folder_label.grid(row=0, column=0, padx=10, pady=5)
    mask_folder_label = tk.Label(root, text="Select Mask Folder:")
    mask_folder_label.grid(row=1, column=0, padx=10, pady=5)
    roi_folder_label = tk.Label(root, text="Select ROI Folder:")
    roi_folder_label.grid(row=2, column=0, padx=10, pady=5)

    # Buttons to select folders
    image_folder_button = tk.Button(root, text="Select", command=lambda: select_folder(image_folder_label))
    image_folder_button.grid(row=0, column=1, padx=10, pady=5)
    mask_folder_button = tk.Button(root, text="Select", command=lambda: select_folder(mask_folder_label))
    mask_folder_button.grid(row=1, column=1, padx=10, pady=5)
    roi_folder_button = tk.Button(root, text="Select", command=lambda: select_folder(roi_folder_label))
    roi_folder_button.grid(row=2, column=1, padx=10, pady=5)

    output_label = tk.Label(root, text="Output path:")
    output_label.grid(row=3, column=0, padx=10, pady=5)
    text_input_entry = tk.Entry(root)
    text_input_entry.grid(row=3, column=1, padx=10, pady=5)
    
    ## Checkboxes
    checkbox_label = tk.Label(root, text="Optional measurements")
    checkbox_label.grid(row=0, column=2, columnspan=2, padx=10, pady=5)
    checkbox_cyto_var = tk.IntVar()
    checkbox_loc_var = tk.IntVar()
    checkbox_cyto = tk.Checkbutton(root, text="Measure cyto", variable=checkbox_cyto_var)
    checkbox_cyto.grid(row=1, column=2, columnspan=2, padx=10)
    checkbox_loc = tk.Checkbutton(root, text="Determine location", variable=checkbox_loc_var)
    checkbox_loc.grid(row=2, column=2, columnspan=2, padx=10)
    loc_input_label = tk.Label(root, text='Locations:')
    loc_input_label.grid(row=3, column=2)
    loc_input_entry = tk.Entry(root)
    loc_input_entry.grid(row=3, column=3, padx=10, pady=5)
    # Run button
    run_button = tk.Button(root, text="Run", command=run_function)
    run_button.grid(row=4, column=0, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
