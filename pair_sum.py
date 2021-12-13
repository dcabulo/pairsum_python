from helpers import fetch_data


class TwoPairSum:
    def __init__(self, input_number: int):
        self.input_number = input_number
        self.result_list = []
        self.data = fetch_data()

    def two_sum_hashing(self):
        pair_list = {}
        hash_table = {}

        for i in range(len(self.data)):
            int_list = int(self.data[i].get("h_in"))
            complement = self.input_number - int_list
            if complement in hash_table and pair_list.get(f"{int_list}_{complement}") is None:
                if pair_list.get(f"{complement}_{int_list}") is None:
                    list_test = []
                    list_test.extend([int_list, complement])
                    pair_list[f"{int_list}_{complement}"] = list_test
            hash_table[int_list] = int_list
        return pair_list

    def print_name(self, data: dict):
        result_array = []
        if not bool(data):
            return print("No Pair of names in the input data")
        for value in data.values():
            first_list = list(filter(lambda x: int(x["h_in"]) == value[0], self.data))
            second_list = list(filter(lambda x: int(x["h_in"]) == value[1], self.data))
            i = 0
            j = len(second_list) - 1
            while i < len(first_list):
                if j < 0:
                    i += 1
                    j = len(second_list) - 1
                else:
                    j -= 1
                    result_array.append(f"- {first_list[i]['first_name']} {first_list[i]['last_name']} "
                                        f"{second_list[j]['first_name']} {second_list[j]['last_name']}")
        with open('./result.txt', 'w') as file:
            file.write('Pair of names founds are \n')
            file.write('\n'.join(result_array))

