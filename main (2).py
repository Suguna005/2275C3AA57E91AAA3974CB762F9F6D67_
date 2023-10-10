def linearSearchProduct(productList,targetproduct):
	indices=[]
	for index,product in enumerate(productList):
		if product == targetproduct:
			indices.append(index)
		return indices
Products=["sneha" , "boot" , "loafer" , "boot" , "sandal" , "goki"]
target="sneha"
result=linearSearchProduct(Products,target)
print(result)