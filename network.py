"""                                                                                                                                                                     
File:        network.py                                                                                                                                                 
Author:      Korey Webb                                                                                                                                                 
Date:        11/24/23                                                                                                                                                                                                                                                                                               
Description: This program is for creating an effective                                                                                                                  
             network that mimics a caller service.                                                                                                                      
             Multiple dictionary and list structures                                                                                                                    
             are used to facilitate the connections                                                                                                                     
             within the network structure.                                                                                                                              
"""

HYPHEN = "-"
QUIT = 'quit'
SWITCH_CONNECT = 'switch-connect'
SWITCH_ADD = 'switch-add'
PHONE_ADD = 'phone-add'
NETWORK_SAVE = 'network-save'
NETWORK_LOAD = 'network-load'
START_CALL = 'start-call'
END_CALL = 'end-call'
DISPLAY = 'display'
PHONE_NUMBERS = 'Phones'
THE_PHONE = 'Phone'
CONNECTION = 'Connects'
CALLS = 'Calling'
TRUNK_LENGTH_MAX = 3


def connect_switchboards(switchboards, area_1, area_2):
    """ This function serves to connect 2 area codes by                                                                                                                 
        establishing a trunk_line between the two.                                                                                                                      
        Param: switchboards is the current network                                                                                                                      
               structure.                                                                                                                                               
        Param: area_1 is the first area code given.                                                                                                                     
        Param: area_2 is the second area code given.                                                                                                                    
    """

    #  Makes sure that no bad conditions are met.  #                                                                                                                    

    if area_1 != area_2:
        if area_1 in switchboards.keys() and area_2 in switchboards.keys():

            if area_1 not in switchboards[area_2][CONNECTION] and area_2 not in switchboards[area_1][CONNECTION]:

                #  Append is used to add to the list structure regarding the trunk lines.  #                                                                            
                switchboards[area_1][CONNECTION].append(area_2)
                switchboards[area_2][CONNECTION].append(area_1)
                print(switchboards)
            else:
                print('you already connected them')

        else:
            print('One of those area codes are not valid, try again.')

    else:
        print('You used the same area code twice...')


def add_switchboard(switchboards, area_code):
    """ This function creates the switchboard                                                                                                                           
        structure for the rest of the functions                                                                                                                         
        to work correctly.                                                                                                                                              
        Param: switchboards is the given switchboards                                                                                                                   
               network structure.                                                                                                                                       
        Param: area_code is the given area code that                                                                                                                    
               the user seeks to add.                                                                                                                                   
    """


    if area_code not in switchboards.keys():

        #  This is the structure that I chose regarding the networking for switchboards.  #                                                                             
        switchboards[area_code] = {}
        switchboards[area_code][CONNECTION] = []
        switchboards[area_code][PHONE_NUMBERS] = []
        switchboards[area_code][CALLS] = {}

    else:
        print('That area code is already used..')


def add_phone(switchboards, area_code, phone_number):
    """ This function is for adding a phone number to a                                                                                                                 
        given area code. While also making sure the                                                                                                                     
        area_code exists and the phone number doesn't                                                                                                                   
        exist.                                                                                                                                                          
        Param: switchboards is the current network saved.                                                                                                               
        Param: area_code is the given area code.                                                                                                                        
        Param: phone_number is the given phone number                                                                                                                   
               that the user wants.                                                                                                                                     
    """

    if area_code in switchboards.keys():

        if phone_number not in switchboards[area_code][PHONE_NUMBERS]:

            #  The phone number has to be appended within the list just like "CONNECTIONS."  #                                                                          
            switchboards[area_code][PHONE_NUMBERS].append(phone_number)
            print('The phone number was able to be set.')

            #  the extra print statement is just for better terminal flow.  #                                                                                           

        else:
            print('That phone number is already used.')
    else:
        print('You caused an error somewhere, try again.')


def save_network(switchboards, file_name):
    """ This function is used to save the current                                                                                                                       
        switchboards network to a file for later                                                                                                                        
        usage.                                                                                                                                                          
        Param: switchboards is the current network.                                                                                                                     
        Param: file_name is the given file name.                                                                                                                        
    """

    file = open(file_name,'w')

    for keys in switchboards:

        #  This serves as another line of security regarding switchboard resetting the calls.  #                                                                        
        switchboards[keys][CALLS] = {}

    #  The file structure is set up very similar to how JSON achieves its results.  #     
    for area_code in switchboards.keys():
        file.write(str(area_code))
        file.write(';')

        for trunk_lines in switchboards[area_code][CONNECTION]:
            file.write(str(trunk_lines) + " ")
        file.write(';')

        for phones in switchboards[area_code][PHONE_NUMBERS]:

            file.write(str(phones)+ " ")
        file.write(';' +'\n')

        #  The new line is used in order to create another line within the file.  #                                                                                     

