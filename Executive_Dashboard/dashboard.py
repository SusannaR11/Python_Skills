import streamlit as st
#import plotly_express as px
import matplotlib.pyplot as plt
from read_data import load_data

df = load_data("data/supahcoolsoft.csv")

def layout():
#===== Dashboard headline ======
    st.markdown("# Executive dashboard")
#-----Sub-header ---------------
    st.markdown("### Employee overview")
    st.write(f"Total Number of Employees: {len(df)}")
    st.write(f"Average Age of Employees: {df['Age'].mean():.1f}")
    st.write(f"Average Salary: {df['Salary_SEK'].mean():,.2f} SEK")


    st.markdown("### KPIs from employee data")


if __name__ == "__main__":
    layout()


 #   streamlit run dashboard.py