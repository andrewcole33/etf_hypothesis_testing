# *Module 3 Project*

## *Project Members: Andrew Cole & Will Herzog*

### Goals:
To gather data and perform necessary statistical analysis on collected data in order to present results to stakeholders
- Where is a safe place to put investment funds when looking for sound long-term returns? 
- How does the mutual fund's performance relate to it's benchmark fund?
- 

### Responsibilities
#### Andrew:
- Collect API data from alphavantage.co for indices XLV (Healthcare Mutual Fund), INX (S&P 500 Index), and JNJ (Johnston & Johnston Company)
- Organize collected data into operable DataFrames in JupyterLab
- Create 'daily avg. percent change' series upon which hypothesis testing will occur
- Create appropriate visualizations from collected & calculated data 
- Input test statistics and visualizations into presentation slide deck
- Create markdown README file on project
- Collaborate with Will on both technical and non-technical jupyter notebooks
- Write asset_cleaner & test_statistics modules for importing to the jupyter notebook

#### Will:
- 

### Summary of Included Files
The following files are included underthe Module_3_Project folder within the Github repository:
- Mod_3_Project_Technical.ipynb
    - Jupyter Notebook for a technical audience
    - PEP 8 Standards
    - Imports cleaning & testing modules
    - Data importation, Data Cleaning, and Visualizations

- Mod_3_Project_Non_Technical.ipynb
    - Jupyter Notebook for non-technical audience
    - Description of stakeholder needs and purpose of hypothesis testing
    - Visualiztions with detailed non-technical explanations
    - Actionable insights for stakeholder
    
- asset_cleaner.py
    - Imports asset data from alphavantage.co API (Since 1999)
    - Gathers JSON data and organizes into pandas DataFrame
    - Calculates series which will be used for hypothesis testing
    - Returns cleaned DF for use in hypothesis testing for respective asset performances
    
- test_statistics.py
    - Module for performing hypothesis testing 
    - Z-test function
    - P-value function