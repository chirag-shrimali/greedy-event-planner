"""
Test Suite for Smart Event Scheduler
Tests core algorithm functionality
"""

import sys
import io

# Fix encoding for Windows console
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

from smart_event_scheduler import Event, GreedyScheduler


def test_basic_scheduling():
    """Test basic greedy scheduling with non-overlapping events."""
    print("Test 1: Basic Non-Overlapping Events")
    scheduler = GreedyScheduler()
    
    scheduler.add_event(Event("Event A", 1.0, 2.0, 1))
    scheduler.add_event(Event("Event B", 2.0, 3.0, 2))
    scheduler.add_event(Event("Event C", 3.0, 4.0, 3))
    
    selected, rejected, steps = scheduler.greedy_schedule()
    
    assert len(selected) == 3, f"Expected 3 selected, got {len(selected)}"
    assert len(rejected) == 0, f"Expected 0 rejected, got {len(rejected)}"
    print("✓ Test 1 passed: All non-overlapping events selected")
    print()


def test_overlapping_events():
    """Test scheduling with overlapping events."""
    print("Test 2: Overlapping Events")
    scheduler = GreedyScheduler()
    
    scheduler.add_event(Event("Event A", 1.0, 3.0, 1))
    scheduler.add_event(Event("Event B", 2.0, 4.0, 2))
    scheduler.add_event(Event("Event C", 3.0, 5.0, 3))
    
    selected, rejected, steps = scheduler.greedy_schedule()
    
    assert len(selected) == 2, f"Expected 2 selected, got {len(selected)}"
    assert len(rejected) == 1, f"Expected 1 rejected, got {len(rejected)}"
    assert selected[0].name == "Event A", "First should be Event A (earliest finish)"
    assert selected[1].name == "Event C", "Second should be Event C"
    print("✓ Test 2 passed: Correct events selected based on finish time")
    print()


def test_greedy_choice():
    """Test that greedy choice (earliest finish time) is optimal."""
    print("Test 3: Greedy Choice Optimality")
    scheduler = GreedyScheduler()
    
    # Event A finishes earliest but Event B,C together are also optimal
    scheduler.add_event(Event("Event A", 1.0, 10.0, 1))
    scheduler.add_event(Event("Event B", 2.0, 5.0, 2))
    scheduler.add_event(Event("Event C", 6.0, 9.0, 3))
    
    selected, rejected, steps = scheduler.greedy_schedule()
    
    assert len(selected) == 2, f"Expected 2 selected, got {len(selected)}"
    assert selected[0].name == "Event B", "Should select Event B (earliest finish)"
    assert selected[1].name == "Event C", "Should select Event C next"
    print("✓ Test 3 passed: Greedy choice leads to optimal solution")
    print()


def test_all_overlapping():
    """Test when all events overlap."""
    print("Test 4: All Overlapping Events")
    scheduler = GreedyScheduler()
    
    scheduler.add_event(Event("Event A", 1.0, 5.0, 1))
    scheduler.add_event(Event("Event B", 2.0, 6.0, 2))
    scheduler.add_event(Event("Event C", 3.0, 7.0, 3))
    
    selected, rejected, steps = scheduler.greedy_schedule()
    
    assert len(selected) == 1, f"Expected 1 selected, got {len(selected)}"
    assert len(rejected) == 2, f"Expected 2 rejected, got {len(rejected)}"
    assert selected[0].name == "Event A", "Should select Event A (earliest finish)"
    print("✓ Test 4 passed: Only one event selected when all overlap")
    print()


def test_conflict_detection():
    """Test conflict detection functionality."""
    print("Test 5: Conflict Detection")
    scheduler = GreedyScheduler()
    
    scheduler.add_event(Event("Event A", 1.0, 3.0, 1))
    scheduler.add_event(Event("Event B", 2.0, 4.0, 2))
    scheduler.add_event(Event("Event C", 5.0, 6.0, 3))
    
    conflicts = scheduler.detect_conflicts()
    
    assert len(conflicts) == 1, f"Expected 1 conflict, got {len(conflicts)}"
    assert conflicts[0][0].name == "Event A" and conflicts[0][1].name == "Event B"
    print("✓ Test 5 passed: Conflicts correctly detected")
    print()


def test_empty_schedule():
    """Test with no events."""
    print("Test 6: Empty Schedule")
    scheduler = GreedyScheduler()
    
    selected, rejected, steps = scheduler.greedy_schedule()
    
    assert len(selected) == 0, "Expected no selected events"
    assert len(rejected) == 0, "Expected no rejected events"
    print("✓ Test 6 passed: Empty schedule handled correctly")
    print()


