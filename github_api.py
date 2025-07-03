import argparse
import requests

def get_event(user):
    api_url = f"https://api.github.com/users/{user}/events"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        print(data)


parser = argparse.ArgumentParser(prog = 'task-cli')
parser.add_argument("username")
args = parser.parse_args()

# https://api.github.com/users/<username>/events
# Example: https://api.github.com/users/kamranahmedse/events

user = args.username
get_event(user)

