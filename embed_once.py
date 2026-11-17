from openai import OpenAI

client = OpenAI()

sentence = "A cache stores frequently accessed data."

response = client.embeddings.create(
    model="text-embedding-3-small",
    input=sentence
)

embedding = response.data[0].embedding

print("Dimensions:", len(embedding))
print("First 3 values:", embedding[:3])
print("All values are numbers:", all(isinstance(value, float) for value in embedding))





