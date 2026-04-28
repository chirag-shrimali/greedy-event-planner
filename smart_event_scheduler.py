# Smart Event Scheduler

import tkinter as tk
from tkinter import messagebox

# ----------------- EVENT CLASS -----------------

class Event:
    def __init__(self, name, start, end) :
        self.name = name
        self.start = start
        self.end = end


# ----------------- GREEDY ALGORITHM -----------------

def greedy_schedule(events) :
    events.sort(key = lambda x : x.end)

    selected = []

    if len(events) == 0 :
        return selected

    selected.append(events[0])
    last_end = events[0].end

    for i in range(1, len(events)) :
        if events[i].start >= last_end :
            selected.append(events[i])
            last_end = events[i].end

    return selected

# ----------------- MAIN APP -----------------

class App :
    def __init__(self, root) :
        self.root = root
        self.root.title("Smart Event Scheduler")
        self.root.geometry("700x500")

        self.events = []

        # -------- INPUT --------

        frame = tk.Frame(root)
        frame.pack(pady = 10)

        tk.Label(frame, text = "Event Name").grid(row = 0, column = 0)
        tk.Label(frame, text = "Start").grid(row = 0, column = 1)
        tk.Label(frame, text = "End").grid(row = 0, column = 2)

        self.name_entry = tk.Entry(frame)
        self.start_entry = tk.Entry(frame)
        self.end_entry = tk.Entry(frame)

        self.name_entry.grid(row = 1, column = 0)
        self.start_entry.grid(row = 1, column = 1)
        self.end_entry.grid(row = 1, column = 2)

        tk.Button(frame, text = "Add Event", command = self.add_event).grid(row = 1 , column = 3, padx = 10)

        # -------- LIST --------

        self.listbox = tk.Listbox(root , width=80)
        self.listbox.pack(pady = 10)

        # Load saved events AFTER listbox is created

        self.load_events()

        # -------- BUTTONS --------

        btn_frame = tk.Frame(root)
        btn_frame.pack()

        tk.Button(btn_frame , text = "Run Algorithm" , command = self.run_algo).pack(side = tk.LEFT , padx = 10)
        tk.Button(btn_frame , text = "Delete Selected" , command = self.delete_event).pack(side = tk.LEFT , padx = 10)
        tk.Button(btn_frame , text = "Reset", command = self.reset).pack(side = tk.LEFT, padx = 10)

        # -------- RESULT --------

        self.result_label = tk.Label(root, text = "" , fg = "green")
        self.result_label.pack(pady = 10)

    # ----------------- FUNCTIONS -----------------

    def add_event(self) :
        try :
            name = self.name_entry.get()
            start = float(self.start_entry.get())
            end = float(self.end_entry.get())

            if name == "" or start >= end :
                messagebox.showerror("Error", "Invalid input")
                return

            event = Event(name, start , end)
            self.events.append(event)

            self.listbox.insert(tk.END, f"{name} ({start} - {end})")

            self.save_events()

            self.name_entry.delete(0 , tk.END)
            self.start_entry.delete(0 , tk.END)
            self.end_entry.delete(0 , tk.END)

        except :
            messagebox.showerror("Error" , "Enter valid numbers")

    def delete_event(self) :
        try :
            index = self.listbox.curselection()[0]
            self.listbox.delete(index)
            self.events.pop(index)
            self.save_events()
        except :
            messagebox.showwarning("Warning" , "Select an event to delete")

    def run_algo(self) :
        if len(self.events) == 0 :
            messagebox.showinfo("Info" , "No events added")
            return

        selected = greedy_schedule(self.events)

        result_text = "Selected Events :\n"
        for e in selected :
            result_text += f"{e.name} ({e.start} - {e.end})\n"

        self.result_label.config(text = result_text)

    def reset(self) :
        self.events.clear()
        self.listbox.delete(0 , tk.END)
        self.result_label.config(text = "")
        self.save_events()

    # ----------------- FILE HANDLING -----------------

    def save_events(self) :
        try :
            with open("events.txt" , "w") as f :
                for e in self.events :
                    f.write(f"{e.name} , {e.start} , {e.end}\n")
        except :
            pass

    def load_events(self) :
        try :
            with open("events.txt" , "r") as f :
                for line in f :
                    parts = line.strip().split(",")
                    if len(parts) == 3 :
                        name, start, end = parts
                        event = Event(name, float(start), float(end))
                        self.events.append(event)
                        self.listbox.insert(tk.END, f"{name} ({start} - {end})")
        except FileNotFoundError :
            pass

# ----------------- RUN -----------------

root = tk.Tk()

app = App(root)

root.mainloop()