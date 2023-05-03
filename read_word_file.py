def read_words_from_file(file_path):
    """
    Reads words from a text file where words are separated by commas or new lines.
    
    Args:
        file_path (str): The path to the text file.
        
    Returns:
        list: A list of words.
    """
    
    with open(file_path, 'r', encoding="utf-8") as file:
        # Read the entire file as a string
        text = file.read()
        
    # Split the string on commas and new lines to get a list of words
    words = text.replace('\n', ',').split(',')
    
    # Strip any whitespace from each word
    words = [word.strip() for word in words]
    
    # Remove any empty strings
    words = list(filter(None, words))
    
    return words