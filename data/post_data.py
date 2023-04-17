NEW_USER_DATA = {
    "name": "morpheus",
    "job": "leader"
}

CREATE_SCHEMA = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "job": {"type": "string"},
        "id": {"type": "string"},
        "createdAt": {"type": "string"},
    },
    "required": ["name", "job", "id", "createdAt"]
}


NEGATIVE_DATA = {
    "name": "negative"
}
