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

dl = DataLoader("/input/day_3.xlsx")

PCC = PowerConsumptionCalculator(dl.transformed_df)

