# from http://www.blog.pythonlibrary.org/2018/10/16/testing-jupyter-notebooks/
 
import nbformat
import os
import unittest
from nbconvert.preprocessors import ExecutePreprocessor
 
 
def run_notebook(notebook_path):
    nb_name, _ = os.path.splitext(os.path.basename(notebook_path))
    dirname = os.path.dirname(notebook_path)
 
    with open(notebook_path) as f:
        nb = nbformat.read(f, as_version=4)
 
    proc = ExecutePreprocessor(timeout=600, kernel_name='python3')
    proc.allow_errors = True
 
    proc.preprocess(nb, {'metadata': {'path': './'}})
    #output_path = os.path.join(dirname, '{}_all_output.ipynb'.format(nb_name))
 
    #with open(output_path, mode='wt') as f:
    #    nbformat.write(nb, f)
 
    errors = []
    for cell in nb.cells:
        if 'outputs' in cell:
            for output in cell['outputs']:
                if output.output_type == 'error':
                    errors.append(output)
 
    return nb, errors
 

 
class TestNotebook(unittest.TestCase):
 
    def test_notebooks(self):
        from glob import glob
        notebooks_files = glob("*.ipynb", recursive=True)
        print("Found %d python notebooks" % (len(notebooks_files),))
        for file  in notebooks_files:
            with self.subTest(notebook=file):
                print("Processing:" + file + "...", end='')
                nb, errors = run_notebook(file)
                if errors == []:
                    print("OK")
                else:
                    print("Failed")
                self.assertEqual(errors, [])
                
 
 
if __name__ == '__main__':
    unittest.main()