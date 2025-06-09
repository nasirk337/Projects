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

HYPHENS = "-"
QUITS = 'quit'
CONNECT_SWITCH = 'switch-connect'
ADD_SWITCH = 'switch-add'
ADD_PHONE = 'phone-add'
SAVE_NETWORK = 'network-save'
LOAD_NETWORK = 'network-load'
CALL_START = 'start-call'
CALL_END = 'end-call'
DISPLAY = 'display'
PHONE_NUMS = 'Phones'
THE_PHONE = 'Phone'
CONNECTS = 'Connects'
CALLS = 'Calling'
TRUNK_MAX = 3


def switchboards_connect(switchboards, switch_1, switch_2):
    """ This function serves to connect 2 area codes by                                                                                                                 
        establishing a trunk_line between the two.                                                                                                                      
        Param: switchboards is the current network                                                                                                                      
               structure.                                                                                                                                               
        Param: switch_1 is the first area code given.                                                                                                                     
        Param: switch_2 is the second area code given.                                                                                                                    
    """

    #  Makes sure that no bad conditions are met.  #                                                                                                                    

    if switch_1 != switch_2:
        if switch_1 in switchboards.keys() and switch_2 in switchboards.keys():

            if switch_1 not in switchboards[switch_2][CONNECTS] and switch_2 not in switchboards[switch_1][CONNECTS]:

                #  Append is used to add to the list structure regarding the trunk lines.  #                                                                            
                switchboards[switch_1][CONNECTS].append(switch_2)
                switchboards[switch_2][CONNECTS].append(switch_1)
                print(switchboards)
            else:
                print('you already connected them')

        else:
            print('One of those area codes are not valid, try again.')

    else:
        print('You used the same area code twice...')


def switchboard_add(switchboards, area_code):
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
        switchboards[area_code][CONNECTS] = []
        switchboards[area_code][PHONE_NUMS] = []
        switchboards[area_code][CALLS] = {}

    else:
        print('That area code is already used..')


def phone_add(switchboards, area_code, p_number):
    """ This function is for adding a phone number to a                                                                                                                 
        given area code. While also making sure the                                                                                                                     
        area_code exists and the phone number doesn't                                                                                                                   
        exist.                                                                                                                                                          
        Param: switchboards is the current network saved.                                                                                                               
        Param: area_code is the given area code.                                                                                                                        
        Param: p_number is the given phone number                                                                                                                   
               that the user wants.                                                                                                                                     
    """

    if area_code in switchboards.keys():

        if p_number not in switchboards[area_code][PHONE_NUMS]:

            #  The phone number has to be appended within the list just like "CONNECTIONS."  #                                                                          
            switchboards[area_code][PHONE_NUMS].append(p_number)
            print('The phone number was able to be set.')

            #  the extra print statement is just for better terminal flow.  #                                                                                           

        else:
            print('That phone number is already used.')
    else:
        print('You caused an error somewhere, try again.')


def network_save(switchboards, file_save):
    """ This function is used to save the current                                                                                                                       
        switchboards network to a file for later                                                                                                                        
        usage.                                                                                                                                                          
        Param: switchboards is the current network.                                                                                                                     
        Param: file_save is the given file name.                                                                                                                        
    """

    file = open(file_save,'w')

    for keys in switchboards:

        #  This serves as another line of security regarding switchboard resetting the calls.  #                                                                        
        switchboards[keys][CALLS] = {}

    #  The file structure is set up very similar to how JSON achieves its results.  #     
    for area_code in switchboards.keys():
        file.write(str(area_code))
        file.write(';')

        for trunk_lines in switchboards[area_code][CONNECTS]:
            file.write(str(trunk_lines) + " ")
        file.write(';')

        for phones in switchboards[area_code][PHONE_NUMS]:

            file.write(str(phones)+ " ")
        file.write(';' +'\n')

        #  The new line is used in order to create another line within the file.  #                                                                                     

