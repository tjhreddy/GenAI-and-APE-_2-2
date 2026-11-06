



import os
import time
from dotenv import load_dotenv
from google import genai

# Step 1: Load API key
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env!")

# Step 2: Initialize Gemini
client = genai.Client(api_key=api_key)

# Step 3: Send prompt with automatic retries
print("Connecting to Gemini...")

for attempt in range(3):
    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents="What is Artificial Intelligence? Explain in simple words."
        )

        # Step 4: Display response
        print("\nLLM Response:")
        print(response.text)
        break

    except Exception as e:
        if "503" in str(e) or "UNAVAILABLE" in str(e):
            print(f"Server busy. Retry {attempt + 1}/3...")
            if attempt < 2:
                time.sleep(10)
            else:
                print("Gemini server is still unavailable. Try again later.")
        else:
            print("Error:", e)
            break
