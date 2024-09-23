from ctransformers import AutoModelForCausalLM
from llm.src.conf.Configurations import llama2_model_path, logger

logger.info("Loading Llama2 model")
llm = AutoModelForCausalLM.from_pretrained(llama2_model_path,
                                            model_type='llama')

context = """
The men's high jump event at the 2020 Summer Olympics took place between 30 July and 1 August 2021 at the Olympic Stadium.
33 athletes from 24 nations competed; the total possible number depended on how many nations would use universality places
to enter athletes in addition to the 32 qualifying through mark or ranking (no universality places were used in 2021).
Italian athlete Gianmarco Tamberi along with Qatari athlete Mutaz Essa Barshim emerged as joint winners of the event following
a tie between both of them as they cleared 2.37m. Both Tamberi and Barshim agreed to share the gold medal in a rare instance
where the athletes of different nations had agreed to share the same medal in the history of Olympics.
Barshim in particular was heard to ask a competition official "Can we have two golds?" in response to being offered a
'jump off'. Maksim Nedasekau of Belarus took bronze. The medals were the first ever in the men's high jump for Italy and
Belarus, the first gold in the men's high jump for Italy and Qatar, and the third consecutive medal in the men's high jump
for Qatar (all by Barshim). Barshim became only the second man to earn three medals in high jump, joining Patrik Sjöberg
of Sweden (1984 to 1992)."""

query = "Who won the gold in 2020 Summer Olympics men's high jump?"
# query = "Who won the bronze in 2020 Summer Olympics men's high jump?"
# query = "Who won the silver in 2020 Summer Olympics men's high jump?"
# query = "How many persons participated in high jump 2020 Summer Olympics men's high jump?"

prompt = f"""Answer based on context:\n\n{context}\n\n{query}"""
# prompt = f"""Answer based on context. If the answer cannot be found in the context, respond with 'ER001: I cannot find answer in context. :\n\n{context}\n\n{query}"""

logger.info("Generating response from Llama2 model")
res = llm(prompt=prompt,temperature=0.1,max_new_tokens=1024)
print(res)