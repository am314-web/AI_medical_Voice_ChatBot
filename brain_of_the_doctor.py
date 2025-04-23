# Step1: setup Groq AI API
import os
import base64

GROQ_API_KEY = "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"

# Step2: convert image to required format
image_path = "acne.jpg"
image_file = open(image_path, "rb")
encoded_image = base64.b64encode(image_file.read()).decode("utf-8")

# Step3: Setup Multi model LLM
from groq import Groq

query = "Is there something wrong with my face?"
model = "meta-llama/llama-4-scout-17b-16e-instruct"
# model="llama-3.2-90b-vision-preview" #Deprecated


def analyze_image_with_query(query, model, encoded_image):
    client = Groq(api_key=GROQ_API_KEY)
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": query
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}",
                    },
                },
            ],
        }
    ]
    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model
    )

    print(chat_completion.choices[0].message.content)

# ✅ Add this part to actually run it
if __name__ == "__main__":
    analyze_image_with_query(query, model, encoded_image)
