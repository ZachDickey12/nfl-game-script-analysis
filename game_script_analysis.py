import pandas as pd
import matplotlib.pyplot as plt

# Load 2025 NFL play-by-play data
url = "https://github.com/nflverse/nflverse-data/releases/download/pbp/play_by_play_2025.parquet"

pbp = pd.read_parquet(url)


# Keep only regular-season offensive plays
plays = pbp[
    (pbp["season_type"] == "REG")
    & pbp["score_differential"].notna()
    & (
        (pbp["pass_attempt"] == 1)
        | (pbp["rush_attempt"] == 1)
    )
].copy()


# Create game-script categories
bins = [
    -float("inf"),
    -10,
    -4,
    3,
    9,
    float("inf")
]

labels = [
    "Trailing 10+",
    "Trailing 4-9",
    "Within 3",
    "Leading 4-9",
    "Leading 10+"
]

plays["game_script"] = pd.cut(
    plays["score_differential"],
    bins=bins,
    labels=labels
)


# Calculate pass rate
summary = (
    plays
    .groupby("game_script", observed=False)
    .agg(
        plays=("play_id", "count"),
        pass_rate=("pass_attempt", "mean")
    )
    .reset_index()
)

summary["pass_rate_pct"] = (
    summary["pass_rate"] * 100
).round(1)


print(summary[
    ["game_script", "plays", "pass_rate_pct"]
])# Create a bar chart of pass rate by game script
plt.figure(figsize=(9, 5))

plt.bar(
    summary["game_script"].astype(str),
    summary["pass_rate_pct"]
)

plt.title("NFL Pass Rate by Game Script — 2025")
plt.xlabel("Game Situation")
plt.ylabel("Pass Rate (%)")

plt.xticks(rotation=20)

plt.tight_layout()

# Save a copy of the chart inside our project folder
plt.savefig("pass_rate_by_game_script.png", dpi=200)

# Display the chart
# --------------------------------------------------
# Compare 1st-quarter and 4th-quarter pass rates
# --------------------------------------------------

quarter_plays = plays[
    plays["qtr"].isin([1, 4])
].copy()

quarter_summary = (
    quarter_plays
    .groupby(["qtr", "game_script"], observed=False)
    .agg(
        plays=("play_id", "count"),
        pass_rate=("pass_attempt", "mean")
    )
    .reset_index()
)

quarter_summary["pass_rate_pct"] = (
    quarter_summary["pass_rate"] * 100
).round(1)

print("\nPass rate by game script and quarter:")
print(quarter_summary[
    ["qtr", "game_script", "plays", "pass_rate_pct"]
])
# --------------------------------------------------
# Graph: 1st quarter vs 4th quarter
# --------------------------------------------------

quarter_chart = quarter_summary.pivot(
    index="game_script",
    columns="qtr",
    values="pass_rate_pct"
)

quarter_chart.columns = ["1st Quarter", "4th Quarter"]

quarter_chart.plot(
    kind="bar",
    figsize=(10, 6)
)

plt.title("NFL Pass Rate by Game Script: 1st vs 4th Quarter — 2025")
plt.xlabel("Game Situation")
plt.ylabel("Pass Rate (%)")

plt.xticks(rotation=20)

plt.tight_layout()

plt.savefig(
    "pass_rate_q1_vs_q4.png",
    dpi=200
)

plt.show()