MONTH = {
  'label': 'MONTH',
  'values': (
    'month',
  ),
}

MONTH_PATTERNS = [
  [['MONTH']], 
]

def shorten(entity):
  return entity.capitalize()[0]

ENTITY_DEFINITION = {
  'patterns': MONTH_PATTERNS,
  'extraTokens': (MONTH,),
  'spacing': {
    'default': '',
  },
  'entityCleaning': shorten
}
