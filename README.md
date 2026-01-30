# Smart Event Scheduler using Greedy Algorithm

A comprehensive Python application demonstrating the **Greedy Activity Selection Algorithm** from Design and Analysis of Algorithms with a modern Tkinter GUI.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)
![Algorithm](https://img.shields.io/badge/Algorithm-Greedy-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Algorithm Explanation](#algorithm-explanation)
- [Installation](#installation)
- [Usage](#usage)
- [Use Cases](#use-cases)
- [Screenshots](#screenshots)
- [Project Structure](#project-structure)
- [Technical Details](#technical-details)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

The **Smart Event Scheduler** is an educational project that visualizes and demonstrates the **Greedy Activity Selection Algorithm**, a fundamental algorithm in computer science for optimizing event scheduling. The application helps users understand how greedy algorithms work by providing:

- Interactive event management
- Real-time conflict detection
- Step-by-step algorithm execution
- Visual timeline representation
- Multiple real-world use case scenarios

**Key Algorithm:** Greedy Activity Selection  
**Time Complexity:** O(n log n)  
**Space Complexity:** O(n)

---

## ✨ Features

### Core Functionality
- ✅ **Event Management**: Add, delete, and manage events with name, start time, and end time
- ✅ **Conflict Detection**: Automatically detect scheduling conflicts between overlapping events
- ✅ **Greedy Optimization**: Apply greedy algorithm to maximize non-overlapping events
- ✅ **Visual Timeline**: Graphical timeline with colored horizontal bars
  - 🟢 Green: Selected events (optimal schedule)
  - 🔴 Red: Rejected events (conflicts)
  - ⚪ Gray: Not yet processed

### Algorithm Features
- 📊 **Step-by-Step Execution**: Detailed trace of algorithm decisions
- 📈 **Statistics Display**: 
  - Total events
  - Scheduled events
  - Rejected events
  - Scheduling efficiency percentage
- ⏱️ **Complexity Analysis**: Shows O(n log n) time complexity explanation
- 🔄 **Sorting Visualization**: View events before and after greedy selection

### User Interface
- 🎨 **Modern GUI**: Clean, presentation-ready interface
- 🌓 **Theme Switching**: Dark and light themes
- 💾 **Save/Load**: Export and import schedules using JSON
- ♻️ **Reset Options**: Clear results or all events
- 💡 **Tooltips**: Helpful explanations throughout the interface
- 📖 **About Dialog**: Comprehensive algorithm explanation

### Sample Use Cases
1. 🎓 **College Timetable Planning**: Optimize class schedules
2. 🎤 **Conference Session Scheduling**: Maximize concurrent sessions
3. 🏥 **Hospital Appointment Management**: Optimize patient scheduling
4. 🏢 **Meeting Room Booking**: Maximize room utilization

---

## 🧮 Algorithm Explanation

### The Greedy Activity Selection Algorithm

The algorithm solves the **Activity Selection Problem**: Given a set of activities with start and finish times, select the maximum number of non-overlapping activities.

#### Strategy
The greedy approach always selects the activity with the **earliest finish time** among remaining activities. This locally optimal choice leads to a globally optimal solution.

#### Why It Works (Greedy Choice Property)
By selecting activities that finish earliest, we maximize the time available for subsequent activities, allowing us to schedule the maximum number of events.

#### Algorithm Steps

```
1. Sort all events by finish time (earliest first)
   Time: O(n log n)

2. Select the first event
   Time: O(1)

3. For each remaining event:
   - If start_time >= last_selected_finish_time:
       Select it (no conflict)
   - Else:
       Reject it (conflicts with schedule)
   Time: O(n)

4. Return selected events

Total Time Complexity: O(n log n)
```

#### Pseudocode

```python
def greedy_activity_selection(events):
    # Sort by finish time
    sorted_events = sort(events, key=finish_time)  # O(n log n)
    
    selected = [sorted_events[0]]  # Select first event
    last_finish = sorted_events[0].end_time
    
    for event in sorted_events[1:]:  # O(n)
        if event.start_time >= last_finish:
            selected.append(event)
            last_finish = event.end_time
    
    return selected
```

#### Proof of Optimality

Let **A** = greedy solution, **O** = optimal solution

- If A ≠ O, we can replace activities in O with those from A
- This replacement maintains optimality
- Therefore, greedy solution is also optimal

**Key Insight:** Choosing earliest finish times maximizes opportunities for future activities.

---

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- Tkinter (usually included with Python)

### Installation Steps

1. **Clone or Download the Repository**
   ```bash
   git clone https://github.com/yourusername/smart-event-scheduler.git
   cd smart-event-scheduler
   ```

2. **Verify Python Installation**
   ```bash
   python --version
   ```

3. **Check Tkinter (Optional)**
   ```bash
   python -m tkinter
   ```
   A small window should appear if Tkinter is installed.

4. **No Additional Dependencies Required**  
   The project uses only Python standard library modules.

---

## 💻 Usage

### Running the Application

```bash
python smart_event_scheduler.py
```

### Basic Workflow

1. **Add Events**
   - Enter event name (e.g., "Math Class")
   - Enter start time (e.g., 9.0 for 9:00 AM)
   - Enter end time (e.g., 10.5 for 10:30 AM)
   - Click "Add Event"

2. **Detect Conflicts (Optional)**
   - Click "🔍 Detect Conflicts"
   - View overlapping events

3. **Run Greedy Algorithm**
   - Click "🚀 Run Greedy Algorithm"
   - Algorithm optimizes schedule
   - View results in timeline and event list

4. **Analyze Results**
   - Check timeline visualization
   - Review algorithm steps
   - View statistics

5. **Save/Load Schedules**
   - File → Save Schedule (JSON format)
   - File → Load Schedule

### Sample Use Cases

Load pre-configured scenarios from the menu:
- **Sample Use Cases → College Timetable**
- **Sample Use Cases → Conference Sessions**
- **Sample Use Cases → Hospital Appointments**
- **Sample Use Cases → Meeting Room Booking**

### Keyboard Shortcuts

- **Enter**: Add event (when in input field)
- **Delete**: Remove selected event

---

## 🎯 Use Cases

### 1. College Timetable Planning
**Scenario:** Schedule maximum classes without conflicts

**Sample Events:**
- Mathematics 101: 9:00 - 10:30
- Physics Lab: 9:30 - 11:00
- Computer Science: 10:00 - 11:30
- English Literature: 11:00 - 12:30

**Greedy Solution:** Selects non-overlapping classes to maximize course attendance

### 2. Conference Session Scheduling
**Scenario:** Maximize concurrent session attendance

**Sample Events:**
- Keynote Speech: 9:00 - 10:00
- AI Track Session: 9:30 - 10:30
- Workshop A: 10:00 - 11:30
- Panel Discussion: 10:30 - 12:00

**Greedy Solution:** Optimal session schedule for single attendee

### 3. Hospital Appointment Management
**Scenario:** Optimize doctor's appointment schedule

**Sample Events:**
- Patient A Checkup: 9:00 - 9:30
- Patient B Surgery: 9:15 - 11:00
- Patient C Consultation: 10:00 - 10:30

**Greedy Solution:** Maximum patients seen without overlaps

### 4. Meeting Room Booking
**Scenario:** Maximize meeting room utilization

**Sample Events:**
- Team Standup: 9:00 - 9:30
- Project Review: 9:15 - 10:30
- Client Call: 10:00 - 11:00

**Greedy Solution:** Optimal room booking schedule

---

## 📸 Screenshots

### Main Interface
*The main window shows event input, timeline visualization, algorithm steps, and statistics*

### Timeline Visualization
- **Green Bars**: Selected events (optimal schedule)
- **Red Bars**: Rejected events (conflicts)
- **Time Axis**: Shows time progression with labels

### Algorithm Steps
*Detailed trace showing:*
- Sorting by finish time
- Selection decisions
- Rejection reasons
- Final statistics

### Dark Theme
*Professional dark mode for reduced eye strain*

---

## 📁 Project Structure

```
smart-event-scheduler/
│
├── smart_event_scheduler.py    # Main application file
├── README.md                    # Project documentation
├── requirements.txt             # Python dependencies (empty - uses stdlib)
├── LICENSE                      # MIT License
│
├── samples/                     # Sample schedule files (JSON)
│   ├── college_schedule.json
│   ├── conference_schedule.json
│   ├── hospital_schedule.json
│   └── meeting_schedule.json
│
└── screenshots/                 # Application screenshots
    ├── main_interface.png
    ├── timeline_view.png
    ├── algorithm_steps.png
    └── dark_theme.png
```

---

## 🔧 Technical Details

### Architecture

#### Classes

1. **Event**
   - Represents a single event
   - Properties: name, start_time, end_time, event_id, selected, rejected
   - Methods: to_dict(), from_dict()

2. **GreedyScheduler**
   - Core algorithm implementation
   - Methods:
     - `add_event()`: Add event to scheduler
     - `detect_conflicts()`: Find overlapping events
     - `greedy_schedule()`: Apply greedy algorithm
     - `get_statistics()`: Calculate metrics

3. **TimelineCanvas**
   - Custom canvas for visualization
   - Methods:
     - `draw_timeline()`: Render event bars
     - `update_events()`: Refresh display
     - `set_theme()`: Apply color theme

4. **SmartEventSchedulerApp**
   - Main GUI application
   - Manages all UI components
   - Coordinates between GUI and algorithm

### Technology Stack

- **Language**: Python 3.7+
- **GUI Framework**: Tkinter
- **Data Format**: JSON for save/load
- **Standard Library Only**: No external dependencies

### Code Organization

```python
# Modular Functions:

# Event Management
- add_event()
- delete_event()
- clear_all_events()

# Conflict Detection
- detect_conflicts()

# Greedy Scheduling
- greedy_schedule()

# Timeline Drawing
- draw_timeline()
- update_events()

# File Handling
- save_schedule()
- load_schedule()

# UI Components
- create_input_section()
- create_timeline_section()
- create_steps_section()
- create_statistics_section()
```

### Algorithm Complexity

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Sorting events | O(n log n) | O(n) |
| Selecting events | O(n) | O(n) |
| Conflict detection | O(n²) | O(1) |
| **Total** | **O(n log n)** | **O(n)** |

---

## 🎓 Educational Value

### Learning Objectives

This project helps students understand:

1. **Greedy Algorithms**
   - Greedy choice property
   - Optimal substructure
   - Proof of correctness

2. **Algorithm Analysis**
   - Time complexity calculation
   - Space complexity analysis
   - Best/worst case scenarios

3. **Data Structures**
   - Lists and sorting
   - Object-oriented design
   - Event handling

4. **GUI Development**
   - Tkinter framework
   - Event-driven programming
   - User interface design

### Comparison with Other Approaches

| Approach | Time Complexity | Optimal? | Notes |
|----------|----------------|----------|-------|
| Brute Force | O(2^n) | Yes | Too slow for large n |
| Dynamic Programming | O(n²) | Yes | Slower than greedy |
| **Greedy** | **O(n log n)** | **Yes** | **Fastest optimal** |

---

## 🚀 Future Enhancements

### Potential Features

1. **Advanced Scheduling**
   - [ ] Weighted events (priority-based)
   - [ ] Multi-resource scheduling
   - [ ] Recurring events
   - [ ] Break/buffer time

2. **Visualization**
   - [ ] Animation of algorithm execution
   - [ ] Multiple timeline views
   - [ ] Gantt chart representation
   - [ ] Export timeline as image

3. **Analysis**
   - [ ] Compare with other algorithms
   - [ ] Performance benchmarking
   - [ ] What-if scenarios
   - [ ] Optimization suggestions

4. **Integration**
   - [ ] Calendar import (iCal format)
   - [ ] Google Calendar sync
   - [ ] Excel export
   - [ ] Database storage

5. **User Experience**
   - [ ] Drag-and-drop events
   - [ ] Time range picker
   - [ ] Custom color schemes
   - [ ] Internationalization

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the Repository**
2. **Create a Feature Branch**
   ```bash
   git checkout -b feature/YourFeature
   ```
3. **Commit Your Changes**
   ```bash
   git commit -m "Add YourFeature"
   ```
4. **Push to Branch**
   ```bash
   git push origin feature/YourFeature
   ```
5. **Open a Pull Request**

### Contribution Guidelines

- Follow PEP 8 style guide
- Add docstrings to functions
- Include comments for complex logic
- Test thoroughly before submitting
- Update README if needed

---

## 📝 License

This project is licensed under the MIT License.

```
MIT License

Copyright (c) 2026 Smart Event Scheduler

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 📧 Contact

For questions, suggestions, or feedback:

- **GitHub Issues**: [Report bugs or request features](https://github.com/yourusername/smart-event-scheduler/issues)
- **Email**: your.email@example.com

---

## 🙏 Acknowledgments

- Algorithm concepts from "Introduction to Algorithms" (CLRS)
- Inspired by real-world scheduling challenges
- Built for educational purposes

---

## 📚 References

1. **Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C.** (2009). *Introduction to Algorithms* (3rd ed.). MIT Press.

2. **Kleinberg, J., & Tardos, É.** (2005). *Algorithm Design*. Pearson.

3. **Greedy Algorithms**: [Wikipedia](https://en.wikipedia.org/wiki/Greedy_algorithm)

4. **Activity Selection Problem**: [GeeksforGeeks](https://www.geeksforgeeks.org/activity-selection-problem-greedy-algo-1/)

---

## ⭐ Star This Repository

If you find this project helpful, please consider giving it a star! ⭐

---

**Made with ❤️ for Algorithm Enthusiasts**

*Last Updated: January 2026*
