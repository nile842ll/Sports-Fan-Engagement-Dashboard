# Sports Fan Engagement Dashboard

This project analyzes how fan engagement around sports content changes across a season using **Google Trends** as a proxy for audience interest. It explores how performance, timing, and major moments correlate with spikes in attention, surfacing insights relevant to **sports media, marketing, and digital strategy** teams.

## What this answers
- How does audience interest fluctuate over time?
- Which teams/players/topics drive the biggest spikes?
- What patterns could inform content timing and editorial strategy?

## Method
- Pull search interest data with `pytrends` (Google Trends)
- Visualize trends over time
- Identify peak moments and compare relative attention across terms


## Key Findings
- Fan interest in the Super Bowl exhibits an extreme, short-lived spike relative to baseline league and team interest, highlighting the outsized impact of tentpole events on audience attention.
- League-wide interest (NFL) remains relatively stable throughout the season, while team-specific interest shows higher volatility tied to performance and narrative context.
- Engagement accelerates during late-season and playoff periods, reinforcing the importance of timing content, campaigns, and product launches around high-stakes moments.

## How to run
```bash
pip install -r requirements.txt
jupyter notebook
