# Financial Decision Tool

A Python command-line application for personal finance calculations and investment analysis.

The project has evolved progressively from individual Python scripts into a modular application, focusing on financial calculations, code organization, and software development best practices.

It is an educational project designed to explore investment returns, fees, taxes, and financial scenarios while developing practical Python programming skills.

## Features

The project has explored the following financial tools throughout its development:

- **Simple Interest:** Calculate interest earned over a specified period.
- **Compound Interest:** Calculate investment growth through compounding.
- **Investment Analysis:** Estimate investment performance after fees (TER) and taxes.
- **Annual Investment Evolution:** Track capital growth and accumulated returns year by year.
- **Dollar-Cost Averaging (DCA):** Planned for integration into the modular application.
- **Investment Comparator:** Planned for integration into the modular application.

Feature availability may differ between historical scripts and the current modular application.

## Project Structure

```text
FINANCIAL_DECISION_TOOL/
├── CODE/
│   ├── V1_Fundamentals.py
│   ├── V2.0_Time_&_Interests.py
│   ├── V2.5_Investment_Comparator.py
│   ├── V3.0_TER_&_Taxes.py
│   ├── V3.1_Scenario_Analysis.py
│   └── V3.2_Annual_Evolution.py
├── financial_decision_tool/
│   ├── cli.py
│   ├── calculations.py
│   └── validators.py       # Planned
├── tests/                  # Automated tests planned
├── LICENSE
└── README.md
```

The `CODE/` directory preserves the historical versions developed throughout the project.

The `financial_decision_tool/` directory contains the new modular application, separating user interaction from financial calculation logic.

Input validation and automated testing are planned improvements and may not yet be implemented.

## Modular Architecture

The project is transitioning from standalone scripts to a more maintainable structure.

- **CLI module:** Handles menus, user input, and the presentation of results.
- **Calculations module:** Contains reusable financial calculation functions.
- **Validation module:** Planned component for validating user input and preventing invalid values.
- **Tests:** Planned automated checks to verify calculation results and edge cases.

This separation aims to improve readability, maintainability, and future extensibility.

## Historical Development

### V1 — Fundamentals

Introduced the basic concepts of personal finance and Python programming:

- Saving capacity and saving rate.
- Uninvested savings.
- Functions and return values.
- Conditional logic and loops.
- Basic input validation.

### V2.0 — Time and Interests

Expanded the application with investment calculations:

- Simple and compound interest.
- Dollar-Cost Averaging (DCA).
- Monthly contributions.
- Total contributed capital and investment returns.
- Reusable functions and multiple return values.
- Input validation and error handling.

### V2.5 — Investment Comparator

Introduced comparisons between investment scenarios:

- Different initial capital amounts.
- Different investment periods and annual rates.
- Final capital calculations.
- Structured storage and comparison of results.
- Input validation and retry logic.

### V3.0 — TER and Taxes

Expanded investment analysis to account for fees and taxes:

- Compound investment growth.
- Gross profit and gross returns.
- TER (Total Expense Ratio).
- Annual fee calculations.
- Fractional investment periods.
- Profit after fees and simplified tax calculations.
- Iterative calculations using loops.

### V3.1 — Scenario Analysis

Introduced investment scenario analysis:

- Individual annual rate scenarios.
- Configurable rate ranges and increments.
- Comparison of final capital under different assumptions.
- Lists and loops for processing multiple scenarios.
- Reuse of compound interest calculations.

### V3.2 — Annual Evolution

Introduced a year-by-year view of investment growth:

- Annual compound growth.
- Capital evolution over time.
- Fractional investment periods.
- Year-to-capital dictionaries.
- Code cleanup and minor refactoring.

### Modular Application — Current Development Stage

The project is moving towards a modular architecture:

- Separation of the command-line interface and financial calculations.
- Improved code organization and readability.
- More consistent output presentation.
- Preparation for dedicated input validation and automated tests.

## Roadmap

- [x] Develop the initial personal finance calculation scripts.
- [x] Introduce investment analysis and scenario comparison in historical versions.
- [x] Develop annual investment evolution in the historical version.
- [x] Begin separating CLI logic from financial calculations.
- [ ] Complete and verify the modular application.
- [ ] Implement a dedicated input validation module.
- [ ] Add automated tests in `tests/`.
- [ ] Integrate DCA into the modular application.
- [ ] Integrate the investment comparator into the modular application.
- [ ] Improve documentation and expand test coverage.

## How to Run

Run the appropriate Python script from the project root, using a compatible Python 3 installation.

For the modular application, the exact command depends on the package entry point and import structure. Update this section once the execution method has been finalized.

## Technologies

- Python 3
- Git and GitHub

Potential future technologies include NumPy, Pandas, SQL, PostgreSQL, and Docker as the project grows.

## Disclaimer

This project is intended for educational purposes, experimentation, and personal learning.

Financial calculations use simplified assumptions and may not account for every real-world factor, including changing market conditions, fees, tax rules, or individual circumstances. Results should not be considered professional financial or investment advice.

## License

This project is released under the [CC0 1.0 Universal license](LICENSE).

## About

Financial Decision Tool is a personal Python project focused on learning software development through practical financial calculations and investment analysis.

The project evolves incrementally, preserving historical versions while moving towards a more modular, testable, and maintainable application.
