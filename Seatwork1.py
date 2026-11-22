# Seatwork 1: Nickname Atlas

from pyscript import document, display #type: ignore

# make function called inputUser from button in index
def inputUser (e):
    # erases previous answers for new ones
    document.getElementById('output').innerHTML =''

    # make variable
    input = document.getElementById('country').value

    # prints it on website
    display(input, target='output')