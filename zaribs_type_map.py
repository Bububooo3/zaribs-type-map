import pandas, plotly.express

data = pandas.read_csv("my_friends_type_data.csv")

# I'm lowk a genius guys
threshold, step, increment, low, high = 5.5, .1, .05, 0, .5

data["hRate"] = ((data["hAvg"] - threshold)/step) * increment + low
data["hRate"] = data["hRate"].clip(low, high)
data["count"] = data["ageRangePopulationEstimate"] * data["hRate"] * .11 # (Brunettes in US from WPR is like 11%)
data["percent"] = data["count"] / data["ageRangePopulationEstimate"] * 100

# Percent
fig1 = plotly.express.choropleth(
    data,
    locations="state",
    locationmode="USA-states",
    color="percent",
    range_color=[low, high],
    scope="usa",
    labels={"percent": "% estimate"},
    title="Heatmap of Friend's Type by State (%)<br><sup>18–22, ≥5′8\", Natural Brunette</sup>"
)

fig1.show()
fig1.write_html("friends_type_heatmap_percent.html")

# "Raw" numbers
fig2 = plotly.express.choropleth(
    data,
    locations="state",
    locationmode="USA-states",
    color="count",
    range_color=[data["count"].min(), data["count"].max()],
    scope="usa",
    labels={"count": "# estimate"},
    title="Heatmap of Friend's Type by State (#)<br><sup>18–22, ≥5′8\", Natural Brunette</sup>"
)

fig2.show()
fig2.write_html("friends_type_heatmap_populous.html")

data.to_csv("zaribs_type_results.csv", index=False)