def load_network(file_name):
    """                                                                                                                                                                 
    :param file_name: the name of the file to load.                                                                                                                     
    :return: you must return the new switchboard network.  If you don't, then it won't load properly.                                                                   
    """


    file = open(file_name,'r')
    new_switchboard = dict()

    #  This for loop is to get rid of the semi-colons separting the components of each line.  #                                                                         
    for line in file:
        line_test = line.split(";")

        #  The new structure of the switchboard is created and set.  #                                                                                                  
        new_switchboard[int(line_test[0])] = {}
        new_switchboard[int(line_test[0])][CONNECTION] = []
        new_switchboard[int(line_test[0])][PHONE_NUMBERS] = []
        new_switchboard[int(line_test[0])][CALLS] = {}

        #  Strips any extra whitespace inside the file's components  #                                                                                                  
        file_list = []
        for i in line_test[1:]:
            if i != '\n':
                i = i.strip()
                file_list.append(i)

                #  Serves as the way the trunk lines and the phone numbers are added.  #                                                                                
                for value in file_list:

                    #  TRUNK_LENGTH_MAX is used to determine which is a area code or not.  #                                                                            

                    if len(str(value)) <= TRUNK_LENGTH_MAX:

                        if str(value) != '':

                            if int(value) not in new_switchboard[int(line_test[0])][CONNECTION]:
                                new_switchboard[int(line_test[0])][CONNECTION].append(int(value))

                    else:
                        if int(value) not in new_switchboard[int(line_test[0])][PHONE_NUMBERS] and str(value) != '':
                            new_switchboard[int(line_test[0])][PHONE_NUMBERS].append(int(value))

    return new_switchboard

def start_call(switchboards, start_area, start_number, end_area, end_number):
    """ This function is to connect 2 phone numbers together                                                                                                            
        using a recursion based helper function. When the                                                                                                               
        recursion helper function named trunk_connections                                                                                                               
        condition is met. It will connect the phone_numbers                                                                                                             
        together and set it in switchboards.                                                                                                                            
        Param: switchboards is the 2D dictionary network.                                                                                                               
        Param: start_area is the beginning area code.                                                                                                                   
        Param: start_number is the beginning given phone                                                                                                                
               number.                                                                                                                                                  
        Param: end_area is the ending area code.                                                                                                                        
        Param: end number is the ending given phone                                                                                                                     
               number                                                                                                                                                   
    """

    if start_area in switchboards.keys() and end_area in switchboards.keys():

        if start_number != end_number:

            if start_number in switchboards[start_area][PHONE_NUMBERS]:

                if end_number in switchboards[end_area][PHONE_NUMBERS]:

                    if switchboards[start_area][CALLS] == {} and switchboards[end_area][CALLS] == {}:

                        #  trunk_connections is the helper function which uses the recursion.  #                                                                        
                        if trunk_connections(switchboards, start_area, end_area, [] ) == True:
                            switchboards[start_area][CALLS][start_number] = str(end_area) + '-' + str(end_number)
                            switchboards[end_area][CALLS][end_number] = str(start_area) + '-' + str(start_number)

                            print(start_number, 'is connected with', end_number)
                        else:
                            print(start_number, 'and', end_number, 'were not connected.')
                else:
                    print('There is a error corresponding with the end_number.')

            else:
                print('The start number is not with that area code or it does not exist.')
        else:
            print('The start_number and end_number cannot be the same in such a way.')


def trunk_connections(switchboards, start, end, visited):
    """ This function serves as a helper function for                                                                                                                   
        start_call. It uses recursion to find the                                                                                                                       
        pathway connecting trunk lines together, if                                                                                                                     
        available.                                                                                                                                                      
        Param: switchboards is the current network                                                                                                                      
               structure.                                                                                                                                               
        Param: start is the starting area_code.                                                                                                                         
        Param: end is the ending area_code.                                                                                                                             
        Param: visited is the previously accessed                                                                                                                       
               or assigned area code for the                                                                                                                            
               recursion element.                                                                                                                                       
    """

    if start == end:
        return True

    elif switchboards[start][CONNECTION] == []:
        print('There is no Trunk line connecting the start and the end areas.')
        return False

    else:

        #  The recursive case which finds the network's pathway to connect calls.  #                                                                                    
        visited.append(start)
        for area in switchboards[start][CONNECTION]:
            if area not in visited:
                if trunk_connections(switchboards, area, end, visited):
                    return True
        return False


