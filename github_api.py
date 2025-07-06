import argparse
import requests

def get_event(user):
    api_url = f"https://api.github.com/users/{user}/events"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        for event in data:
            # Covering only the most common events
            if event['type'] == 'IssueCommentEvent':
                print(f"- :smiley: commented on issue {event['payload']['issue']['number']}")
            elif event['type'] == 'PushEvent':
                print(f"- :smiley: pushed {event["payload"]["size"]} commits to {event['repo']['name']}")
            elif event['type'] == 'IssuesEvent':
                print(f"- :smiley: created issue {event['payload']['issue']['number']}")
            elif event['type'] == 'WatchEvent':
                print(f"- :smiley: starred {event['repo']['name']}")
            elif event['type'] == 'PullRequestEvent':
                print(f"- :smiley: created pull request {event['payload']['pull_request']['number']}")
            elif event['type'] == 'PullRequestReviewEvent':
                print(f"- :smiley: reviewed pull request {event['payload']['pull_request']['number']}")
            elif event['type'] == 'PullRequestReviewCommentEvent':
                print(f"- :smiley: commented on pull request {event['payload']['pull_request']['number']}")
            elif event['type'] == 'CreateEvent':
                print(f"- :smiley: created {event['payload']['ref_type']} {event['payload']['ref']}")
            else:
                print(f"- :smiley: {event['type']}")
    else:
        print(f"Error fetching response for {user} - response code: {response.status_code}")


parser = argparse.ArgumentParser(prog = 'task-cli')
parser.add_argument("username")
args = parser.parse_args()

# https://api.github.com/users/<username>/events
# Example: https://api.github.com/users/kamranahmedse/events

user = args.username
get_event(user)