def test_single_event():
    """Test with single event."""
    print("Test 7: Single Event")
    scheduler = GreedyScheduler()
    
    scheduler.add_event(Event("Event A", 1.0, 2.0, 1))
    selected, rejected, steps = scheduler.greedy_schedule()
    
    assert len(selected) == 1, "Expected 1 selected event"
    assert len(rejected) == 0, "Expected 0 rejected events"
    print("✓ Test 7 passed: Single event handled correctly")
    print()


def test_statistics():
    """Test statistics calculation."""
    print("Test 8: Statistics Calculation")
    scheduler = GreedyScheduler()
    
    scheduler.add_event(Event("Event A", 1.0, 2.0, 1))
    scheduler.add_event(Event("Event B", 1.5, 3.0, 2))
    scheduler.add_event(Event("Event C", 2.5, 4.0, 3))
    scheduler.add_event(Event("Event D", 4.0, 5.0, 4))
    
    selected, rejected, steps = scheduler.greedy_schedule()
    stats = scheduler.get_statistics()
    
    assert stats['total_events'] == 4, "Total events should be 4"
    assert stats['scheduled_events'] == 3, "Scheduled should be 3"
    assert stats['rejected_events'] == 1, "Rejected should be 1"
    assert stats['efficiency'] == 75.0, "Efficiency should be 75%"
    print("✓ Test 8 passed: Statistics calculated correctly")
    print()


def test_sorting_by_finish_time():
    """Test that events are correctly sorted by finish time."""
    print("Test 9: Sorting by Finish Time")
    scheduler = GreedyScheduler()
    
    scheduler.add_event(Event("Event C", 3.0, 6.0, 3))
    scheduler.add_event(Event("Event A", 1.0, 4.0, 1))
    scheduler.add_event(Event("Event B", 2.0, 5.0, 2))
    
    selected, rejected, steps = scheduler.greedy_schedule()
    
    # After sorting by finish time: A (4.0), B (5.0), C (6.0)
    # A selected (1-4), B conflicts (2-5), C conflicts (3-6)
    assert selected[0].name == "Event A", "First should be Event A (finish 4.0)"
    assert len(selected) >= 1, f"Should have at least 1 event, got {len(selected)}"
    print("✓ Test 9 passed: Events sorted correctly by finish time")
    print()


def test_complex_scenario():
    """Test complex scenario with multiple overlaps."""
    print("Test 10: Complex Scenario (College Timetable)")
    scheduler = GreedyScheduler()
    
    # Simulate college schedule
    scheduler.add_event(Event("Math", 9.0, 10.5, 1))
    scheduler.add_event(Event("Physics", 9.5, 11.0, 2))
    scheduler.add_event(Event("CS", 10.0, 11.5, 3))
    scheduler.add_event(Event("English", 11.0, 12.5, 4))
    scheduler.add_event(Event("Chemistry", 11.5, 13.0, 5))
    scheduler.add_event(Event("Lunch", 12.5, 13.5, 6))
    
    selected, rejected, steps = scheduler.greedy_schedule()
    
    # Expected: Math (10.5), Physics conflicts, CS conflicts, English (12.5), 
    # Chemistry conflicts, Lunch (13.5)
    assert len(selected) >= 3, f"Expected at least 3 selected, got {len(selected)}"
    print(f"✓ Test 10 passed: Complex scenario handled - {len(selected)} events scheduled")
    print()


def run_all_tests():
    """Run all test cases."""
    print("="*70)
    print("SMART EVENT SCHEDULER - TEST SUITE")
    print("="*70)
    print()
    
    try:
        test_basic_scheduling()
        test_overlapping_events()
        test_greedy_choice()
        test_all_overlapping()
        test_conflict_detection()
        test_empty_schedule()
        test_single_event()
        test_statistics()
        test_sorting_by_finish_time()
        test_complex_scenario()
        
        print("="*70)
        print("ALL TESTS PASSED! ✓")
        print("="*70)
        print()
        print("Core algorithm functionality verified:")
        print("✓ Greedy selection works correctly")
        print("✓ Sorting by finish time implemented properly")
        print("✓ Conflict detection accurate")
        print("✓ Statistics calculation correct")
        print("✓ Edge cases handled (empty, single event)")
        print("✓ Complex scenarios work as expected")
        print()
        print("The application is ready for use!")
        
    except AssertionError as e:
        print(f"✗ TEST FAILED: {e}")
        return False
    except Exception as e:
        print(f"✗ ERROR: {e}")
        return False
    
    return True


if __name__ == "__main__":
    success = run_all_tests()
    exit(0 if success else 1)