def loading_network(file_save):
    """                                                                                                                                                                 
    :param file_save: the name of the file to load.                                                                                                                     
    :return: you must return the new switchboard network.  If you don't, then it won't load properly.                                                                   
    """


    file = open(file_save,'r')
    new_switchboard = dict()

    #  This for loop is to get rid of the semi-colons separting the components of each line.  #                                                                         
    for line in file:
        line_test = line.split(";")

        #  The new structure of the switchboard is created and set.  #                                                                                                  
        new_switchboard[int(line_test[0])] = {}
        new_switchboard[int(line_test[0])][CONNECTS] = []
        new_switchboard[int(line_test[0])][PHONE_NUMS] = []
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

                    if len(str(value)) <= TRUNK_MAX:

                        if str(value) != '':

                            if int(value) not in new_switchboard[int(line_test[0])][CONNECTS]:
                                new_switchboard[int(line_test[0])][CONNECTS].append(int(value))

                    else:
                        if int(value) not in new_switchboard[int(line_test[0])][PHONE_NUMBERS] and str(value) != '':
                            new_switchboard[int(line_test[0])][PHONE_NUMS].append(int(value))

    return new_switchboard

def starting_call(switchboards, first_area, first_num, end_area, end_num):
    """ This function is to connect 2 phone numbers together                                                                                                            
        using a recursion based helper function. When the                                                                                                               
        recursion helper function named trunk_connections                                                                                                               
        condition is met. It will connect the phone_numbers                                                                                                             
        together and set it in switchboards.                                                                                                                            
        Param: switchboards is the 2D dictionary network.                                                                                                               
        Param: first_area is the beginning area code.                                                                                                                   
        Param: first_num is the beginning given phone                                                                                                                
               number.                                                                                                                                                  
        Param: end_area is the ending area code.                                                                                                                        
        Param: end num is the ending given phone                                                                                                                     
               number                                                                                                                                                   
    """

    if first_area in switchboards.keys() and end_area in switchboards.keys():

        if first_num != end_num:

            if first_num in switchboards[first_area][PHONE_NUMS]:

                if end_num in switchboards[end_area][PHONE_NUMS]:

                    if switchboards[first_area][CALLS] == {} and switchboards[end_area][CALLS] == {}:

                        #  trunk_connections is the helper function which uses the recursion.  #                                                                        
                        if trunk_connections(switchboards, first_area, first_area, [] ) == True:
                            switchboards[first_area][CALLS][first_num] = str(end_area) + '-' + str(end_num)
                            switchboards[end_area][CALLS][end_num] = str(first_area) + '-' + str(first_num)

                            print(first_num, 'is connected with', end_num)
                        else:
                            print(first_num, 'and', end_num, 'were not connected.')
                else:
                    print('There is a error corresponding with the end_number.')

            else:
                print('The start number is not with that area code or it does not exist.')
        else:
            print('The start_number and end_number cannot be the same in such a way.')


def trunk_connects(switchboards, begin, end, visited):
    """ This function serves as a helper function for                                                                                                                   
        start_call. It uses recursion to find the                                                                                                                       
        pathway connecting trunk lines together, if                                                                                                                     
        available.                                                                                                                                                      
        Param: switchboards is the current network                                                                                                                      
               structure.                                                                                                                                               
        Param: begin is the starting area_code.                                                                                                                         
        Param: end is the ending area_code.                                                                                                                             
        Param: visited is the previously accessed                                                                                                                       
               or assigned area code for the                                                                                                                            
               recursion element.                                                                                                                                       
    """

    if begin == end:
        return True

    elif switchboards[begin][CONNECTS] == []:
        print('There is no Trunk line connecting the beginning and the ending areas.')
        return False

    else:

        #  The recursive case which finds the network's pathway to connect calls.  #                                                                                    
        visited.append(start)
        for area in switchboards[start][CONNECTS]:
            if area not in visited:
                if trunk_connections(switchboards, area, end, visited):
                    return True
        return False


