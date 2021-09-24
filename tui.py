def welcome():
    """
    Task 1: Display a welcome message.

    The welcome message should consist of the title 'Solar Record Management System' surrounded by dashes.
    The number of dashes before and after the title should be equal to the number of characters in the title 
    i.e. 30 dashes before and after.

    :return: Does not return anything.
    """
    # TODO: Your code here
    # Solar Record Management System == 30 Characters
    print("------------------------------")
    print("Solar Record Management System")
    print("------------------------------")


def menu():
    """
    Task 2: Display a menu of options and read the user's response.

    A menu consisting of the following options should be displayed:
    'Load Data', 'Process Data', 'Visualise Data', 'Save Data' and 'Exit'

    The user's response should be read in and returned as an integer corresponding to the selected option.
    For example, 1 for 'Load Data', 2 for 'Process Data' and so on.

    If the user enters a invalid option then a suitable error message should be displayed and the value
    None should be returned.

    :return: None if invalid selection otherwise an integer corresponding to a valid selection
    """
    # TODO: Your code here
    print("Please select one of the following option:\n")
    print(" 1. Load Data\n 2. Process Data\n 3. Visualise Data\n 4. Save Data\n 0. Exit")

    # Creating an array to check if the users chose the right option
    menu_options = [0, 1, 2, 3, 4]

    # Retrieving users input into option var.
    option = int(input())

    # Checking if the option is equal as menu_option if not, None returned
    if option in menu_options:
        return option
    else:
        print("Invalid selection!")
        return None


def started(operation):
    """
    Task 3: Display a message to indicate that an operation has started.

    The function should display a message in the following format:
    '{operation} has started.'
    Where {operation} is the value of the parameter passed to this function

    :param operation: A string indicating the operation being started
    :return: Does not return anything
    """
    # TODO: Your code here
    print("Operation {} has started.".format(operation))


def completed(operation):
    """
    Task 4: Display a message to indicate that an operation has completed.

    The function should display a message in the following format:
    '{operation} has completed.'
    Where {operation} is the value of the parameter passed to this function

    :param operation: A string indicating the operation being completed
    :return: Does not return anything
    """
    # TODO: Your code here
    print("Operation {} has completed.".format(operation))


def error(error_msg):
    """
    Task 5: Display an error message.

    The function should display a message in the following format:
    'Error! {error_msg}.'
    Where {error_msg} is the value of the parameter passed to this function

    :param error_msg: A string containing an error message
    :return: Does not return anything
    """
    # TODO: Your code here
    print("Error! {}".format(error_msg))


def source_data_path():
    """
    Task 6: Retrieve a file path to the source data file.

    The function should prompt the user to enter the file path for a data file (e.g. 'data/sol_data.csv').
    If the file path entered by the user does not end in 'csv' then a suitable error message should be displayed
    and the value None should be returned.
    Otherwise, the file path entered by the user should be returned.

    :return: None if the file path does not end in 'csv' otherwise return the file path entered by the user
    """
    # TODO: Your code here
    print("\nNote: .CSV format files accepted only.")

    # Retrieving file path from user
    file_name = input("Please enter the file path for data file:\n")

    # Using the [-4] for file_name we check the last 4 characters for file
    if file_name[-4:] == ".csv":
        return file_name
    else:
        print("We are sorry. Only .CSV format accepted.")
        return None


def process_type():
    """
    Task 7: Display a menu of options for how the file should be processed. Read in the user's response.

    A menu should be displayed that contains the following options:
        'Retrieve entity', 'Retrieve entity details', 'Categorise entities by type',
        'Categorise entities by gravity', 'Summarise entities by orbit'

    The user's response should be read in and returned as an integer corresponding to the selected option.
    For example, 1 for 'Retrieve entity', 2 for 'Retrieve entity details' and so on.

    If the user enters a invalid option then a suitable error message should be displayed and the value
    None should be returned.

    :return: None if an invalid selection made otherwise an integer corresponding to a valid option
    """
    # TODO: Your code here
    print("\nPlease select one of the following option:\n")
    print("1. Retrieve entity \n2. Retrieve entity details \n3. Categorise by type \n4. Categorise entities by gravity \n5. Suummariise entitities by orbit")
    menu_options2 = [1, 2, 3, 4, 5]
    option2 = int(input())

    # Using if statement we check if the user entered the right option
    if option2 in menu_options2:
        return option2
    else:
        print("Invalid selection!")
        return None


def entity_name():
    """
    Task 8: Read in the name of an entity and return the name.

    The function should ask the user to enter the name of an entity e.g. 'Earth'
    The function should then read in and return the user's response.

    :return: the name of an entity
    """
    # TODO: Your code here
    entity = input("Please enter the name of an entity: ")
    return entity


def entity_details():
    """
    Task 9: Read in the name of an entity and column indexes. Return a list containing the name and indexes.

    The function should ask the user to enter the name of an entity e.g. 'Earth'
    The function should also ask the user to enter a list of integer column indexes e.g. 0,1,5,7
    The function should return a list containing the name of the entity and the list of column
    indexes e.g. ['Earth', [0,1,5,7]]

    :return: A list containing the name of an entity and a list of column indexes
    """
    # TODO: Your code here
    # Retrieving entity name
    selected_entity = input("Please enter the name of an entity: ")

    entity_list = []
    entity_list.append(selected_entity)

    # Retrieving the number of column indexes we want, where for loop will ask the user to fill it
    entity_columns = int(input("Please enter the length of columns indexes: "))

    # Depend on user choice this loop will go how many times the user ask using range(,)
    for entity_columns in range(0, entity_columns):
        selected_column = input("Please enter the value for column {}: ".format(entity_columns+1))
        entity_list.append(selected_column)
    return entity_list


