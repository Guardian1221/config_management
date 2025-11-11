class ConstantProcessor:
    def __init__(self):
        self.constants = {}

    def define_constant(self, name, value):
        if not name.isupper():
            raise ValueError("Имена констант должны быть в верхнем регистре.")
        self.constants[name] = value

    def process_expression(self, expression):
        for name, value in self.constants.items():
            expression = expression.replace(f"${name}$", str(value))
        return expression
