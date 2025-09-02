# Copied from Master
def doc_to_text(doc) -> str:
    """
    Q: <question> (A) <choice1> (B) <choice2> (C) <choice3> (D) <choice4>
    A: Provide the final answer enclosed in boxed{the_answer}.
    """
    choices = [doc["opa"], doc["opb"], doc["opc"], doc["opd"]]
    option_choices = {
        "A": choices[0],
        "B": choices[1],
        "C": choices[2],
        "D": choices[3],
    }

    prompt = "Q: " + doc["question"] + "\n"
    for choice, option in option_choices.items():
        prompt += f"({choice.upper()}) {option}"
    prompt += "\nA: Provide the final answer enclosed in boxed{the_answer}."
    return prompt