def list_entity(entity, cols=[]):
    """
    Task 10: Display an entity. Only the data for the specified column indexes will be displayed.
    If no column indexes have been specified, then all the data for the entity will be displayed.

    The entity is a list of values corresponding to particular Solar System space entity
    E.g. ['Earth', TRUE, 9.8].
    The function should only display those values from the entity list that correspond to the column
    indexes provided as part of cols.
    E.g. if cols is [0, 2] then for the entity ['Earth', TRUE, 9.8] the following will be displayed
    ['Earth', 9.8]
    E.g. if cols is an empty list then all the values will be displayed i.e. ['Earth', TRUE, 9.8]

    :param entity: A list of data values related to an entity
    :param cols: A list of integer values that represent column indexes
    :return: does not return anything
    """
    # TODO: Your code here
    list_of_entities = []

    if cols:
        for cols in range(cols[0], cols[1]):
            list_of_entities.append(entity)
            print(entity)
    else:
        print(entity)


def list_entities(entities, cols=[]):
    """
    Task 11: Display each entity in entities. Only the data for the specified column indexes will be displayed.
    If no column indexes have been specified, then all the data for an entity will be displayed.

    The function should have two parameters as follows:
    entities    which is a list of entities where each entity itself is a list of data values
    cols        this is a list of integer values that represent column indexes.
                the default value for this is an empty list i.e. []

    You will need to add these parameters to the function definition.

    The function should iterate through each entity in entities and display the entity.
    An entity is a list of values e.g. ['Earth', TRUE, 9.8]
    Only the columns whose indexes are included in cols should be displayed for each entity.
    If cols is an empty list then all values for the entity should be displayed.

    :param entities: A list of data values related to an entity
    :param cols: A list of integer values that represent column indexes
    :return: Does not return anything
    """
    # TODO: Your code here
    entlist = []
    for entity in entities:
        line = []
        if cols:
            for col in cols:
                line.append(entity[col])
        else:
            for fentity in entity:
                line.append(fentity)
        entlist.append(line)
    for flist in entlist:
        print(flist)


def list_categories(categories):
    """
    Task 12: Display the contents of the dictionary categories.

    The function should take a single parameter categories which is a dictionary containing category names
    and a list of entities that belong to the category.

    You will need to add the parameter categories to the function definition.

    :param categories: A dictionary containing category names and a list of entities that are part of that category
    :return: Does not return anything
    """
    # TODO: Your code here
    for key in categories.keys():
        print("{} : {}".format(key, categories[key]))


def gravity_range():
    """
    Task 13: Ask the user for the lower and upper limits for gravity and return a tuple containing the limits.

    The function should prompt the user to enter the lower and upper limit for a range of values related to gravity.
    The values will be floats e.g. 5.1 for lower limit and 9.8 for upper limit.
    The function should return a tuple containing the lower and upper limits

    :return: a tuple with the lower and upper limits
    """
    # TODO: Your code here
    lower = float(input("Please enter the lower gravity limit: "))
    upper = float(input("Please enter the upper gravity limit: "))
    range_of_gravity = lower, upper
    return range_of_gravity


def orbits():
    """
    Task 14: Ask the user for a list of entity names and return the list.

    The function should prompt the user to enter a list of entity names e.g. Jupiter,Earth,Mars
    The list represents the entities that should be orbited.
    The user may enter as many entity names as they desire.
    The function should return a list of the entity names entered by the user.

    :return: a list of entity names
    """
    # TODO: Your code here
    number_of_planets = int(input("Please enter the number of planets: "))
    planet_list = []

    # Using range for user to input number of planets he would like to
    # Using append we will add the data to the planet_list
    for number_of_planets in range(0, number_of_planets):
        planet_filler = input("Please enter the planet number {}: ".format(number_of_planets+1))
        planet_list.append(planet_filler)
    return planet_list


def visualise():
    """
    Task 15: Display a menu of options for how the data should be visualised. Return the user's response.

    A menu should be displayed that contains the following options:
        'Entities by type', 'Entities by gravity', 'Summary of orbits', 'Animate gravities'

    The user's response should be read in and returned as an integer corresponding to the selected option.
    For example, 1 for 'Entities by type', 2 for 'Entities by gravity' and so on.

    If the user enters an invalid option, then a suitable error message should be displayed and the value
    None should be returned.

    :return: None if an invalid selection is made otherwise an integer corresponding to a valid option
    """
    # TODO: Your code here
    print("\nPlease select one of the following option:\n")
    print(" 1. Entities by type\n 2. Entities by gravity\n 3. Summary of orbits\n 4. Animate gravities")

    visualise_menu_options = [1, 2, 3, 4]
    visualise_option = int(input())

    if visualise_option in visualise_menu_options:
        return visualise_option
    else:
        print("Invalid selection!")
        return None


def save():
    """
    Task 16: Display a menu of options for how the data should be saved. Return the user's response.

    A menu should be displayed that contains the following option:
         'Export as JSON'

    The user's response should be read in and returned as an integer corresponding to the selected option.

    If the user enters a invalid option then a suitable error message should be displayed and the value
    None should be returned.

    :return: None if an invalid selection is made otherwise an integer corresponding to a valid option
    """
    # TODO: Your code here
    print("\nPlease select one of the following option:\n")
    print(" 1. Export as JSON\n 0. Exit")

    export_option = int(input())

    # Checking if user selected option 1 then returning 1 for saving data
    # If is 0 Goodbye message will be displayed otherwise an Error message will be printed
    if export_option == 1:
        return export_option
    elif export_option == 0:
        print("Good bye.")
        return None
    else:
        print("Invalid selection!")
        return None
