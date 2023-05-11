class MenuItem:
    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients

    def __str__(self):
        return f"{self.name}: {self.price}원"


class Menu:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, item):
        """메뉴에 메뉴 아이템 객체 추가"""
        self.items[item_name] = item

    def show_menu(self):
        """메뉴에 저장된 모든 아이템을 출력"""
        for key in self.items:
            print(self.items[key])

    def get_items(self):
        """메뉴에 저장된 모든 아이템을 딕셔너리 형태로 리턴"""
        return self.items

    def get_item(self, item_name):
        """{item_name}의 value, 메뉴 아이템 객체를 리턴"""
        return self.items[item_name]


class InventoryItem:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}: {self.quantity}"

    def add_quantity(self, quantity):
        """아이템의 수량 증가"""
        self.quantity += quantity

    def remove_quantity(self, quantity):
        """아이템의 수량 감소. 결과가 0개 미만일 경우 에러"""
        if self.quantity - quantity < 0:
            return False
        self.quantity -= quantity
        return True

class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, item):
        """인벤토리에 인벤토리 아이템 객체 추가"""
        self.items[item_name] = item

    def get_items(self):
        """인벤토리에 저장된 모든 아이템을 딕셔너리 형태로 리턴"""
        return self.items

    def get_item(self, item_name):
        """{item_name}의 value, 인벤토리 아이템 객체를 리턴"""
        return self.items[item_name]

    def add_item_quantity(self, item_name, quantity):
        """인벤토리에 {item_name}를 key로 등록된 인벤토리 아이템 객체의 수량 증가"""
        self.items[item_name].add_quantity(quantity)

    def remove_item_quantity(self, item_name, quantity):
        """인벤토리에 {item_name}를 key로 등록된 인벤토리 아이템 객체의 수량 감소"""
        self.items[item_name].remove_quantity(quantity)


class Person:
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory

    def action(self, param):
        pass

    def info(self):
        """Person 객체의 이름, 인벤토리 정보를 출력"""
        print(f"이름 : {self.name}")
        print("소지품")
        items = self.inventory.get_items()
        for key in items:
            print(items[key])


class Customer(Person):
    def __init__(self, name, inventory):
        super().__init__(name, inventory)
        self.order = None

    # 주문
    def action(self, order_item):
        price = order_item.price
        my_money = self.inventory.get_item('money')

        if my_money.remove_quantity(price):
            self.order = order_item
            print(f"[주문 성공] {self.order.name}를 주문했습니다. [ 현재 잔고 : {my_money.quantity} ]")
        else:
            print(f"[잔액 부족] {order_item.name}을 주문하기 위해서 {price - my_money.quantity}원이 더 필요합니다. [ 현재 잔고 : {my_money.quantity} ]")

        """
        Q. Person 클래스에게 상속받은 action 메소드를 오버라이딩하여 고객이 주문하는 메소드를 만들어봅시다.
        요구사항.
        1. action 메소드의 인자로는 메뉴 아이템 객체를 받습니다.
        2. 아이템의 가격보다 고객이 가진돈이 적을 경우에는 주문할 수 없습니다. (에러 발생 등 예외처리를 해주세요)
        3. 아이템의 가격을 충분히 지불할 수 있다면 self.order에 아이템을 저장해주세요
        """


class Barista(Person):
    def __init__(self, name, inventory):
        super().__init__(name, inventory)

    # 커피 제조
    def action(self, customer):
        # 주문 메뉴
        order = customer.order
        # 카페 재고
        inventory = self.inventory.get_items()
        # 메뉴 제조에 필요한 재료 순회
        for name,quantity in order.ingredients.items():
            if name in inventory.keys():
                if inventory[name].quantity - quantity > 0:
                    pass
                else:
                    customer.inventory.add_item_quantity(order.price)
                    print("재료가 부족합니다.")
                    return 0

        for name,quantity in order.ingredients.items():
            if name in inventory.keys():
                inventory[name].quantity -= quantity
        self.inventory.add_item_quantity('money',order.price)


    def get_income(self):
        """Barista 객체가 보유한 money를 리턴"""
        return self.inventory.get_item("money")


# 카페 메뉴 생성
menu = Menu() # 생성자로 빈 딕셔너리 생성
menu.add_item("americano", MenuItem("Americano", 3000, {"bean": 2, "water": 2}))
# menu 오브젝트, add_item 메서드 호출 딕셔너리에 아메리카노 정보 추가
# MenuItem 오브젝트 생성 딕셔너리 정보를 기입
# 즉 menu 오브젝트의 item 딕셔너리에 아메리카노 값을 담으며, 이때 MenuItem의 오브젝트도 함께 담겨 있다.


menu.add_item("latte", MenuItem("Latte", 3000, {"bean": 2, "milk": 2}))
print("--메뉴 정보--")
menu.show_menu()



# 고객 생성
customer_inventory = Inventory()
# 고객의 인벤토리 클래스의 빈 딕셔너리 생성
customer_inventory.add_item("money", InventoryItem("Money", 10000))
# 고객의 인벤토리 딕셔너리에 인벤토리 아이템 클래스의 딕셔너리 추가
customer = Customer("철수", customer_inventory)
print("--고객 정보--")
customer.info()

# 바리스타 생성
barista_inventory = Inventory()
barista_inventory.add_item("water", InventoryItem("Water", 20))
barista_inventory.add_item("bean", InventoryItem("Bean", 20))
barista_inventory.add_item("milk", InventoryItem("Milk", 10))
barista_inventory.add_item("money", InventoryItem("Money", 0))
barista = Barista("민수", barista_inventory)
print("--바리스타 정보--")
barista.info()

# 주문
print("--주문 정보--")
customer.action(menu.get_item("americano"))



# 커피 제조
print("--주문 접수--")
barista.action(customer)

# 정보 확인
print("--고객 정보--")
customer.info()
print("--바리스타 정보--")
barista.info()
print("")
print(f"바리스타 수입 : {barista.get_income()}")