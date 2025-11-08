class Order:
    def __init__(self,Customer_name,items,total_amount,discount):
        self.customer_name=Customer_name
        self.items=items
        self.__total_amount=total_amount
        self.__discount=discount
    def __calculate_final(self):
        return self.total_amount-self.__discount
    
    def get_admin_view(self):
        return {
            "Customer":self.customer_name,
            "Items":self.items,
            "Total_Amount":self.__total_amount,
            "discount":self.__discount,
            }
    def get_user_view(self):
        return {
            "Customer":self.customer_name,
            "Items":self.items,
            "Total_Amount":self.__total_amount,
            }
class AdminPortal:
    def show_order(self,order):
        return order.get_admin_view()
class UserPortal:
    def show_order(self,order):
        return order.get_user_view()
order=Order("sivaprakas",8,20002,3000)
obj1=AdminPortal()
obj2=UserPortal()
print(obj1.show_order(order))
print(obj2.show_order(order))
    
        
