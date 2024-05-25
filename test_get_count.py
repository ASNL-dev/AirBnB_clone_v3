#!/usr/bin/python3
""" Test .get() and .count() methods
"""
from models import storage
from models.state import State

print("All objects: {}".format(storage.count()))
print("State objects: {}".format(storage.count(State)))

# Get all state instances
all_states = storage.all(State)
print("All State instances:", all_states)

# Check if there are any state instances
if all_states:
    # Get the first state instance
    first_state = list(all_states.values())[0]
    first_state_id = first_state.id
    print("First state ID:", first_state_id)

    # Get the first state by ID
    first_state_by_id = storage.get(State, first_state_id)
    print("First state by ID:", first_state_by_id)
else:
    print("No State instances found.")
