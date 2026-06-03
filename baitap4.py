
product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20,
        "sold": 5
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 8,
        "sold": 3
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 3,
        "sold": 7
    }
]

def normalize_product_id(product_id):
    return product_id.strip().upper()


def find_product(product_id):
    for product in product_list:
        if product["product_id"] == product_id:
            return product
    return None


def get_positive_integer(message):
    while True:
        value = input(message).strip()

        if not value.isdigit():
            print("Số lượng mua/Nhập kho không hợp lệ")
            continue

        value = int(value)

        if value <= 0:
            print("Số lượng mua/Nhập kho không hợp lệ")
            continue

        return value


def get_stock_status(quantity):
    if quantity == 0:
        return "Hết hàng"
    elif quantity <= 5:
        return "Sắp hết hàng"
    else:
        return "Còn hàng"


def display_products():

    if len(product_list) == 0:
        print("Danh sách sản phẩm hiện đang trống.")
        return

    print("\nDanh sách sản phẩm hiện tại:")

    for index, product in enumerate(product_list, start=1):

        status = get_stock_status(
            product["quantity"]
        )

        print(
            f"{index}. "
            f"Mã SP: {product['product_id']} | "
            f"Tên: {product['product_name']} | "
            f"Giá: {product['price']} | "
            f"Tồn kho: {product['quantity']} | "
            f"Đã bán: {product['sold']} | "
            f"Trạng thái: {status}"
        )

def sell_product():

    product_id = normalize_product_id(
        input("Nhập mã sản phẩm khách muốn mua: ")
    )

    product = find_product(product_id)

    if product is None:
        print("Không tìm thấy sản phẩm cần bán")
        return

    buy_quantity = get_positive_integer(
        "Nhập số lượng khách mua: "
    )

    if buy_quantity > product["quantity"]:
        print("Số lượng trong kho không đủ để bán")
        return

    product["quantity"] -= buy_quantity
    product["sold"] += buy_quantity

    total_price = (
        product["price"] * buy_quantity
    )

    print(
        f"Khách cần thanh toán: "
        f"{total_price} VNĐ"
    )


def import_product():

    product_id = normalize_product_id(
        input("Nhập mã sản phẩm cần nhập thêm: ")
    )

    product = find_product(product_id)

    if product is None:
        print("Không tìm thấy sản phẩm cần nhập kho")
        return

    import_quantity = get_positive_integer(
        "Nhập số lượng nhập thêm: "
    )

    product["quantity"] += import_quantity

    print("Nhập kho thành công")


def revenue_report():

    total_sold = 0

    for product in product_list:
        total_sold += product["sold"]

    if total_sold == 0:
        print("Chưa có doanh thu phát sinh.")
        return

    print(
        "\n===== BÁO CÁO DOANH THU "
        "CỬA HÀNG YODY ====="
    )

    total_revenue = 0

    best_seller = product_list[0]

    for index, product in enumerate(
            product_list,
            start=1
    ):

        revenue = (
            product["price"]
            * product["sold"]
        )

        total_revenue += revenue

        if product["sold"] > best_seller["sold"]:
            best_seller = product

        print(
            f"{index}. "
            f"{product['product_name']} | "
            f"Đã bán: {product['sold']} | "
            f"Doanh thu: {revenue}"
        )

    print(
        f"\nTổng doanh thu: "
        f"{total_revenue}"
    )

    print(
        f"Sản phẩm bán chạy nhất: "
        f"{best_seller['product_name']}"
    )


while True:

    print("\n===== HỆ THỐNG VẬN HÀNH CỬA HÀNG YODY =====")
    print("1. Hiển thị danh sách sản phẩm và cảnh báo tồn kho")
    print("2. Bán sản phẩm cho khách hàng")
    print("3. Nhập thêm hàng vào kho")
    print("4. Xem báo cáo doanh thu")
    print("5. Thoát chương trình")

    choice = input("Nhập lựa chọn: ").strip()

    if not choice.isdigit():
        print(
            "Lựa chọn không hợp lệ, "
            "vui lòng nhập lại!"
        )
        continue

    choice = int(choice)

    if choice == 1:
        display_products()

    elif choice == 2:
        sell_product()

    elif choice == 3:
        import_product()

    elif choice == 4:
        revenue_report()

    elif choice == 5:
        print("Thoát chương trình.")
        break

    else:
        print(
            "Lựa chọn không hợp lệ, "
            "vui lòng nhập lại!"
        )