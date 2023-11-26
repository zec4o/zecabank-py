# ZecaBank 🏦

ZecaBank is a simple, command-line banking experience designed for learning Python. This project allows you to practice fundamental Python concepts while exploring basic money operations like depositing, withdrawing, and checking your account statement.

## New Features

- **Refactored Operations**: Each operation (deposit, withdraw, show statement) is now a separate function, improving code readability and maintainability.
- **User Creation**: You can now create a new user with a name, birth date, CPF, and address.
- **Account Creation**: You can now create a new account for a user.
- **List Accounts**: You can now list all accounts in the system.

## Python Concepts Reinforced 🚀

1. **User Input and Output:**

   - The project extensively uses `input()` to receive user choices and amounts.
   - `print()` statements are employed to provide feedback and display information to the user.

2. **Conditional Statements:**

   - Conditional statements (`if`, `elif`, `else`) control the flow of the program based on user choices and account conditions.

3. **Loops:**

   - A `while` loop is used for the main program flow, allowing the user to interact with the banking system until they choose to exit.

4. **String Formatting:**

   - String formatting is utilized, such as f-strings, to display information concisely.

5. **Error Handling:**

   - The program includes error handling to guide users when they enter invalid values or attempt operations that don't comply with the rules.

6. **Break and Continue Statements:**

   - The `break` statement is used to exit a loop when a condition is met.
   - `continue` is used to skip the rest of the loop and move to the next iteration.

7. **Functions:**

   - The project uses functions to encapsulate operations such as deposit, withdraw, and showing the statement. This improves code readability and reusability.
   - Functions also help in structuring the code and making it easier to understand and maintain.
   - The use of both positional and keyword arguments in function definitions is demonstrated.

## How to Use 🌟

1. Run the `zecabank.py` script with `python zecabank.py`.
2. Follow the menu to choose your operation.

## Operations 💰

- **Deposit (d):**

  - Add money to your account.

- **Withdraw (w):**

  - Make up to 3 withdrawals a "day" (basicly a run), limited to $500 each.

- **Statement (s):**

  - View your transaction history and balance.

- **New User (nu):**

  - Create a new user by entering the user's CPF, name, birth date, and address.

- **New Account (na):**

  - Create a new account for a user by entering the user's CPF.

- **List Accounts (la):**

  - List all accounts in the system.

- **Exit (q):**

  - Exit the system.

## Usage Tips 🚨

- Follow the prompts to enter values and select operations.
- Check error messages for guidance.
- The app limits you to 3 withdrawals "daily", each capped at $500.

## Disclaimer 🛑

This project is for learning purposes. It's a basic simulation, not a real banking solution. Feel free to explore and modify the code to better understand Python and basic banking operations.

## License 📝

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Feedback and Contributions 🤝

If you have any feedback or would like to contribute to this project, please [open an issue](https://github.com/zec4o/zecabank-py/issues) or [create a pull request](https://github.com/zec4o/zecabank-py/pulls). We welcome your input!

Happy ZecaBanking! 🎉🏦
