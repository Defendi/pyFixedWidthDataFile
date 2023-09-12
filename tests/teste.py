from pyFixedWidthDataFile import FWDataFile

app = FWDataFile("./specs") #, separator="|")

HeaderArquivo = {
    'cod_cliente': "19879",
    'nome_cliente': "ALEXANDRE DEFENDI"
}

app.append_line("HeaderArquivo",cod_cliente="1234",nome_cliente="Alexandre Defendi")

print(app)

with open('readme.txt', 'w') as f:
    f.write(str(app))
        # f.write('\n')
    f.close()