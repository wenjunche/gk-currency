NON_ABBREVIATED_NAMES = ('jeffries', 'barclays')

LEGAL_ENTITY_NAME = {
  'label': 'LEGAL_ENTITY_NAME',
  'values': ('JP', 'RBC', 'BNY') + NON_ABBREVIATED_NAMES
}

LEGAL_ENTITY_ABBREVIATIONS = (
  ('j p', 'JP'),
  ('r b c', 'RBC'),
  ('b n y', 'BNY'),
)

def capitalize(entity):
  return entity.capitalize() if entity in NON_ABBREVIATED_NAMES else entity

ENTITY_DEFINITION = {
  'patterns': [
     [['LEGAL_ENTITY_NAME']],
  ],
  'extraTokens': (LEGAL_ENTITY_NAME,),
  'entityCleaning': capitalize,
  'collapsiblePatterns': LEGAL_ENTITY_ABBREVIATIONS,
}