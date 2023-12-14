class Session:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Session, cls).__new__(cls)
        return cls._instance

# Create a few Session object
sa = Session()
sb = Session()

# Print these objects
print(sa)
print(sb)

# Check if they equal or not
print(sa == sb)