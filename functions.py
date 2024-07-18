import matplotlib.pyplot as plt
import mysql.connector
import pandas as pd
import sqlite3
from dotenv import load_dotenv
import os









def create_db_connection(dotenv_path):
    """
    Loads environment variables from a .env file and establishes a MySQL database connection.

    Args:
    dotenv_path (str): The path to the .env file containing the database connection details.

    Returns:
    mysql.connector.connection.MySQLConnection: The database connection object.
    mysql.connector.cursor.MySQLCursor: The cursor object for executing queries.
    """
    # Load environment variables from .env file
    load_dotenv(dotenv_path='/Users/mustafaaldabbas/Desktop/happiness/Data-sets /quieres /.env')
    
    # Retrieve database connection details from environment variables
    host = os.getenv('host')
    user = os.getenv('user')
    password = os.getenv('password')
    database = os.getenv('database')
    
    # Establish the connection to the database
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    
    # Create a cursor object
    cursor = connection.cursor()
    
    return connection, cursor









import pandas as pd

def get_top_happy_countries(cursor):
    """
    Fetches the top 10 happiest countries from the world_happiness_ranking2015 table.

    Args:
    cursor (sqlite3.Cursor or other DB cursor): The database cursor to execute the query.

    Returns:
    pd.DataFrame: DataFrame containing the top 10 happiest countries.
    """
    query = "SELECT * FROM world_happiness_ranking2015 ORDER BY happiness_rank ASC LIMIT 10;"
    cursor.execute(query)
    
    # Fetch the data
    data = cursor.fetchall()
    
    # Convert to DataFrame
    df = pd.DataFrame(data, columns=['country', 'gdp_per_capita', 'family', 'freedom', 'generosity', 'health', 'trust_corruption', 'happiness_score', 'happiness_rank'])
    
    return df






import sqlite3

import sqlite3
import pandas as pd

def fetch_gdp_vs_happiness(cursor):
    query = '''
        SELECT country, gdp_per_capita, happiness_score, happiness_rank
        FROM world_happiness_ranking2015
        ORDER BY gdp_per_capita DESC;
    '''
    cursor.execute(query)
    data = cursor.fetchall()
    return pd.DataFrame(data, columns=['country', 'gdp_per_capita', 'happiness_score', 'happiness_rank'])




def fetch_health_vs_happiness(cursor):
    """
    Fetches data to test the hypothesis that better health conditions are positively correlated with happiness score and rank.

    Args:
    cursor (sqlite3.Cursor): The database cursor to execute the query.

    Returns:
    pd.DataFrame: DataFrame containing the query results with country, health, happiness score, and happiness rank.
    """
    query = '''
        SELECT country, health, happiness_score, happiness_rank
        FROM world_happiness_ranking2015
        ORDER BY health DESC;
    '''
    cursor.execute(query)
    data = cursor.fetchall()
    return pd.DataFrame(data, columns=['country', 'health', 'happiness_score', 'happiness_rank'])


def fetch_freedom_vs_happiness(cursor):
    """
    Fetches data to test the hypothesis that higher freedom scores correlate with higher happiness rank and score.

    Args:
    cursor (sqlite3.Cursor): The database cursor to execute the query.

    Returns:
    pd.DataFrame: DataFrame containing the query results with country, freedom, happiness score, and happiness rank.
    """
    query = '''
        SELECT country, freedom, happiness_score, happiness_rank
        FROM world_happiness_ranking2015
        ORDER BY freedom DESC;
    '''
    cursor.execute(query)
    data = cursor.fetchall()
    return pd.DataFrame(data, columns=['country', 'freedom', 'happiness_score', 'happiness_rank'])




def fetch_trust_vs_happiness(cursor):
    """
    Fetches data to test the hypothesis that trust in government corruption negatively affects happiness rank and scores.

    Args:
    cursor (sqlite3.Cursor): The database cursor to execute the query.

    Returns:
    pd.DataFrame: DataFrame containing the query results with country, trust_corruption, happiness score, and happiness rank.
    """
    query = '''
        SELECT country, trust_corruption, happiness_score, happiness_rank
        FROM world_happiness_ranking2015
        ORDER BY trust_corruption DESC;
    '''
    cursor.execute(query)
    data = cursor.fetchall()
    return pd.DataFrame(data, columns=['country', 'trust_corruption', 'happiness_score', 'happiness_rank'])



