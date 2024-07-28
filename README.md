### Links Úteis:
+ [![Python](https://img.shields.io/badge/Python-blue)](https://www.python.org/downloads/)
+ [![Pylint](https://img.shields.io/badge/Pylint-yellowgreen)](https://pypi.org/project/pylint/)
+ [![Mypy](https://img.shields.io/badge/Mypy-darkblue)](https://mypy.readthedocs.io/en/stable/)
+ [![Pytest](https://img.shields.io/badge/Pytest-orange)](https://pypi.org/project/pytest/)
+ [![Bcrypt](https://img.shields.io/badge/Bcrypt-ligthbluee)](https://pypi.org/project/bcrypt/)




 ### Instalações:
```
# Para verificar a qualidade de código fonte.
pip install pylint --user

# Para verificar os tipos estáticos. 
pip install mypy --user

# Para testes parametrizados, acessórios e reescrita assertiva.
pip install pytest --user

# Para criptografia do tipo hash para senhas.
pip install bcrypt

#Para total de cobertura de testes.
pip install pytest-cov

```

### Comandos para Verificação Estática de Código (pylint e mypy):
```
# Para testar todos:
pylint *

#Para testar cada arquivo:
pylint <nome_do_arquivo.py> util

#Para testar um ou mais arquivos
mypy --show-error-codes --check-untyped-defs <nome_do_arquivo.py>  <nome_da_pasta>

# Testes com relatório de cobertura para o sonar (coverage.xml).
pytest tests/ -vv --cov=src --cov-report=xml

# Testes com relatório de cobertura exibido no console.
pytest tests/ -vv --cov=src

```
