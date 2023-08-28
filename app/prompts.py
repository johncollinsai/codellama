# gpt-4
USER_PROMPT = """
Please describe this code {prompt}. Please check and comment upon the following where appropriate to do so, with regard to {prompt}:
1. Functional Aspects
    - Correctness: Does the code do what it's supposed to do? Is it handling all edge cases?
    - Performance: Will the code run efficiently with large datasets or under heavy load?
    - Security: Are there any security vulnerabilities like SQL injection, XSS, etc.?
    - Error Handling: Are errors caught and managed effectively? Is the user notified in an understandable way?
2. Code Quality
    - Readability: Is the code easy to read and understand?
    - Consistency: Is the code consistent with the project's coding standards?
    - Modularity and Structure: Is the code well-organized, modular, and divided into functions or classes appropriately?
    - Comments and Documentation: Are comments clear, concise, and necessary? Is there documentation for complex parts of the code?
    - Duplication: Is there duplicated code that could be refactored?
3. Best Practices
    - SOLID Principles: Does the code adhere to the SOLID principles (Single Responsibility, Open-Closed, Liskov Substitution, Interface Segregation, Dependency Inversion)?
    - DRY (Don't Repeat Yourself): Are there parts of the code that could be more modular or reusable?
    - KISS (Keep It Simple, Stupid): Is the code as simple as possible? Is complexity introduced only when necessary?
    - YAGNI (You Aren't Gonna Need It): Is the code focused on current requirements and not over-engineered for future needs?
4. Refactoring the code
    - What would you change about this code?
    - What would you add to this code?
    - What would you remove from this code?
    - What would you refactor in this code?
    - Provide examples of how you would refactor this code.
"""

# codellama-7b
USER_PROMPT_LLAMA = """
Please describe this code {prompt}. 
"""