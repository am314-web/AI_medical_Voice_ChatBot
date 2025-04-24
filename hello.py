import os
from dotenv import load_dotenv
load_dotenv()
GROQ_API_KEY=os.environ.get("GROQ_API_KEY")


print(GROQ_API_KEY)