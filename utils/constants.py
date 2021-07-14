#!/usr/bin/python3.9
# -*- coding: utf-8 -*-

CURRENT_SESSION = 1029

GA_LEGISLATION_ROUTES = {
    'sessions': {
        'url': 'https://www.legis.ga.gov/committees/house',
        'intercept_routes': ['/api/sessions'],
    },
    'committees': {
        'url': 'https://www.legis.ga.gov/committees/house',
        'intercept_routes': ['/api/committees/List/{current_session}'],
    },
    'representatives': {
        'url': 'https://www.legis.ga.gov/members/house',
        'intercept_routes': ['/api/members/list/{current_session}?chamber=1'],
    },
    'senators': {
        'url': 'https://www.legis.ga.gov/members/senate',
        'intercept_routes': ['/api/members/list/{current_session}?chamber=2'],
    },
    'legislative_summaries': {
        'url': 'https://www.legis.ga.gov/legislation/all',
        'intercept_routes': ['/api/Legislation/Search/20/0'],
    },
    'legislative_details': {
        'url': 'https://www.legis.ga.gov/legislation/{legislation_id}',
        'intercept_routes': ['/api/legislation/detail', '/api/legislation/html'], # noqa
    }
}
