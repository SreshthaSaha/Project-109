import statistics
import csv
import pandas as pd

data = pd.read_csv("StudentsPerformance.csv")
writing_score_list = data["writing score"].to_list()

mean = statistics.mean(writing_score_list)

writing_Score_STD  =statistics.stdev(writing_score_list)

writing_Score_first_STD_start ,  writing_Score_first_STD_end = mean - writing_Score_STD , mean + writing_Score_STD
writing_Score_second_STD_start ,  writing_Score_second_STD_end = mean - (2 * writing_Score_STD) , mean + (2 * writing_Score_STD)
writing_Score_third_STD_start ,  writing_Score_third_STD_end = mean - (3 * writing_Score_STD) , mean + (3 * writing_Score_STD)

writing_score_list_of_data_btw_STD1 = [result for result in writing_score_list if result > writing_Score_first_STD_start and result < writing_Score_first_STD_end]
print("Data between first deviation : " , format(len(writing_score_list_of_data_btw_STD1)* 100 / len(writing_score_list)))

weight_list_of_data_btw_STD2 = [result for result in writing_score_list if result > writing_Score_second_STD_start and result < writing_Score_second_STD_end]
print("Data between second deviation : ", format(len(weight_list_of_data_btw_STD2)* 100 / len(writing_score_list)))

weight_list_of_data_btw_STD3 = [result for result in writing_score_list if result > writing_Score_third_STD_start and result < writing_Score_third_STD_end]
print("Data between third deviation : ", format(len(weight_list_of_data_btw_STD3)* 100 / len(writing_score_list)))