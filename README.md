\# NFL Game Script Analysis



\## Research Question



How does score differential affect NFL offensive passing rate, and does that relationship become stronger late in games?



\## Data



This project uses 2025 NFL play-by-play data from nflverse.



\## Tools



\- Python

\- Pandas

\- Matplotlib

\- nflverse data



\## Method



I categorized offensive plays into five game-script situations based on score differential:



\- Trailing by 10 or more points

\- Trailing by 4–9 points

\- Within 3 points

\- Leading by 4–9 points

\- Leading by 10 or more points



I then calculated the percentage of offensive plays that were passes in each situation.



I also compared first-quarter and fourth-quarter passing rates to determine whether game script becomes more important later in games.



\## Overall Results



\- Trailing 10+: 67.2% pass rate

\- Trailing 4–9: 59.8%

\- Within 3: 54.9%

\- Leading 4–9: 51.4%

\- Leading 10+: 43.1%



Passing frequency increased as teams fell further behind.



!\[Pass Rate by Game Script](pass\_rate\_by\_game\_script.png)



\## First Quarter vs Fourth Quarter



\### First Quarter



\- Trailing 10+: 52.8%

\- Trailing 4–9: 54.4%

\- Within 3: 52.8%

\- Leading 4–9: 51.9%

\- Leading 10+: 48.6%



The difference between trailing by 10+ and leading by 10+ was 4.2 percentage points.



\### Fourth Quarter



\- Trailing 10+: 75.4%

\- Trailing 4–9: 69.2%

\- Within 3: 57.6%

\- Leading 4–9: 40.3%

\- Leading 10+: 29.6%



The difference between trailing by 10+ and leading by 10+ increased to 45.8 percentage points.



!\[First Quarter vs Fourth Quarter](pass\_rate\_q1\_vs\_q4.png)



\## Conclusion



Score differential has a much stronger relationship with offensive play-calling late in NFL games.



Teams trailing significantly in the fourth quarter become heavily pass-oriented, while teams protecting large leads become much more run-oriented.



\## Limitations



\- This analysis only uses the 2025 NFL season.

\- Extreme score differentials are relatively uncommon in the first quarter, creating smaller sample sizes.

\- The analysis identifies relationships but does not prove that score differential alone causes changes in play-calling.

\- Other factors such as down, distance, team strength, quarterback ability, and win probability may also influence play selection.



\## Future Research



Future projects could investigate:



\- Individual team tendencies

\- Quarterback passing volume

\- Expected pass rate

\- Win probability

\- Down and distance

\- Whether game script improves quarterback passing-yard projections

