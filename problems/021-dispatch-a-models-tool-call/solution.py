def dispatch(response, registry):
    """Run every tool call in a response and return one result per call."""
    results = []
    for call in response.tool_calls:
        try:
            content = registry.call(call.name, call.input)
            is_error = False
        except ToolError as exc:
            content = str(exc)
            is_error = True
        results.append({
    "tool_use_id": call.id,
    "content": content,
    "is_error": is_error,
})
    return results


    
