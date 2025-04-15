import sympy as sp

#solve  math equations
class MathSolution:
    def execute(self):
        equation_str = input("What is the Equation? ")  # This was the problem: you used `equations` instead
        try:
            # Replace "^" with "**" for Python syntax
            equation_str = equation_str.replace("^", "**")
            
            # Split into left and right sides
            if "=" in equation_str:
                lhs, rhs = equation_str.split("=")
                equation = sp.Eq(sp.sympify(lhs), sp.sympify(rhs))
                solution = sp.solve(equation)
            else:
                # If it's just an expression (like "2 + 3")
                solution = sp.sympify(equation_str).evalf()
            
            return f"Chatbot: {round(solution)}"
        except Exception as e:
            return f"Error: {e}"