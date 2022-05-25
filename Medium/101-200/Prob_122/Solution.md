### Here we have the advantage of knowing when stock price is gonna be High.

So we will buy stock today If the price is going to be higher tomorrow.
Then We can keep the profit and buy again if we see price is going to be higher tomorrow

So We only have to keep track to 2 days at a time.

Here, Price of Today = prices[i]
Price of Previous day = prices[i-1]

    We add our profit by selling our stock today
    and if we see our prices will be higher tomorrow then we buy again at today's price.

# Finally we return the profit
