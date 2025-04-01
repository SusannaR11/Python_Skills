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

def salary_histogram


