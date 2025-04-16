import sympy as sp

#solves math equations
class MathSolution:
    def execute(self, equation_str=None):
        if not equation_str:
            return "Please provide an equation to solve. For example: `solve 2x + 3 = 7`"

        try:
            # Remove "solve" if it's included in the input
            equation_str = equation_str.lower().replace("solve", "").strip()

            # Replace "^" with "**" for Python-style exponentiation
            equation_str = equation_str.replace("^", "**")

            # If an equation is provided with '=', split it into left and right sides
            if "=" in equation_str:
                lhs, rhs = equation_str.split("=")
                equation = sp.Eq(sp.sympify(lhs), sp.sympify(rhs))
                solution = sp.solve(equation)
                return f"Solution: {solution}"

            # Otherwise, evaluate the expression (like "3 + 2")
            else:
                result = round(sp.sympify(equation_str).evalf())
                return f"Result: {result}"

        except Exception as e:
            return f"Error: {e}"
