import streamlit as st
import duckdb
from read_data import load_data
import matplotlib.pyplot as plt


def employees_by_department_bar():
    
    df = load_data("Executive_Dashboard/data/supahcoolsoft.csv")

    df = duckdb.query("""
                    SELECT Department, COUNT(*) AS Employee_Count
                    FROM df
                    GROUP BY Department
                    ORDER BY Employee_Count Desc
                    """).df()
    
    st.bar_chart(df, x = "Department", y = "Employee_Count")

def salary_histogram():
    
    df = load_data("Executive_Dashboard/data/supahcoolsoft.csv")
    fig, ax = plt.subplots()
    ax.hist(df["Salary_SEK"], bins=10, edgecolor='white')
    ax.set_xlabel("Salary (SEK)")
    ax.set_ylabel("Number of Employees")
    ax.set_title("Salary Distribution")
    st.pyplot(fig)




