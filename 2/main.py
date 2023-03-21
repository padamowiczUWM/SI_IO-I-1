import gradio as gr
import pandas as pd

queries = [
    'a) Ile klas decyzyjnych',
    'b) Wielkość każdej klasy decyzyjnej'
]

def execute_query(file, n, query=""):
    df = pd.read_csv(file)
    df.dropna(axis=0, inplace=True)
    df = df.head(int(n))

    shape = df.shape
    _count = df.iloc[:, -1].value_counts()

    if query == "":
        return query, df, "Ilość atrybutów: {}, ilość obiektów: {}".format(shape[1], shape[1] * shape[0])
    if query == queries[0]:
        return query, df, "Ilość klas decyzyjnych: {}".format(len(_count))
    if query == queries[1]:
        return query, df, "Wielkości klas decyzyjnych: {}".format(_count.to_dict())

    return query, df, "Coś poszło nie tak."


gr.Interface(
    execute_query,
    inputs=[
        gr.Textbox(label="Nazwa pliku CSV"),
        gr.Number(default=15, label="Liczba wierszy"),
        gr.inputs.Dropdown(["a) Ile klas decyzyjnych", "b) Wielkość każdej klasy decyzyjnej", ""], label="Pytanie")
    ],
    outputs=[
        gr.outputs.Textbox(label="Pytanie"),
        gr.outputs.Dataframe(label="Dane", type='pandas'),
        gr.outputs.Textbox(label="Wynik")
    ]).launch()
