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


def tool_uses(response):
    result = []
    content = response.get("content", [])
    for block in content:
        if block['type'] == "tool_use":
            result.append(block)
        
    return result


def wants_tool(response):
    wants = response.get("stop_reason")
    if wants == 'tool_use':
        return True
    else:
        return False


def assistant_message(response):
    message = response.get('content', [])
    return {'role': 'assistant', 'content': message}
