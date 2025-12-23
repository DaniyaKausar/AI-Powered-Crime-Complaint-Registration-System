from google import genai

client = genai.Client(
    api_key="AIzaSyDnBjkGsFL6uuyiD_FRC5TOtbgzYxOj9UY"
)

response = client.models.generate_content(
    model="models/gemini-2.5-flash",
    contents="Say hello in one sentence"
)

print(response.text)


