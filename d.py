from transformers import pipeline

def get_res(string1, string2):
    sentiment_model = pipeline("sentiment-analysis")
    sentiment1 = sentiment_model(string1)[0]
    sentiment2 = sentiment_model(string2)[0]

    print(f"'{string1}' sentiment: {sentiment1}")
    print(f"'{string2}' sentiment: {sentiment2}")

    if sentiment1['label'] != sentiment2['label']:
        print(f"'{string1}' and '{string2}' are opposites!")
    else:
        print(f"'{string1}' and '{string2}' are contextually similar.")


if __name__ == "__main__":
    s1 = "Answer not found in the context"
    s2 = "this is a government contract none document "

    get_res(s1, s2)



