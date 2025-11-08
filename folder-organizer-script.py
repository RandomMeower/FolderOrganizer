import os
import sys
import shutil
from tkinter import Tk, filedialog, messagebox


def sort(dir_path):

    if not os.path.exists(dir_path):
        raise FileNotFoundError(f"Path '{dir_path}' is not a valid directory.")
    
    print (f"Organizing {dir_path}...")

    for filename in os.listdir(dir_path):
        file_path = os.path.join(dir_path, filename)

        if filename.startswith("."):
            continue

        if os.path.isdir(file_path):
            continue

        file_root, file_ext = os.path.splitext(filename)

        if not file_ext:
            misc_path = os.path.join(dir_path, "MISC")
            os.makedir(misc_path, exist_ok=True)
            shutil.move(file_path, misc_path)
            continue

        folder_name = f"{file_ext[1:].upper()}_Files"

        new_folder_path = os.path.join(dir_path, folder_name)
        os.makedirs(new_folder_path, exist_ok=True)

        try:
            shutil.move(file_path, new_folder_path)
            print(f"Moved: '{file_path}' to '{folder_name}'")
        except Exception as e:
            print(f"An error occured: {e}")
            print(f"Couldn't move {filename} to {folder_name}")

    print("### Sorting Complete! ###")
 
def run_gui():
    # Create a root Tk window
    root = Tk()
    root.withdraw() # hides empty parts of the window

    dir_path = filedialog.askdirectory(
        title="Select the Folder You Want to Organize"
    )

    # Checks if the user selected a folder (or just clicked "Cancel")
    if dir_path: # if selected:
        try:
            sort(dir_path)
            messagebox.showinfo(
                "Success!",
                f"Successfully organized the folder:\n{dir_path}"
            )
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        print("No folder selected. Exiting.")
    
    root.destroy()


if __name__ == "__main__":
    # CLI
    if len(sys.argv) > 1:
        cli_path = sys.argv[1]
        try:
            sort(cli_path)
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("No path provided. Launching GUI")
        run_gui()