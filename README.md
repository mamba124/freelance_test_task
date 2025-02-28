# LLM-Based Feature Extractor  

This tool leverages Large Language Models (LLMs) to extract features from product descriptions.  
**Supported Engines**: OpenAI, Anthropic  

---

## Getting Started  

This is a command-line interface (CLI) application. Follow the steps below to set up and run the tool:  

### 0. Set Up an Isolated Environment  
Create an isolated environment using either `conda` or `pyenv`.  

### 1. Install Dependencies  
Run the following command to install the required Python libraries:  

```
    pip install -r requirements.txt
```

### 2. Run the Application
Use the following command to start the feature extraction process:

```
    export LLM=<your llm model name>
    export LLM_API_TOKEN=<your llm api token>
    python -m main --data_folder <path_to_product_descriptions> --features_path <path_to_feature_list> --output_path <path_to_output_excel>
```

#### *Note*

If you want to update an existing output file instead of generating a new one, set the --output_path parameter to the name of the existing document.


### How It Works
The script follows these steps:

1. Extract Features

    - Reads the list of features from a .txt file.

    - Iterates through the folder containing product descriptions.

2. Build a DataFrame

    - Creates a Pandas DataFrame where:

    ```
        Rows: Features
        Columns: Product titles
    ```

3. Generate Prompts and Extract Data

    - Sends the descriptions and feature list to the LLM for processing.

    - Constructs prompts to ensure the output includes a dictionary:

    ```
    Keys: Features
    Values: Extracted data
    ```

    - For uncertain features, the LLM flags them under a special key: **NOTFOUND.**

4. Populate the DataFrame

    - Updates the DataFrame with the LLM's output.

#### Example Usage:

```
    python -m main --data_folder ./data/ --features_path ./utils/features.txt --output_path ./results.xlsx
```

This command processes all product descriptions in the ./products folder using the features specified in features.txt and saves the results in results.xlsx.

### Cost

Average cost of the procedure per document is in range €(0.047-0.057)