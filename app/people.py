people = [{'name': 'Jason Statham', 'position_id': 1},
          {'name': 'Filipp Kirkorov', 'position_id': 2},
          {'name': 'Boris The Blade', 'position_id': 3},
          {'name': 'Gordon Ramsay', 'position_id': 2},
          {'name': 'Alex Navalny', 'position_id': 4},
          {'name': 'He-who-must-not-be-named', 'position_id': 1}]

positions = [{'id': 1, 'name': 'repairman', 'salary': 2000},
             {'id': 2, 'name': 'stripper', 'salary': 3000},
             {'id': 3, 'name': 'postman', 'salary': 4000},
             {'id': 4, 'name': 'sniper', 'salary': 66666666}]


def get_employees():
    return [{'name': p['name'],
             'position': next(i['name'] for i in positions if i['id'] == p['position_id']),
             'id': p['position_id'],
             'salary': next(i['salary'] for i in positions if i['id'] == p['position_id'])} for p in people]
