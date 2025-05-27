from langchain_ollama import ChatOllama
import pandas as pd
import sqlite3
from langchain_community.agent_toolkits import create_sql_agent
from langchain_community.utilities import SQLDatabase

excel_file = 'Docs/Python Batch 01.xlsx'
db_file = 'student_details.db'

# First part remains the same - create DB and load data
conn = sqlite3.connect(db_file)
df = pd.read_excel(excel_file)
df.to_sql('python_batch_1', conn, if_exists='replace', index=False)

# Create a LangChain SQLDatabase object from your connection
db = SQLDatabase.from_uri(f"sqlite:///{db_file}")

# Now create the agent with the proper database object
llm = ChatOllama(model="llama3.2")
agent_executor = create_sql_agent(llm, db=db, verbose=True)

agent_executor.invoke(
    "what is university most attented students course in python_batch_1 table?"
)

# "refere this connected db and generate only query.what is university most attented students course?"
# "what the column name in python_batch_1 table?"
conn.close()