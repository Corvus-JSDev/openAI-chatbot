#! Warning: The current model being used `text-davinci-003` has been deprecated and no loger works.

import openai
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_KEY = os.getenv("OPENAI_KEY")


class ChatBot:
	def __init__(self):
		openai.api_key = OPENAI_KEY
	def get_response(self, user_prompt):
		response = openai.Completion.create(
			engine="text-davinci-003",
			prompt=user_prompt,
			max_tokens=3000,  # Max amount of words the AI can generate
			temperature=0.7  # How ridged or diverse are the response (0-1)
		).choices[0].text()

		return response



if __name__ == "__main__":
	chatbot = ChatBot()
	response = chatbot.get_response("Give me a classic dad joke.")
	print(response)