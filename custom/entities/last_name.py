''' this contians the entity definition for a us license plate '''
# Each interpreter needs a list of patterns to look for

LAST_NAME = {
  'label': 'LAST_NAME',
  'values': (
    'doerr',
    'josling',
    'jostling',
  )
}

LAST_NAME_PATTERNS = [[['LAST_NAME']]]

ENTITY_DEFINITION = {
  'extraTokens': (LAST_NAME,),
  'patterns': LAST_NAME_PATTERNS,
}
