from datetime import datetime
from docx import Document
from docx.shared import Cm
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
import os
import tempfile
import platform
import streamlit as st

def salvar_docx_temporario(doc, nome_processo="sentenca"):
    with tempfile.NamedTemporaryFile(delete=False, suffix='.docx') as temp_file:
        temp_file_path = temp_file.name
        doc.save(temp_file_path)
    st.success("Sentença gerada com sucesso!")
    st.download_button("Baixar Sentença", open(temp_file_path, "rb").read(), file_name=f"{nome_processo}.docx")

def alinhamento_parag_dispositivo(doc, lista_de_paragrafos):
    for texto in lista_de_paragrafos:
        parag = doc.add_paragraph(texto)
        parag.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY
        parag.paragraph_format.first_line_indent = Cm(2)