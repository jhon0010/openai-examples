# Taked from 

https://github.com/JayZeeDesign/researcher-gpt

# How to use it 

## Insall the requirements

Install using the requirements.txt file.

```bash
pip install -r requirements.txt
```

Remeber to use this specific version of pyautogen to avoid errors with the latest version.

```bash
pip install pyautogen==0.2.0b5
```

## Configure the environment variables

* Use the .env file to configure the environment variables that are required.

* Go to the .gitattributes file and change the values for the api_key and also the model if you want it.


## Configure the assistant_id variable

Go to the app.py file and change the assistant_id variable to the id of your assistant.

You can find the assistant id in the assistant settings page (OpenAI). https://platform.openai.com/assistants

## Register new functions

Go to the app.py file and register new functions in the functions dictionary, something like this:

```python
director.register_function(
    function_map={
        "get_airtable_records": get_airtable_records,
        "update_single_airtable_record": update_single_airtable_record
    }
)
```