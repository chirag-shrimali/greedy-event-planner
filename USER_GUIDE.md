# Smart Event Scheduler - User Guide

A comprehensive guide to using the Smart Event Scheduler application.

---

## Table of Contents
1. [Getting Started](#getting-started)
2. [Interface Overview](#interface-overview)
3. [Adding Events](#adding-events)
4. [Running the Algorithm](#running-the-algorithm)
5. [Understanding Results](#understanding-results)
6. [Advanced Features](#advanced-features)
7. [Tips & Best Practices](#tips--best-practices)
8. [Troubleshooting](#troubleshooting)

---

## Getting Started

### Launching the Application

1. Open terminal/command prompt
2. Navigate to project directory:
   ```bash
   cd path/to/smart-event-scheduler
   ```
3. Run the application:
   ```bash
   python smart_event_scheduler.py
   ```

### First Look

When the application starts, you'll see:
- **Left Panel**: Event input form and event list
- **Right Panel**: Timeline visualization, control buttons, algorithm steps, and statistics
- **Menu Bar**: File, View, Sample Use Cases, and Help options

---

## Interface Overview

### Left Panel

#### 1. Add New Event Section
- **Event Name**: Descriptive name for the event
- **Start Time**: When the event begins (decimal format)
- **End Time**: When the event ends (decimal format)
- **Add Event Button**: Adds the event to the scheduler

#### 2. Event List Section
Shows all events with columns:
- **Event Name**: Name of the event
- **Start**: Start time
- **End**: End time
- **Duration**: Event duration (calculated automatically)
- **Status**: Pending/Selected/Rejected

**Buttons:**
- **Delete Selected**: Remove selected event
- **Clear All**: Remove all events

### Right Panel

#### 1. Timeline Visualization
Graphical representation showing:
- **Green bars**: Selected events (optimal schedule)
- **Red bars**: Rejected events (conflicts)
- **Gray bars**: Not yet processed
- **Time axis**: Shows time progression
- **Legend**: Explains color coding

#### 2. Control Buttons
- **🚀 Run Greedy Algorithm**: Execute optimization
- **🔍 Detect Conflicts**: Find overlapping events
- **↺ Reset Results**: Clear results, keep events
- **📋 View Algorithm Steps**: Show detailed steps

#### 3. Algorithm Execution Steps
Text area showing:
- Sorting process
- Selection decisions
- Rejection reasons
- Algorithm summary

#### 4. Scheduling Statistics
Displays:
- **Total Events**: Number of events added
- **Scheduled**: Events selected by algorithm
- **Rejected**: Events not scheduled (conflicts)
- **Efficiency**: Percentage of events scheduled
- **Time Complexity**: O(n log n) explanation

---

## Adding Events

### Time Format

Times are entered in **decimal format**:
- `9.0` = 9:00 AM
- `9.5` = 9:30 AM
- `10.25` = 10:15 AM
- `14.75` = 2:45 PM (14:45)

### Step-by-Step

1. **Enter Event Name**
   - Click in "Event Name" field
   - Type descriptive name
   - Example: "Team Meeting"

2. **Enter Start Time**
   - Click in "Start Time" field
   - Enter decimal number
   - Example: `9.0`

3. **Enter End Time**
   - Click in "End Time" field
   - Enter decimal number (must be > start time)
   - Example: `10.5`

4. **Click "Add Event"**
   - Event appears in event list
   - Timeline updates automatically
   - Input fields clear for next entry

### Example Events

**Morning Schedule:**
```
Event: Morning Briefing
Start: 9.0
End: 9.5

Event: Project Review
Start: 9.5
End: 11.0

Event: Client Call
Start: 10.0
End: 11.0  (This will conflict with Project Review)
```

---

## Running the Algorithm

### Detect Conflicts (Optional)

Before optimization, you can check for conflicts:

1. Click **"🔍 Detect Conflicts"**
2. Dialog shows:
   - Number of conflicts found
   - List of conflicting event pairs
   - Suggestion to run greedy algorithm

**Example Output:**
```
Found 3 conflicts:

1. 'Project Review' [9.5-11.0] ↔ 'Client Call' [10.0-11.0]
2. 'Team Meeting' [11.0-12.0] ↔ 'Design Review' [11.5-13.0]
3. 'Lunch Break' [12.0-13.0] ↔ 'Design Review' [11.5-13.0]
```

### Run Greedy Algorithm

1. Click **"🚀 Run Greedy Algorithm"**
2. Algorithm executes in three phases:
   - **Sorting**: Events sorted by finish time
   - **Selection**: Greedy choices made
   - **Results**: Timeline and statistics updated

3. Success dialog shows:
   - Total events
   - Scheduled events
   - Rejected events
   - Efficiency percentage

### What Happens During Execution?

#### Phase 1: Sorting
Events are sorted by **finish time** (earliest first):
```
Before: [Event A (9-11), Event B (8-10), Event C (10-12)]
After:  [Event B (8-10), Event A (9-11), Event C (10-12)]
```

#### Phase 2: Greedy Selection
Algorithm selects events using greedy strategy:

1. **Select first event** (earliest finish time)
2. **For each remaining event:**
   - If start_time ≥ last_finish_time → **SELECT**
   - Otherwise → **REJECT** (conflict)

#### Phase 3: Update Display
- Timeline shows color-coded bars
- Event list shows status
- Statistics updated
- Algorithm steps displayed

---

## Understanding Results

### Timeline Visualization

**Color Coding:**
- 🟢 **Green**: Selected events (optimal schedule)
- 🔴 **Red**: Rejected events (conflicting)
- ⚪ **Gray**: Not yet processed

**Reading the Timeline:**
- **Horizontal axis**: Time progression
- **Vertical bars**: Events
- **Bar width**: Event duration
- **Bar position**: Event timing

### Algorithm Steps

The steps text area shows detailed execution trace:

```
STEP 1: Sort events by finish time (earliest first)
Original events: 5
Sorted order:
  1. Event A: [9.0, 10.0]
  2. Event B: [9.5, 11.0]
  3. Event C: [10.5, 12.0]
  ...

STEP 2: Select first event (earliest finish time)
✓ Selected: Event A (finish time: 10.0)

STEP 3: Process remaining events
Select event if start_time >= last_finish_time

✗ Rejected: Event B [9.5, 11.0]
   (conflicts: start 9.5 < last finish 10.0)
   
✓ Selected: Event C [10.5, 12.0]
   (start 10.5 >= last finish 10.0)
   
===================================================
ALGORITHM SUMMARY
===================================================
Total events: 5
Selected events: 3
Rejected events: 2
Efficiency: 60.0%

Time Complexity: O(n log n) - dominated by sorting
Space Complexity: O(n) - storing events and results
```

### Statistics Panel

**Metrics Explained:**

1. **Total Events**: Number of events in scheduler
   - All events you added
   
2. **Scheduled**: Events selected by algorithm
   - Non-overlapping events
   - Maximum possible count
   
3. **Rejected**: Events not scheduled
   - Conflicting events
   - Could not fit in optimal schedule
   
4. **Efficiency**: Percentage scheduled
   - Formula: (Scheduled / Total) × 100
   - Higher is better
   - 100% = no conflicts
   - 50% = half the events conflict
   
5. **Time Complexity**: Algorithm performance
   - O(n log n) due to sorting
   - Very efficient even for large schedules

---

## Advanced Features

### Saving Schedules

**To Save:**
1. Click **File → Save Schedule**
2. Choose location and filename
3. File saved in JSON format

**Use Cases:**
- Backup your work
- Share schedules with others
- Compare different scenarios
- Create reusable templates

### Loading Schedules

**To Load:**
1. Click **File → Load Schedule**
2. Select JSON file
3. Events loaded automatically

**What Gets Loaded:**
- All events with details
- Selection status (if previously optimized)
- Timeline updates automatically

### Sample Use Cases

Pre-configured scenarios for different domains:

#### 1. College Timetable
**Sample Use Cases → College Timetable**
- 10 class/activity events
- Typical school day schedule
- Mix of lectures, labs, breaks

#### 2. Conference Sessions
**Sample Use Cases → Conference Sessions**
- 10 conference events
- Keynotes, workshops, panels
- Networking and social events

#### 3. Hospital Appointments
**Sample Use Cases → Hospital Appointments**
- 10 patient appointments
- Checkups, surgeries, consultations
- Staff meetings and breaks

#### 4. Meeting Room Booking
**Sample Use Cases → Meeting Room Booking**
- 10 meeting events
- Team meetings, client calls
- Project reviews and planning

### Theme Switching

**Light Theme:**
- View → Light Theme
- Default theme
- Best for bright environments

**Dark Theme:**
- View → Dark Theme
- Reduced eye strain
- Professional appearance
- Better for presentations

### Viewing Detailed Steps

For larger window with full algorithm trace:

1. Run algorithm first
2. Click **"📋 View Algorithm Steps"**
3. New window opens with:
   - Full step-by-step execution
   - Scrollable text area
   - Read-only format

### Resetting Results

**To Reset:**
1. Click **"↺ Reset Results"**
2. Confirmation appears
3. Results cleared, events preserved

**What Gets Reset:**
- Selection status
- Rejection status
- Algorithm steps
- Statistics (except total events)

**What's Preserved:**
- All events
- Event details
- Timeline (shows gray bars)

---

## Tips & Best Practices

### Input Tips

1. **Use Consistent Time Format**
   - Stick to decimal notation
   - Example: 9.5 instead of 9:30
   
2. **Meaningful Names**
   - Use descriptive event names
   - Example: "Client Call - ABC Corp" not "Call 1"
   
3. **Realistic Durations**
   - Consider buffer times
   - Account for transitions
   
4. **Check Before Adding**
   - Verify times are logical
   - Start < End always

### Optimization Tips

1. **Review Conflicts First**
   - Use "Detect Conflicts" before optimization
   - Understand what needs resolving
   
2. **Analyze Rejected Events**
   - Check why events were rejected
   - Consider if you can adjust times
   
3. **Aim for High Efficiency**
   - 80%+ is excellent
   - <50% suggests too many conflicts
   
4. **Save Different Scenarios**
   - Try different event arrangements
   - Compare efficiency metrics

### Presentation Tips

1. **Use Dark Theme**
   - Better for projectors
   - Professional appearance
   
2. **Load Sample Use Case**
   - Quick demonstration
   - Shows real-world application
   
3. **Show Algorithm Steps**
   - Educational value
   - Demonstrates greedy strategy
   
4. **Explain Color Coding**
   - Point out green/red meaning
   - Connect to greedy decisions

---

## Troubleshooting

### Common Issues

#### Problem: "Invalid time format" error
**Solution:**
- Use numeric values only
- Use decimal point (.) not colon (:)
- Example: 9.5 not 9:30

#### Problem: Events not appearing in timeline
**Solution:**
- Check if timeline canvas is visible
- Resize window to refresh
- Reset results and try again

#### Problem: "Start time must be before end time"
**Solution:**
- Verify start < end
- Check for typos in input
- Use larger end time value

#### Problem: Algorithm shows no selected events
**Solution:**
- Check if events were added
- Verify events have valid times
- Look for all events having same time range

#### Problem: Can't delete event
**Solution:**
- Click on event in list first
- Ensure event is selected (highlighted)
- Use "Clear All" as alternative

#### Problem: JSON file won't load
**Solution:**
- Verify file format is valid JSON
- Check file wasn't corrupted
- Try loading sample files first

### Performance Issues

#### Slow rendering with many events
**Solution:**
- Timeline may take time with 100+ events
- Consider splitting into smaller schedules
- Close other applications

#### Application not responding
**Solution:**
- Wait for algorithm to complete
- Very large datasets (1000+ events) may take time
- Consider using fewer events for testing

---

## Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| Add event (when in input field) | Enter |
| Delete selected event | Delete |
| Close dialogs | Escape |

---

## File Formats

### JSON Structure

Saved schedules use this format:

```json
{
  "events": [
    {
      "name": "Event Name",
      "start_time": 9.0,
      "end_time": 10.5,
      "event_id": 1
    }
  ],
  "selected": [...],
  "rejected": [...]
}
```

**Fields:**
- `name`: Event name (string)
- `start_time`: Start time (number)
- `end_time`: End time (number)
- `event_id`: Unique identifier (integer)

---

## Getting Help

### Within the Application

1. **Tooltips**: Hover over buttons/fields
2. **About Algorithm**: Help → About Algorithm
3. **How to Use**: Help → How to Use
4. **About**: Help → About

### External Resources

- **Algorithm Theory**: See README.md
- **Code Documentation**: See docstrings in source
- **Issues**: GitHub Issues page

---

## Best Practices Checklist

Before Running Algorithm:
- [ ] All events added
- [ ] Times verified (start < end)
- [ ] Event names are descriptive
- [ ] Checked for obvious conflicts

After Running Algorithm:
- [ ] Reviewed selected events
- [ ] Understood rejected events
- [ ] Checked efficiency percentage
- [ ] Read algorithm steps
- [ ] Saved schedule if needed

For Presentations:
- [ ] Loaded relevant use case
- [ ] Switched to dark theme
- [ ] Explained greedy strategy
- [ ] Showed algorithm steps
- [ ] Demonstrated timeline visualization

---

**Last Updated: January 2026**

For more information, see README.md or visit the project repository.
