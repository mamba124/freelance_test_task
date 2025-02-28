def build_system_prompt(features_list):
    return f"""
    You are a data extraction assistant. 
    Your task is to extract numeric values corresponding to specific features from text data. 

    Features:  
    {features_list}

    Output:  
    Return the results as a dictionary in the format :""" + \
        """{
            "feature1": "value1",
            "feature2": "value2",
            "NOTFOUND": [list of not found features]
        }, where "feature" is name from the list,
        and "value" is a pure number without units or quantity measures. 
        If a feature is not found or you are not sure about the feature's values add only it's first letter to the NOTFOUND.
    """


def build_main_prompt(description):
    return f"""
    Extract numeric values corresponding to the given features from the text below. 
    The features' values you are absolutely sure assign to the corresponding feature key. 
    Focus on extracting only factual numeric data and avoid including units, symbols, or irrelevant information.
    The features' values described in a vague or unclear manner, so you are not sure they were even mentioned add to a list in "NOTFOUND" key.

    Text:  
    {description}
    """