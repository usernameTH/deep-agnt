def tool_spec(name, description, properties=None, required=None):
    return {'name': name, 
    'description': description, 
    "input_schema": {
    "type": "object",
    "properties": dict(properties) if properties is not None else {},
    "required": list(required) if required is not None else [],
}}
