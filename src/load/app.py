import streamlit as st
import pandas as pd
import plotly.express as px


df = pd.read_feather("data/processed/ready_data.feather")

st.title("MVM Engagement Analysis!")

st.subheader("Supporter donations vs actions")

df.fillna(0, inplace=True)


# Line graph showing actions vs donations, the data set for this
# Can be changed by the user via a slider which selects
# min and max values for donation_size score
selected_range = st.slider(
    "Select the percentile group of donators:",
    min_value=0,
    max_value=100,
    value=(0, 100),
    format="%d%%",
    step=1
)

fig0_df = df.loc[(df["donation_size_score"] >= (selected_range[0]/100))
                 & (df["donation_size_score"] <= (selected_range[1]/100))].copy()


avg_by_action = fig0_df.groupby("actions_taken")["donation_amount"].mean().reset_index()
avg_by_action.rename(columns={"donation_amount": "avg_donation"}, inplace=True)

fig0 = px.line(
            avg_by_action,
            x="actions_taken",
            y="avg_donation",
            labels={"actions_taken": "Actions",
                    "avg_donation": "Average Donation"},
            markers=True,
            title="Average Donation per Action"
)

selection = st.plotly_chart(fig0, on_select="rerun")

# Graph showing engagement (engagement_score) on a bar graph against different tags
# Tags selectable by user
# Default tags for party lines

st.subheader("Engagement vs Alignment")


options_tags = ["supports_reform",
                "against_reform",
                "supports_conservative",
                "supports_libdem",
                "supports_labour",
                "supports_green",
                "supports_your"]

multiselect_answers = st.multiselect(
    label="Select tags to be included in graph",
    options=options_tags,
    default=["supports_reform", "supports_green"]
)

engagement_averages_for_tag = {}

for tag in multiselect_answers:

    filtered_df = df[df[tag] == True]
    engagement_averages_for_tag[tag] = filtered_df["engagement_score"].mean()


fig1_df = pd.DataFrame({"tag": list(engagement_averages_for_tag.keys()),
                        "engagement_averages": list(engagement_averages_for_tag.values())})

fig1 = px.bar(
    fig1_df,
    x="tag",
    y="engagement_averages"
)


fig1.update_traces(width=0.2)
fig1.update_layout(
    bargap=0.6,
    # yaxis_range=[0, 1],
    xaxis={'categoryorder': 'total descending'}
)

selection1 = st.plotly_chart(fig1, on_select="rerun")


for tag in multiselect_answers:
    value = int(df[tag].value_counts()[1])
    st.metric(label=f"Counts of tag owners for '{tag}'", value=value)
