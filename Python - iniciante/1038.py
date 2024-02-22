item = input().split()
code, quantidade = item

if code == "1":print("Total: R$ {:.2f}".format(4.00*float(quantidade)));
if code == "2": print("Total: R$ {:.2f}".format(4.50*float(quantidade)))
if code == "3": print("Total: R$ {:.2f}".format(5.00*float(quantidade)))
if code == "4":print("Total: R$ {:.2f}".format(2.00*float(quantidade)))
if code == "5":print("Total: R$ {:.2f}".format(1.50*float(quantidade)))
  