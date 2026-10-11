name: Crear EXE
on: [push, workflow_dispatch]
jobs:
  build:
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - name: Instalar y Compilar EXE
        run: |
          pip install pyinstaller svgpathtools ezdxf numpy
          pyinstaller --onefile --noconsole --exclude-module scipy --name "Empaquetador_CAD" convertidor_cad.py
      - uses: actions/upload-artifact@v4
        with:
          name: Programa_Lista_Para_Usar
          path: dist/Empaquetador_CAD.exe
