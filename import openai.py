import openai

# Replace with your OpenAI API key
api_key = "your_api_key_here"

def test_openai_api(api_key):
    try:
        # Set up the OpenAI API key
        openai.api_key = api_key

        # Make a simple API call to verify the key
        response = openai.chat_completions.create(
            model="gpt-3.5-turbo",  # Replace with the model you're using
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Hello! Can you confirm you're working?"}
            ]
        )

        # Print the response from the API
        print("API Key Test Successful!")
        print("Response from API:", response["choices"][0]["message"]["content"])

    except openai.error.AuthenticationError:
        print("Authentication Error: Invalid API Key.")
    except openai.error.RateLimitError:
        print("Rate Limit Error: Too many requests. Try again later.")
    except Exception as e:
        print("An error occurred:", str(e))

# Run the test function
test_openai_api(api_key)






