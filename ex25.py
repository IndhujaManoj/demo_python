def month_name(month_number):
    if month_number==1:
        return "JANUARY"
    elif month_number==2:
        return "FEBRUARY"
    elif month_number==3:
        return "MARCH"
    elif month_number==4:
        return "APRIL"
    elif month_number==5:
        return "MAY"
    elif month_number==6:
        return "JUNE"
    elif month_number==7:
        return "JULY"
    elif month_number==8:
        return "AUGUST"
    elif month_number==9:
        return "SEPTEMBER"
    elif month_number==10:
        return "OCTOBER"
    elif month_number==11:
        return "NOVEMBER"
    elif month_number==12:
        return "DECEMBER"
    else:
        return "ERROR"
month_name(3)
print("the month is:",month_name(7))
    
