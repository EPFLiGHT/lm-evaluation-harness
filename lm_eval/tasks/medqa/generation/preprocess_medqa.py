def doc_to_text(doc) -> str:
    option_choices = {
        "A": doc["ending0"],
        "B": doc["ending1"],
        "C": doc["ending2"],
        "D": doc["ending3"],
    }
    answers = "".join((f"({k}) {v}\n") for k, v in option_choices.items())
    return f"Q: {doc['sent1']}\n{answers}" + "A: Provide the final answer enclosed in boxed{the_answer}."


def doc_to_target(doc) -> int:
    return doc["label"]
