import sympy as sp

class MathSolution:
    def execute(self, equation_str=None):
        if not equation_str:
            return "Please provide an equation to solve. For example: `solve 2x + 3 = 7`"

        try:
            # Replace "^" with "**" for Python-style exponentiation
            equation_str = equation_str.replace("^", "**")

            # Split into left and right sides
            if "=" in equation_str:
                lhs, rhs = equation_str.split("=")
                equation = sp.Eq(sp.sympify(lhs), sp.sympify(rhs))
                solution = sp.solve(equation)
                return f"Solution: {solution}"
            else:
                # If it's just an expression (like "2 + 3")
                result = sp.sympify(equation_str).evalf()
                return f"Result: {result}"

        except Exception as e:
            return f"Error: {e}"
