import pandas as pd

def extract_data():
    clientes = pd.read_csv("data/raw/clientes.csv")
    produtos = pd.read_csv("data/raw/produtos.csv")
    pedidos = pd.read_csv("data/raw/pedidos.csv")
    itens = pd.read_csv("data/raw/itens_pedido.csv")

    print("Dados extraidos com sucesso !")

    return{
        "clientes": clientes,
        "produtod": produtos,
        "pedidos": pedidos,
        "itens": itens
    }

if __name__ == "__main__":
    data = extract_data()
    for nome, df in data.items():
        print(f"\n{nome.upper()}")
        print(df.head())