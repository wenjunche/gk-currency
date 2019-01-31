''' this contians the entity definition for a us license plate '''
# Each interpreter needs a list of patterns to look for

CITY = {
  'label': 'CITY',
  'values': (
    'london',
    'new york',
  )
}

CITY_PATTERNS = [[['CITY']]]

ENTITY_DEFINITION = {
  'extraTokens': (CITY,),
  'patterns': CITY_PATTERNS,
}
