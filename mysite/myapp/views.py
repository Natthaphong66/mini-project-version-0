from django.shortcuts import render

def home(request):
    """หน้าแรกของระบบ"""
    featured_products = [
        {'name': 'iPhone 15 Pro Max', 'category': 'อิเล็กทรอนิกส์', 'price': 48900, 'emoji': '📱'},
        {'name': 'MacBook Air M3', 'category': 'คอมพิวเตอร์', 'price': 44900, 'emoji': '💻'},
        {'name': 'AirPods Pro 2', 'category': 'เครื่องเสียง', 'price': 8990, 'emoji': '🎧'},
        {'name': 'Apple Watch Series 9', 'category': 'แกดเจ็ต', 'price': 15900, 'emoji': '⌚'},
        {'name': 'PlayStation 5', 'category': 'เกม', 'price': 18990, 'emoji': '🎮'},
        {'name': 'Samsung Smart TV 55"', 'category': 'เครื่องใช้ไฟฟ้า', 'price': 22900, 'emoji': '📺'},
    ]
    return render(request, 'myapp/home.html', {'featured_products': featured_products})

def products(request):
    """หน้ารายการสินค้า"""
    products_list = [
        {'name': 'iPhone 15 Pro Max', 'category': 'อิเล็กทรอนิกส์', 'price': 48900, 'emoji': '📱'},
        {'name': 'MacBook Air M3', 'category': 'คอมพิวเตอร์', 'price': 44900, 'emoji': '💻'},
        {'name': 'AirPods Pro 2', 'category': 'เครื่องเสียง', 'price': 8990, 'emoji': '🎧'},
        {'name': 'Apple Watch Series 9', 'category': 'แกดเจ็ต', 'price': 15900, 'emoji': '⌚'},
        {'name': 'PlayStation 5', 'category': 'เกม', 'price': 18990, 'emoji': '🎮'},
        {'name': 'Samsung Smart TV 55"', 'category': 'เครื่องใช้ไฟฟ้า', 'price': 22900, 'emoji': '📺'},
        {'name': 'Nike Air Max', 'category': 'แฟชั่น', 'price': 5990, 'emoji': '👟'},
        {'name': 'Canon EOS R6', 'category': 'กล้อง', 'price': 79900, 'emoji': '📷'},
        {'name': 'Nintendo Switch OLED', 'category': 'เกม', 'price': 12990, 'emoji': '🎮'},
        {'name': 'iPad Pro 12.9"', 'category': 'แท็บเล็ต', 'price': 39900, 'emoji': '📱'},
    ]
    return render(request, 'myapp/products.html', {'products': products_list})
