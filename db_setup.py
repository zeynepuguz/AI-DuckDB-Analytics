import duckdb
from pathlib import Path

DB_PATH = "datacamp.duckdb"
CSV_PATH = Path("data") / "bank-marketing.csv"

if not CSV_PATH.exists():
    raise FileNotFoundError(f"CSV not found: {CSV_PATH.resolve()}")

con = duckdb.connect(DB_PATH)

# CSV > table
con.execute("""
    CREATE TABLE IF NOT EXISTS bank AS
    SELECT * FROM read_csv_auto(?)
""", [str(CSV_PATH)])

# Verify
tables = con.execute("SHOW TABLES").fetchall()
print("Tables:", tables)

preview = con.execute("SELECT * FROM bank WHERE duration < 100 LIMIT 5").fetchdf()
print(preview)

con.close()
print(f"DB created/updated: {Path(DB_PATH).resolve()}")