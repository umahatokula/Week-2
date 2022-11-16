faculties = {
  'Law': {
    'Private Law': 50,
    'Public Law': 60,
    'International and Comparative Law': 70
  },
  'Engineering': {
    'Chemical Engineering': 20,
    'Civil Engineering': 45,
    'Mechanical Engineering': 56
  },
  'Natural Sciences': {
    'Biochemistry': 48,
    'Microbiology': 50,
    'Physics': 52
  },
  'Medicine': {
    'Anatomy': 80,
    'Medical Laboratory Science': 85,
    'Pharmacology': 90
  },
}

# get faculties as a list
facultiesList = list(faculties.keys())

selectedOption = int(
  input(
    'Please type \n 0 for Law\n 1 for Engineering \n 2 for : Natural Sciences or \n 3 for Medicine \n'
  ))

selectedFaculty = faculties[facultiesList[selectedOption]]

score = int(input('Please enter your score: '))


def suggestDept(score):
  """
  Determine dept based on selected faculty and score
  """
  l1 = []

  for dept, scores in selectedFaculty.items():

    if int(score) >= int(scores):
      l1.append((facultiesList[selectedOption], dept))

  return l1


def printSuggestedDept(suggestions):
  """
  Print suggested Dept and Faculty
  """
  if len(suggestions) > 1:
    print('\n You qualify for any of the following: ')
  elif len(suggestions) == 1:
    print('\n You qualify for ')
  else:
    print('\n Your score is too low for admission')

  for s in suggestions:
    print('\n {} department - faculty of {} \n'.format(s[1], s[0]))


suggesedtDepts = suggestDept(score)
printSuggestedDept(suggesedtDepts)
