## Synthetic Data Generation and Processing

This project provides a framework for generating synthetic data and processing it into structured outputs using OpenAI's API. The code is designed to be flexible, allowing users to generate various types of data by modifying the system prompt and user input. Below is a detailed explanation of the project's functionality, how to set it up, and how to customize it for your specific needs.

## Features

- **Synthetic Data Generation**:
    
    - Generate data using OpenAI's chat completions API.
        
    - Customize the generation process with dynamic prompts.
        
- **Data Storage**:
    
    - Save generated data to an Excel file for easy access and sharing.
        
- **Data Processing**:
    
    - Process the generated data into structured articles or outputs.
        
    - Append processed data to the same Excel file for organization.
    
## How It Works

The project operates in two phases:

1. **Data Generation**:
    
    - The user specifies a system prompt and a user input prompt.
        
    - Synthetic data is generated based on these prompts and saved in an Excel file (`human_facts.xlsx`).
        
2. **Data Processing**:
    
    - The generated data is read from the Excel file.
        
    - Additional content (e.g., articles or detailed descriptions) is created and appended to the same file in a new column.
## How to Run the Project

1. **Start LM Studio**:
    
    - Ensure LM Studio is running locally on your machine.
    - The base URL for LM Studio should be accessible (e.g., `http://localhost:1234/v1`).
    - Use the model llama 3.2 3B Instruct or you can also use llama 3.2 1B instruct or any other model as you prefer.
    - Load the model in LM Studio
2. **Set Up the Project**:
    
    - Clone or download this repository to your machine.
    - Open VS code run the file name generator.py
    - Provide system prompt and user input in the code as per your requirement
     
3. **Interact with the Chatbot**:
    - Enter the number of loops (interactions) you'd like to perform.
    
5. **View the Files**:
    - Once the file has run properly you will see one .xlsx file getting created.
    - You can open the .xlsx file it will have 3 columns as per your requirement
## File Structure

<<<<<<< HEAD
- `generate_data.py`: The main script for data generation and processing.
    
- `requirements.txt`: Dependencies required to run the project.
    
- `human_facts.xlsx`: Output file containing generated data and processed articles.
## Example Output:

![Alt text](Pasted image 20250120030029.png)
![C:\Users\ANTARA DAS\Documents\GitDemo\SDGP\Terminal_Output.png](file:///c%3A/Users/ANTARA%20DAS/Documents/GitDemo/SDGP/Terminal_Output.png)

=======
├── app.py # Main script for chatbot interactions
├── human_facts.xlsx # Excel file to store chat data (generated automatically) ├──generated_articles_excel # Folder stores the files that are created from the contents of the Excel File
└── README.md # Project documentation
└──Requirement.txt
### Example output in VS Code:
![Pasted image 20250120030029](https://github.com/user-attachments/assets/3724d348-7223-442e-bd33-081890347a83)
>>>>>>> 1e90bb1b59913fa11831e26d667a73bc97a54981
### Excel Output:

The following is an example of what the `human_facts.xlsx` file may look like:

| Fact Number | One-Liner Human Fact                           | Generated Article                                    |
|-------------|-----------------------------------------------|-----------------------------------------------------|
| 1           | Humans are the only species that blush.       | Blushing is a unique reaction, reflecting emotions in a visible fashion. |
| 2           | The human brain contains around 86 billion neurons. | Each neuron in the human brain contributes to a vast network, enabling thoughts and actions. |

## Customization

## Customization

### Modifying Prompts

- To generate different types of data, modify the `system_instruction` and `user_input` variables in the code:
    
    ```
    system_instruction = {"role": "system", "content": "Your system-level prompt here."}
    user_input = "Your user-level input prompt here."
    ```
    

### Examples

1. **Generate Product Descriptions**:
    
    - System Prompt: `"Create a detailed product description."`
        
    - User Input: `"Describe a smart vacuum cleaner."`
        
2. **Generate Inspirational Quotes**:
    
    - System Prompt: `"Provide an inspirational quote."`
        
    - User Input: `"Inspire someone to start their day."`
        
3. **Generate Coding Tutorials**:
    
    - System Prompt: `"Write a beginner-friendly Python tutorial."`
        
    - User Input: `"Explain how to use a for loop in Python."`

## Troubleshooting

- **404 Not Found**: Verify LM Studio is running and accessible at the specified base URL.
- **Excel File Issues**: Ensure the .xlsx file is not open in another program while the script is running.
- **Dependency Errors**: Ensure all required libraries are installed.

## Contributing
Feel free to fork this repository and add enhancements or optimizations. Contributions are welcome!
