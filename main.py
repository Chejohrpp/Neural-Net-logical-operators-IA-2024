from entities.sp_logical_operator import FactorsX, LogicalOperatorFactors, SpLogicalOperator

FACTOR_OR = LogicalOperatorFactors(2)
FACTOR_OR.add_factors(FactorsX([0,0], 0))
FACTOR_OR.add_factors(FactorsX([0,1], 1))
FACTOR_OR.add_factors(FactorsX([1,0], 1))
FACTOR_OR.add_factors(FactorsX([1,1], 1))

LOGICAL_OR = SpLogicalOperator(FACTOR_OR)
LOGICAL_OR.training()

# FACTOR_AND = LogicalOperatorFactors(2)
# FACTOR_AND.add_factors(FactorsX([0,0], 0))
# FACTOR_AND.add_factors(FactorsX([0,1], 0))
# FACTOR_AND.add_factors(FactorsX([1,0], 0))
# FACTOR_AND.add_factors(FactorsX([1,1], 1))

# LOGICAL_AND = SpLogicalOperator(FACTOR_AND)
# LOGICAL_AND.training()

# FACTOR_AND = LogicalOperatorFactors(3)
# FACTOR_AND.add_factors(FactorsX([0,0,0], 0))
# FACTOR_AND.add_factors(FactorsX([0,0,1], 1))
# FACTOR_AND.add_factors(FactorsX([0,1,0], 1))
# FACTOR_AND.add_factors(FactorsX([0,1,1], 1))
# FACTOR_AND.add_factors(FactorsX([1,0,0], 0))
# FACTOR_AND.add_factors(FactorsX([1,0,0], 0))
# FACTOR_AND.add_factors(FactorsX([1,0,1], 1))
# FACTOR_AND.add_factors(FactorsX([1,1,1], 1))

# LOGICAL_AND = SpLogicalOperator(FACTOR_AND)
# LOGICAL_AND.training()


# FACTOR_XOR = LogicalOperatorFactors(2)
# FACTOR_XOR.add_factors(FactorsX([0,0], 0))
# FACTOR_XOR.add_factors(FactorsX([0,1], 1))
# FACTOR_XOR.add_factors(FactorsX([1,0], 1))
# FACTOR_XOR.add_factors(FactorsX([1,1], 0))

# LOGICAL_XOR = SpLogicalOperator(FACTOR_XOR)
# LOGICAL_XOR.training()


# FACTOR_NAND = LogicalOperatorFactors(2)
# FACTOR_NAND.add_factors(FactorsX([0,0], 1))
# FACTOR_NAND.add_factors(FactorsX([0,1], 1))
# FACTOR_NAND.add_factors(FactorsX([1,0], 1))
# FACTOR_NAND.add_factors(FactorsX([1,1], 0))

# LOGICAL_NAND = SpLogicalOperator(FACTOR_NAND)
# LOGICAL_NAND.training()