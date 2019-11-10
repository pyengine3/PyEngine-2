class Component:
    def __init__(self):
        self.entity = None
        self.required_components = set()
        self.incompatible_components = set()
