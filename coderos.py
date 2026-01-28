import os
import requests
import pyperclip

API_KEY = os.getenv("DEEPSEEK_API_KEY")
URL = "https://api.deepseek.com/chat/completions"
MODEL = "deepseek-chat"


def generate_code(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "You are a helpful coding assistant. Output only code."},
            {"role": "user", "content": prompt}
        ]
    }

    r = requests.post(URL, headers=headers, json=data)
    r.raise_for_status()

    return r.json()["choices"][0]["message"]["content"]


def main():
    prompt = input("CoderOS > ")

    code = generate_code(prompt)

    with open("coderos_output.py", "w", encoding="utf-8") as f:
        f.write(code)

    pyperclip.copy(code)

    print("Code generated and copied to clipboard.")


if __name__ == "__main__":
    main()
