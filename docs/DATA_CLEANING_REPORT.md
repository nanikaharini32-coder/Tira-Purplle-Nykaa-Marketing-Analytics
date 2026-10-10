# Dashboard-aligned data cleaning report

## Row/column preservation
- Raw rows: 166,665
- Cleaned rows: 166,665
- Raw columns: 17
- Cleaned columns: 17
- Rows removed: 0
- Missing cells in raw file: 0
- Exact duplicate rows in raw file: 0

## Cleaning performed
1. Saved an untouched copy of the original CSV under `data/raw/`.
2. Trimmed leading and trailing whitespace in text columns.
3. Converted count/amount fields (`Duration`, `Impressions`, `Clicks`, `Leads`, `Conversions`, `Revenue`) to integer numeric types.
4. Converted `Acquisition_Cost`, `ROI`, and `Engagement_Score` to numeric decimal types without rounding their values.
5. Converted `Date` to a proper date type in the cleaned DataFrame and exported it as `YYYY-MM-DD`.
6. Verified that row count and column count did not change.

## Important
The original file has no missing cells and no exact duplicate rows, so no rows needed to be deleted or filled. This is type/format cleaning, not fabricated correction. Unusual values should only be changed if you have a confirmed business rule.

## Matching your Power BI dashboard
Use the following fields from the cleaned CSV:
- Brand
- Campaign_ID
- Campaign_Type
- Channel_Used
- Date
- Impressions
- Clicks
- Conversions
- Revenue
- ROI
- Acquisition_Cost
- Target_Audience
- Language
- Customer_Segment

Recommended measures:
- Total Revenue = `SUM(Revenue)`
- Total Campaign Records = `COUNT(Campaign_ID)` (this counts rows, not unique campaigns)
- Unique Campaigns = `DISTINCTCOUNT(Campaign_ID)` if each campaign ID should be counted once
- Total Impressions = `SUM(Impressions)`
- Total Clicks = `SUM(Clicks)`
- Total Conversions = `SUM(Conversions)`
- Average ROI = `AVERAGE(ROI)` (confirm whether ROI is stored as a ratio or percentage before formatting)

For a visual titled "Revenue over years", use Year from `Date`; if using Quarter, title it "Revenue by quarter" and sort quarters by date/year correctly.
