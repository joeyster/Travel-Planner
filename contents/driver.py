from best_first import Best_First


######### user input
point_A = "California"
point_B = "Nevada"
point_C = "Illinois"
point_D = "New York"
point_E = "Maine"
######### user input end

#backend
point_list = [point_A, point_B, point_C, point_D, point_E]
hit_list = point_list[1:len(point_list)]

print(Best_First(point_list[0], hit_list, "distance"))
print(Best_First(point_list[0], hit_list, "time"))
