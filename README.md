# Tira, Purplle & Nykaa Marketing Campaign Analytics

This portfolio project supports the Power BI dashboard with a raw dataset, a cleaned dataset, reproducible Pandas code, and a data quality report.

## Dataset
- Raw rows: 166,665
- Cleaned rows: 166,665
- Columns: 17
- Rows removed: 0
- Brands: Tira, Purplle, Nykaa


## Pandas cleaning
The script trims whitespace, converts numeric columns to suitable types, parses the date column, and checks that row/column counts remain unchanged. It does not delete duplicate rows or invent missing values.

Run:
```bash
python -m pip install pandas
python scripts/clean_data.py
```

## Power BI dashboard mapping
- KPI cards: Revenue, campaign records, impressions, clicks, conversions
- Brand comparison: `Brand` + `Revenue`
- Campaign type doughnut: `Campaign_Type` + `Revenue`
- Trend: `Date` + `Revenue`
- Brand table: `Brand`, `Revenue`, `Campaign_ID`, `Conversions`, `Clicks`, `ROI`
- Insights: segment by `Channel_Used`, `Target_Audience`, `Language`, and `Customer_Segment`

Important: `COUNT(Campaign_ID)` counts records; `DISTINCTCOUNT(Campaign_ID)` counts unique campaign IDs. Pick the one that matches your intended KPI. Verify insight percentages against the cleaned data before publishing.
