import os

def read_secret(secret_name: str) -> str | None:
    path = f"/run/secrets/{secret_name}"
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return os.getenv(secret_name)
