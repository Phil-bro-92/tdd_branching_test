class CompoundInterest:
    def __init__(self, starting_amount, years, interest_rate):
        self.starting_amount = starting_amount
        self.years = years
        self.interest_rate = interest_rate
    
    def calculate_compound_interest(self,):
        result = (self.starting_amount * contribution) * (1 + self.interest_rate / 12) ** (self.years * 12)
        return round(result, 2)


