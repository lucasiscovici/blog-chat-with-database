from langchain.chains.base import Chain

from langchain.utilities import SQLDatabase
from langchain.chains import LLMChain

from .prompts import SQL_QUERY_PROMPT, RESPONSE_PROMPT, FACTS_PROMPT

class SQLChain(Chain):

    db: SQLDatabase
    llm_chain_query: LLMChain
    llm_chain_response: LLMChain
    llm_chain_facts: LLMChain
    table_descriptions: str

    input_key: str = "question" #: :meta private:
    output_key: str = "output"  #: :meta private:

    @property
    def input_keys(self):
        return [self.input_key]

    @property
    def output_keys(self):
        return [self.output_key]

    def _call(self, inputs, run_manager=None):
        # get table names
        table_names_list = self.db.get_usable_table_names()

        # get table infos
        table_infos_str = self.db.get_table_info_no_throw(table_names_list)

        # get facts
        facts = self.llm_chain_facts.run(
            {
                **inputs,
                "schemas": table_infos_str,
                "descriptions": self.table_descriptions,
            }
        )

        # generate the sql query
        sql_query = self.llm_chain_query.run(
            {
                **inputs,
                "schemas": table_infos_str,
                "descriptions": self.table_descriptions,
                "facts": facts,
            }
        )
        print("sql_query", sql_query)

        # execute the sql query
        query_response = self.db.run_no_throw(sql_query)

        # generate the response
        response = self.llm_chain_response.run(
            {**inputs, "query": sql_query, "facts": facts, "response": query_response}
        )

        return {self.output_key: response}


    @classmethod
    def from_db_and_llm(
        cls,
        db,
        llm,
        prompt_sql_query = SQL_QUERY_PROMPT,
        prompt_response = RESPONSE_PROMPT,
        prompt_facts = FACTS_PROMPT,
        table_descriptions="",
        verbose = False,
        **kwargs
    ):
        return cls(
            db=db, 
            llm=llm, 
            llm_chain_query=LLMChain(llm=llm, prompt=prompt_sql_query, verbose=verbose), 
            llm_chain_response=LLMChain(llm=llm, prompt=prompt_response, verbose=verbose),
            llm_chain_facts=LLMChain(llm=llm, prompt=prompt_facts, verbose=verbose),
            table_descriptions=table_descriptions,
            **kwargs
        )

