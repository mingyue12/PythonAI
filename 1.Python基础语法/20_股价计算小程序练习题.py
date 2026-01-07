

name = "黑马程序员"
stock_price = 6.5
stock_code = "003032"
stock_price_daily_growth_factor = 1.2
growth_days = 7
print(f"股票代码是{stock_code}，名称是{name}，当前股价是{stock_price}，未来{growth_days}天股价增长率为{stock_price_daily_growth_factor}，则未来{growth_days}天股价为{stock_price * stock_price_daily_growth_factor ** growth_days:.2f}")
