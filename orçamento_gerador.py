#!/usr/bin/env python
# coding: utf-8

# ##### gerando pdf automaticamente utilizando o python

# # Gerador de Orçamento

# In[3]:


print("Orçamento gerado com sucesso! ")


# # Entrada de Dados do Usuário

# In[4]:


input("Digite a descrição do projeto: ")
input("Digite a quantidade de horas previstas: ")
input("Digite o valor da hora trabalhada: ")
input("Digite o prazo estimado: ")


# # Armazenando dados em variáveis
# - nomes significativos

# In[8]:


projeto = input("Digite a descrição do projeto: ")
horas_previstas = input("Digite a quantidade de horas previstas: ")
valor_hora = input("Digite o valor da hora trabalhada: ")
prazo = input("Digite o prazo estimado: ")


# # Realizando cálculos com o Python
# - quantidade de horas previstas * valor hora trabalhada

# In[10]:


valor_total = int(horas_previstas) * int(valor_hora)


# In[11]:


valor_total


# # Tipo de dado
# - texto (str)
# - número (int)

# In[12]:


int("10")


# # Gerando o PDF

# In[16]:


get_ipython().system('pip install fpdf')


# In[17]:


from fpdf import FPDF


# In[26]:


pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial")

pdf.image("template.png", x=0,y=0)

pdf.text(115,145, projeto)
pdf.text(115,160, horas_previstas)
pdf.text(115,175, valor_hora)
pdf.text(115,190, prazo)
pdf.text(115,205, str(valor_total))


pdf.output("Orçamento.pdf")
print("Orçamento gerado com sucesso!")


# In[ ]:





# In[ ]:




