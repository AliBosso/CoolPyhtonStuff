import os
import time
import json
import socket
import colorama
import requests


logo = '''
░░░░░░░ ░░░░░░░ ████▀■▄▒█ ░░░░░░░ ░░░░░░░ ░░░░░░░
░░░░░░░ ░░░░░░░ ████ ███▓ ░░░░░░░ ░░░░░░░ ░░░░░░░
░     ░ ░░    ░ ████ █░█▒ ░     ░ ░     ░ ░    ░░
                ░███ █▒█░                       ░
███▀▀▓▒ ██■ █▀▒ ▒██░  ▓▄█ ██■ █▀▒ ▀▀▀▀▀▓▒ █▀▓    
░██ ██░ ▒██ ██░ ▒  ▒ ▀▀▀▀ ▒██ ██░ ▄▄▄▄██░ ░██▄█▀▄
▒██▄░█░ ▀▀▀▀░██ ▓█▄▓ █▄▄░ ▓█■▀░██ ▒██ ░█░ ▒██ ▀▀ 
▓▄▐     ▓▀▄ ▒■░ █▄▒█ ■▄▀▒ ▓▀▄ ▒■░ ▓▄▐ ▒▄■ ▓▄▐ ▒▄■
███ ░░░ ██▓▄▓█▓ ██▓█▄███▓ ██▓ ▓█▓ ███▄▓█▄ ███▄▓█▄

'''


def data():
    chatbot_intents = {
    "weather": {
        "topic": [
            "weather",
            "temperature",
            "forecast",
            "rain",
            "snow",
            "sunny",
            "cloudy",
            "humidity",
            "wind",
            "degrees",
            "storm",
        ],
        "action": [
            "show",
            "get",
            "check",
            "look",
            "tell",
            "what",
            "is",
            "give",
            "find",
            "can",
        ],
    },
    "joke": {
        "topic": ["joke", "funny", "laugh", "humor", "haha", "pun"],
        "action": ["tell", "give", "know", "hear", "got", "share"],
    },
    "time": {
        "topic": ["time", "clock", "hour", "date", "day", "today", "tomorrow"],
        "action": ["what", "is", "tell", "check", "current", "show"],
    },
    "movie": {
        "topic": [
            "movie",
            "film",
            "show",
            "watch",
            "series",
            "cinema",
            "netflix",
        ],
        "action": ["recommend", "suggest", "good", "best", "find", "give"],
    },
    "support": {
        "topic": ["help", "error", "bug", "issue", "problem", "broken", "crash"],
        "action": ["fix", "solve", "how", "can", "need", "resolve"],
    },
    "music": {
        "topic": [
            "music",
            "song",
            "track",
            "artist",
            "playlist",
            "album",
            "spotify",
        ],
        "action": ["play", "listen", "put", "queue", "stream", "find", "start"],
    },
    "food": {
        "topic": [
            "food",
            "restaurant",
            "eat",
            "hungry",
            "pizza",
            "burger",
            "snack",
        ],
        "action": ["find", "suggest", "recommend", "order", "near", "get", "deliver"],
    },
    "sports": {
        "topic": [
            "score",
            "game",
            "match",
            "team",
            "football",
            "basketball",
            "soccer",
        ],
        "action": ["how", "did", "won", "play", "result", "check", "status"],
    },
    "travel": {
        "topic": [
            "direction",
            "route",
            "map",
            "traffic",
            "flight",
            "hotel",
            "trip",
        ],
        "action": ["navigate", "find", "show", "get", "book", "plan", "drive"],
    },
    "finance": {
        "topic": [
            "stock",
            "price",
            "crypto",
            "bitcoin",
            "money",
            "bank",
            "balance",
        ],
        "action": ["check", "how", "much", "show", "track", "get", "view"],
    },
    "health": {
        "topic": [
            "workout",
            "calories",
            "exercise",
            "steps",
            "sleep",
            "weight",
            "diet",
        ],
        "action": ["track", "log", "count", "calculate", "show", "record", "monitor"],
    },
    "shopping": {
        "topic": [
            "price",
            "deal",
            "sale",
            "cart",
            "product",
            "order",
            "shipping",
        ],
        "action": ["buy", "search", "find", "compare", "track", "get", "check"],
    },
    "education": {
        "topic": [
            "homework",
            "definition",
            "translation",
            "math",
            "science",
            "history",
            "word",
            "+",
            "-",
            "/",
            "sqrt",
            "^",
        ],
        "action": [
            "solve",
            "define",
            "translate",
            "explain",
            "teach",
            "help",
            "calculate",
        ],
    },
    "gaming": {
        "topic": [
            "game",
            "steam",
            "playstation",
            "xbox",
            "nintendo",
            "multiplayer",
            "rpg",
        ],
        "action": ["play", "launch", "download", "buy", "find", "join", "start"],
    },
    "photo": {
        "topic": [
            "photo",
            "image",
            "picture",
            "camera",
            "screenshot",
            "gallery",
        ],
        "action": ["take", "capture", "open", "show", "save", "view", "edit"],
    },
    "reminder": {
        "topic": ["alarm", "reminder", "timer", "schedule", "meeting", "event"],
        "action": ["set", "create", "remind", "add", "start", "stop", "cancel"],
    },
    "news": {
        "topic": ["news", "headlines", "articles", "breaking", "politics", "world"],
        "action": ["read", "show", "get", "tell", "find", "latest", "check"],
    },
    "home": {
        "topic": [
            "lights",
            "thermostat",
            "door",
            "lock",
            "plug",
            "camera",
            "fan",
        ],
        "action": ["turn", "switch", "dim", "open", "close", "raise", "lower"],
    },
    "social": {
        "topic": [
            "message",
            "text",
            "email",
            "post",
            "tweet",
            "chat",
            "notification",
        ],
        "action": ["send", "write", "reply", "read", "check", "forward", "delete"],
    },
}
    return chatbot_intents


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


str = ""
running = True
user_choice = ""


weather = "https://api.open-meteo.com/v1/forecast"


def iterate():
  global user_choice
  user_choice = input("User: ").strip().lower()
  words_list = user_choice.split()

  intents = data()
  matched_situation = None

  for situation, keywords in intents.items():
    has_topic = any(word in words_list for word in keywords["topic"])
    has_action = any(word in words_list for word in keywords["action"])

    if has_topic or has_action:
      matched_situation = situation
      break

  return matched_situation


def response(matched_situation):
  if matched_situation == "weather":
    print("\nBot: Let me check the weather forecast for you...")

  elif matched_situation == "joke":
    print("\nBot: Why don't skeletons fight each other? They don't have the guts!")

  elif matched_situation == "time":
    print(f"\nBot: The current system time is {time.strftime('%H:%M:%S')}.")

  elif matched_situation is None:
    print("\nBot: I'm not sure what you mean. Try asking about weather, time, or jokes!")

  else:
    print(f"\nBot: I see you want to talk about {matched_situation}, but I'm still learning how to answer that!")

  input("\nPress Enter to continue...")


while running:
    clear()
    print(logo)
    while True:
        matched_intent = iterate()
        
        if user_choice in ["exit", "bye"]:
            print("\nBot: Goodbye!")
            time.sleep(1)
            running = False
            break
            
        response(matched_intent)
        break