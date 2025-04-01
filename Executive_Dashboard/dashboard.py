import streamlit as st
#import plotly_express as px
import matplotlib.pyplot as plt
from read_data import load_data
from charts import employees_by_department_bar

df = load_data("Executive_Dashboard/data/supahcoolsoft.csv")

def layout():
#===== Dashboard headline ======
    st.markdown("# Executive dashboard")
#-----Sub-header ---------------
    st.markdown("### Employee overview")
    st.write(f"Total Number of Employees: {len(df)}")
    st.write(f"Average Age of Employees: {df['Age'].mean():.1f}")
    st.write(f"Average Salary: {df['Salary_SEK'].mean():,.2f} SEK")

#----Table of employee details-----------
    st.markdown("### Employee Details")
    st.dataframe(df)
    df_sorted = df.sort_values(by=["Department", "Position"])

#---- Bar chart showing number of employees across departments------
    st.markdown("### Number of Employees by Department")
    employees_by_department_bar()



#-----KPI
    st.markdown("### KPIs from employee data")


if __name__ == "__main__":
    layout()


 #   streamlit run Executive_Dashboard/dashboard.py