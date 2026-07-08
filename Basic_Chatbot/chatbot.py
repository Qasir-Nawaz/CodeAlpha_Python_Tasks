"""
AI-Powered Chatbot - CodeAlpha Python Internship Task 4
Author: Qasir Nawaz
Powered by Groq API (llama-3.3-70b-versatile)
"""

import os
import json
import time
from groq import Groq

GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "your_key_here")
MODEL        = "llama-3.3-70b-versatile"
HISTORY_FILE = "chat_history.json"
MAX_HISTORY  = 20

class C:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    CYAN    = "\033[96m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    MAGENTA = "\033[95m"
    RED     = "\033[91m"
    GRAY    = "\033[90m"
    WHITE   = "\033[97m"

SYSTEM_PROMPT = """You are PyBot, a smart AI chatbot built with Python by Qasir Nawaz for CodeAlpha internship.
Rules:
- Reply in the SAME language the user uses. Roman Urdu → Roman Urdu. English → English.
- Keep replies SHORT and to the point. 1-2 sentences max.
- Answer exactly what was asked. Nothing more, nothing less.
- Be natural and casual like a friend texting."""

client = Groq(api_key=GROQ_API_KEY)
conversation_history = []

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return []

def save_history(history):
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2, ensure_ascii=False)

def stream_response(user_input):
    conversation_history.append({"role": "user", "content": user_input})
    trimmed = conversation_history[-MAX_HISTORY:]
    stream = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "system", "content": SYSTEM_PROMPT}] + trimmed,
        max_tokens=500,
        temperature=0.7,
        stream=True,
    )
    full_reply = ""
    print(f"\n{C.CYAN}{C.BOLD}PyBot:{C.RESET} ", end="", flush=True)
    for chunk in stream:
        delta = chunk.choices[0].delta.content
        if delta:
            print(f"{C.WHITE}{delta}{C.RESET}", end="", flush=True)
            full_reply += delta
    print("\n")
    conversation_history.append({"role": "assistant", "content": full_reply})
    return full_reply

def print_header():
    print(f"\n{C.CYAN}{'═' * 54}{C.RESET}")
    print(f"{C.CYAN}║{C.RESET}  {C.BOLD}{C.MAGENTA}🤖  PYBOT — AI Chatbot  (CodeAlpha){C.RESET}          {C.CYAN}║{C.RESET}")
    print(f"{C.CYAN}║{C.RESET}  {C.GRAY}Powered by Groq + LLaMA 3.3 70B{C.RESET}             {C.CYAN}║{C.RESET}")
    print(f"{C.CYAN}{'═' * 54}{C.RESET}")
    print(f"  {C.GRAY}Type in English or Roman Urdu. 'bye' to exit.{C.RESET}\n")

def main():
    print_header()
    old = load_history()
    if old:
        ans = input(f"  {C.YELLOW}📂 Previous chat found. Load it? (y/n):{C.RESET} ").strip().lower()
        if ans == "y":
            conversation_history.extend(old)
            print(f"  {C.GREEN}✅ {len(old)} messages loaded!{C.RESET}\n")
    while True:
        try:
            user_input = input(f"{C.GREEN}{C.BOLD}You:{C.RESET} ").strip()
            if not user_input:
                continue
            if user_input.lower() in ("bye", "exit", "quit", "goodbye"):
                save_history(conversation_history)
                print(f"\n  {C.CYAN}PyBot:{C.RESET} {C.WHITE}Allah Hafiz! 👋{C.RESET}\n")
                break
            stream_response(user_input)
        except KeyboardInterrupt:
            save_history(conversation_history)
            print(f"\n\n  Goodbye! 👋\n")
            break
        except Exception as e:
            print(f"\n  {C.RED}Error: {e}{C.RESET}\n")

if __name__ == "__main__":
    main()
