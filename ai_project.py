import tkinter as tk
from tkinter import ttk

def heuristic(subject, faculty, faculty_preferences):
    if subject in faculty_preferences[faculty]:
        return 1
    else:
        return 2

def is_subject_available(subject, room):
    return True

def is_faculty_available(faculty, subject):
    return True

def check_room_collisions(faculty_assignments):
    room_assignments = {}
    for faculty, subject in faculty_assignments.items():
        if subject is not None:
            room = room_assignments.get(subject)
            if room is not None:
                return False
            room_assignments[subject] = faculty
    return True

def check_constraints(faculty_assignments):
    if not check_room_collisions(faculty_assignments):
        return False
    return True



def display_valid_assignments(num_subjects, subjects, rooms, faculty_preferences, output_text, window):
    window.valid_assignment_found = False
    valid_assignments = []
    faculty_assignments = {faculty: None for faculty in faculty_preferences.keys()}
    backtracking(0, faculty_assignments, num_subjects, subjects, rooms, faculty_preferences, valid_assignments, window)

    output_text.config(state=tk.NORMAL)
    output_text.delete(1.0, tk.END)

    if valid_assignments:
        assignment = valid_assignments[0]
        output_text.insert(tk.END, f"Valid Assignment: {assignment}\n")
    else:
        output_text.insert(tk.END, "No valid assignment found.\n")

    output_text.config(state=tk.DISABLED)

def create_gui():
    global num_rooms_entry, num_faculty_entry
    window = tk.Tk()
    window.title("SUBJECT-ALLOCATION OF FACULTY MEMBERS:")
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window.geometry(f"{screen_width}x{screen_height}+0+0")
    num_faculty_var = tk.IntVar()
    num_subjects_var = tk.IntVar()
    num_rooms_var = tk.IntVar()
    ttk.Label(window, text="Number of Faculty Members:").grid(row=0, column=0, padx=10, pady=5)
    num_faculty_entry = ttk.Entry(window, textvariable=num_faculty_var)
    num_faculty_entry.grid(row=0, column=1, padx=10, pady=5)
    ttk.Label(window, text="Number of Subjects:").grid(row=1, column=0, padx=10, pady=5)
    num_subjects_entry = ttk.Entry(window, textvariable=num_subjects_var)
    num_subjects_entry.grid(row=1, column=1, padx=10, pady=5)
    ttk.Label(window, text="Number of Rooms:").grid(row=2, column=0, padx=10, pady=5)
    num_rooms_entry = ttk.Entry(window, textvariable=num_rooms_var)
    num_rooms_entry.grid(row=2, column=1, padx=10, pady=5)
    start_button = ttk.Button(window, text="Start Backtracking", command=lambda: start_backtracking(window, num_subjects_var, num_faculty_var, num_rooms_var, num_subjects_entry, num_rooms_entry, output_text))
    start_button.grid(row=3, column=1, pady=10)
    output_text = tk.Text(window, height=50, width=100, state=tk.DISABLED)
    output_text.grid(row=4, column=0, columnspan=10, pady=10)
    window.after(1000, display_valid_assignments, num_subjects_var.get(), [], [], {}, output_text, window)
    window.mainloop()

def start_backtracking(window, num_subjects_var, num_faculty_var, num_rooms_var, num_subjects_entry, num_rooms_entry, output_text):
    num_subjects = num_subjects_var.get()
    num_faculty = num_faculty_var.get()
    num_rooms = num_rooms_var.get()
    faculty_preferences = {}
    for i in range(num_faculty):
        faculty_name = input(f"Enter the name of faculty {i + 1}: ")
        preferences = input(f"Enter faculty {faculty_name}'s preferred subjects (comma-separated): ")
        faculty_preferences[faculty_name] = [subject.strip() for subject in preferences.split(',')]
    subjects = [input(f"Enter the name of subject {i + 1}: ") for i in range(num_subjects)]
    rooms = [input(f"Enter the name of room {i + 1}: ") for i in range(num_rooms)]
    display_valid_assignments(num_subjects, subjects, rooms, faculty_preferences, output_text, window)

create_gui()
