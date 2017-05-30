import numpy as np

from pylatex import Document, Section, Subsection, Math, Matrix, VectorName, Enumerate

np.set_printoptions(formatter='int')

def calc_eigvectors(matrix):
    return

def make_int_eigs(shape):
    int_eigs_array = []
    while len(int_eigs_array) < 99:
        while True:
            mat1 = np.random.randint(-5, high=5, size=(shape,shape))
            try:
                inver = np.linalg.inv(mat1)
                break
            except np.linalg.linalg.LinAlgError:
                pass
        mat2 = np.diag(np.diag(np.random.randint(-5, high=5, size=(shape,shape))))
        det = np.linalg.det(mat1)
        A = np.dot(det,np.dot(mat1,np.dot(mat2,inver)))
        keep = True
        for i in A:
            for j in i:
                if abs(j) > 70:
                    keep = False
                    break
                elif abs(j) == 0:
                    keep = False
                    break
                elif abs(j) < 1:
                    keep = False
                    break
        if keep == True:
            int_eigs_array.append(A)
    return int_eigs_array

int_eigs_twos = make_int_eigs(2)
int_eigs_threes = make_int_eigs(3)

if __name__ == '__main__':
    matrix_twos = [np.random.randint(-10, high=10, size=(2,2)) for i in range(100)]
    matrix_threes = [np.random.randint(-10, high=10, size=(3,3)) for i in range(100)]

    answers = []
    eiganswers = []
    eiganswers3 = []


    doc = Document()
    with doc.create(Section('Matrix Practice')):
        '''
        with doc.create(Subsection('Multiplication - 2x2')):
            with doc.create(Enumerate(enumeration_symbol=r"\arabic*)")) as enum:
                for j in range(15):
                    ar1 = matrix_twos.pop()
                    ar2 = matrix_twos.pop()
                    vec1 = Matrix(ar1)
                    vec2 = Matrix(ar2)
                    ans = np.dot(ar1,ar2)
                    math = Math(data=[vec1,vec2])
                    enum.add_item(math)
                    answers.append(ans)

        with doc.create(Subsection('Multiplication - 3x3')):
            with doc.create(Enumerate(enumeration_symbol=r"\arabic*)", options={'start': 16})) as enum:
                for j in range(15):
                    ar1 = matrix_threes.pop()
                    ar2 = matrix_threes.pop()
                    vec1 = Matrix(ar1)
                    vec2 = Matrix(ar2)
                    ans = np.dot(ar1,ar2)
                    math = Math(data=[vec1,vec2])
                    enum.add_item(math)
                    answers.append(ans)
        '''

        with doc.create(Subsection('Eigenvectors - 2x2')):
            with doc.create(Enumerate(enumeration_symbol=r"\arabic*)")) as enum:
                for j in range(50):
                    ar1 = int_eigs_twos.pop()
                    vec1 = Matrix(ar1)
                    ans = np.linalg.eig(ar1)
                    math = Math(data=[vec1])
                    enum.add_item(math)
                    eiganswers.append(ans)

        with doc.create(Subsection('Eigenvectors - 3x3')):
            with doc.create(Enumerate(enumeration_symbol=r"\arabic*)", options={'start': 51})) as enum:
                for j in range(5):
                    ar1 = int_eigs_threes.pop()
                    vec1 = Matrix(ar1)
                    ans = np.linalg.eig(ar1)
                    math = Math(data=[vec1])
                    enum.add_item(math)
                    eiganswers3.append(ans)

        with doc.create(Subsection('Answers')):
            with doc.create(Enumerate(enumeration_symbol=r"\arabic*)")) as enum:
                for ans in eiganswers:

                    evals = np.array([[int(ans[0][0]),int(ans[0][1])]]).T
                    evalsm = Matrix(evals)

                    eigvects = ans[1]
                    eigenvectors = np.array([[ans[1][0][0]/ans[1][1][0],ans[1][0][1]/ans[1][1][1]]]).T
                    #eigvalsmatrix = Matrix(eigvals)
                    evmatrix = Matrix(eigenvectors)

                    math = Math(data=['eigenvalues:',evalsm,'eigenvectors:',evmatrix])
                    enum.add_item(math)

doc.generate_pdf('eigen_practice', clean_tex=False)
