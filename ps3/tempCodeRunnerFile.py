    tf_dict = {} 

    text_file = load_file(file_path)
    text_list = text_to_list(text_file)

    total_words = len(text_list)

    freq_dict = get_frequencies(text_list)
    for key in freq_dict:
        tf = freq_dict[key] / total_words
        tf_dict[key] = tf
    return tf_dict