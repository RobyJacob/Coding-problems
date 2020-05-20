def max_num_houses(house_prices, budget):
    count = [0 for _ in range(1001)]
    sorted_house_prices = [0 for _ in range(len(house_prices))]

    for price in house_prices:
        count[price] += 1

    for i in range(len(count)):
        count[i] += count[i-1]

    for i in range(len(house_prices)):
        sorted_house_prices[count[house_prices[i]]-1] = house_prices[i]
        count[house_prices[i]] -= 1

    current_cost = 0
    num_of_houses = 0

    for house_price in sorted_house_prices:
        if current_cost < budget and current_cost + house_price <= budget:
            current_cost += house_price
            num_of_houses += 1

    return num_of_houses

def main():
    test_cases = int(input())

    for t in range(test_cases):
        N, B = list(map(int, input().split()))
        house_prices = list(map(int, input().split()))
        print("Case #{}: {}".format(t+1, max_num_houses(house_prices, B)))

if __name__ == "__main__":
    main()
