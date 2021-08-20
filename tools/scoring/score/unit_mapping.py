# Unit Mappings

# Dimensional fields should have correct mappings for their units of measure or states to standard DBO values.  In practical terms, identification of the units field for any known field will be trivial in the data participants receive.  We will therefore assume it is correct and not score it.

# What we can score is the Key:value mapping of native unit names to canonical names.  This may be done for each dimensional field in the solution set field-by-field basis (though it is somewhat redundant in practical terms).  Scoring will be:
#  (number of correctly defined Key:value pairs) - (number of incorrectly defined key:value pairs) total key:value pairs

# This score should be calculated independently overall and for fields that were correctly identified as important.

class UnitMapping:
    def __init__(self):
        return False
