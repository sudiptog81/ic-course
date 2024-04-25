import unittest

def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):
                            #    take_out_idx=0, dine_in_idx=0, served_idx=0):

    # Check if we're serving orders first-come, first-served
    # if len(served_orders) == 0:
    #     return True
    
    # if len(take_out_orders) and take_out_orders[0] == served_orders[0]:
    #     return is_first_come_first_served(take_out_orders[1:], dine_in_orders, served_orders[1:])
    # elif len(dine_in_orders) and dine_in_orders[0] == served_orders[0]:
    #     return is_first_come_first_served(take_out_orders, dine_in_orders[1:], served_orders[1:])
    
    # return False

    # if served_idx == len(served_orders):
    #     return True
    
    # if ((take_out_idx < len(take_out_orders)) and (served_orders[served_idx] == take_out_orders[take_out_idx])):
    #     take_out_idx += 1
    # elif ((dine_in_idx < len(dine_in_orders)) and (served_orders[served_idx] == dine_in_orders[dine_in_idx])):
    #     dine_in_idx += 1
    # else:
    #     return False
    
    # return is_first_come_first_served(take_out_orders, dine_in_orders, served_orders,
    #                                   take_out_idx, dine_in_idx, served_idx + 1)

    take_out_idx = dine_in_idx = 0
    take_out_max = len(take_out_orders) - 1
    dine_in_max = len(dine_in_orders) - 1

    for order in served_orders:
        if take_out_idx <= take_out_max and order == take_out_orders[take_out_idx]: 
            take_out_idx += 1
        elif dine_in_idx <= dine_in_max and order == dine_in_orders[dine_in_idx]:
            dine_in_idx += 1
        else:
            return False
        
    if take_out_idx != len(take_out_orders) or dine_in_idx != len(dine_in_orders):
        return False

    return True










# Tests

class Test(unittest.TestCase):

    def test_both_registers_have_same_number_of_orders(self):
        result = is_first_come_first_served([1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6])
        self.assertTrue(result)

    def test_registers_have_different_lengths(self):
        result = is_first_come_first_served([1, 5], [2, 3, 6], [1, 2, 6, 3, 5])
        self.assertFalse(result)

    def test_one_register_is_empty(self):
        result = is_first_come_first_served([], [2, 3, 6], [2, 3, 6])
        self.assertTrue(result)

    def test_served_orders_is_missing_orders(self):
        result = is_first_come_first_served([1, 5], [2, 3, 6], [1, 6, 3, 5])
        self.assertFalse(result)

    def test_served_orders_has_extra_orders(self):
        result = is_first_come_first_served([1, 5], [2, 3, 6], [1, 2, 3, 5, 6, 8])
        self.assertFalse(result)

    def test_one_register_has_extra_orders(self):
        result = is_first_come_first_served([1, 9], [7, 8], [1, 7, 8])
        self.assertFalse(result)

    def test_one_register_has_unserved_orders(self):
        result = is_first_come_first_served([55, 9], [7, 8], [1, 7, 8, 9])
        self.assertFalse(result)

    def test_order_numbers_are_not_sequential(self):
        result = is_first_come_first_served([27, 12, 18], [55, 31, 8], [55, 31, 8, 27, 12, 18])
        self.assertTrue(result)

unittest.main(verbosity=2)