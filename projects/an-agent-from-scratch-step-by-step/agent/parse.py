def text_blocks(response):
    result = []

    for block in response.get('content', []):
        if block['type'] == 'text':
            result.append(block['text'])
    
    return result


def text_of(response):
    result = text_blocks(response)
    seperator = '\n'.join(result)
    return seperator.strip()
