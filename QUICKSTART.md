# Quick Start Guide - Smart Event Scheduler

Get started with the Smart Event Scheduler in 5 minutes!

---

## Installation

### Prerequisites
- Python 3.7 or higher
- Tkinter (usually included with Python)

### Setup

1. **Download the project files**
2. **Open terminal/command prompt**
3. **Navigate to project folder:**
   ```bash
   cd path/to/smart-event-scheduler
   ```

4. **Run the application:**
   ```bash
   python smart_event_scheduler.py
   ```

---

## 5-Minute Tutorial

### Option 1: Try a Sample Use Case (Fastest)

1. **Load a sample:**
   - Click **Sample Use Cases** menu
   - Choose **College Timetable**
   - 10 events loaded automatically!

2. **Run the algorithm:**
   - Click **🚀 Run Greedy Algorithm** button
   - Watch the optimization happen!

3. **View results:**
   - ✅ Green bars = Selected events
   - ❌ Red bars = Rejected events
   - 📊 Check statistics panel

**Done!** You've just optimized a schedule using the Greedy Algorithm.

---

### Option 2: Create Your Own Schedule

1. **Add events:**
   ```
   Event Name: "Morning Meeting"
   Start Time: 9.0
   End Time: 10.0
   Click "Add Event"
   ```

2. **Add more events** (create some conflicts):
   ```
   Event: "Project Review"
   Start: 9.5
   End: 11.0
   
   Event: "Client Call"
   Start: 10.5
   End: 12.0
   
   Event: "Lunch Break"
   Start: 12.0
   End: 13.0
   
   Event: "Team Planning"
   Start: 12.5
   End: 14.0
   ```

3. **Detect conflicts (optional):**
   - Click **🔍 Detect Conflicts**
   - See which events overlap

4. **Run optimization:**
   - Click **🚀 Run Greedy Algorithm**
   - Algorithm selects maximum non-overlapping events!

5. **Understand the results:**
   - Check the **Timeline Visualization**
   - Read **Algorithm Execution Steps**
   - View **Statistics** (efficiency, complexity)

---

## Understanding the Interface

```
┌─────────────────────────────────────────────────────────────┐
│  File    View    Sample Use Cases    Help                   │
├──────────────────┬──────────────────────────────────────────┤
│ ADD NEW EVENT    │  TIMELINE VISUALIZATION                  │
│                  │  [Green & Red Bars Timeline]             │
│ Event Name: ____ │                                          │
│ Start Time: ____ │  CONTROL BUTTONS                         │
│ End Time:   ____ │  [Run] [Detect] [Reset] [Steps]         │
│ [Add Event]      │                                          │
│                  │  ALGORITHM STEPS    │  STATISTICS        │
│ EVENT LIST       │  Step 1: Sort...   │  Total: 10         │
│ ┌──────────────┐ │  Step 2: Select... │  Scheduled: 6      │
│ │Name  S  E  D │ │  Step 3: Process...│  Rejected: 4       │
│ │Event1 9 10 1h│ │  ...               │  Efficiency: 60%   │
│ │Event2 ...    │ │                    │  O(n log n)        │
│ └──────────────┘ │                    │                    │
│ [Delete] [Clear] │                    │                    │
└──────────────────┴────────────────────┴────────────────────┘
```

---

## Key Features

### 🚀 Run Greedy Algorithm
- Optimizes schedule automatically
- Maximizes non-overlapping events
- O(n log n) time complexity

### 🔍 Detect Conflicts
- Finds overlapping events
- Shows conflict pairs
- Helps understand problem before optimization

### 📊 Timeline Visualization
- **Green bars**: Selected (scheduled)
- **Red bars**: Rejected (conflicts)
- **Gray bars**: Not processed yet

### 📋 Algorithm Steps
- Detailed execution trace
- Shows sorting process
- Explains each decision

### 💾 Save/Load
- Export to JSON
- Share schedules
- Create templates

### 🎨 Themes
- Light theme (default)
- Dark theme (professional)

---

## Time Format

Events use **decimal time format**:

| Decimal | Clock Time | Decimal | Clock Time |
|---------|-----------|---------|-----------|
| 9.0 | 9:00 AM | 14.0 | 2:00 PM |
| 9.25 | 9:15 AM | 14.25 | 2:15 PM |
| 9.5 | 9:30 AM | 14.5 | 2:30 PM |
| 9.75 | 9:45 AM | 14.75 | 2:45 PM |
| 10.0 | 10:00 AM | 15.0 | 3:00 PM |

