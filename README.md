### Links Úteis:
+ [![Python](https://img.shields.io/badge/Python-blue)](https://www.python.org/downloads/)
+ [![Pylint](https://img.shields.io/badge/Pylint-yellowgreen)](https://pypi.org/project/pylint/)
+ [![Mypy](https://img.shields.io/badge/Mypy-darkblue)](https://mypy.readthedocs.io/en/stable/)
+ [![Pytest](https://img.shields.io/badge/Pytest-orange)](https://pypi.org/project/pytest/)
+ [![Bcrypt](https://img.shields.io/badge/Bcrypt-ligthbluee)](https://pypi.org/project/bcrypt/)




 ### Instalações:
 [Requisitos para este projeto](docs/requirements.txt)



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