def fetch_generosity_vs_happiness(cursor):
    """
    Fetches data to test the hypothesis that countries with a high level of generosity have better happiness rank.

    Args:
    cursor (sqlite3.Cursor): The database cursor to execute the query.

    Returns:
    pd.DataFrame: DataFrame containing the query results with country, generosity, and happiness score.
    """
    query = '''
        SELECT country, generosity, happiness_score
        FROM world_happiness_ranking2015
        ORDER BY generosity DESC;
    '''
    cursor.execute(query)
    data = cursor.fetchall()
    return pd.DataFrame(data, columns=['country', 'generosity', 'happiness_score'])


#load Happiness dataframe
def load_happiness_data(file_path):
    """
    Loads the world happiness ranking data from a CSV file into a pandas DataFrame.

    Args:
    file_path (str): The path to the CSV file containing the world happiness ranking data.

    Returns:
    pd.DataFrame: DataFrame containing the loaded data.
    """
    # Load the CSV file
    data = pd.read_csv(file_path)
    
    # Return the DataFrame
    return data



##General visualizations 

import pandas as pd
import matplotlib.pyplot as plt

def plot_top_10_happiest_countries(data):
    top_10_happiest = data.nsmallest(10, 'happiness_rank')
    plt.figure(figsize=(10, 6))
    plt.barh(top_10_happiest['country'], top_10_happiest['happiness_score'], color='skyblue')
    plt.xlabel('Happiness Score')
    plt.title('Top 10 Happiest Countries')
    plt.gca().invert_yaxis()
    plt.show()

def plot_bottom_10_happiest_countries(data):
    bottom_10_happiest = data.nlargest(10, 'happiness_rank')
    plt.figure(figsize=(10, 6))
    plt.barh(bottom_10_happiest['country'], bottom_10_happiest['happiness_score'], color='salmon')
    plt.xlabel('Happiness Score')
    plt.title('Bottom 10 Happiest Countries')
    plt.gca().invert_yaxis()
    plt.show()

def plot_top_10_trust_countries(data):
    top_10_trust = data.nlargest(10, 'trust_corruption')
    plt.figure(figsize=(10, 6))
    plt.barh(top_10_trust['country'], top_10_trust['trust_corruption'], color='lightgreen')
    plt.xlabel('Trust in Government or Corruption')
    plt.title('Top 10 Countries with Highest Trust in Government')
    plt.gca().invert_yaxis()
    plt.show()

def plot_top_10_gdp_countries(data):
    top_10_gdp = data.nlargest(10, 'gdp_per_capita')
    plt.figure(figsize=(10, 6))
    plt.barh(top_10_gdp['country'], top_10_gdp['gdp_per_capita'], color='lightblue')
    plt.xlabel('GDP per Capita')
    plt.title('Top 10 Countries with Highest GDP per Capita')
    plt.gca().invert_yaxis()
    plt.show()

def plot_top_10_freedom_countries(data):
    top_10_freedom = data.nlargest(10, 'freedom')
    plt.figure(figsize=(10, 6))
    plt.barh(top_10_freedom['country'], top_10_freedom['freedom'], color='lightcoral')
    plt.xlabel('Freedom')
    plt.title('Top 10 Countries with Highest Freedom')
    plt.gca().invert_yaxis()
    plt.show()

def plot_top_10_generosity_countries(data):
    top_10_generosity = data.nlargest(10, 'generosity')
    plt.figure(figsize=(10, 6))
    plt.barh(top_10_generosity['country'], top_10_generosity['generosity'], color='pink')
    plt.xlabel('Generosity')
    plt.title('Top 10 Countries with Highest Generosity Level')
    plt.gca().invert_yaxis()
    plt.show()

def plot_top_10_family_countries(data):
    top_10_family = data.nlargest(10, 'family')
    plt.figure(figsize=(10, 6))
    plt.barh(top_10_family['country'], top_10_family['family'], color='black')
    plt.xlabel('Family Support')
    plt.title('Top 10 Countries with Most Family Support')
    plt.gca().invert_yaxis()
    plt.show()



