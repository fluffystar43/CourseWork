NOT_FIT = 1         # кандидатка не подходит
FIT = 2             # кандидатка подходит

def classify(X):
    iq_level, articles_count, has_education, ratio = X    
    if iq_level <= 70:
        return NOT_FIT
    elif articles_count == 1:
        return FIT
    elif ratio <= 2.2:
        return FIT
    else:
        return NOT_FIT