import webbrowser

print("Welcome to the Style Quiz! Please answer the following questions to determine your clothing preferences.")

# Ask the user for their preferred style of clothing
print("What style of clothing do you like? (e.g. casual, formal, sporty)")
style = input()

# Ask the user for their preferred colors
print("What colors do you like to wear? (e.g. bright, pastel, neutral)")
colors = input()

# Ask the user for their preferred fabric types
print("What fabric types do you prefer? (e.g. cotton, silk, leather)")
fabrics = input()

# Ask the user for their preferred patterns
print("What patterns do you like? (e.g. stripes, floral, animal print)")
patterns = input()

# Ask the user for their preferred brands
print("What are your favorite clothing brands?")
brands = input()
print("What gender)")
gender = input()
# Construct the search query
query = style + " " + colors + " " + fabrics + " " + patterns + " " + brands + gender +" clothing"

# Search the web for the top results
search_url = "https://www.google.com/search?q=" + query
try:
    webbrowser.open(search_url)
except Exception as e:
    print("Error occurred while trying to search for clothing: " + str(e))


import openai_secret_manager
import openai

# Load OpenAI API key from environment variable
assert "openai" in openai_secret_manager.get_services()
secrets = openai_secret_manager.get_secret("openai")
openai.api_key = secrets["api_key"]

# Define the user's style preferences
style = "casual"
colors = "neutral"
fabrics = "cotton"
patterns = "stripes"
brands = ""

# Generate the search query
query = f"show me {style} {colors} {fabrics} {patterns} clothing"

# Use the OpenAI API to generate a feed of clothing items based on the query
response = openai.Completion.create(
  engine="davinci",
  prompt=query,
  max_tokens=1024,
  n=1,
  stop=None,
  temperature=0.7,
)

# Extract the generated text from the API response
feed = response.choices[0].text

# Print the generated feed
print(feed)



import openai_secret_manager
import openai

# Load OpenAI API key from environment variable
assert "openai" in openai_secret_manager.get_services()
secrets = openai_secret_manager.get_secret("openai")
openai.api_key = secrets["api_key"]

# Define the user's style preferences
style = input("What is your preferred style of clothing? ")
colors = input("What colors do you like to wear? ")
fabrics = input("What fabrics do you prefer? ")
patterns = input("Do you like any particular patterns? ")
brands = input("Do you prefer any particular brands? ")

# Prompt the user for filtering options
price_range = input("What is your preferred price range? ")
size = input("What is your preferred size? ")

# Generate the search query
query = f"show me {style} {colors} {fabrics} {patterns} {brands} clothing in {price_range} price range in size {size}"

# Use the OpenAI API to generate a feed of clothing items based on the query
response = openai.Completion.create(
  engine="davinci",
  prompt=query,
  max_tokens=1024,
  n=1,
  stop=None,
  temperature=0.7,
)

# Extract the generated text from the API response
feed = response.choices[0].text

# Print the generated feed
print(feed)
