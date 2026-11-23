def text_blocks(response):
    result = []

    for block in response.get('content', []):
        if block['type'] == 'text':
            result.append(block['text'])
    
    return result
