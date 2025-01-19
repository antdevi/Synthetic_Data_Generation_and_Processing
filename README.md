![Pasted image 20250120030029](https://github.com/user-attachments/assets/3724d348-7223-442e-bd33-081890347a83)## Synthetic Data Generation and Processing

**Synthetic Data Generation and Processing** is a field focused on creating artificial data that mimics real-world scenarios. This data is widely used for testing, training machine learning models, and validating algorithms, especially when obtaining or using real data is expensive, impractical, or restricted due to privacy concerns. This project implements a chatbot that interacts with users, processes their input using a locally hosted LM Studio instance, and stores the chat responses in an Excel file. The chatbot also includes a looping feature to allow multiple interactions within a single session.

This project contributes to synthetic data generation by:

- Capturing user interactions and chatbot responses.
- Storing these interactions systematically for later analysis or use.
- Allowing users to customize the number of interactions, effectively controlling the data size.

By generating synthetic conversation datasets, this project can help:

- Train AI models for natural language understanding.
- Benchmark chatbot performance and response quality.
- Provide structured data for further processing and insights.
## How to Run the Project

1. **Start LM Studio**:
    
    - Ensure LM Studio is running locally on your machine.
    - The base URL for LM Studio should be accessible (e.g., `http://localhost:1234/v1`).
    - User the model llama 3.2 3B Instruct or you can also use llama 3.2 1B instruct.
    - Load the model in LM Studio
2. **Set Up the Project**:
    
    - Clone or download this repository to your machine.
    - Open VS code run the file name app.py
    - Provide system prompt and user input in the 
     
3. **Interact with the Chatbot**:
    - Enter the number of loops (interactions) you'd like to perform.
    
5. **View the Files**:
    - Once the file has run properly you will see one .xlsx file getting created and one folder where the files taking the input from .xlsx file is getting stored.

## File Structure

├── app.py # Main script for chatbot interactions
├── human_facts.xlsx # Excel file to store chat data (generated automatically) ├──generated_articles_excel # Folder stores the files that are created from the contents of the Excel File
└── README.md # Project documentation
└──Requirement.txt

### Excel Output:

| User Input         | Bot Response                                       |
| ------------------ | -------------------------------------------------- |
| Tell me a fact.    | A fact to know, for your delight, the stars shine… |
| What's the secret… | Life is a journey, not a race, filled with wonder… |

## Customization

You can customize the system instruction to modify how the chatbot responds. For example:

system_instruction = {"role": "system", "content": "Always answer in rhymes."}
user_input = "Generate a one-liner fact about humans."

Also you can customize the instruction in phase two of the code:
system_instruction = {"role": "system", "content": "Create an article based on the user prompt."}

## Troubleshooting

- **404 Not Found**: Verify LM Studio is running and accessible at the specified base URL.
- **Excel File Issues**: Ensure the .xlsx file is not open in another program while the script is running.
- **Dependency Errors**: Ensure all required libraries are installed.

