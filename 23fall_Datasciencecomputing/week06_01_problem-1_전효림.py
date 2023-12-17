class Category: # 입력 받은 과일/채소 카테고리 분류
    # name:str
    # categ:str
    def __init__(self, name):
        ### Edit Here ###
        self.__name = name
        vegetables = ['Potato', 'Broccoli', 'Cucumber', 'Spinach']
        if name in vegetables:
            self.__categ = 'vegetable'
        else:
            self.__categ = 'fruit'
    
    def get_name(self) -> str:
        ### Edit Here ###
        return self.__name
    
    def get_categ(self) -> str:
        ### Edit Here ###
        return self.__categ

class Product(Category):
    # name:str
    # cost:float
    # quantity:int
    def __init__(self, name, cost, quantity):
        ### Edit Here ###
        super().__init__(name)
        self.__cost = cost
        self.__quantity = quantity

    def get_cost(self) -> int:
        ### Edit Here ###
        return self.__cost

    def get_quantity(self) -> int:
        ### Edit Here ###
        return self.__quantity

    def inStock(self) -> bool:
        ### Edit Here ###
        return self.__quantity >=5
    
    def update_quantity(self, nsold):
        ### Edit Here ###
        self.__quantity -= nsold


class Finance:
    # money:float
    def __init__(self):
        ### Edit Here ###
        self.__money = 0.0

    def get_money(self) -> int:
        ### Edit Here ###
        return self.__money

    def update(self, product, nsold):
        ### Edit Here ###
        self.__money += product.get_cost() * nsold
    
        
class Market:
    # cash:Finance
    # p_list:List[Product]
    def __init__(self, p_list):
        ### Edit Here ###
        self.__cash = Finance()
        self.__p_list = p_list

    def get_cash(self) -> int:
        ### Edit Here ###
        return self.__cash.get_money()

    def get_list(self) -> list:
        ### Edit Here ###
        return self.__p_list

    def checkStock(self) -> int:
        ### Edit Here ###
        stock = 0
        for p in self.__p_list:
            if p.inStock():
                stock += 1
        return stock

    def sell(self, prod, nsold):
        ### Edit Here ###
        if prod.inStock() and prod.get_quantity() >= nsold:
            prod.update_quantity(nsold) # 재고
            self.__cash.update(prod, nsold) # 재정
        else:
            print(f"{prod.get_name()}은/는 재고가 적어 팔 수 없습니다.")

#### Do not edit Here ####
potato = Product("Potato", 0.40, 20)
broccoli = Product("Broccoli", 0.60, 3)
mangosteen = Product("Mangosteen", 10.00, 5)
cucumber = Product("Cucumber", 13.00, 15)
spinach = Product('Spinach', 4.00, 30)
blueberry = Product('Blueberry', 5.00, 4)
grapefruit = Product('Grapefruit', 7.00, 17)

PL0 = Market([])
PL1 = Market([potato, broccoli]) # 야채
PL2 = Market([mangosteen, blueberry, grapefruit]) # 과일
market = Market([potato, broccoli, mangosteen, cucumber, spinach, blueberry, grapefruit]) # cucumber, spinach, 두개 추가

print(PL0.checkStock() == 0)
print(PL1.checkStock() == 1)
print(PL2.checkStock() == 2)
print(market.checkStock() == 5)

for p in PL1.get_list():
    print(p.get_categ() == 'vegetable')

for p in PL2.get_list():
    print(p.get_categ() == 'fruit')

for p in market.get_list():
    if p in [broccoli, blueberry]:
        print(p.inStock() == False)
    else:
        print(p.inStock() == True)

for p,s in zip(market.get_list(), [15,15,3,8,20,2,13]):
    market.sell(p,s)

for p in [potato, broccoli, mangosteen, cucumber, spinach, blueberry, grapefruit]:
    print('현재 {}의 재고는 {}입니다'.format(p.get_name(), p.get_quantity()))

print('현재 수확물을 팔고 남은 돈은 {}입니다.'.format(market.get_cash()))
