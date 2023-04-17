UPDATE_VALIDATE_SCHEMA = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "job": {"type": "string"},
        "updatedAt": {"type": "string"},
    },
    "required": ["name", "job", "updatedAt"]
}

UPDATE_CORRECT_SCHEMA = {
    "name": "morpheus",
    "job": "leader"
}
