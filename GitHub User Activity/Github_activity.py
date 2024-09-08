#!/usr/bin/env python
import requests
from colorama import Fore,Style,init
import argparse


init(autoreset=True)

BASE_URL='https://api.github.com/users/'

def fetch_user_info(username):
    """Fetch and display Github user info"""
    url= f"{BASE_URL}{username}"
    
    try:
        response=requests.get(url)
        response.raise_for_status()
        user=response.json()
        print(Fore.GREEN + f"User: {user['name']}")
        print(f"Bio: {user['bio']}")
    except requests.exceptions.RequestException as e:
        print(Fore.RED + "Error fetching user data:", e)


def fetch_user_repo(username):
    url= f"{BASE_URL}{username}/repos"
    try:
        response = requests.get(url)
        response.raise_for_status()
        repos = response.json()
        for repo in repos:
            print(Fore.BLUE + f"Repo: {repo['name']}")
            print(f"Stars: {repo['stargazers_count']}, Forks: {repo['forks_count']}")
            print(f"Language: {repo['language']}")
            print('---')
    except requests.exceptions.RequestException as e:
        print(Fore.RED + "Error fetching repositories:", e)

def main():
    parser=argparse.ArgumentParser(description='Github user activity cli tool')
    parser.add_argument('username',help='Github Username')
    parser.add_argument('command',choices=['user','repo'], help='Command to run (user or repos)')
    
    args=parser.parse_args()
    
    if args.command== 'user':
        fetch_user_info(args.username)
    if args.command == 'repo':
        fetch_user_repo(args.username)

if __name__== "__main__":
    main()