def ending_call(switchboards, first_area, first_num):
    """ This function is to end the call that was previously                                                                                                            
        started. Its also used to determine if that number                                                                                                              
        ever has a call connection.                                                                                                                                     
        Param: switchboards is the current network structure.                                                                                                           
        Param: first_area is the given area code with the                                                                                                               
               number.                                                                                                                                                  
        Param: first_num is the given phone number.                                                                                                                  
    """


    if first_area in switchboards.keys():

        if first_num in switchboards[first_area][CALLS].keys():
            print('hanging up...\nconnection terminated')

            #  Connects to how start call stores the area code and phone number.  #                                                                                     
            last_area = int(switchboards[first_area][CALLS][first_num][0:3])
            last_num = int(switchboards[first_area][CALLS][first_num][4:])

            del switchboards[first_area][CALLS][first_num]
            del switchboards[last_area][CALLS][last_num]

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
    for a_key in switchboards:
        print('Switchboard with area code:', area_key)
        print('\t Trunk lines are:')

        for trunk_line in switchboards[a_key][CONNECTS]:
            print('\t\t Trunk lines connection to:', trunk_line)

        print('\t local phone numbers are:')
        for numbers in switchboards[a_key][PHONE_NUMS]:

            if numbers not in switchboards[a_key][CALLS]:
                print('\t\t Phone with number:', numbers, 'not in use.')

            else:
                print('\t\t Phone with number:', numbers, 'is connected to', switchboards[a_key][CALLS][numbers])


if __name__ == '__main__':
    switchboards = {}                                                                                                                          
    s = input('Enter command: ')
    while s.strip().lower() != QUIT:
        split_command = s.split()
        if len(split_command) == 3 and split_command[0].lower() == CONNECT_SWITCH:
            area1 = int(split_command[1])
            area2 = int(split_command[2])
            connect_switchboards(switchboards, area1, area2)

        elif len(split_command) == 2 and split_command[0].lower() == ADD_SWITCH:
            if len(split_command[1]) <= TRUNK_MAX:
                if split_command[1][0] == '0':
                    add_switchboard(switchboards, (split_command[1]))
                else:
                    add_switchboard(switchboards, int(split_command[1]))

        elif len(split_command) == 2 and split_command[0].lower() == ADD_PHONE:
            number_parts = split_command[1].split('-')
            area_code1 = int(number_parts[0])
            phone_num1 = int(''.join(number_parts[1:]))
            add_phone(switchboards, area_code1, phone_num1)

        elif len(split_command) == 2 and split_command[0].lower() == SAVE_NETWORK:
            save_network(switchboards, split_command[1])
             print('Network saved to {}.'.format(split_command[1]))

        elif len(split_command) == 2 and split_command[0].lower() == LOAD_NETWORK:
            switchboards = load_network(split_command[1])
            print('Network loaded from {}.'.format(split_command[1]))

        elif len(split_command) == 3 and split_command[0].lower() == CALL_START:
            sync_parts = split_command[1].split(HYPHEN)
            sync_code = int(sync_parts[0])
            sync_number = int(''.join(sync_parts[1:]))

            dest_parts = split_command[2].split(HYPHEN)
            dest_code = int(dest_parts[0])
            dest_number = int(''.join(dest_parts[1:]))
            start_call(switchboards, sync_code, sync_number, dest_code, dest_number)

        elif len(split_command) == 2 and split_command[0].lower() == CALL_END:
            num_parts = split_command[1].split(HYPHEN)
            area_code = int(num_parts[0])
            number = int(''.join(num_parts[1:]))
            end_call(switchboards, area_code, number)

        elif len(split_command) >= 1 and split_command[0].lower() == DISPLAY:
            display(switchboards)

        s = input('Enter command: ')
