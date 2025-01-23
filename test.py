from SDGP import dynamic_improvement
from openai import OpenAI

# Step 1: Set up the OpenAI client
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

# Step 2: Initialize the library
library = dynamic_improvement(client)
# Step 3: Test Phase 1 - Generate Facts
try:
    print("Testing Phase 1: Generating Facts...")
    output_file = "test_facts.xlsx"
    facts_file = library.generate_facts(
        system_prompt="Always respond in rhymes.",
        user_prompt="Tell me a fact about life.",
        num_loops=3,
        output_file=output_file,
        facts_column_name="Generated Facts"
    )
    print(f"Facts generated and saved to: {facts_file}")
except Exception as e:
    print(f"Error during Phase 1: {e}")

# Step 4: Test Phase 2 - Generate Articles
try:
    print("Testing Phase 2: Generating Articles...")
    library.generate_articles(
        input_file="test_facts.xlsx",
        system_prompt="Write an article expanding on this fact.",
        user_prompt_column="Generated Facts"
    )
    print("Articles generated and appended successfully.")
except Exception as e:
    print(f"Error during Phase 2: {e}")


