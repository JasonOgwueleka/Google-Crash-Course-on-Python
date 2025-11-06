# This Python program tracks which users are currently logged into which computers.
# It processes a list of login and logout events, sorts them by time, and builds a dictionary mapping each machine to the users still logged in.
# Finally, it prints a report showing the active users on each machine.

def get_event_date(event):
    return event.date

# Function to determine which users are currently logged in to which machines
def current_users(events):
    # Sort events chronologically using the event date
    events.sort(key=get_event_date)

    # Dictionary to map each machine to a set of users currently logged in
    machines = {}

    # Iterate through all events
    for event in events:
        # If this machine hasn't been seen before, initialize an empty set for it
        if event.machine not in machines:
            machines[event.machine] = set()

        # If it's a login event, add the user to that machine's set
        if event.type == "login":
            machines[event.machine].add(event.user)

        # If it's a logout event, safely remove the user (only if they're logged in)
        elif event.type == "logout":
            if event.user in machines[event.machine]:
                machines[event.machine].remove(event.user)

    # Return the dictionary containing all machines and their logged-in users
    return machines


# Function to generate report of active users per machine
def generate_report(machines):
    # Loop through each machine and its corresponding set of users
    for machine, users in machines.items():
        # Only print machines that currently have active users
        if len(users) > 0:
            # Join the usernames with commas for neat output
            user_list = ", ".join(users)
            # Print the machine name followed by the users logged in
            print("{}: {}".format(machine, user_list))


# Class to represent an event (login or logout)
class Event:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user

events = [
    Event('2020-01-21 12:45:46', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'login', 'mailserver.local', 'chris'),
]

# Generate a dictionary of machines and current users
users = current_users(events)

print(users)
generate_report(users)
