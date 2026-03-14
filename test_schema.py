from sqlalchemy import create_engine, text
import os

# Change to script directory
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

print('Starting star schema creation...')
engine = create_engine('mysql+pymysql://root:password@localhost/ecommerce_analytics')

with open('sql/star_schema.sql', 'r') as f:
    sql_script = f.read()

print('SQL script loaded, executing...')
with engine.connect() as conn:
    statements = [stmt.strip() for stmt in sql_script.split(';') if stmt.strip() and not stmt.strip().startswith('--')]
    print(f'Found {len(statements)} statements to execute')

    for i, stmt in enumerate(statements):
        print(f'Executing statement {i+1}/{len(statements)}: {stmt[:50]}...')
        try:
            conn.execute(text(stmt))
            print('✓ Success')
        except Exception as e:
            print(f'✗ Error: {e}')
            break
    else:
        conn.commit()
        print('All statements executed successfully!')

print('Checking tables...')
with engine.connect() as conn:
    result = conn.execute(text('SHOW TABLES'))
    tables = [row[0] for row in result]
    print('Tables in database:', tables)

    # Check row counts for key tables
    for table in ['dim_customer', 'fact_sessions']:
        if table in tables:
            try:
                result = conn.execute(text(f'SELECT COUNT(*) FROM {table}'))
                count = result.fetchone()[0]
                print(f'{table}: {count} rows')
            except Exception as e:
                print(f'Error checking {table}: {e}')