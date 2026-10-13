import math

## Interest calculations
# simple_interest()
def simple_interest(initial_capital, time, annual_rate):
    interests_s = initial_capital * time * annual_rate
    simple_f_c = initial_capital + interests_s
    return interests_s, simple_f_c
# compound_interest()
def compound_interest(initial_capital, time, annual_rate):
    compound_f_c = initial_capital * (1 + annual_rate) ** time
    interests_c = compound_f_c - initial_capital
    return compound_f_c, interests_c

## Investment analysis

def inv_analysis(initial_capital, time, annual_rate, ter, taxes):
    """
    Estimates an investment's performance after TER fees and taxes.

    TER (Total Expense Ratio) is the annual operating expense ratio
    of an investment fund, expressed as a proportion of its assets.

    MODEL ASSUMPTIONS:
    - The annual investment return is applied before the TER fee.
    - The TER is approximated as a yearly deduction from the capital
      after applying the annual return.
    - For fractional years, the TER is estimated proportionally
      to the fraction of the year.
    - Taxes are applied to positive profits after TER fees.
    - The model assumes a constant annual return and TER.

    IMPORTANT LIMITATIONS:
    This is a simplified estimation, not an exact simulation of how
    fund expenses affect its net asset value over time. In practice,
    fund expenses are generally reflected progressively in the
    fund's net asset value rather than deducted as a single annual
    charge. The timing and compounding of fees may therefore produce
    slightly different results.

    PARAMETERS:
        initial_capital (float): Initial investment amount in euros.
        time (float): Investment duration in years.
        annual_rate (float): Assumed annual return as a decimal.
        ter (float): Annual TER as a decimal
                     (e.g. 0.0012 represents 0.12%).
        taxes (float): Tax rate as a decimal
                       (e.g. 0.19 represents 19%).

    RETURNS:
        A tuple containing:
        - tax_rate: Tax rate applied.
        - current_ter: Sum of estimated TER deductions in euros.
        - tax_amount: Estimated taxes in euros.
        - compound_f_c: Final capital before TER and taxes.
        - profit: Gross profit before TER and taxes.
        - final_profit: Profit after estimated TER and taxes.
        - ter_total_effect: Difference between final capital before
          TER and final capital after TER, before taxes.

    NOTE:
        ter_total_effect includes the estimated impact of lost future
        growth due to fees; it is not simply the sum of TER deductions.
    """
    compound_f_c, interests_c = compound_interest(initial_capital, time, annual_rate)
    
    profit = compound_f_c - initial_capital
    full_years = math.floor(time)
    fractional_years = time - full_years

    current_capital = initial_capital
    current_ter = 0

    for i in range(full_years):

        annual_return = current_capital * annual_rate
        current_capital += annual_return
        annual_ter = current_capital * ter
        current_ter += annual_ter
        current_capital -= annual_ter

    if fractional_years > 0:
        current_capital *= (1 + annual_rate) ** fractional_years

        fractional_ter = current_capital * ter * fractional_years
        current_ter += fractional_ter
        current_capital -= fractional_ter

    profit_after_ter = current_capital - initial_capital

    tax_rate = taxes
    taxable_profit = max(0, profit_after_ter)
    tax_amount = taxable_profit * tax_rate
    final_profit = profit_after_ter - tax_amount

    capital_after_ter = initial_capital + profit_after_ter
    ter_total_effect = compound_f_c - capital_after_ter
# Mide la diferencia de capital final respecto al escenario sin comisiones, incluyendo la rentabilidad perdida.

    return (
        tax_rate,
        current_ter,
        tax_amount,
        compound_f_c,
        profit,
        final_profit,
        ter_total_effect,
    )

#Evolution:
def evolution_function(initial_capital, time, annual_rate):
    full_years = math.floor(time)
    fractional_years = time - full_years

    current_capital = initial_capital
    capital_evolution = {0: initial_capital}
    fractional_return = 0

    for year in range(1, full_years + 1):

        annual_return = current_capital * annual_rate
        current_capital += annual_return
        capital_evolution[year] = current_capital

    if fractional_years > 0:
        fractional_return = current_capital * annual_rate * fractional_years
        current_capital += fractional_return

    for year, capital in capital_evolution.items():
        print (f'Year {year}: {capital:.2f} €')

    if fractional_years > 0:
        print (f'Final fractional period: {fractional_years:.2f} years')

    gross_return = current_capital - initial_capital
    accumulated_return = ((gross_return) / initial_capital) * 100
    return(
        gross_return,
        current_capital,
        accumulated_return
    )