#Hypotheses functions 


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_gdp_vs_happiness(data):
    """
    Plots a scatter plot of GDP per Capita vs. Happiness Score.

    Args:
    data (pd.DataFrame): DataFrame containing the data with 'gdp_per_capita' and 'happiness_score' columns.

    Returns:
    None
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(data['gdp_per_capita'], data['happiness_score'], color='blue')
    plt.xlabel('GDP per Capita')
    plt.ylabel('Happiness Score')
    plt.title('GDP per Capita vs. Happiness Score')
    plt.show()

def plot_health_vs_happiness(data):
    """
    Plots a scatter plot of Health (Life Expectancy) vs. Happiness Score.

    Args:
    data (pd.DataFrame): DataFrame containing the data with 'health' and 'happiness_score' columns.

    Returns:
    None
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(data['health'], data['happiness_score'], color='green')
    plt.xlabel('Health (Life Expectancy)')
    plt.ylabel('Happiness Score')
    plt.title('Health (Life Expectancy) vs. Happiness Score')
    plt.show()

def plot_freedom_vs_happiness(data):
    """
    Plots a scatter plot of Freedom vs. Happiness Score.

    Args:
    data (pd.DataFrame): DataFrame containing the data with 'freedom' and 'happiness_score' columns.

    Returns:
    None
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(data['freedom'], data['happiness_score'], color='red')
    plt.xlabel('Freedom')
    plt.ylabel('Happiness Score')
    plt.title('Freedom vs. Happiness Score')
    plt.show()

def plot_trust_vs_happiness(data):
    """
    Plots a scatter plot of Trust in Government/Corruption vs. Happiness Score.

    Args:
    data (pd.DataFrame): DataFrame containing the data with 'trust_corruption' and 'happiness_score' columns.

    Returns:
    None
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(data['trust_corruption'], data['happiness_score'], color='purple')
    plt.xlabel('Trust in Government/Corruption')
    plt.ylabel('Happiness Score')
    plt.title('Trust in Government/Corruption vs. Happiness Score')
    plt.show()

def plot_family_vs_happiness(data):
    """
    Plots a scatter plot of Family Support vs. Happiness Score.

    Args:
    data (pd.DataFrame): DataFrame containing the data with 'family' and 'happiness_score' columns.

    Returns:
    None
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(data['family'], data['happiness_score'], color='orange')
    plt.xlabel('Family Support')
    plt.ylabel('Happiness Score')
    plt.title('Family Support vs. Happiness Score')
    plt.show()

def plot_generosity_vs_happiness(data):
    """
    Plots a scatter plot of Generosity vs. Happiness Score.

    Args:
    data (pd.DataFrame): DataFrame containing the data with 'generosity' and 'happiness_score' columns.

    Returns:
    None
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(data['generosity'], data['happiness_score'], color='brown')
    plt.xlabel('Generosity')
    plt.ylabel('Happiness Score')
    plt.title('Generosity vs. Happiness Score')
    plt.show()

def plot_correlation_matrix(data):
    """
    Plots a heatmap of the correlation matrix of numeric columns in the data.

    Args:
    data (pd.DataFrame): DataFrame containing the data with numeric columns.

    Returns:
    None
    """
    # Select only numeric columns
    numeric_data = data.select_dtypes(include=['float64', 'int64'])

    # Compute the correlation matrix
    correlation_matrix = numeric_data.corr()

    # Plot the heatmap
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix of Happiness Metrics')
    plt.show()

# Usage example
if __name__ == "__main__":
    # Assuming 'data' is a DataFrame loaded with the relevant data
    # data = pd.read_csv('/path/to/your/data.csv')  # Replace with the path to your data file

    # Example DataFrame (replace with actual data)
    

    plot_gdp_vs_happiness(data)
    plot_health_vs_happiness(data)
    plot_freedom_vs_happiness(data)
    plot_trust_vs_happiness(data)
    plot_family_vs_happiness(data)
    plot_generosity_vs_happiness(data)
    plot_correlation_matrix(data)





#Results
def calculate_and_print_correlations(data):
    """
    Selects numeric columns from the data, calculates the correlation matrix,
    and prints the correlation results for the 'happiness_score' column.

    Args:
    data (pd.DataFrame): DataFrame containing the data with numeric columns.

    Returns:
    pd.Series: Series containing the correlation results for the 'happiness_score' column.
    """
    # Select only numeric columns
    numeric_data = data.select_dtypes(include=[float, int])
    
    # Calculate the correlation matrix for the numeric data
    correlation_results = numeric_data.corr()['happiness_score']
    
    # Print the correlation results
    print(correlation_results)
    
    return correlation_results