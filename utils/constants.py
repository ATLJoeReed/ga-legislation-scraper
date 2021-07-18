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
        'intercept_routes': ['/api/Legislation/Search'],
    },
    'legislative_details': {
        'url': 'https://www.legis.ga.gov/legislation/{legislation_id}',
        'intercept_routes': ['/api/legislation/detail', '/api/legislation/html'], # noqa
    },
    'house_votes': {
        'url': 'https://www.legis.ga.gov/votes/house',
        'intercept_routes': ['/api/Vote/list/1/{current_session}'],
    },
    'senate_votes': {
        'url': 'https://www.legis.ga.gov/votes/senate',
        'intercept_routes': ['/api/Vote/list/2/{current_session}'],
    },
    'house_member_votes': {
        'url': 'https://www.legis.ga.gov/votes/house',
        'intercept_routes': ['api/Vote/detail/{vote_id}']
    },
    'senate_member_votes': {
        'url': 'https://www.legis.ga.gov/votes/senate',
        'intercept_routes': ['api/Vote/detail/{vote_id}']
    },
}
