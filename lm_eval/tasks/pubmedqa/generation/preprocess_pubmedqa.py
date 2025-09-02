def doc_to_text(doc) -> str:
    ctxs = "\n".join(doc["CONTEXTS"])
    return f"Abstract: {ctxs}\nQ: {doc['QUESTION']}\n" + "A: Provide the final answer [yes,no,maybe] enclosed in boxed{the_answer}."
    #return f"Q: {doc['QUESTION']}\n" + "A: Provide the final answer enclosed in boxed{the_answer}."