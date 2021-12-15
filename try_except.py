try:
    num = input("請輸入一個數字")
    num = int(num)
    total = num+1
    print(total)
except ValueError:
	print("輸入錯誤")
except:
	print("發生錯誤")
else:
	print("成功執行")
finally:
	print("程式結束")
