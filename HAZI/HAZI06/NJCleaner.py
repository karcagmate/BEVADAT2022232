import pandas as pd
import numpy as np
class NJCleaner:
    def __init__(self,path:str) -> None:
        self.data=pd.read_csv(path)
    def order_by_scheduled_time(self)->pd.DataFrame:
        #newdata=self.data.copy()
        return self.data.sort_values(by=["scheduled_time"])
    def drop_columns_and_nan(self)->pd.DataFrame:
        colum=self.data.drop(columns=['from','to'])
        nan= colum.dropna()
        self.data=nan
        return self.data
    def convert_date_to_day(self)->pd.DataFrame:
        self.data['day']=pd.to_datetime(self.data['date']).dt.day_name()
        return self.data
    def convert_scheduled_time_to_part_of_the_day(self)->pd.DataFrame:
        self.data["part_of_the_day"]=pd.to_datetime(self.data['scheduled_time']).dt.hour.apply(lambda time:'early_morning' if time>=4 and time<8 
                                                                       else('morning'  if time>=8 and time<12  
                                                                       else ('afternoon' if time>=12 and time<16  
                                                                         else('evening' if time>=16 and time<20  
                                                                         else('night'if time>=20 and time<24  
                                                                         else 'late_night')))))
        
        colum=self.data.drop(columns=['scheduled_time'])
        self.data=colum
        return self.data   
    def convert_delay(self)->pd.DataFrame:
        self.data['delay']=self.data['delay_minutes'].apply(lambda delay:0 if delay<=5 else 1)
        return self.data
    def drop_unnecessary_columns(self)->pd.DataFrame:
        colum=self.data.drop(columns=['train_id','actual_time','delay_minutes'])
        self.data=colum
        return self.data
    def save_first_60k(self,path:str):
        sixtyk=self.data.iloc[:60000]
        sixtyk.to_csv(path,index=False)
    def prep_df(self,path:str):
        self.order_by_scheduled_time()
        self.drop_columns_and_nan()
        self.convert_date_to_day()
        self.convert_scheduled_time_to_part_of_the_day()
        self.convert_delay()
        self.drop_unnecessary_columns()
        self.save_first_60k(path)
