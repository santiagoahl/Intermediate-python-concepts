DATA = [ #this is a constant, that's why it's in capital letters
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Hector',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def main():
    #using comprehensions
    all_python_devs = [worker['name'] for worker in DATA if worker['language'] =='python' ]
    all_platzi_workers = [worker['name'] for worker in DATA if worker['organization'] == 'Platzi']
    adults_comp = [worker for worker in DATA if worker['age'] >= 28]
    old_people_comp = [worker | {'old': worker['age'] >= 70} for worker in DATA]
    #using FILTER
    adults = list(filter(lambda worker: worker['age'] >= 28, DATA))
    all_python_devs_filter = list(filter(lambda worker: worker['language'] == 'python', DATA))
    all_platzi_workers_filter = list(filter(lambda worker: worker['organization'] == 'Platzi',DATA))
    adults_names = list(map(lambda worker: worker['name'], DATA))
    #using MAP
    old_people = list(map(lambda worker: worker | {'old': worker['age'] >= 70}, DATA)) #We transform a dictionary adding a new key if it satisfies a condition
    for worker in old_people_comp:
        print(worker)

if __name__ == '__main__':
    main()