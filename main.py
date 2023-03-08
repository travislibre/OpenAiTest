import os
import openai

openai.api_key = os.getenv("**********************************")
response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Extract the airport codes and generate the top 3 tourist destinations for the given city from this text:\n\nText: \"I want to fly from Los Angeles to Miami.\"\nAirport codes: LAX, MIA\n\"I want to fly to Miami.\"\nAirport codes: MIA\n\nText: \"I want to fly to Boston\"\nAirport codes:",
  temperature=2,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0,
  stop=["\n"]
)
