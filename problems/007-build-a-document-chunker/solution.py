def chunk_document(text, chunk_size, overlap):
    """Split text into overlapping word chunks."""
    string = text.split()
    substrings = []
    if len(string) == 0:
        return string
    else:
        while len(string) != 0:
            substrings.append(" ".join(string[0:chunk_size]))
            if len(string) <= chunk_size:
                break
            string = string[chunk_size-overlap:]

    return(substrings)



 #[abcde]
