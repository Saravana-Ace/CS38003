def years_to_million(amount, interestRate, dividend):
    if(amount < 0 or interestRate < 0 or interestRate > 0.1 or dividend < 0):
        return -1

    final = amount
    counter = 0
    while(final < 1000000):
        final += (final * interestRate)
        counter += 1
        if (counter % 5 == 0):
            final += dividend

    return counter
