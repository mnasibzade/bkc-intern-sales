import sys
import os
from telegram.ext import Application, CommandHandler

def read_token():
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        token_path = os.path.join(base_dir, 'token.txt')
        with open(token_path, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        print("Token file (token.txt) not found.", file=sys.stderr)
        return None

TOKEN = read_token()

if not TOKEN:
    print("Bot token is missing. Please make sure the token.txt file exists.", file=sys.stderr)
    sys.exit(1)