import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_feather("data/processed/ready_data.feather")

st.title("This Is A Title!")

st.subheader("Supporter donations vs actions")

df.fillna(0, inplace=True)
# st.dataframe(df)

lower_than_95, greater_than_95 = st.tabs(["Excluding top 25%", "Only top 25%"])


def dono_vs_action_scatter(less_than: bool):

    if less_than:
        fig0_df = df.loc[df["donation_size_score"] < 0.75]
    else:
        fig0_df = df.loc[df["donation_size_score"] > 0.75]

    avg_by_action = fig0_df.groupby("actions_taken")["donation_amount"].mean().reset_index()
    avg_by_action.rename(columns={"donation_amount": "avg_donation"}, inplace=True)

    fig0 = px.line(
                avg_by_action,
                x="actions_taken",
                y="avg_donation",
                labels={"actions_taken": "Actions", "avg_donation": "Average Donation"},
                markers=True,
                title="Average Donation per Action"
    )

    selection = st.plotly_chart(fig0, on_select="rerun")


with lower_than_95:
    dono_vs_action_scatter(True)
with greater_than_95:
    dono_vs_action_scatter(False)
