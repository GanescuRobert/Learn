class Robot:
    def __init__(self, instruction_file):
        self.instruction_file = instruction_file
        self.instruction_list = None

    def write_intructions(self):
        f = open(self.instruction_file, 'w')
        while True:
            movement_x = input('Enter horizontal movement, or q to quit: ')
            if movement_x == 'q':
                break
            movement_y = input('Enter vertical movement, or q to quit: ')
            if movement_y == 'q':
                break
            f.write(movement_x + ' ' + movement_y + '\n')
        f.close()

    def read_instructions(self):
        try:
            f = open(self.instruction_file, 'r')
        except FileNotFoundError as error:
            print(error)
        else:
            self.instruction_list = f.readlines()
            f.close()

    def get_location(self):
        position_x, position_y = 0, 0
        distance_x, distance_y = 0, 0
        self.read_instructions()
        if self.instruction_list != None:
            for data in self.instruction_list:
                temp = data.split()
                x, y = float(temp[0]), float(temp[1])

                position_x += x
                distance_x += abs(x)
                position_y += y
                distance_y += abs(y)
        return position_x, position_y, distance_x, distance_y


robot_1 = Robot('robot_1.txt')
robot_1.write_intructions()
pos_x, pos_y, dis_x, dis_y = robot_1.get_location()

print('The robot is finnaly at ('+str(pos_x) + ','+str(pos_y), ')')
print('The robot has traveled a distance of '+str(dis_x) +
      ' horizontally and '+str(dis_y)+' vertically')