def end_call(switchboards, start_area, start_number):
    """ This function is to end the call that was previously                                                                                                            
        started. Its also used to determine if that number                                                                                                              
        ever has a call connection.                                                                                                                                     
        Param: switchboards is the current network structure.                                                                                                           
        Param: start_area is the given area code with the                                                                                                               
               number.                                                                                                                                                  
        Param: start_number is the given phone number.                                                                                                                  
    """


    if start_area in switchboards.keys():

        if start_number in switchboards[start_area][CALLS].keys():
            print('hanging up...\nconnection terminated')

            #  Connects to how start call stores the area code and phone number.  #                                                                                     
            end_area = int(switchboards[start_area][CALLS][start_number][0:3])
            end_number = int(switchboards[start_area][CALLS][start_number][4:])

            del switchboards[start_area][CALLS][start_number]
            del switchboards[end_area][CALLS][end_number]

        else:
            print('Unable to disconnect')
            print('The start number does not exist...')
            print(switchboards)


    else:
        print('This area code does not exist.')


def display(switchboards):
    """ This function is to set the display when asked                                                                                                                  
        for it by given user input.                                                                                                                                     
        Param: switchboards is the full 2D dictionary                                                                                                                   
               regarding the network structure.                                                                                                                         
    """

    #  Finds all the area_keys within the 2d dictionary(switchboards).  #                                                                                               
    for area_key in switchboards:
        print('Switchboard with area code:', area_key)
        print('\t Trunk lines are:')

        for trunk_line in switchboards[area_key][CONNECTION]:
            print('\t\t Trunk lines connection to:', trunk_line)

        print('\t local phone numbers are:')
        for numbers in switchboards[area_key][PHONE_NUMBERS]:

            if numbers not in switchboards[area_key][CALLS]:
                print('\t\t Phone with number:', numbers, 'not in use.')

            else:
                print('\t\t Phone with number:', numbers, 'is connected to', switchboards[area_key][CALLS][numbers])


if __name__ == '__main__':
    switchboards = {}  # probably {} or []                                                                                                                              
    s = input('Enter command: ')
    while s.strip().lower() != QUIT:
        split_command = s.split()
        if len(split_command) == 3 and split_command[0].lower() == SWITCH_CONNECT:
            area_1 = int(split_command[1])
            area_2 = int(split_command[2])
            connect_switchboards(switchboards, area_1, area_2)

        elif len(split_command) == 2 and split_command[0].lower() == SWITCH_ADD:
            if len(split_command[1]) <= TRUNK_LENGTH_MAX:
                if split_command[1][0] == '0':
                    add_switchboard(switchboards, (split_command[1]))
                else:
                    add_switchboard(switchboards, int(split_command[1]))

        elif len(split_command) == 2 and split_command[0].lower() == PHONE_ADD:
            number_parts = split_command[1].split('-')
            area_code = int(number_parts[0])
            phone_number = int(''.join(number_parts[1:]))
            add_phone(switchboards, area_code, phone_number)

        elif len(split_command) == 2 and split_command[0].lower() == NETWORK_SAVE:
            save_network(switchboards, split_command[1])
             print('Network saved to {}.'.format(split_command[1]))

        elif len(split_command) == 2 and split_command[0].lower() == NETWORK_LOAD:
            switchboards = load_network(split_command[1])
            print('Network loaded from {}.'.format(split_command[1]))

        elif len(split_command) == 3 and split_command[0].lower() == START_CALL:
            src_number_parts = split_command[1].split(HYPHEN)
            src_area_code = int(src_number_parts[0])
            src_number = int(''.join(src_number_parts[1:]))

            dest_number_parts = split_command[2].split(HYPHEN)
            dest_area_code = int(dest_number_parts[0])
            dest_number = int(''.join(dest_number_parts[1:]))
            start_call(switchboards, src_area_code, src_number, dest_area_code, dest_number)

        elif len(split_command) == 2 and split_command[0].lower() == END_CALL:
            number_parts = split_command[1].split(HYPHEN)
            area_code = int(number_parts[0])
            number = int(''.join(number_parts[1:]))
            end_call(switchboards, area_code, number)

        elif len(split_command) >= 1 and split_command[0].lower() == DISPLAY:
            display(switchboards)

        s = input('Enter command: ')
