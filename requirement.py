import random
from beer import Beer
"""
Docstring for requirement

Describes a test for one of the grids columns or rows.
"""
class Requirement:
    types = {
        'abv': ['high', 'low']
        ,'ibu': ['high', 'low']
        ,'brewery': ['macro', 'micro']
        ,'rating': ['high', 'low']
        ,'style': ['pale_ale', 'ipa', 'stout', 'lager', 'sour', 'wheat', 'blonde']
        ,'dom_intl': ['domestic', 'international']
        ,'region': ['midwest', 'east_coast', 'west_coast']
    }

    texts = {
        ('abv', 'high'): 'ABV ≥ 6.0%'
        ,('abv', 'low'): 'ABV ≤ 6.0%'
        ,('ibu', 'high'): 'IBU ≥ 30'
        ,('ibu', 'low'): 'IBU ≤ 30'
        ,('brewery', 'macro'): 'Macrobrewery'
        ,('brewery', 'micro'): 'Microbrewery'
        ,('rating', 'high'): 'Rating ≥ 3.5'
        ,('rating', 'low'): 'Rating ≤ 3.5'
        ,('style', 'pale_ale'): 'Pale Ale'
        ,('style', 'ipa'): 'IPA'
        ,('style', 'stout'): 'Stout'
        ,('style', 'lager'): 'Lager'
        ,('style', 'sour'): 'Sour'
        ,('style', 'wheat'): 'Wheat Ale'
        ,('style', 'blonde'): 'Blonde Ale'
        ,('dom_intl', 'domestic'): 'Domestic'
        ,('dom_intl', 'international'): 'International'
        ,('region', 'midwest'): 'Midwest'
        ,('region', 'east_coast'): 'East Coast'
        ,('region', 'west_coast'): 'West Coast'
    }

    def __init__(self, exclude = None, dups = None, session = None) -> None:
        if session is None:
            if exclude is None:
                exclude = set()
            if dups is None:
                dups = set()
            available = set(self.types.keys()) - exclude
            self.type = random.choice(list(available))
            self.req = random.choice(self.types[self.type])
            while (self.type, self.req) in dups:
                self.type = random.choice(list(available))
                self.req = random.choice(self.types[self.type])
            self.text = self.texts[(self.type, self.req)]
        else:
            self.type = session['type']
            self.req = session['req']
            self.text = session['text']

    def get_excluded_set(self):
        if self.type in ['dom_intl', 'region']:
            return {'dom_intl', 'region'}
        else:
            return {self.type}
        
    def __repr__(self) -> str:
        return self.text
    
    def __str__(self) -> str:
        return self.text

    """
    Given beer object, determine if it matches this requirement of the grid

    Params: beer - Beer object to compare to

    Returns: True if the Beer Object passes the requirment, False if not
    """
    def compare_beer(self, beer: Beer) -> bool:
        abv_cutoff = 6.0
        ibu_cutoff = 30
        macro_cutoff = 1000000
        rating_cutoff = 3.5
        match self.type:
            case 'abv':
                if self.req == 'high':
                    return beer.abv >= abv_cutoff
                else:
                    return beer.abv <= abv_cutoff
            case 'ibu':
                if self.req == 'high':
                    return beer.ibu >= ibu_cutoff
                else:
                    return beer.ibu <= ibu_cutoff
            case 'brewery':
                if self.req == 'macro':
                    return beer.brewery.ratings >= macro_cutoff
                else:
                    return beer.brewery.ratings <= macro_cutoff
            case 'rating':
                if self.req == 'high':
                    return beer.rating >= rating_cutoff
                else:
                    return beer.rating <= rating_cutoff
            case 'style':
                match self.req:
                    case 'pale_ale':
                        return 'Pale Ale' in beer.style
                    case 'ipa':
                        return 'IPA' in beer.style
                    case 'stout':
                        return 'Stout' in beer.style
                    case 'lager':
                        return 'Lager' in beer.style
                    case 'sour':
                        return 'Sour' in beer.style
                    case 'wheat':
                        return 'Wheat' in beer.style
                    case 'blonde':
                        return 'Blonde' in beer.style
                    case _:
                        return False
            case 'dom_intl':
                if self.req == 'domestic':
                    return len(beer.brewery.state) != 2
                else:
                    return len(beer.brewery.state) == 2
            case 'region':
                match self.req:
                    case 'midwest':
                        return beer.brewery.state in ['WI','IL','IN','OH','MI','MN','IA']
                    case 'east_coast':
                        return beer.brewery.state in ['ME','NH','VT','NY','MA','RI','CT','NJ','DE','PA','MD','DC','WV','VA','NC','SC','GA','FL']
                    case 'west_coast':
                        return beer.brewery.state in ['WA','OR','CA','HI','AK','NV','AZ','CO','WY','ID','UT','MT']
                    case _:
                        return False
            case _:
                return False
            
    def serialize(self) -> dict:
        return {
            'type': self.type
            ,'req': self.req
            ,'text': self.text
        }