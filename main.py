import sys
import os

#region Código main
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from UI.Principal import VentanaPrincipal

if __name__ == "__main__":
    app = VentanaPrincipal()
    app.ejecutar()
#endregion