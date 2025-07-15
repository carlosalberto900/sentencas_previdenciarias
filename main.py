import streamlit as st
import time
import subprocess

def aviso_sentenca_nao_implementada():
    texto = "Esta sentença ainda não foi implementada no sistema."
    for char in texto:
        yield char
        time.sleep(0.02)  # ajuste o tempo se quiser mais rápido ou mais lento

# Interface gráfica com Streamlit

st.markdown("## 👩‍⚖️👨‍⚖️ Sistema de Apoio à Sentença Previdenciária")
st.caption("Justiça Federal – 1ª Vara Federal com JEF Adjunto em Caraguatatuba")
st.caption("Criado por: Carlos Alberto Antonio Junior - Juiz Federal - TRF3")
st.divider()
# st.title("GERADOR DE SENTENÇAS EM BENEFÍCIOS PREVIDENCIÁRIOS")
# st.title("PARA JUIZADO ESPECIAL FEDERAL")
# st.write("Criado por: Carlos Alberto Antonio Junior - Juiz Federal - TRF3")
# st.write("1 Vara Federal com JEF Adjunto em Caraguatatuba/SP")
# Input do processo
processo = st.text_input("Qual o número do processo? O número do processo contém 20 dígitos numéricos.")
if processo:
    processo_limpo = "".join(filter(str.isdigit, processo))
    if len(processo_limpo) == 20:
        processo_formatado = f"{processo_limpo[:7]}-{processo_limpo[7:9]}.{processo_limpo[9:13]}.{processo_limpo[13:14]}.{processo_limpo[14:16]}.{processo_limpo[16:]}"
    else:
        st.error("Formato inválido! O número do processo deve ter 20 dígitos numéricos, após remoção de caracteres especiais.")
if 'processo_formatado' in locals():
    st.write(f"Processo: {processo_formatado}")

    beneficio = st.radio("Qual o benefício será analisado?",
                         [1, 2, 3, 4, 5, 6, 7],
                         format_func=lambda x:
                         "21 - Pensão por morte previdenciária" if x==1 else
                         "25 - Auxílio-reclusão" if x==2 else
                         "31 - Auxílio por incapacidade temporária\n\n"
                         "32 - Aposentadoria por incapacidade permanente" if x==3 else
                         "36 - Auxílio-acidente previdenciário" if x==4 else
                         "41 - Aposentadoria por idade\n\n"
                         "42 - Aposentadoria por tempo de contribuição (com ou sem conversão de tempo especial)\n\n"
                         "46 - Aposentadoria especial\n\n"
                         "57 - Aposentadoria por tempo de contribuição do professor" if x==5 else
                         "80 - Salário-maternidade" if x==6 else
                         "87 - Amparo assistencial ao deficiente (LOAS)\n\n"
                         "88 - Amparo assistencial ao deficiente ou ao idoso (LOAS)"                         
                         )
    if beneficio == 1:
        exec(open("pensao_morte.py").read())
    if beneficio == 2:
        st.write_stream(aviso_sentenca_nao_implementada)
    if beneficio == 3:
        exec(open("Incapacidade.py").read())
    if beneficio == 4:
        st.write_stream(aviso_sentenca_nao_implementada)
    if beneficio == 5:
        exec(open("aposentadorias.py").read())
    if beneficio == 6:
        st.write_stream(aviso_sentenca_nao_implementada)
    if beneficio == 7:
        exec(open("loas.py").read()) 

