# How to Run - Smart Event Scheduler

Quick reference for running the application.

---

## Prerequisites

- **Python 3.7 or higher** installed
- **Tkinter** (usually comes with Python)

### Check Python Version

Open terminal/command prompt and run:

```bash
python --version
```

or

```bash
python3 --version
```

You should see: `Python 3.7.x` or higher

---

## Running the Application

### Method 1: Direct Execution (Recommended)

**Windows:**
```cmd
cd C:\Users\CHIRAG\Downloads\Cursor
python smart_event_scheduler.py
```

**macOS/Linux:**
```bash
cd /path/to/Cursor
python3 smart_event_scheduler.py
```

### Method 2: Double-Click (Windows)

1. Navigate to the folder in File Explorer
2. Double-click `smart_event_scheduler.py`
3. If prompted, select Python to open the file

---

## Running Tests

To verify the algorithm works correctly:

**Windows:**
```cmd
python test_scheduler.py
```

**macOS/Linux:**
```bash
python3 test_scheduler.py
```

You should see:
```
======================================================================
ALL TESTS PASSED! ✓
======================================================================
```

---

## Troubleshooting

### Issue: "python is not recognized"

**Solution:**
- Install Python from python.org
- Make sure to check "Add Python to PATH" during installation

### Issue: "No module named 'tkinter'"

**Solution:**

**Windows:** Tkinter comes with Python - reinstall Python

**Ubuntu/Debian:**
```bash
sudo apt-get install python3-tk
```

**macOS:** Tkinter comes with Python

**Fedora:**
```bash
sudo dnf install python3-tkinter
```

### Issue: Application window is blank

**Solution:**
- Try resizing the window
- Make sure you're using Python 3.7+
- Check if Tkinter is properly installed

### Issue: Unicode errors in test output (Windows)

**Solution:**
- The tests will still pass
- This is just a console encoding issue
- The main application works fine

---

## First-Time Users

### Quick Demo (2 minutes)

1. **Run the application**
   ```bash
   python smart_event_scheduler.py
   ```

2. **Load a sample**
   - Click: **Sample Use Cases → College Timetable**

3. **Run the algorithm**
   - Click: **🚀 Run Greedy Algorithm**

4. **View results**
   - Check the colored timeline
   - Read algorithm steps
   - View statistics

**Done!** You've just optimized a schedule using the Greedy Algorithm.

---

## File Structure

After running, your folder contains:

```
Cursor/
├── smart_event_scheduler.py    ← Main application
├── test_scheduler.py            ← Test suite
├── README.md                    ← Full documentation
├── USER_GUIDE.md                ← User manual
├── QUICKSTART.md                ← Quick start
├── PRESENTATION_GUIDE.md        ← Presentation help
├── PROJECT_SUMMARY.md           ← Project overview
├── HOW_TO_RUN.md                ← This file
├── LICENSE                      ← MIT License
├── requirements.txt             ← Dependencies
└── samples/                     ← Sample files
    ├── college_schedule.json
    ├── conference_schedule.json
    ├── hospital_schedule.json
    └── meeting_schedule.json
```

---

## Next Steps

### Learn More
- Read **QUICKSTART.md** for a 5-minute tutorial
- Read **USER_GUIDE.md** for comprehensive instructions
- Check **PRESENTATION_GUIDE.md** if presenting the project

### Explore Features
- Try different sample use cases
- Add your own events
- Save and load schedules
- Switch between light and dark themes
- View detailed algorithm steps

### For Presentations
1. Run the application
2. Load a sample use case
3. Follow the PRESENTATION_GUIDE.md script
4. Use dark theme for better projector visibility

---

## Support

### Documentation
- **README.md** - Complete project documentation
- **USER_GUIDE.md** - Detailed user manual
- **QUICKSTART.md** - Fast start guide

### In-App Help
- **Help → About Algorithm** - Algorithm explanation
- **Help → How to Use** - Usage instructions
- **Tooltips** - Hover over buttons for hints

---

## Common Commands Reference

| Task | Command |
|------|---------|
| Run application | `python smart_event_scheduler.py` |
| Run tests | `python test_scheduler.py` |
| Check Python version | `python --version` |
| Check Tkinter | `python -m tkinter` |

---

## Quick Keyboard Reference

| Action | Key |
|--------|-----|
| Add event (in input field) | Enter |
| Delete selected event | Delete |
| Close dialogs | Escape |

---

## Example Session

```bash
# 1. Navigate to project folder
cd C:\Users\CHIRAG\Downloads\Cursor

# 2. Run the application
python smart_event_scheduler.py

# Application window opens
# 3. Use the menu: Sample Use Cases → College Timetable
# 4. Click: 🚀 Run Greedy Algorithm
# 5. View results in timeline and statistics

# To close: Click X or File → Exit
```

---

## Platform-Specific Notes

### Windows
- Use `python` command
- Paths use backslashes: `C:\Users\...`
- May see PowerShell errors in output (ignore them)

### macOS/Linux
- Use `python3` command
- Paths use forward slashes: `/home/...`
- May need to install tkinter separately

---

**Ready to start? Run the application now:**

```bash
python smart_event_scheduler.py
```

---

*Last Updated: January 2026*
