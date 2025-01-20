from openai import OpenAI
import pandas as pd
import os

# Set up the client to connect to the local chatbot
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

# Phase 1: Generate facts and save them to an Excel sheet
def generate_facts_and_save():
    system_instruction = {"role": "system", "content": "Always answer in rhymes."}
    user_input = "Generate a one-liner fact about humans."
    num_loops = int(input("Enter the number of facts to generate: "))
    data = []

    for i in range(num_loops):
        completion = client.chat.completions.create(
            model="model-identifier",
            messages=[
                system_instruction,
                {"role": "user", "content": user_input}
            ],
            temperature=0.7,
        )
        bot_response = completion.choices[0].message.content
        data.append({"Fact Number": i + 1, "One-Liner Human Fact": bot_response})
        print(f"Fact {i + 1}: {bot_response}")

    # Save to Excel
    output_file = "human_facts.xlsx"
    df = pd.DataFrame(data)
    df.to_excel(output_file, index=False)
    print(f"Facts saved to {output_file}")
    return output_file

# Phase 2: Read facts and append articles to the same Excel file
def generate_articles_in_same_file(input_file):
    system_instruction = {"role": "system", "content": "Create an article based on the user prompt."}
    try:
        df = pd.read_excel(input_file)
    except FileNotFoundError:
        print(f"File not found: {input_file}. Please generate facts first.")
        return

    # Generate articles and add them to the DataFrame
    articles = []
    for index, row in df.iterrows():
        user_prompt = row["One-Liner Human Fact"]
        completion = client.chat.completions.create(
            model="model-identifier",
            messages=[
                system_instruction,
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7,
        )
        bot_response = completion.choices[0].message.content
        articles.append(bot_response)
        print(f"Article for Fact {index + 1}: {bot_response}")

    # Add the articles to a new column in the DataFrame
    df["Generated Article"] = articles

    # Save back to the same Excel file
    df.to_excel(input_file, index=False)
    print(f"All articles have been added to {input_file}")

# Execute both phases
facts_file = generate_facts_and_save()
generate_articles_in_same_file(facts_file)
