from openai import OpenAI
import pandas as pd
import os

def dynamic_library():
    # Set up the client to connect to the local chatbot
    client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

    # Phase 1: Generate outputs based on user-defined system prompt and input
    def generate_data_and_save(system_prompt, user_prompt, num_loops, output_file, facts_column_name):
        data = []

        for i in range(num_loops):
            completion = client.chat.completions.create(
                model="model-identifier",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.7,
            )
            bot_response = completion.choices[0].message.content
            data.append({"Iteration": i + 1, facts_column_name: bot_response})
            print(f"Response {i + 1}: {bot_response}")

        # Save to Excel
        df = pd.DataFrame(data)
        if not output_file.endswith(".xlsx"):
            output_file += ".xlsx"
        df.to_excel(output_file, index=False)
        print(f"Data saved to {output_file} with columns: {', '.join(df.columns)}")
        return output_file

    # Phase 2: Read file and apply additional transformations based on user-defined prompts
    def customize_and_add_to_file(input_file, system_prompt, user_prompt_column):
        try:
            df = pd.read_excel(input_file)
        except FileNotFoundError:
            print(f"File not found: {input_file}. Please generate data first.")
            return

        print(f"Available columns in the file: {', '.join(df.columns)}")
        if user_prompt_column not in df.columns:
            print(f"Column '{user_prompt_column}' not found in the Excel file. Please check the column name.")
            return

        # Generate additional outputs and add them to the DataFrame
        new_column_data = []
        for index, row in df.iterrows():
            user_input = row[user_prompt_column]
            completion = client.chat.completions.create(
                model="model-identifier",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input}
                ],
                temperature=0.7,
            )
            bot_response = completion.choices[0].message.content
            new_column_data.append(bot_response)
            print(f"Generated Article for Row {index + 1}: {bot_response}")

        # Add the new column to the DataFrame
        new_column_name = "Generated Article"
        df[new_column_name] = new_column_data

        # Save back to the same Excel file
        df.to_excel(input_file, index=False)
        print(f"Custom outputs added to {input_file} with columns: {', '.join(df.columns)}")

    # User interface for dynamic input
    def main():
        print("Welcome to the Dynamic Library!")

        try:
            # Phase 1 inputs
            system_prompt_phase1 = input("Enter the system prompt for Phase 1: ").strip()
            user_prompt_phase1 = input("Enter the user input prompt for Phase 1: ").strip()
            num_loops = int(input("Enter the number of iterations for Phase 1: ").strip())
            output_file = input("Enter the output Excel file name for Phase 1 (e.g., output.xlsx): ").strip()
            facts_column_name = input("Enter the column name: ").strip()

            if not system_prompt_phase1 or not user_prompt_phase1 or num_loops <= 0 or not facts_column_name:
                print("Invalid input. Please provide valid prompts, a positive number of iterations, and a column name for the facts.")
                return

            # Execute Phase 1
            facts_file = generate_data_and_save(system_prompt_phase1, user_prompt_phase1, num_loops, output_file, facts_column_name)

            # Phase 2 inputs
            system_prompt_phase2 = input("Enter the system prompt for Phase 2: ").strip()
            user_prompt_column = input("Enter the column name in the Excel file to use as user prompts for Phase 2: ").strip()

            if not system_prompt_phase2 or not user_prompt_column:
                print("Invalid input. Please provide a valid system prompt and column name.")
                return

            # Execute Phase 2
            customize_and_add_to_file(facts_file, system_prompt_phase2, user_prompt_column)
        except ValueError as e:
            print(f"Error: {e}. Please ensure all inputs are correct.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    main()

# Run the library
dynamic_library()