**Formula:** Decimal time = Hours + (Minutes / 60)

---

## Sample Scenarios

### College Timetable
10 classes with overlaps → Algorithm finds optimal schedule

### Conference Sessions
Multiple tracks → Maximize sessions attended

### Hospital Appointments
Doctor's schedule → Optimize patient appointments

### Meeting Rooms
Booking conflicts → Maximize room utilization

---

## Common Tasks

### How do I add an event?
1. Fill in name, start time, end time
2. Click "Add Event"

### How do I run the algorithm?
1. Add events first
2. Click "🚀 Run Greedy Algorithm"

### How do I see detailed steps?
1. Run algorithm first
2. Check "Algorithm Execution Steps" panel
3. Or click "📋 View Algorithm Steps" for larger view

### How do I save my schedule?
1. File → Save Schedule
2. Choose location and filename
3. Saves as JSON

### How do I load a schedule?
1. File → Load Schedule
2. Select JSON file
3. Events load automatically

### How do I change themes?
- View → Light Theme
- View → Dark Theme

### How do I reset results?
1. Click "↺ Reset Results"
2. Keeps events, clears optimization results

### How do I clear everything?
1. Click "Clear All" button
2. Removes all events

---

## Quick Tips

💡 **Tooltip hints**: Hover over buttons for explanations

💡 **Start with samples**: Try pre-loaded use cases first

💡 **Check conflicts**: Use conflict detection before optimization

💡 **Read steps**: Algorithm steps explain every decision

💡 **Dark theme**: Better for presentations

💡 **Save often**: Export schedules for backup

---

## What's Next?

### Learn More
- Read **USER_GUIDE.md** for comprehensive documentation
- Check **README.md** for algorithm theory
- Explore **Help → About Algorithm** in the app

### Experiment
- Try different event combinations
- Compare efficiency percentages
- Test edge cases (all overlap, no overlap)

### Share
- Save and share schedules
- Present algorithm execution
- Demonstrate greedy strategy

---

## Troubleshooting

### "Invalid time format" error
→ Use decimal format (e.g., 9.5 not 9:30)

### Events not showing in timeline
→ Try resizing window or reset results

### Can't delete event
→ Select event in list first, then click "Delete Selected"

### Algorithm seems slow
→ Normal for 100+ events, wait for completion

---

## Need Help?

- **In-app help**: Help menu → How to Use
- **Algorithm info**: Help menu → About Algorithm
- **Full documentation**: See USER_GUIDE.md
- **Issues**: Check README.md for contact info

---

## Example Session

Here's a complete example walkthrough:

```
1. Launch application
   $ python smart_event_scheduler.py

2. Load sample
   Sample Use Cases → College Timetable
   ✓ 10 events loaded

3. Check conflicts
   Click "🔍 Detect Conflicts"
   → "Found 7 conflicts"

4. Optimize
   Click "🚀 Run Greedy Algorithm"
   ✓ Algorithm complete!

5. Review results
   - Timeline: Green/red bars shown
   - Statistics: 6 scheduled, 4 rejected, 60% efficiency
   - Steps: Detailed trace available

6. Save schedule
   File → Save Schedule
   ✓ Saved as "college_optimized.json"
```

**Total time: 2 minutes!**

---

## Quick Reference Card

### Main Actions
| Button | Action |
|--------|--------|
| Add Event | Add new event to scheduler |
| Run Algorithm | Optimize schedule (greedy) |
| Detect Conflicts | Find overlapping events |
| Reset Results | Clear optimization, keep events |
| Clear All | Remove all events |
| View Steps | Show detailed algorithm trace |

### Menus
| Menu | Options |
|------|---------|
| File | Save, Load, Exit |
| View | Light Theme, Dark Theme |
| Sample Use Cases | College, Conference, Hospital, Meeting |
| Help | About Algorithm, How to Use, About |

### Time Format
- Use decimals: 9.5 = 9:30 AM
- Start must be < End
- Non-negative values only

### Color Coding
- 🟢 Green = Selected
- 🔴 Red = Rejected
- ⚪ Gray = Pending

---

**Ready to optimize schedules? Launch the app and try it now!**

```bash
python smart_event_scheduler.py
```

---

*For detailed documentation, see USER_GUIDE.md*

*Last Updated: January 2026*
