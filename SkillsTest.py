# Element Finder

from pyscript import document, display #type:ignore

# make function
def user_input (e):
    # erases previous answer
    document.getElementById('output').innerHTML = ''
    # connects to id and make the input stripped and titled
    element = document.getElementById('input').value.strip().title()
    # dictionary
    element_information = {
            'He' : ['Symbol: He',
                            'Element: Helium',
                            'Atomic Mass: 4.002602 u',
                            'Atomic Number: 2'],
            'Ne' : ['Symbol: Ne',
                            'Element: Neon',
                            'Atomic Mass: 20.1797 u',
                            'Atomic Number: 10'],
            'Ar' : ['Symbol: Ar',
                            'Element: Argon',
                            'Atomic Mass: 39.95 u',
                            'Atomic Number: 18'],
            'Kr' : ['Symbol: Kr',
                            'Element: Krypton',
                            'Atomic Mass: 83.798 u',
                            'Atomic Number: 36'],
            'Xe' : ['Symbol: Xe',
                            'Element: Xenon',
                            'Atomic Mass: 131.29 u',
                            'Atomic Number: 54'],
            'Rn' : ['Symbol: Rn',
                            'Element: Radon',
                            'Atomic Mass: 222 u',
                            'Atomic Number: 86'],
            'Og' : ['Symbol: Og',
                            'Element: Oganesson',
                            'Atomic Mass: 294 u',
                            'Atomic Number: 118'],
        }

    # checking input in dictionary
    checker = element in element_information
    # message
    message = ('Element not found.', f'{element_information.get(element)} found.')
    # make output with the message
    display(message[checker], target = 'output')