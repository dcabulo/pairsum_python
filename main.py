from pair_sum import TwoPairSum

input_number = int(input("Ingresa un numero por favor=> "))
two_pair_sum = TwoPairSum(input_number=input_number)
pair_result_dict = two_pair_sum.two_sum_hashing()

two_pair_sum.print_name(pair_result_dict)


