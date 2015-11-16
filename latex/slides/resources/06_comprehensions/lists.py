varList = [var*8 for var in range(10)]
# => [0, 8, 16, 24, 32, 40, 48, 56, 64, 72]


# Mit Filter (hier: Fuer i ist gerade)
evenVarList = [var*8 for var in range(10) if var % 2 == 0]
# => [0, 16, 32, 48, 64]
