import pandas as pd

url = "https://github.com/nflverse/nflverse-data/releases/download/pbp/play_by_play_2025.parquet"

pbp = pd.read_parquet(url)

print("Dataset size:")
print(pbp.shape)

print("\nFirst 10 plays:")

print(
    pbp[
        [
            "game_id",
            "posteam",
            "qtr",
            "down",
            "ydstogo",
            "play_type",
            "score_differential"
        ]
    ].head(10)
)