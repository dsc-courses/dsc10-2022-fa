test = {   'name': 'q2_3',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> callable(effective_tax_rate) and np.isclose(effective_tax_rate(75_000), 15.743, 0.1)\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> effective_tax_rate(-1) == 0 # Make sure you address the case where the input is less than or equal to 0. The function should evaluate to 0 in that '
                                               'case.\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
