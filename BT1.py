# Phân tích và thiết kế giải pháp 
# Phân tích Output 
# Chức năng 1 : Xem giỏ hàng 
# Đầu vào (Input): Không có (Đọc từ biến cart_items)
# Dữ liệu đầu (Ouput): Bảng hiện thị danh sách sản phẩm , tổng số lượng , tổng tiền 

# Chức năng 2 : Thêm/ Tăng số lượng 
# Mã SP(str) , tên SP (str) , số lượng (int), đơn giá (int/float)
# Đầu ra (Output): Thông báo thành công hoặc thông báo lỗi (nếu dữ liệu số âm)

# Chức năng 3 : Cập nhật số lượng 
#  Input : Mã SP(str), Số lượng mới (int)
# Output : Cập nhật số lượng mới hoặc báo lỗi không tồn tại / số lượng âm 

# Chức năng 4: Xóa sản phẩm 
# Input : Mã sản phẩm (Str)
# Output : Xóa sản phẩm khỏi danh sách hoặc báo lỗi không tồn tại 

# Chức năng 5 : Thoát 

# Input : Lựa chọn số 5 

# Output : Thông báo kết thúc chương 

# Giải pháp 

# Sử dụng một list chứa các phần tử con, trong đó mỗi list con đại diện cho một sản phẩm :[id,name,quantity,price]

# Kiểm tra dữ liệu : Sử dụng vòng lặp while true kết isdigit () để lấy dữ liệu 
# Tìm kiếm sản phẩm : Duyệt qua danh sách bằng vòng lặp để so sánh mã sản phẩm 

cart_items =[
    ["P001","Điện thoại Iphone 15",1,25000000]
    ["P002","Ốp lưng Silicon",2,150000]
]
while True:
    print ("\n"+"="*20+"SHOPPE CART MANAGEMENT CLI" + "=" *20)
    print ("1.Xem chi tiết giỏ hàng và tổng tiền")
    print ("2.Thêm sản phẩm mới hoặc tăng số lượng sản phẩm")
    print ("3.Cập nhật số lượng sản phẩm")
    print ("4.Xóa sản phẩm khỏi giỏ hàng")
    print ("5.Thoát chương trình")
    print ("=" * 68)
    
    choice = input("Nhập vào lựa chọn của bạn (1-5) : ").strip()
    
    if choice =="1":
        if not cart_items:
            print ("\n Giỏ hàng của bạn đang trống !")
        else :
            print("\n" + "=" *70)
            print (f"{'Mã SP :<10'}{'TÊN SẢN PHẨM':<25}{'SỐ LƯỢNG':<10}{'ĐƠN GIÁ (VND)':<15}{'THÀNH TIỀN':<15}")
            print ("-" *70)
            
            total_quantity =0
            total_amount =0
            
            for item in cart_items:
                product_id,product_name,quantity,price = item
                subtotal = quantity * price 
                total_quantity +=quantity
                total_amount += subtotal 
                print(f"{product_id:<10}{product_name:<25}{quantity:<10}{price:<15,.0f}{subtotal:<15,.0f}")
                
            print ("-" *70)
            print (f" Tổng số lượng tất cả sản phẩm : {total_quantity}")
            print (f"Tổng tiền toàn bộ giỏ hàng  : {total_amount:,.0f} VND")
            print ("=" *70)
            
    elif choice == "2":
         print("\n-THÊM SẢN PHẨM/TĂNG SỐ LƯỢNG----")
         product_id = input("Nhập mã sản phẩm ").strip().upper()
         product_name =input("Nhập tên sản phẩm : ").strip()
         
         quantity_str = input("Nhập số lượng : ").strip()
         if not quantity_str.isdigit():
             print("Lỗi : Số lượng phải là số nguyên dương ")    
             continue
         quantity = int(quantity_str)
         if quantity <=0:
             print ("Lỗi : Số lượng nhập vào phải lớn hơn 0")
             continue 
         price_str = input("Nhập đơn giá : ").strip()
         if not price_str.isdigit():
             print ("Lỗi : Đơn giá phải là số nguyên dương !")
             continue
         price = int(price_str)
         
         is_existed = False
         for item in cart_items:
             if item[0] == product_id:
                 item[2] += quantity
                 print (f"Mã sản phẩm {product_id } đã tồn tại . Đã cộng dồn thêm {quantity} cái.")
                 is_existed =True
                 break
             
             if not is_existed:
                 new_product = [product_id,product_name,quantity,price]
                 cart_items.append(new_product)
                 print (f"Đã thêm mới thành công sản phẩm : {product_name}")
                 
    elif choice =="3":
        print ("\n --CẬP NHẬT SỐ LƯỢNG SẢN PHẨM ---")
        product_id = input("Nhập mã sản phẩm cần sửa số lượng ").strip().upper()
        
        found_item=None
        for item in cart_items:
            if item[0] ==product_id:
                found_item = item
                break
            if found_item is None:
                print ("Mã sản phẩm không tồn tại trong giỏ hàng.")
                continue
            
            new_quantity_str = input(f"Nhập số lượng mới cho [{found_item[1]}] :").strip()
            if not new_quantity_str.isdigit():
                print("Lỗi : Số lượng sửa đổi phải là số nguyên dương !")
                continue
            
            new_quantity = int(new_quantity_str)
            if new_quantity <=0:
                print ("Lỗi : Số lượng sửa đổi phải lớn hơn 0 !")
                continue 
            found_item[2] = new_quantity_str
            print (f"Đã cập nhật số lượng mới thành công cho mã sản phẩm {product_id}.")
            
    elif choice =="4":
        print ("\n -- XÓA SẢN PHẨM KHỎI GIỎ HÀNG ----")
        product_id = input("Nhập mã sản phẩm muốn xóa : ").strip().upper()
        
        is_deleted = False 
        for i in range (len(cart_items)):
            if cart_items[i][0] == product_id:
                confirm = input(f"Bạn có chắc muốn xóa sản phẩm [{cart_items[i][1]}] không ? (y/n) :").strip().lower()
                if confirm == 'y':
                    del cart_items[i]
                    print (f"Đã xóa hoàn toàn sản phẩm {product_id} khỏi giỏ hàng .")
                else:
                    print ("Thao tác xóa đã bị hủy bỏ .")
                    is_deleted = True
                    break
                if not is_deleted:
                    print ("Mã sản phẩm không tồn tại trong giỏ hàng .")
            elif choice =="5":
                print ("\n Cảm ơn bạn đã sử dụng hệ thống quản lý giỏ hàng Shoppe. Hẹn gặp lại sau nhé ")   
                break
            
            else :
                print ("Lỗi : Lựa chọn không hợp lê ! Vui lòng chỉ nhập số từ 1 đến 5.")     
            
        
            
            
        