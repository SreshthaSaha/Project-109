import statistics
import csv
import pandas as pd

data = pd.read_csv("StudentsPerformance.csv")
math_score_list = data["math score"].to_list()

mean = statistics.mean(math_score_list)

Math_Score_STD  =statistics.stdev(math_score_list)

Math_Score_first_STD_start ,  Math_Score_first_STD_end = mean - Math_Score_STD , mean + Math_Score_STD
Math_Score_second_STD_start ,  Math_Score_second_STD_end = mean - (2 * Math_Score_STD) , mean + (2 * Math_Score_STD)
Math_Score_third_STD_start ,  Math_Score_third_STD_end = mean - (3 * Math_Score_STD) , mean + (3 * Math_Score_STD)

math_score_list_of_data_btw_STD1 = [result for result in math_score_list if result > Math_Score_first_STD_start and result < Math_Score_first_STD_end]
print("Data between first deviation : " , format(len(math_score_list_of_data_btw_STD1)* 100 / len(math_score_list)))

weight_list_of_data_btw_STD2 = [result for result in math_score_list if result > Math_Score_second_STD_start and result < Math_Score_second_STD_end]
print("Data between second deviation : ", format(len(weight_list_of_data_btw_STD2)* 100 / len(math_score_list)))

weight_list_of_data_btw_STD3 = [result for result in math_score_list if result > Math_Score_third_STD_start and result < Math_Score_third_STD_end]
print("Data between third deviation : ", format(len(weight_list_of_data_btw_STD3)* 100 / len(math_score_list)))