import streamlit as st
def jedi():
    name = st.text_input("Nome do Jedi:")
    age = st.number_input("Idade do Jedi:", value=0, step=1, min_value=0,  max_value=1500)
    return name, age
st.title("Jedi App")
# Pede o nome e a idade do jedi usando a função jedi
name, age = jedi()
st.write('Selecione a categoria do Jedi:')
categoria = st.selectbox('Categoria Jedi', ('Padawan', 'Cavaleiro', 'Abandonado por tudo e todos'))

submit = st.button('Enviar dados')

if submit:
    st.write('Dados enviados com sucesso!')

    st.write(f'O Jedi {name} possui {age} anos e está na categoria {categoria}')

# Exibe uma mensagem com os dados do jedi
st.write("O Jedi", name, "tem", age, "anos.")
st.image("C:\\Users\\vinic\\Desktop\\MeuProjeto\\handsON8\\starwar.jpg", width=200)