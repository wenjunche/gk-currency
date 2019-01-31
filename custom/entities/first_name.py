''' this contians the entity definition for a us license plate '''
# Each interpreter needs a list of patterns to look for

FIRST_NAME = {
  'label': 'FIRST_NAME',
  'values': (
    'alexandra',
    'chuck',
    'mark',
    'tony,'
  )
}

FIRST_NAME_PATTERNS = [[['FIRST_NAME']]]

ENTITY_DEFINITION = {
  'extraTokens': (FIRST_NAME,),
  'patterns': FIRST_NAME_PATTERNS,
}
