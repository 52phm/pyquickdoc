
if __name__ == '__main__':
    filepath = "./examples/"

    import pyquickdoc as pdoc
    import numpy as np
    import pandas as pd

    # 样例 1
    pdoc.func_apidoc(pdoc.func_apidoc, filename=filepath + "pyquickdoc.func_apidoc.html")
    pdoc.func_apidoc(pdoc.func_apidoc, filename=filepath + "pyquickdoc.func_apidoc.md")
    # 样例 2
    pdoc.func_apidoc(np.fft.rfft, filename=filepath + "np.fft.rfft.html")
    pdoc.func_apidoc(np.fft.rfft, filename=filepath + "np.fft.rfft.md")
    # 样例 3
    pdoc.func_apidoc(pd.read_csv, filename=filepath + "pd.read_csv.html")
    pdoc.func_apidoc(pd.read_csv, filename=filepath + "pd.read_csv.md")


