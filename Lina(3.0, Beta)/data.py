from response import *



 #Make all responses list as 1
list_responses = {}
list_responses.update(responses)
list_responses.update(responses2)
list_responses.update(responses3)
list_responses.update(responses4)
list_responses.update(responses5)
list_responses.update(responses6)



global_best_category = None
# Function to set the global variable
def set_global_variable(value):
    global global_best_category
    global_best_category = value
def access_global_variable():
    return global_best_category



def remove_response(input_to_remove, responses_dict):
    """
    Remove a key-value pair from the responses dictionary based on user input.

    Parameters:
    - input_to_remove (str): The user input corresponding to the key to be removed.
    - responses_dict (dict): The dictionary containing the responses.

    Returns:
    - str: A message indicating whether the removal was successful or not.
    """
    if input_to_remove in responses_dict:
        removed_response = responses_dict.pop(input_to_remove)
        return f"Successfully removed response for '{input_to_remove}': {removed_response}"
    else:
        return f"Response for '{input_to_remove}' not found in the dictionary."
    '''
    # Example usage:
    user_input = "yo"
    result_message = remove_response(user_input, responses)
    print(result_message)
    '''



def reload_items():
     #Make all responses list as 1
    list_responses = {}
    list_responses.update(responses)
    list_responses.update(responses2)
    list_responses.update(responses3)
    list_responses.update(responses4)
    list_responses.update(responses5)
    list_responses.update(responses6)
    return list_responses



#------------***---------------