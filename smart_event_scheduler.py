import tkinter as tk
from tkinter import messagebox

# ---------- EVENT ----------

class Event :
    def __init__(self , name, start, end):
        self.name = name
        self.start = start
        self.end = end

# ---------- GREEDY ----------

def greedy_schedule(events):
    events.sort(key = lambda x: x.end)
    selected = []

    if not events:
        return selected

    selected.append(events[0])
    last_end = events[0].end

    for i in range(1, len(events)):
        if events[i].start >= last_end:
            selected.append(events[i])
            last_end = events[i].end

    return selected


# ---------- APP ----------

class App :
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Event Scheduler ✨")
        self.root.geometry("750x550")
        self.root.config(bg="#1e1e2f")

        self.events = []

        # ---------- TITLE ----------

        tk.Label(root, text="Smart Event Scheduler",
                 font=("Arial", 20, "bold"),
                 fg="#00ffcc", bg="#1e1e2f").pack(pady=10)

        # ---------- INPUT CARD ----------
        frame = tk.Frame(root, bg="#2c2c3e", bd=2, relief="ridge")
        frame.pack(pady=10, padx=20, fill="x")

        tk.Label(frame, text="Event Name", fg="white", bg="#2c2c3e").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(frame, text="Start (1-24)", fg="white", bg="#2c2c3e").grid(row=0, column=1)
        tk.Label(frame, text="End (1-24)", fg="white", bg="#2c2c3e").grid(row=0, column=2)

        self.name_entry = tk.Entry(frame, width=20, font=("Arial", 11))
        self.start_entry = tk.Entry(frame, width=10, font=("Arial", 11), justify="center")
        self.end_entry = tk.Entry(frame, width=10, font=("Arial", 11), justify="center")

        self.name_entry.grid(row=1, column=0, padx=10, pady=5)
        self.start_entry.grid(row=1, column=1)
        self.end_entry.grid(row=1, column=2)

        tk.Button(frame, text="➕ Add",
                  bg="#00ffcc", fg="black",
                  command=self.add_event).grid(row=1, column=3, padx=10)

        # ---------- LIST ----------

        list_frame = tk.Frame(root, bg="#1e1e2f")
        list_frame.pack(pady=10)

        self.listbox = tk.Listbox(list_frame, width=80, height=10,
                                 bg="#2c2c3e", fg="white",
                                 selectbackground="#00ffcc")
        self.listbox.pack()

        self.load_events()

        # ---------- BUTTONS ----------

        btn_frame = tk.Frame(root, bg="#1e1e2f")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="▶ Run",
                  bg="#00cc99", width=12,
                  command=self.run_algo).grid(row=0, column=0, padx=5)

        tk.Button(btn_frame, text="🗑 Delete",
                  bg="#ff4d4d", width=12,
                  command=self.delete_event).grid(row=0, column=1, padx=5)

        tk.Button(btn_frame, text="🔄 Reset",
                  bg="#ffaa00", width=12,
                  command=self.reset).grid(row=0, column=2, padx=5)

        # ---------- RESULT ----------

        self.result_label = tk.Label(root, text="",
                                     fg="#00ffcc",
                                     bg="#1e1e2f",
                                     font=("Arial", 11))
        self.result_label.pack(pady=10)

    # ---------- ADD EVENT ----------
    
    def add_event(self) :
        try :
            name = self.name_entry.get().strip()
            start_text = self.start_entry.get().strip()
            end_text = self.end_entry.get().strip()

            self.start_entry.config(bg="white")
            self.end_entry.config(bg="white")

            if name == "":
                messagebox.showerror("Error", "⚠ Please enter event name")
                return

            if start_text == "" or end_text == "":
                messagebox.showerror("Error", "⚠ Enter both start and end time")
                return

            start = float(start_text)
            end = float(end_text)

            # ----------- SPLIT HOURS & MINUTES -----------

            sh = int(start)
            sm = int(round((start - sh) * 100))

            eh = int(end)
            em = int(round((end - eh) * 100))

            # ----------- VALIDATION -----------

            if not (1 <= sh <= 24):
                self.start_entry.config(bg="#ffcccc")
                messagebox.showerror("Invalid Time", "⛔ Start hour must be 1–24")
                return

            if not (1 <= eh <= 24):
                self.end_entry.config(bg="#ffcccc")
                messagebox.showerror("Invalid Time", "⛔ End hour must be 1–24")
                return

            # Minute check

            if not (0 <= sm <= 59):
                self.start_entry.config(bg="#ffcccc")
                messagebox.showerror("Invalid Time", "⛔ Minutes must be 00–59 (e.g., 10.30)")
                return

            if not (0 <= em <= 59):
                self.end_entry.config(bg="#ffcccc")
                messagebox.showerror("Invalid Time", "⛔ Minutes must be 00–59 (e.g., 14.45)")
                return

            # Duration check

            if start >= end:
                self.start_entry.config(bg="#ffcccc")
                self.end_entry.config(bg="#ffcccc")
                messagebox.showerror("Invalid Duration", "⛔ Start must be less than End")
                return

            # ----------- ADD EVENT -----------

            event = Event(name, start, end)
            self.events.append(event)

            self.listbox.insert(tk.END, f"{name}   ({start} - {end})")

            self.save_events()

            # Clear fields

            self.name_entry.delete(0, tk.END)
            self.start_entry.delete(0, tk.END)
            self.end_entry.delete(0, tk.END)

        except ValueError:
            messagebox.showerror("Error", "⚠ Enter valid numeric time (e.g., 10.30)")

    # ---------- DELETE ----------

    def delete_event(self):
        try :
            index = self.listbox.curselection()[0]
            self.listbox.delete(index)
            self.events.pop(index)
            self.save_events()
        except :
            messagebox.showwarning("Warning", "Select event to delete")

    # ---------- RUN ----------

    def run_algo(self):
        if not self.events:
            messagebox.showinfo("Info", "No events added")
            return

        selected = greedy_schedule(self.events)

        text = "✨ Optimal Schedule:\n"
        for e in selected:
            text += f"✔ {e.name} ({e.start}-{e.end})\n"

        self.result_label.config(text = text)

    # ---------- RESET ----------

    def reset(self):
        self.events.clear()
        self.listbox.delete(0, tk.END)
        self.result_label.config(text="")
        self.save_events()

    # ---------- FILE ----------
    
    def save_events(self):
        try:
            with open("events.txt", "w") as f:
                for e in self.events:
                    f.write(f"{e.name},{e.start},{e.end}\n")
        except:
            pass

    def load_events(self):
        try:
            with open("events.txt", "r") as f:
                for line in f:
                    name, start, end = line.strip().split(",")
                    event = Event(name, float(start), float(end))
                    self.events.append(event)
                    self.listbox.insert(tk.END, f"{name} ({start}-{end})")
        except:
            pass

# ---------- RUN ----------

root = tk.Tk()
app = App(root)
root.mainloop()