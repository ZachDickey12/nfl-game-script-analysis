\# NFL Game Script Analysis



\## Research Question



How does score differential affect NFL offensive passing rate, and does that relationship become stronger late in games?



\## Data



This project uses 2025 NFL play-by-play data from nflverse.



The analysis focuses on offensive plays and compares passing frequency across different score situations.



\## Tools



\- Python

\- Pandas

\- Matplotlib

\- nflverse play-by-play data



\## Method



I grouped offensive plays into five game-script categories based on score differential:



\- Trailing by 10 or more points

\- Trailing by 4–9 points

\- Within 3 points

\- Leading by 4–9 points

\- Leading by 10 or more points



I then calculated the percentage of offensive plays that were passes in each category.



To test whether game script becomes more important later in games, I also compared first-quarter and fourth-quarter passing rates.



\## Overall Results



The overall 2025 passing rates were:



\- Trailing 10+: 67.2%

\- Trailing 4–9: 59.8%

\- Within 3: 54.9%

\- Leading 4–9: 51.4%

\- Leading 10+: 43.1%



Passing frequency increased as teams fell further behind and decreased as teams built larger leads.



<img src="pass\_rate\_by\_game\_script.png" alt="Pass Rate by Game Script">



\## First Quarter vs Fourth Quarter



\### First Quarter



\- Trailing 10+: 52.8%

\- Trailing 4–9: 54.4%

\- Within 3: 52.8%

\- Leading 4–9: 51.9%

\- Leading 10+: 48.6%



The difference between trailing by 10+ and leading by 10+ was only 4.2 percentage points.



This suggests that score differential has a relatively limited relationship with play-calling early in games.



\### Fourth Quarter



\- Trailing 10+: 75.4%

\- Trailing 4–9: 69.2%

\- Within 3: 57.6%

\- Leading 4–9: 40.3%

\- Leading 10+: 29.6%



The difference between trailing by 10+ and leading by 10+ increased to 45.8 percentage points.



This shows that game script has a much stronger relationship with offensive play-calling late in games.



<img src="pass\_rate\_q1\_vs\_q4.png" alt="First Quarter vs Fourth Quarter">



\## Key Finding



The strongest result from this analysis is the difference between early-game and late-game play-calling.



In the first quarter, teams trailing by 10+ and teams leading by 10+ had similar passing rates.



In the fourth quarter, the difference became much larger:



\- Trailing 10+: 75.4% pass rate

\- Leading 10+: 29.6% pass rate



That is a 45.8 percentage-point difference.



\## Conclusion



Score differential appears to have a much stronger relationship with offensive play-calling as an NFL game approaches its end.



Teams that are trailing significantly in the fourth quarter become heavily pass-oriented, while teams protecting large leads become much more run-oriented.



This supports the idea that game script should be considered when analyzing quarterback passing volume, offensive tendencies, and potentially player projections.



\## Limitations



There are several limitations to this analysis:



\- Only the 2025 NFL season was included.

\- Extreme score differentials were relatively uncommon in the first quarter, which resulted in smaller sample sizes.

\- The analysis shows relationships but does not prove that score differential alone causes changes in play-calling.

\- Other variables such as down, distance, team quality, quarterback ability, opponent strength, time remaining, and win probability may also affect play selection.



\## Future Research



Future analysis could expand this project by examining:



\- Individual team tendencies

\- Quarterback passing attempts

\- Passing yards

\- Down and distance

\- Win probability

\- Expected pass rate

\- Opponent strength

\- Whether game script improves quarterback passing-yard projections



\## Project Files



\- `game\_script\_analysis.py` — main Python analysis

\- `pass\_rate\_by\_game\_script.png` — overall game-script visualization

\- `pass\_rate\_q1\_vs\_q4.png` — first-quarter vs fourth-quarter comparison

\- `requirements.txt` — Python package requirements



\## Skills Demonstrated



This project demonstrates experience with:



\- Working with large sports datasets

\- Data cleaning and filtering

\- Grouping and aggregation with Pandas

\- Calculating rates and summary statistics

\- Data visualization with Matplotlib

\- Interpreting sample size and limitations

\- Communicating analytical findings clearly

