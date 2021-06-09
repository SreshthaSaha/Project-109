import statistics
import csv
import pandas as pd

data = pd.read_csv("StudentsPerformance.csv")
reading_score_list = data["reading score"].to_list()

mean = statistics.mean(reading_score_list)

Reading_Score_STD  =statistics.stdev(reading_score_list)

Reading_Score_first_STD_start ,  Reading_Score_first_STD_end = mean - Reading_Score_STD , mean + Reading_Score_STD
Reading_Score_second_STD_start ,  Reading_Score_second_STD_end = mean - (2 * Reading_Score_STD) , mean + (2 * Reading_Score_STD)
Reading_Score_third_STD_start ,  Reading_Score_third_STD_end = mean - (3 * Reading_Score_STD) , mean + (3 * Reading_Score_STD)

reading_score_list_of_data_btw_STD1 = [result for result in reading_score_list if result > Reading_Score_first_STD_start and result < Reading_Score_first_STD_end]
print("Data between first deviation : " , format(len(reading_score_list_of_data_btw_STD1)* 100 / len(reading_score_list)))

weight_list_of_data_btw_STD2 = [result for result in reading_score_list if result > Reading_Score_second_STD_start and result < Reading_Score_second_STD_end]
print("Data between second deviation : ", format(len(weight_list_of_data_btw_STD2)* 100 / len(reading_score_list)))

weight_list_of_data_btw_STD3 = [result for result in reading_score_list if result > Reading_Score_third_STD_start and result < Reading_Score_third_STD_end]
print("Data between third deviation : ", format(len(weight_list_of_data_btw_STD3)* 100 / len(reading_score_list)))