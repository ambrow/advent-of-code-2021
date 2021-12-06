import pandas as pd
import constants

class DataLoader:
    def __init__(self, path:str):
        self.original_df = pd.read_excel(constants.wd + path, dtype=str)
        self._transform_data()
    
    def _transform_data(self):
        self.transformed_df = pd.DataFrame(self.original_df.binary.apply(lambda x: pd.Series(list(x))))

class PowerConsumptionCalculator:
    def __init__(self, df: pd.DataFrame):
        self.transformed_df = df.copy()
        self._calc_gamma_rate()
        self._calc_epsilon_rate()
        self.calc_power_consumption()


    def _calc_gamma_rate(self):
        gamma_rate_dict = {i:self.transformed_df[i].mode().values[0] for i in range(0, len(self.transformed_df.columns))}
        self.most_common_bits = ("".join(v for v in gamma_rate_dict.values()))
        self.gamma_rate = int(self.most_common_bits, 2)
        
    def _calc_epsilon_rate(self):
        self.least_common_bits = self.most_common_bits.replace("1","a").replace("0","1").replace("a","0")
        self.epsilon_rate = int(self.least_common_bits, 2)
    
    def calc_power_consumption(self):
        
        print(f"Power Consumption is: {self.gamma_rate*self.epsilon_rate}")

dl = DataLoader("/inputs/day_3.xlsx")

PCC = PowerConsumptionCalculator(dl.transformed_df)

class LifeSupportCalculator:
    def __init__(self, df: pd.DataFrame):
        self.transformed_df = df.copy()
        self.calc_life_support()

    def find_most_common_value(self, s: pd.Series):

        if len(s.mode().values) > 1:
            ret_val = "1"
        else:
            ret_val = s.mode().values[0]

        return ret_val

    def find_indices(self, s: pd.Series, v):
        return (s == v)

    def _calc_oxygen_generator_rating(self):
        op_df = self.transformed_df.copy()

        for col in op_df.columns.tolist():
            
            current_value = self.find_most_common_value(op_df[col])
            print(f"mode is: {current_value} for column {col}")
            indices = self.find_indices(op_df[col], current_value)
            
            op_df = op_df.loc[indices].copy()
            print(f"data is of shape: {op_df.shape}")

            if op_df.shape[0] == 1:
                self.oxygen_generator_rating = "".join(v for v in op_df.values.tolist()[0])
                print(f"oxygen generator rating is: {int(self.oxygen_generator_rating, 2)}")
                break
            
    def _calc_co2_scrubber_rating(self):
        op_df = self.transformed_df.copy()

        for col in op_df.columns.tolist():
            
            current_value = self.find_most_common_value(op_df[col])
            if current_value == "0":
                lcv = "1"
            else:
                lcv = "0"
            print(f"mode is: {current_value} for column {col}")
            indices = self.find_indices(op_df[col], lcv)
            
            op_df = op_df.loc[indices].copy()
            print(f"data is of shape: {op_df.shape}")

            if op_df.shape[0] == 1:
                self.co2_scrubber_rating = "".join(v for v in op_df.values.tolist()[0])
                print(f"co2 scrubber rating is: {int(self.co2_scrubber_rating, 2)}")
                break
    
    def calc_life_support(self):
        self._calc_oxygen_generator_rating()
        self._calc_co2_scrubber_rating()
        print(f"life support rating is: {int(self.oxygen_generator_rating, 2) * int(self.co2_scrubber_rating, 2)}")
            

LSC = LifeSupportCalculator(dl.transformed_df)