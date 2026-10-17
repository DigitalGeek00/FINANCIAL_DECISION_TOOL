# Financial Decision Tool

A Python project for exploring financial concepts and evaluating investment decisions through interactive calculations.

The project began as a collection of standalone scripts and is evolving into a modular application, with the goal of improving code organization, maintainability, and extensibility.

## Overview

Financial Decision Tool provides calculations and analysis related to interest, investment performance, and the impact of fees and taxes.

The project also preserves its earlier versions to document its development and the progression from individual scripts to a more structured application.

**Disclaimer:** This project is intended for educational purposes only. It does not provide financial advice. Results depend on the assumptions and inputs supplied by the user.

## Features

### Current modular application

The modular application currently includes:

- **Simple interest:** Calculate interest and accumulated capital over time.
- **Compound interest:** Estimate capital growth through compounding.
- **Investment analysis:** Evaluate investment outcomes considering fees and taxes.
- **Annual evolution:** Explore how an investment may evolve over time.

The application is being developed incrementally. Some features from the historical scripts may still need to be integrated into the modular version.

### Features planned for integration

- **Dollar-cost averaging (DCA):** Model recurring investments over time.
- **Investment comparator:** Compare investment alternatives under different assumptions.
- **Input validation:** Improve the handling of invalid or unexpected user input.
- **Automated tests:** Verify the correctness and reliability of financial calculations.

## Project Structure

```text
FINANCIAL_DECISION_TOOL/
├── legacy/
│   ├── V1_Fundamentals.py
│   ├── V2.0_Time_&_Interests.py
│   ├── V2.5_Investment_Comparator.py
│   ├── V3.0_TER_&_Taxes.py
│   ├── V3.1_Scenario_Analysis.py
│   └── V3.2_Annual_Evolution.py
├── financial_decision_tool/
│   ├── cli.py
│   └── calculations.py
├── tests/
├── README.md
└── LICENSE
```

This structure reflects the intended organization of the repository. Additional modules, such as `validators.py`, can be introduced as development progresses. The `tests/` directory is intended for automated tests.

## Architecture

The current application separates responsibilities into modules:

- **`cli.py`:** Handles the command-line interface and user interaction.
- **`calculations.py`:** Contains the core financial calculation functions.
- **`tests/`:** Reserved for automated tests as the testing suite is developed.
- **`legacy/`:** Preserves previous versions of the project for reference.

This separation aims to make the code easier to understand, maintain, test, and extend.

## Project Evolution

The project has developed through several iterations:

| Version | Focus                               |
| ------- | ----------------------------------- |
| V1      | Fundamental financial calculations  |
| V2.0    | Time and interest calculations      |
| V2.5    | Investment comparison               |
| V3.0    | Total Expense Ratio (TER) and taxes |
| V3.1    | Investment scenario analysis        |
| V3.2    | Annual investment evolution         |

These historical scripts are retained in `legacy/` to document the project's progression and preserve earlier implementations.

## Getting Started

### Requirements

- Python 3

No third-party dependencies are currently required for the basic application, unless additional packages are introduced in future development.

### Running the application

Run the application from the repository root using the entry point configured for the current project structure.

For example, if the package is configured to support module execution:

```bash
python -m financial_decision_tool.cli
```

If the current imports or package configuration do not support this command yet, run the entry-point script using the invocation appropriate to the existing setup.

## Roadmap

Planned development includes:

- [X] Complete the integration of DCA and investment comparison into the modular application.
- [ ] Add input validation and more robust error handling.
- [ ] Introduce automated tests for financial calculations.
- [ ] Evaluate the use of libraries such as NumPy and Pandas where they provide clear benefits.
- [ ] Explore data persistence and database integration if the project requirements justify it.
- [ ] Consider packaging and containerization as the application matures.

The roadmap may change as the project evolves.

## Technologies

- **Python** — Application logic and financial calculations.
- **Git and GitHub** — Version control and project collaboration.

## License

This project is released under the [CC0 1.0 Universal license](LICENSE).

## About

Financial Decision Tool is a personal learning project focused on Python development, financial calculations, and the gradual evolution of a codebase toward a modular application.

Contributions, suggestions, and constructive feedback are welcome.
