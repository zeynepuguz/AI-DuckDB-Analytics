import duckdb

con = duckdb.connect("datacamp.duckdb")

print("\nTotal rows:")
print(con.execute("SELECT COUNT(*) FROM bank").fetchdf())

print("\nCampaign success distribution:")
print(con.execute("""
    SELECT y, COUNT(*) as count
    FROM bank
    GROUP BY y
""").fetchdf())

print("\nTop 5 jobs by average duration:")
print(con.execute("""
    SELECT job, AVG(duration) as avg_duration
    FROM bank
    GROUP BY job
    ORDER BY avg_duration DESC
    LIMIT 5
""").fetchdf())

print("\n--- Relation API Example ---")

rel = con.table("bank")

print("\nColumns:")
print(rel.columns)

print("\nDuration < 100 (first 3 rows):")
print(
    rel.filter("duration < 100")
       .limit(3)
       .df()
)

print(
    rel.filter("duration < 100")
       .project("job, education, loan")
       .order("job")
       .limit(3)
       .df()
)

print("\n--- Direct CSV Query (duckdb.query) ---")

res = duckdb.query("""
    SELECT
        job,
        COUNT(*) AS total_clients_contacted,
        AVG(duration) AS avg_campaign_duration
    FROM 'data/bank-marketing.csv'
    WHERE age > 30
    GROUP BY job
    ORDER BY total_clients_contacted DESC
""")

print(res.df())

print("\n--- Tables in DuckDB ---")
print(con.execute("SHOW ALL TABLES").fetchdf())

con.close()