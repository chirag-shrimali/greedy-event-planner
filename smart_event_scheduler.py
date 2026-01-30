"""
Smart Event Scheduler using Greedy Algorithm
Demonstrates the Greedy Activity Selection Algorithm from Design and Analysis of Algorithms
Author: AI Assistant
Date: January 2026
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
from datetime import datetime, timedelta
from typing import List, Tuple, Dict
import math


class Event:
    """Represents an event with name, start time, and end time."""
    
    def __init__(self, name: str, start_time: float, end_time: float, event_id: int = None):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.event_id = event_id
        self.selected = False
        self.rejected = False
        
    def to_dict(self) -> Dict:
        """Convert event to dictionary for JSON serialization."""
        return {
            'name': self.name,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'event_id': self.event_id
        }
    
    @staticmethod
    def from_dict(data: Dict) -> 'Event':
        """Create event from dictionary."""
        return Event(data['name'], data['start_time'], data['end_time'], data.get('event_id'))
    
    def __repr__(self):
        return f"Event({self.name}, {self.start_time}-{self.end_time})"


class GreedyScheduler:
    """
    Implements the Greedy Activity Selection Algorithm.
    Time Complexity: O(n log n) due to sorting
    Space Complexity: O(n)
    
    Algorithm Strategy:
    1. Sort events by finish time (earliest finish time first)
    2. Select the first event
    3. For each subsequent event, if its start time >= last selected event's end time, select it
    4. This greedy choice maximizes the number of non-overlapping events
    """
    
    def __init__(self):
        self.events: List[Event] = []
        self.selected_events: List[Event] = []
        self.rejected_events: List[Event] = []
        self.algorithm_steps: List[str] = []
        
    def add_event(self, event: Event):
        """Add an event to the scheduler."""
        self.events.append(event)
        
    def clear_events(self):
        """Clear all events."""
        self.events.clear()
        self.selected_events.clear()
        self.rejected_events.clear()
        self.algorithm_steps.clear()
        
    def detect_conflicts(self) -> List[Tuple[Event, Event]]:
        """
        Detect all scheduling conflicts between events.
        Returns list of conflicting event pairs.
        """
        conflicts = []
        for i in range(len(self.events)):
            for j in range(i + 1, len(self.events)):
                event1, event2 = self.events[i], self.events[j]
                # Two events conflict if one starts before the other ends
                if (event1.start_time < event2.end_time and 
                    event2.start_time < event1.end_time):
                    conflicts.append((event1, event2))
        return conflicts
    
    def greedy_schedule(self, step_by_step: bool = False) -> Tuple[List[Event], List[Event], List[str]]:
        """
        Apply Greedy Activity Selection Algorithm.
        
        Algorithm:
        1. Sort events by finish time O(n log n)
        2. Select first event O(1)
        3. Iterate through remaining events O(n)
        4. Select event if it doesn't overlap with last selected O(1)
        
        Total Time Complexity: O(n log n)
        
        Args:
            step_by_step: If True, generate detailed algorithm steps
            
        Returns:
            Tuple of (selected_events, rejected_events, algorithm_steps)
        """
        if not self.events:
            return [], [], ["No events to schedule"]
        
        # Clear previous results
        self.selected_events.clear()
        self.rejected_events.clear()
        self.algorithm_steps.clear()
        
        # Reset event states
        for event in self.events:
            event.selected = False
            event.rejected = False
        
        # Step 1: Sort by finish time (Greedy Choice Property)
        self.algorithm_steps.append("STEP 1: Sort events by finish time (earliest first)")
        self.algorithm_steps.append(f"Original events: {len(self.events)}")
        
        sorted_events = sorted(self.events, key=lambda e: e.end_time)
        
        self.algorithm_steps.append("Sorted order:")
        for i, event in enumerate(sorted_events):
            self.algorithm_steps.append(
                f"  {i+1}. {event.name}: [{event.start_time:.1f}, {event.end_time:.1f}]"
            )
        
        # Step 2: Select first event (Greedy Choice)
        self.algorithm_steps.append("\nSTEP 2: Select first event (earliest finish time)")
        first_event = sorted_events[0]
        first_event.selected = True
        self.selected_events.append(first_event)
        last_finish_time = first_event.end_time
        
        self.algorithm_steps.append(
            f"✓ Selected: {first_event.name} (finish time: {first_event.end_time:.1f})"
        )
        
        # Step 3: Iterate and apply greedy selection
        self.algorithm_steps.append("\nSTEP 3: Process remaining events")
        self.algorithm_steps.append("Select event if start_time >= last_finish_time\n")
        
        for i in range(1, len(sorted_events)):
            event = sorted_events[i]
            
            # Greedy choice: select if compatible with last selected event
            if event.start_time >= last_finish_time:
                event.selected = True
                self.selected_events.append(event)
                last_finish_time = event.end_time
                
                self.algorithm_steps.append(
                    f"✓ Selected: {event.name} "
                    f"[{event.start_time:.1f}, {event.end_time:.1f}] "
                    f"(start {event.start_time:.1f} >= last finish {last_finish_time - event.end_time + last_finish_time:.1f})"
                )
                last_finish_time = event.end_time
            else:
                event.rejected = True
                self.rejected_events.append(event)
                
                self.algorithm_steps.append(
                    f"✗ Rejected: {event.name} "
                    f"[{event.start_time:.1f}, {event.end_time:.1f}] "
                    f"(conflicts: start {event.start_time:.1f} < last finish {last_finish_time:.1f})"
                )
        
        # Summary
        self.algorithm_steps.append(f"\n{'='*60}")
        self.algorithm_steps.append("ALGORITHM SUMMARY")
        self.algorithm_steps.append(f"{'='*60}")
        self.algorithm_steps.append(f"Total events: {len(self.events)}")
        self.algorithm_steps.append(f"Selected events: {len(self.selected_events)}")
        self.algorithm_steps.append(f"Rejected events: {len(self.rejected_events)}")
        self.algorithm_steps.append(f"Efficiency: {len(self.selected_events)/len(self.events)*100:.1f}%")
        self.algorithm_steps.append(f"\nTime Complexity: O(n log n) - dominated by sorting")
        self.algorithm_steps.append(f"Space Complexity: O(n) - storing events and results")
        
        return self.selected_events, self.rejected_events, self.algorithm_steps
    
    def get_statistics(self) -> Dict:
        """Get scheduling statistics."""
        total = len(self.events)
        selected = len(self.selected_events)
        rejected = len(self.rejected_events)
        efficiency = (selected / total * 100) if total > 0 else 0
        
        return {
            'total_events': total,
            'scheduled_events': selected,
            'rejected_events': rejected,
            'efficiency': efficiency
        }


class TimelineCanvas(tk.Canvas):
    """Custom canvas for drawing timeline visualization."""
    
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.events = []
        self.theme = 'light'
        
    def set_theme(self, theme: str):
        """Set canvas theme."""
        self.theme = theme
        if theme == 'dark':
            self.configure(bg='#2b2b2b')
        else:
            self.configure(bg='white')
        self.draw_timeline()
        
    def draw_timeline(self):
        """Draw timeline with event bars."""
        self.delete('all')
        
        if not self.events:
            # Draw empty state message
            text_color = '#cccccc' if self.theme == 'dark' else '#666666'
            self.create_text(
                self.winfo_width() // 2, self.winfo_height() // 2,
                text="No events to display\nAdd events to see timeline visualization",
                fill=text_color, font=('Arial', 12), justify='center'
            )
            return
        
        # Get canvas dimensions
        width = self.winfo_width()
        height = self.winfo_height()
        
        if width <= 1 or height <= 1:
            return
        
        # Calculate time range
        min_time = min(e.start_time for e in self.events)
        max_time = max(e.end_time for e in self.events)
        time_range = max_time - min_time
        
        if time_range == 0:
            time_range = 1
        
        # Margins
        margin_left = 60
        margin_right = 40
        margin_top = 40
        margin_bottom = 40
        
        drawable_width = width - margin_left - margin_right
        drawable_height = height - margin_top - margin_bottom
        
        # Calculate bar height
        num_events = len(self.events)
        bar_height = min(40, drawable_height // (num_events + 1))
        spacing = 10
        
        # Draw time axis
        axis_color = '#cccccc' if self.theme == 'dark' else '#333333'
        text_color = '#ffffff' if self.theme == 'dark' else '#000000'
        
        self.create_line(
            margin_left, margin_top, 
            width - margin_right, margin_top,
            fill=axis_color, width=2
        )
        
        # Draw time labels
        num_labels = 5
        for i in range(num_labels + 1):
            x = margin_left + (drawable_width * i / num_labels)
            time_val = min_time + (time_range * i / num_labels)
            
            self.create_line(x, margin_top - 5, x, margin_top + 5, fill=axis_color, width=2)
            self.create_text(
                x, margin_top - 15, 
                text=f"{time_val:.1f}", 
                fill=text_color, font=('Arial', 9)
            )
        
        # Draw title
        self.create_text(
            width // 2, 15,
            text="Event Timeline Visualization (Greedy Algorithm)",
            fill=text_color, font=('Arial', 12, 'bold')
        )
        
        # Draw event bars
        for i, event in enumerate(self.events):
            y = margin_top + spacing + i * (bar_height + spacing)
            
            # Calculate bar position
            start_x = margin_left + (event.start_time - min_time) / time_range * drawable_width
            end_x = margin_left + (event.end_time - min_time) / time_range * drawable_width
            bar_width = end_x - start_x
            
            # Choose color based on selection status
            if event.selected:
                color = '#4CAF50'  # Green for selected
                outline = '#2E7D32'
            elif event.rejected:
                color = '#F44336'  # Red for rejected
                outline = '#C62828'
            else:
                color = '#9E9E9E'  # Gray for not processed
                outline = '#616161'
            
            # Draw bar
            self.create_rectangle(
                start_x, y, end_x, y + bar_height,
                fill=color, outline=outline, width=2
            )
            
            # Draw event name
            self.create_text(
                10, y + bar_height // 2,
                text=event.name[:15] + ('...' if len(event.name) > 15 else ''),
                fill=text_color, font=('Arial', 8), anchor='w'
            )
            
            # Draw time labels on bar
            label = f"{event.start_time:.1f}-{event.end_time:.1f}"
            self.create_text(
                (start_x + end_x) // 2, y + bar_height // 2,
                text=label, fill='white', font=('Arial', 8, 'bold')
            )
        
        # Draw legend
        legend_y = height - 20
        legend_items = [
            ('Selected (Greedy Choice)', '#4CAF50'),
            ('Rejected (Conflict)', '#F44336'),
            ('Not Processed', '#9E9E9E')
        ]
        
        x_offset = margin_left
        for label, color in legend_items:
            self.create_rectangle(
                x_offset, legend_y - 8, x_offset + 15, legend_y + 8,
                fill=color, outline='black'
            )
            self.create_text(
                x_offset + 20, legend_y,
                text=label, fill=text_color, font=('Arial', 8), anchor='w'
            )
            x_offset += 180
    
    def update_events(self, events: List[Event]):
        """Update events and redraw timeline."""
        self.events = events
        self.draw_timeline()


class SmartEventSchedulerApp:
    """Main application class for Smart Event Scheduler."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Event Scheduler - Greedy Algorithm")
        self.root.geometry("1400x900")
        
        self.scheduler = GreedyScheduler()
        self.event_counter = 0
        self.current_theme = 'light'
        
        # Configure style
        self.style = ttk.Style()
        self.setup_styles()
        
        # Create GUI
        self.create_menu()
        self.create_main_layout()
        
        # Load sample data
        self.load_sample_use_case('college')
        
    def setup_styles(self):
        """Setup ttk styles for the application."""
        self.style.theme_use('clam')
        
        # Light theme colors
        self.light_colors = {
            'bg': '#f0f0f0',
            'fg': '#000000',
            'select_bg': '#0078d7',
            'select_fg': '#ffffff',
            'frame_bg': '#ffffff',
            'button_bg': '#e0e0e0'
        }
        
        # Dark theme colors
        self.dark_colors = {
            'bg': '#1e1e1e',
            'fg': '#ffffff',
            'select_bg': '#0078d7',
            'select_fg': '#ffffff',
            'frame_bg': '#2b2b2b',
            'button_bg': '#3c3c3c'
        }
        
        self.apply_theme('light')
        
    def apply_theme(self, theme: str):
        """Apply color theme to the application."""
        self.current_theme = theme
        colors = self.light_colors if theme == 'light' else self.dark_colors
        
        self.root.configure(bg=colors['bg'])
        
        self.style.configure('TFrame', background=colors['bg'])
        self.style.configure('TLabel', background=colors['bg'], foreground=colors['fg'])
        self.style.configure('TButton', background=colors['button_bg'], foreground=colors['fg'])
        self.style.configure('Header.TLabel', font=('Arial', 14, 'bold'), 
                           background=colors['bg'], foreground=colors['fg'])
        self.style.configure('Stats.TLabel', font=('Arial', 11), 
                           background=colors['frame_bg'], foreground=colors['fg'])
        
        # Update timeline canvas theme
        if hasattr(self, 'timeline_canvas'):
            self.timeline_canvas.set_theme(theme)
        
    def create_menu(self):
        """Create application menu bar."""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Save Schedule", command=self.save_schedule)
        file_menu.add_command(label="Load Schedule", command=self.load_schedule)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        
        # View menu
        view_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="View", menu=view_menu)
        view_menu.add_command(label="Light Theme", command=lambda: self.apply_theme('light'))
        view_menu.add_command(label="Dark Theme", command=lambda: self.apply_theme('dark'))
        
        # Use Cases menu
        cases_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Sample Use Cases", menu=cases_menu)
        cases_menu.add_command(label="College Timetable", 
                              command=lambda: self.load_sample_use_case('college'))
        cases_menu.add_command(label="Conference Sessions", 
                              command=lambda: self.load_sample_use_case('conference'))
        cases_menu.add_command(label="Hospital Appointments", 
                              command=lambda: self.load_sample_use_case('hospital'))
        cases_menu.add_command(label="Meeting Room Booking", 
                              command=lambda: self.load_sample_use_case('meeting'))
        
        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About Algorithm", command=self.show_about_algorithm)
        help_menu.add_command(label="How to Use", command=self.show_how_to_use)
        help_menu.add_command(label="About", command=self.show_about)
        
    def create_main_layout(self):
        """Create main application layout."""
        # Create main container
        main_container = ttk.Frame(self.root)
        main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Left panel - Event input and list
        left_panel = ttk.Frame(main_container)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=(0, 5))
        
        self.create_input_section(left_panel)
        self.create_event_list_section(left_panel)
        
        # Right panel - Timeline, steps, and statistics
        right_panel = ttk.Frame(main_container)
        right_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(5, 0))
        
        self.create_timeline_section(right_panel)
        self.create_control_section(right_panel)
        
        # Bottom panel - Algorithm steps and statistics
        bottom_panel = ttk.Frame(right_panel)
        bottom_panel.pack(fill=tk.BOTH, expand=True, pady=(10, 0))
        
        self.create_steps_section(bottom_panel)
        self.create_statistics_section(bottom_panel)
        
    def create_input_section(self, parent):
        """Create event input section."""
        input_frame = ttk.LabelFrame(parent, text="Add New Event", padding=10)
        input_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Event name
        ttk.Label(input_frame, text="Event Name:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.event_name_entry = ttk.Entry(input_frame, width=30)
        self.event_name_entry.grid(row=0, column=1, pady=5, padx=5)
        self.create_tooltip(self.event_name_entry, "Enter a descriptive name for the event")
        
        # Start time
        ttk.Label(input_frame, text="Start Time:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.start_time_entry = ttk.Entry(input_frame, width=30)
        self.start_time_entry.grid(row=1, column=1, pady=5, padx=5)
        self.create_tooltip(self.start_time_entry, "Enter start time (e.g., 9.0 for 9:00)")
        
        # End time
        ttk.Label(input_frame, text="End Time:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.end_time_entry = ttk.Entry(input_frame, width=30)
        self.end_time_entry.grid(row=2, column=1, pady=5, padx=5)
        self.create_tooltip(self.end_time_entry, "Enter end time (e.g., 10.5 for 10:30)")
        
        # Add button
        add_btn = ttk.Button(input_frame, text="Add Event", command=self.add_event)
        add_btn.grid(row=3, column=0, columnspan=2, pady=10)
        self.create_tooltip(add_btn, "Add event to the scheduler")
        
    def create_event_list_section(self, parent):
        """Create event list section."""
        list_frame = ttk.LabelFrame(parent, text="Event List (Before Greedy Selection)", padding=10)
        list_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create treeview
        columns = ('Name', 'Start', 'End', 'Duration', 'Status')
        self.event_tree = ttk.Treeview(list_frame, columns=columns, show='headings', height=15)
        
        # Configure columns
        self.event_tree.heading('Name', text='Event Name')
        self.event_tree.heading('Start', text='Start')
        self.event_tree.heading('End', text='End')
        self.event_tree.heading('Duration', text='Duration')
        self.event_tree.heading('Status', text='Status')
        
        self.event_tree.column('Name', width=180)
        self.event_tree.column('Start', width=60)
        self.event_tree.column('End', width=60)
        self.event_tree.column('Duration', width=70)
        self.event_tree.column('Status', width=100)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.event_tree.yview)
        self.event_tree.configure(yscrollcommand=scrollbar.set)
        
        self.event_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Buttons
        btn_frame = ttk.Frame(list_frame)
        btn_frame.pack(fill=tk.X, pady=(10, 0))
        
        delete_btn = ttk.Button(btn_frame, text="Delete Selected", command=self.delete_event)
        delete_btn.pack(side=tk.LEFT, padx=2)
        
        clear_btn = ttk.Button(btn_frame, text="Clear All", command=self.clear_all_events)
        clear_btn.pack(side=tk.LEFT, padx=2)
        
    def create_timeline_section(self, parent):
        """Create timeline visualization section."""
        timeline_frame = ttk.LabelFrame(parent, text="Timeline Visualization", padding=5)
        timeline_frame.pack(fill=tk.BOTH, expand=True)
        
        self.timeline_canvas = TimelineCanvas(timeline_frame, height=300, bg='white')
        self.timeline_canvas.pack(fill=tk.BOTH, expand=True)
        self.timeline_canvas.bind('<Configure>', lambda e: self.timeline_canvas.draw_timeline())
        
    def create_control_section(self, parent):
        """Create control buttons section."""
        control_frame = ttk.Frame(parent)
        control_frame.pack(fill=tk.X, pady=10)
        
        # Main action buttons
        btn_frame1 = ttk.Frame(control_frame)
        btn_frame1.pack(fill=tk.X, pady=5)
        
        schedule_btn = ttk.Button(btn_frame1, text="🚀 Run Greedy Algorithm", 
                                 command=self.run_greedy_algorithm)
        schedule_btn.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)
        self.create_tooltip(schedule_btn, 
            "Execute Greedy Activity Selection Algorithm\nTime Complexity: O(n log n)")
        
        detect_btn = ttk.Button(btn_frame1, text="🔍 Detect Conflicts", 
                               command=self.detect_conflicts)
        detect_btn.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)
        self.create_tooltip(detect_btn, "Find all overlapping events before optimization")
        
        # Secondary buttons
        btn_frame2 = ttk.Frame(control_frame)
        btn_frame2.pack(fill=tk.X, pady=5)
        
        reset_btn = ttk.Button(btn_frame2, text="↺ Reset Results", 
                              command=self.reset_results)
        reset_btn.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)
        
        step_btn = ttk.Button(btn_frame2, text="📋 View Algorithm Steps", 
                             command=self.show_algorithm_steps)
        step_btn.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)
        
    def create_steps_section(self, parent):
        """Create algorithm steps display section."""
        steps_frame = ttk.LabelFrame(parent, text="Algorithm Execution Steps", padding=5)
        steps_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        
        self.steps_text = tk.Text(steps_frame, height=12, width=50, 
                                 font=('Consolas', 9), wrap=tk.WORD)
        
        steps_scrollbar = ttk.Scrollbar(steps_frame, orient=tk.VERTICAL, 
                                       command=self.steps_text.yview)
        self.steps_text.configure(yscrollcommand=steps_scrollbar.set)
        
        self.steps_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        steps_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
    def create_statistics_section(self, parent):
        """Create statistics display section."""
        stats_frame = ttk.LabelFrame(parent, text="Scheduling Statistics", padding=10)
        stats_frame.pack(side=tk.LEFT, fill=tk.BOTH, padx=(5, 0))
        
        self.stats_labels = {}
        
        stats_items = [
            ('total', 'Total Events:', '0'),
            ('scheduled', 'Scheduled:', '0'),
            ('rejected', 'Rejected:', '0'),
            ('efficiency', 'Efficiency:', '0%'),
            ('complexity', 'Time Complexity:', 'O(n log n)')
        ]
        
        for i, (key, label, default) in enumerate(stats_items):
            ttk.Label(stats_frame, text=label, style='Stats.TLabel').grid(
                row=i, column=0, sticky=tk.W, pady=5, padx=5
            )
            value_label = ttk.Label(stats_frame, text=default, 
                                   style='Stats.TLabel', font=('Arial', 11, 'bold'))
            value_label.grid(row=i, column=1, sticky=tk.W, pady=5, padx=5)
            self.stats_labels[key] = value_label
        
        # Add complexity explanation
        complexity_note = ttk.Label(
            stats_frame, 
            text="O(n log n) from sorting\nGreedy selection: O(n)",
            font=('Arial', 8), justify=tk.LEFT
        )
        complexity_note.grid(row=len(stats_items), column=0, columnspan=2, 
                           pady=10, sticky=tk.W)
        
    def create_tooltip(self, widget, text):
        """Create tooltip for widget."""
        def on_enter(event):
            tooltip = tk.Toplevel()
            tooltip.wm_overrideredirect(True)
            tooltip.wm_geometry(f"+{event.x_root+10}+{event.y_root+10}")
            
            label = tk.Label(tooltip, text=text, background="#ffffe0", 
                           relief=tk.SOLID, borderwidth=1, font=('Arial', 9))
            label.pack()
            
            widget.tooltip = tooltip
            
        def on_leave(event):
            if hasattr(widget, 'tooltip'):
                widget.tooltip.destroy()
                del widget.tooltip
        
        widget.bind('<Enter>', on_enter)
        widget.bind('<Leave>', on_leave)
        
    def add_event(self):
        """Add a new event to the scheduler."""
        try:
            name = self.event_name_entry.get().strip()
            start = float(self.start_time_entry.get())
            end = float(self.end_time_entry.get())
            
            if not name:
                messagebox.showerror("Error", "Event name cannot be empty")
                return
            
            if start >= end:
                messagebox.showerror("Error", "Start time must be before end time")
                return
            
            if start < 0 or end < 0:
                messagebox.showerror("Error", "Times must be non-negative")
                return
            
            # Create event
            self.event_counter += 1
            event = Event(name, start, end, self.event_counter)
            self.scheduler.add_event(event)
            
            # Update display
            self.update_event_list()
            self.timeline_canvas.update_events(self.scheduler.events)
            
            # Clear inputs
            self.event_name_entry.delete(0, tk.END)
            self.start_time_entry.delete(0, tk.END)
            self.end_time_entry.delete(0, tk.END)
            self.event_name_entry.focus()
            
        except ValueError:
            messagebox.showerror("Error", "Invalid time format. Please enter numeric values.")
            
    def delete_event(self):
        """Delete selected event."""
        selection = self.event_tree.selection()
        if not selection:
            messagebox.showwarning("Warning", "Please select an event to delete")
            return
        
        item = self.event_tree.item(selection[0])
        event_name = item['values'][0]
        
        # Find and remove event
        self.scheduler.events = [e for e in self.scheduler.events if e.name != event_name]
        
        self.update_event_list()
        self.timeline_canvas.update_events(self.scheduler.events)
        self.update_statistics()
        
    def clear_all_events(self):
        """Clear all events."""
        if messagebox.askyesno("Confirm", "Clear all events?"):
            self.scheduler.clear_events()
            self.update_event_list()
            self.timeline_canvas.update_events([])
            self.steps_text.delete(1.0, tk.END)
            self.update_statistics()
            
    def update_event_list(self):
        """Update event list treeview."""
        # Clear existing items
        for item in self.event_tree.get_children():
            self.event_tree.delete(item)
        
        # Add events
        for event in self.scheduler.events:
            duration = event.end_time - event.start_time
            status = 'Selected' if event.selected else ('Rejected' if event.rejected else 'Pending')
            
            self.event_tree.insert('', tk.END, values=(
                event.name,
                f"{event.start_time:.1f}",
                f"{event.end_time:.1f}",
                f"{duration:.1f}h",
                status
            ))
            
    def detect_conflicts(self):
        """Detect and display scheduling conflicts."""
        if not self.scheduler.events:
            messagebox.showinfo("Info", "No events to check")
            return
        
        conflicts = self.scheduler.detect_conflicts()
        
        if not conflicts:
            messagebox.showinfo("Conflict Detection", 
                              "✓ No conflicts detected!\nAll events can be scheduled.")
        else:
            conflict_msg = f"Found {len(conflicts)} conflicts:\n\n"
            for i, (e1, e2) in enumerate(conflicts[:10], 1):  # Show first 10
                conflict_msg += f"{i}. '{e1.name}' [{e1.start_time:.1f}-{e1.end_time:.1f}] ↔ "
                conflict_msg += f"'{e2.name}' [{e2.start_time:.1f}-{e2.end_time:.1f}]\n"
            
            if len(conflicts) > 10:
                conflict_msg += f"\n... and {len(conflicts) - 10} more conflicts"
            
            conflict_msg += f"\n\nUse Greedy Algorithm to optimize schedule!"
            
            messagebox.showwarning("Conflicts Detected", conflict_msg)
            
    def run_greedy_algorithm(self):
        """Run the greedy scheduling algorithm."""
        if not self.scheduler.events:
            messagebox.showinfo("Info", "No events to schedule")
            return
        
        # Run algorithm
        selected, rejected, steps = self.scheduler.greedy_schedule(step_by_step=True)
        
        # Update displays
        self.update_event_list()
        self.timeline_canvas.update_events(self.scheduler.events)
        self.display_algorithm_steps(steps)
        self.update_statistics()
        
        # Show summary
        stats = self.scheduler.get_statistics()
        messagebox.showinfo(
            "Greedy Algorithm Complete",
            f"Optimization completed successfully!\n\n"
            f"Total Events: {stats['total_events']}\n"
            f"Scheduled: {stats['scheduled_events']}\n"
            f"Rejected: {stats['rejected_events']}\n"
            f"Efficiency: {stats['efficiency']:.1f}%\n\n"
            f"Time Complexity: O(n log n)"
        )
        
    def display_algorithm_steps(self, steps: List[str]):
        """Display algorithm execution steps."""
        self.steps_text.delete(1.0, tk.END)
        for step in steps:
            self.steps_text.insert(tk.END, step + '\n')
        self.steps_text.see(1.0)
        
    def show_algorithm_steps(self):
        """Show algorithm steps in a separate window."""
        if not self.scheduler.algorithm_steps:
            messagebox.showinfo("Info", "Run the algorithm first to see steps")
            return
        
        steps_window = tk.Toplevel(self.root)
        steps_window.title("Algorithm Execution Steps - Detailed View")
        steps_window.geometry("700x600")
        
        text_widget = tk.Text(steps_window, font=('Consolas', 10), wrap=tk.WORD)
        scrollbar = ttk.Scrollbar(steps_window, orient=tk.VERTICAL, 
                                 command=text_widget.yview)
        text_widget.configure(yscrollcommand=scrollbar.set)
        
        text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, pady=10)
        
        for step in self.scheduler.algorithm_steps:
            text_widget.insert(tk.END, step + '\n')
        
        text_widget.configure(state=tk.DISABLED)
        
    def update_statistics(self):
        """Update statistics display."""
        stats = self.scheduler.get_statistics()
        
        self.stats_labels['total'].configure(text=str(stats['total_events']))
        self.stats_labels['scheduled'].configure(text=str(stats['scheduled_events']))
        self.stats_labels['rejected'].configure(text=str(stats['rejected_events']))
        self.stats_labels['efficiency'].configure(text=f"{stats['efficiency']:.1f}%")
        
    def reset_results(self):
        """Reset algorithm results while keeping events."""
        for event in self.scheduler.events:
            event.selected = False
            event.rejected = False
        
        self.scheduler.selected_events.clear()
        self.scheduler.rejected_events.clear()
        self.scheduler.algorithm_steps.clear()
        
        self.update_event_list()
        self.timeline_canvas.update_events(self.scheduler.events)
        self.steps_text.delete(1.0, tk.END)
        self.update_statistics()
        
        messagebox.showinfo("Reset", "Results cleared. Events preserved.")
        
    def save_schedule(self):
        """Save schedule to JSON file."""
        if not self.scheduler.events:
            messagebox.showinfo("Info", "No events to save")
            return
        
        filename = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        
        if filename:
            try:
                data = {
                    'events': [e.to_dict() for e in self.scheduler.events],
                    'selected': [e.to_dict() for e in self.scheduler.selected_events],
                    'rejected': [e.to_dict() for e in self.scheduler.rejected_events]
                }
                
                with open(filename, 'w') as f:
                    json.dump(data, f, indent=2)
                
                messagebox.showinfo("Success", "Schedule saved successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save: {str(e)}")
                
    def load_schedule(self):
        """Load schedule from JSON file."""
        filename = filedialog.askopenfilename(
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        
        if filename:
            try:
                with open(filename, 'r') as f:
                    data = json.load(f)
                
                self.scheduler.clear_events()
                
                # Load events
                for event_data in data['events']:
                    event = Event.from_dict(event_data)
                    self.scheduler.add_event(event)
                
                # Restore selected/rejected status if available
                if 'selected' in data:
                    selected_ids = {e['event_id'] for e in data['selected']}
                    for event in self.scheduler.events:
                        if event.event_id in selected_ids:
                            event.selected = True
                            self.scheduler.selected_events.append(event)
                
                if 'rejected' in data:
                    rejected_ids = {e['event_id'] for e in data['rejected']}
                    for event in self.scheduler.events:
                        if event.event_id in rejected_ids:
                            event.rejected = True
                            self.scheduler.rejected_events.append(event)
                
                self.event_counter = max((e.event_id for e in self.scheduler.events), default=0)
                
                self.update_event_list()
                self.timeline_canvas.update_events(self.scheduler.events)
                self.update_statistics()
                
                messagebox.showinfo("Success", f"Loaded {len(self.scheduler.events)} events!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load: {str(e)}")
                
    def load_sample_use_case(self, case_type: str):
        """Load sample use case data."""
        self.scheduler.clear_events()
        self.event_counter = 0
        
        samples = {
            'college': [
                ('Mathematics 101', 9.0, 10.5),
                ('Physics Lab', 9.5, 11.0),
                ('Computer Science', 10.0, 11.5),
                ('English Literature', 11.0, 12.5),
                ('Chemistry', 11.5, 13.0),
                ('Lunch Break', 12.5, 13.5),
                ('Biology', 13.0, 14.5),
                ('History', 14.0, 15.5),
                ('Physical Education', 15.0, 16.5),
                ('Study Hall', 16.0, 17.0)
            ],
            'conference': [
                ('Keynote Speech', 9.0, 10.0),
                ('AI Track Session 1', 9.5, 10.5),
                ('Workshop A', 10.0, 11.5),
                ('Panel Discussion', 10.5, 12.0),
                ('Networking Break', 11.5, 12.0),
                ('ML Track Session 2', 12.0, 13.0),
                ('Lunch Symposium', 12.5, 13.5),
                ('Poster Session', 13.0, 14.0),
                ('Tech Demo', 13.5, 15.0),
                ('Closing Remarks', 14.5, 15.5)
            ],
            'hospital': [
                ('Patient A Checkup', 9.0, 9.5),
                ('Patient B Surgery', 9.25, 11.0),
                ('Patient C Consultation', 10.0, 10.5),
                ('Patient D X-Ray', 10.5, 11.0),
                ('Staff Meeting', 11.0, 11.5),
                ('Patient E Therapy', 11.25, 12.5),
                ('Lunch Break', 12.0, 13.0),
                ('Patient F Emergency', 12.5, 13.5),
                ('Patient G Follow-up', 13.0, 13.5),
                ('Patient H Vaccination', 14.0, 14.5)
            ],
            'meeting': [
                ('Team Standup', 9.0, 9.5),
                ('Project Alpha Review', 9.25, 10.5),
                ('Client Call - Beta', 10.0, 11.0),
                ('Design Discussion', 10.5, 12.0),
                ('Budget Planning', 11.0, 12.5),
                ('Lunch Meeting', 12.0, 13.0),
                ('Sprint Planning', 13.0, 14.5),
                ('Code Review', 14.0, 15.0),
                ('Marketing Sync', 14.5, 15.5),
                ('Executive Briefing', 15.0, 16.0)
            ]
        }
        
        if case_type in samples:
            for name, start, end in samples[case_type]:
                self.event_counter += 1
                event = Event(name, start, end, self.event_counter)
                self.scheduler.add_event(event)
            
            self.update_event_list()
            self.timeline_canvas.update_events(self.scheduler.events)
            self.update_statistics()
            
            case_names = {
                'college': 'College Timetable',
                'conference': 'Conference Sessions',
                'hospital': 'Hospital Appointments',
                'meeting': 'Meeting Room Booking'
            }
            
            messagebox.showinfo(
                "Sample Loaded", 
                f"Loaded {case_names[case_type]} use case\n"
                f"{len(self.scheduler.events)} events added\n\n"
                f"Click 'Run Greedy Algorithm' to optimize!"
            )
            
    def show_about_algorithm(self):
        """Show information about the Greedy Algorithm."""
        about_window = tk.Toplevel(self.root)
        about_window.title("About Greedy Activity Selection Algorithm")
        about_window.geometry("800x700")
        about_window.resizable(False, False)
        
        # Create text widget with scrollbar
        text_frame = ttk.Frame(about_window)
        text_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        text = tk.Text(text_frame, wrap=tk.WORD, font=('Arial', 10), padx=10, pady=10)
        scrollbar = ttk.Scrollbar(text_frame, orient=tk.VERTICAL, command=text.yview)
        text.configure(yscrollcommand=scrollbar.set)
        
        text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Content
        content = """
GREEDY ACTIVITY SELECTION ALGORITHM
═══════════════════════════════════════════════════════════════════

OVERVIEW
────────
The Activity Selection Problem is a classic optimization problem in computer science.
Given a set of activities with start and finish times, the goal is to select the
maximum number of non-overlapping activities.

GREEDY STRATEGY
────────────────
The algorithm uses a greedy approach: always select the activity that finishes first
among the remaining activities. This greedy choice leads to an optimal solution.

WHY DOES IT WORK?
──────────────────
The greedy choice property: If we select the activity with the earliest finish time,
we leave the maximum amount of time available for remaining activities. This locally
optimal choice leads to a globally optimal solution.

ALGORITHM STEPS
───────────────
1. Sort all activities by finish time (earliest first)
   - Time: O(n log n)
   
2. Select the first activity (earliest finish time)
   - Time: O(1)
   
3. For each remaining activity:
   - If its start time ≥ last selected activity's finish time
     → Select it (greedy choice)
   - Otherwise, reject it (conflicts with schedule)
   - Time: O(n)

4. Return selected activities
   
TOTAL TIME COMPLEXITY: O(n log n)
Dominated by the sorting step. The selection process is linear O(n).

SPACE COMPLEXITY: O(n)
Storage for events and selected/rejected lists.

PROOF OF OPTIMALITY
────────────────────
Let A = {a1, a2, ..., ak} be the greedy solution (sorted by finish time)
Let O = {o1, o2, ..., om} be any optimal solution

If A ≠ O, we can show that replacing activities in O with those from A
maintains optimality, proving the greedy solution is also optimal.

The key insight: By choosing activities with earliest finish times, we
maximize opportunities for subsequent activities.

REAL-WORLD APPLICATIONS
────────────────────────
• College/School Timetable Planning
• Conference Session Scheduling
• Hospital Appointment Management
• Meeting Room Allocation
• CPU Task Scheduling
• Resource Booking Systems
• TV Commercial Scheduling
• Sports Event Planning

ADVANTAGES
──────────
✓ Simple to understand and implement
✓ Efficient: O(n log n) time complexity
✓ Provably optimal solution
✓ No backtracking needed
✓ Works in single pass after sorting

LIMITATIONS
───────────
• Only maximizes COUNT of activities, not other metrics
• Cannot handle weighted activities (different priorities)
• Cannot consider activity dependencies
• Assumes all activities have equal importance

COMPARISON WITH OTHER APPROACHES
─────────────────────────────────
• Brute Force: O(2^n) - tries all combinations
• Dynamic Programming: O(n²) - optimal but slower
• Greedy: O(n log n) - optimal and fastest

The greedy approach is preferred due to its efficiency and simplicity.

KEY TAKEAWAY
────────────
The Greedy Activity Selection Algorithm demonstrates how a simple local
optimization strategy (choosing earliest finish time) can yield a globally
optimal solution. It's a cornerstone example in algorithm design and analysis.
"""
        
        text.insert(1.0, content)
        text.configure(state=tk.DISABLED)
        
        # Close button
        close_btn = ttk.Button(about_window, text="Close", command=about_window.destroy)
        close_btn.pack(pady=10)
        
    def show_how_to_use(self):
        """Show how to use the application."""
        help_text = """
HOW TO USE THE SMART EVENT SCHEDULER
═══════════════════════════════════════════════════════════

BASIC USAGE
───────────
1. ADD EVENTS
   • Enter event name, start time, and end time
   • Click "Add Event"
   • Times can be decimal (e.g., 9.5 = 9:30)

2. DETECT CONFLICTS
   • Click "Detect Conflicts" to find overlapping events
   • Shows which events cannot be scheduled together

3. RUN GREEDY ALGORITHM
   • Click "Run Greedy Algorithm" to optimize
   • Algorithm selects maximum non-overlapping events
   • View results in timeline and event list

4. VIEW RESULTS
   • Green bars = Selected events
   • Red bars = Rejected events (conflicts)
   • Check statistics for efficiency metrics

FEATURES
────────
• Timeline Visualization: Visual representation of schedule
• Algorithm Steps: Detailed execution trace
• Statistics: Efficiency and complexity metrics
• Save/Load: Export and import schedules (JSON)
• Sample Use Cases: Pre-loaded scenarios
• Theme Switching: Light and dark modes
• Tooltips: Hover for helpful hints

MENU OPTIONS
─────────────
File Menu:
  • Save Schedule: Export to JSON
  • Load Schedule: Import from JSON

View Menu:
  • Light/Dark Theme: Change appearance

Sample Use Cases:
  • College Timetable
  • Conference Sessions
  • Hospital Appointments
  • Meeting Room Booking

Help Menu:
  • About Algorithm: Algorithm details
  • How to Use: This help screen

TIPS
────
• Start time must be less than end time
• Use decimal notation for fractional hours
• Run algorithm after adding all events
• Reset results to run algorithm again
• Check algorithm steps to understand decisions

KEYBOARD SHORTCUTS
──────────────────
• Enter: Add event (when in input field)
• Delete: Remove selected event
"""
        
        messagebox.showinfo("How to Use", help_text)
        
    def show_about(self):
        """Show about dialog."""
        about_text = """
Smart Event Scheduler
Version 1.0

A comprehensive demonstration of the Greedy Activity
Selection Algorithm from Design and Analysis of Algorithms.

Features:
• Greedy Activity Selection Algorithm
• Visual Timeline Representation
• Conflict Detection
• Step-by-step Algorithm Execution
• Multiple Real-world Use Cases
• Save/Load Functionality
• Dark/Light Themes

Time Complexity: O(n log n)
Space Complexity: O(n)

Developed in Python with Tkinter GUI

© 2026 - Educational Project
"""
        
        messagebox.showinfo("About", about_text)


def main():
    """Main entry point for the application."""
    root = tk.Tk()
    app = SmartEventSchedulerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
