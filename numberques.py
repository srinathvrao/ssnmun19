with open("que.doc","r") as readfile:
	test=1
	count=1
	with open("numberedques.txt","w") as file:
		for line in readfile:
			if len(line)==1 and test==1:
				st = "-\n"
				test+=1
				count+=1
				file.write(st)
			else:
				if test==2:
					st = str(count)+". "+line
				else:
					st = line	
				test=1
				file.write(st)


