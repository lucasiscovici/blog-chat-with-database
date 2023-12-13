from pathlib import Path

from dotenv import load_dotenv
load_dotenv()

import sqlite3
import pandas as pd
import random
from sqlalchemy.types import DATE

from langchain.utilities import SQLDatabase
from sqlalchemy import  create_engine

from blog_langchain_db.chain import SQLChain 
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory

def create_fake_data_not_prepared(filename="data_not_prepared.csv"):
	# Create a sample DataFrame
	# Fixing the seed
	random.seed(42)
	companies = {
		"TotalEnergies": {
			"sector": "Energy"
		},
		"haribo": {
			"sector": "confectionery"
		},
		"SFR": {
			"sector": "TELECOMMUNICATION"
		}
	}
	df = pd.DataFrame(columns=["date", "company", "sector", "indicator", "value", "type"])
	year = "2022"
	for company in companies.keys():
		for type_ in ["actual", "Budget"]: 
			for indicator in ["ebitda","SALES"]:
				for i in range(1,13):
						value = random.randint(0,2e5)
						df = df._append({
							"date": f"{str(i).zfill(2)}-{year}",
							"company": company,
							"sector": companies[company]["sector"],
							"indicator": indicator,
							"value": value,
							# "sales": sales, 
							# "ebitda": ebitda,
							"type": type_
						},  ignore_index=True)
	df.to_csv(filename,index=False)

def create_fake_data_prepared(filename="data.csv"):
	# Create a sample DataFrame
	# Fixing the seed
	random.seed(42)
	companies = {
		"TotalEnergies": {
			"sector": "ENERGY"
		},
		"Haribo": {
			"sector": "CONFECTIONERY"
		},
		"SFR": {
			"sector": "TELECOMMUNICATION"
		}
	}
	df = pd.DataFrame(columns=["date", "company", "sector", "sales", "ebitda", "type"])
	for year in ["2022","2021"]:
		for company in companies.keys():
			for type_ in ["actual", "budget"]: 
				for i in range(1,13):
					if year == "2021":
						if i in [5, 10]:
							continue
					sales = random.randint(0,2e5)
					ebitda = random.randint(0,2e5)
					df = df._append({
						"date": f"{year}-{str(i).zfill(2)}-01",
						"company": company,
						"sector": companies[company]["sector"],
						"sales": sales,
						"ebitda": ebitda,
						"type": type_
					},  ignore_index=True)
	df.to_csv(filename,index=False)


def fake_data_base():
	data_prepared = True
	filename = "data.csv" if data_prepared else "data_not_prepared.csv"
	data_path = Path(__file__).parent.joinpath(filename)
	if not data_path.exists():
		if data_prepared:
			create_fake_data_prepared()
		else:
			create_fake_data_not_prepared()

	df = pd.read_csv(data_path)

	# Create an SQLite connection to a database in memory
	conn = sqlite3.connect(':memory:')

	# Write the data to a sqlite table
	df.to_sql('data', conn, index=False, if_exists='replace', dtype={"date": "date" if data_prepared else "text"})
	return conn

def create_chain(conn, verbose=True):
	db = SQLDatabase(engine=create_engine('sqlite://', creator = lambda: conn))
	llm = ChatOpenAI(temperature=0, model="gpt-4")
	descriptions_str = Path(__file__).parent.joinpath("description.csv").read_text()  # description of each columns
	memory = ConversationBufferMemory()
	return SQLChain.from_db_and_llm(llm=llm, db=db, verbose=verbose, table_descriptions=descriptions_str, memory=memory)

def main():
	con = None
	try:
		conn = fake_data_base()
		chain = create_chain(conn, verbose=True)
		print(chain("What were the revenue of SFR in 2022 ?")["output"])
		print(chain("in 2021 ?")["output"])
		print(chain("for that year, which months are available ?")["output"])
	finally:
		conn.close()


