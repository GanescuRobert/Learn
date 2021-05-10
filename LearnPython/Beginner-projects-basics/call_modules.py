import operate_list as ol
import handle_numbers as hn

my_number_list = [2, 3, 5, 2, 4, 5, 1, 7]
my_name_list = ['Amy', 'Gloria', 'Tim', 'Ken', 'Stephen', 'Patrick', 'Tim']

ol.delete_names(my_name_list,'Tim')
print(my_name_list)

ol.add_names(my_name_list, 'Lily', 2)
print(my_name_list)

my_sum = hn.add_number(my_number_list,1,5)
print(my_sum)

my_average = hn.get_mean(my_number_list,1,5)
print(my_average)