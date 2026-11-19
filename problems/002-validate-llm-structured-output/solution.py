import json

def validate_response(raw, schema):
    """Parse and validate a model's JSON reply against a {field: type} schema.

    Return the cleaned dict, or None if it cannot be trusted.
    """
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        return None
    
    cleaned = {}

    if isinstance(data, dict):
        for field, expected in schema.items():
            if field in data and type(data[field]) is expected:
                cleaned[field] = data[field]
            else:
                return None
        return cleaned

   

        
        

