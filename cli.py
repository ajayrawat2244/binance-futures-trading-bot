import argparse
import os
from dotenv import load_dotenv
from bot.orders import OrderService

load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

print(API_KEY)
print(API_SECRET)

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

    parser.add_argument("--symbol", required=True, help="Trading symbol")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        service = OrderService(API_KEY, API_SECRET)

        print("\n===== ORDER REQUEST =====")
        print(f"Symbol: {args.symbol}")
        print(f"Side: {args.side}")
        print(f"Order Type: {args.type}")
        print(f"Quantity: {args.quantity}")

        if args.type == "LIMIT":
            print(f"Price: {args.price}")

        response = service.create_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price,
        )

        print("\n===== ORDER RESPONSE =====")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")
        print(f"Average Price: {response.get('avgPrice')}")

        print("\nOrder placed successfully.")

    except Exception as e:
        print(f"\nOrder failed: {str(e)}")


if __name__ == "__main__":
    main()
