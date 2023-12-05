# OpenAI Examples

# Create a virtual env using this command

1. Set up a virtual environment (optional but recommended):
   - Create a new directory for your project.
   - Open a terminal or command prompt and navigate to the project directory.
   - Create a virtual environment using the following command:
     ```
     python3 -m venv myenv
     ```
   - Activate the virtual environment:
     - On macOS and Linux:
       ```
       source myenv/bin/activate
       ```
     - On Windows:
       ```
       myenv\Scripts\activate
       ```

2. Install all the required dependencies:
   - While inside the virtual environment, install the requirements using pip:
     ```
     pip install -r requirements.txt
     ```
## Create the following variables in your SO

    Add the following env variables in order to use the postgres database locally

    OPEN_AI_API_KEY

## Run the application locally using the following command

```
    /bin/python3 /${your-path}/openai-examples/src/main.py
```

# Open AI - Assistances examples 

Take a look at the following ROLES examples:

```
    /${your-path}/resources/openai/assistant/roles
```

Take a look at the following FUNCTIONS (skills) examples:

```
    /${your-path}/resources/openai/assistant/functions
```

# More code examples 

Take a look at the following examples:

## Using [Microsoft autogen](ttps://www.microsoft.com/en-us/research/project/autogen/) h to orquestrate and Agent conversation

```
    /${your-path}/openai-examples/src/research-agents-main/README.md
```
