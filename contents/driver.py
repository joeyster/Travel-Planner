from best_first import Best_First


######### user input
point_A = "CA"
point_B = "NV"
point_C = "IL"
point_D = "NY"
point_E = "ME"
######### user input end

#backend
point_list = [point_A, point_B, point_C, point_D, point_E]
hit_list = point_list[1:len(point_list)-1]
hit_list_count = len(point_list)-2
point_count = len(point_list)

Best_First(point_list, hit_list)