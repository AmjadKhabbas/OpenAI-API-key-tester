import openai

# Replace with your OpenAI API key
api_key = "your_api_key_here"

def test_openai_api(api_key):
    try:
        # Set up the OpenAI API key
        openai.api_key = api_key

        # Make a simple API call to verify the key
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # You can also use "gpt-4" if available for your API key
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Hello! Can you confirm you're working?"}
            ]
        )

        # Print the response from the API
        print("API Key Test Successful!")
        print("Response from API:", response["choices"][0]["message"]["content"])

    except ope
