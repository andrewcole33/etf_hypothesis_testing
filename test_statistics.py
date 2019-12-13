import statistics
import scipy.stats as stats
import math
import numpy as np

def calculate_test_stats(avg_pct_index1, avg_pct_index2):
    '''
    Function to calculate the Z-statistic of a sample mutual fund index compared to its benchmark index (population) as well as a p-value for the same two indices
    
    Input: 
    
    avg_pct_index1: list containing random sampling (n>50) of average daily percent changes for asset index in question 
    avg_pct_index2: list containing random sampling (n>50) of average daily percent changes for benchmark index (population)
    
    Output: Z-stat, P-value
    '''
    
    x_hat = sum(avg_pct_index1)/len(avg_pct_index1)
    mu = sum(avg_pct_index2)/len(avg_pct_index2)
    sigma = statistics.stdev(avg_pct_index2)
    n = len(avg_pct_index1)
    
    z_stat = (x_hat - mu)/sigma/math.sqrt(n)
    
    p_val = stats.norm.cdf(z_stat)
    
    standard_error = sigma/math.sqrt(n)
    
    return print(f" Z-stat; {z_stat}",'\n', f"P-Value: {p_val}",'\n', f"Standard Error: {standard_error}")

    
def calculate_cohens_d(sample_asset, population_asset):
    '''
    Function to calculate Cohen's D test statistic
    
    Input: 
    
    '''
    sample_pct_change_mean = sample_asset['day_pct_change'].mean()
    population_pct_change_mean = population_asset['day_pct_change'].mean()
    
    diff_mean = sample_pct_change_mean - population_pct_change_mean
    
    n_sample = len(sample_asset['day_pct_change'])
    n_pop = len(population_asset['day_pct_change'])
    var_sample = sample_asset['day_pct_change'].var()
    var_pop = population_asset['day_pct_change'].var()
    
    pooled_var = (n_sample * var_sample + n_pop * var_pop)/(n_sample + n_pop)
    
    cod = diff_mean / np.sqrt(pooled_var)
    
    return print(f"Cohen's D: {cod}")

