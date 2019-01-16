from import_modules import *

def calculate_determinant(matrix):
  matrix = np.array(matrix)
  result = np.linalg.det(matrix)
  return result


def create_sorted_determinant_list(vectors):
  comb = combinations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
  determinant_list = []

  for i, combination in enumerate(comb):
    result = {}
    vector1 = vectors[combination[0]]
    vector2 = vectors[combination[1]]
    vector3 = vectors[combination[2]]

    matrix = np.matrix([vector1, vector2, vector3])
    determinant = calculate_determinant(matrix)

    result['determinant'] = determinant
    result['indices'] = combination
    determinant_list.append(result)

  return determinant_list
